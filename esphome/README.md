# pc_power_controller — ESPHome ファームウェア

`../circuit/` の回路（Seeed XIAO ESP32C3 + TLP225A(F) + TLP621-1）用の
ESPHomeファームウェア設定です。PCの電源ボタンをリモート操作し、電源LED
(PLED) の状態（点灯／消灯／点滅）をHome Assistantから監視できます。

## ファイル構成

```
esphome/
├── pc_power_controller.yaml   ESPHome設定本体
├── secrets.yaml.example        secrets.yaml のテンプレート（実値は別途用意）
└── README.md                   このファイル
```

## セットアップ手順

### 1. secrets.yaml を用意する

```
cp esphome/secrets.yaml.example esphome/secrets.yaml
```

`secrets.yaml` を開き、Wi-Fi SSID/パスワード・フォールバックAPパスワード・
API暗号化キー・OTAパスワードを実際の値に置き換えてください。
**`secrets.yaml` は絶対にgit管理下に置かないでください**（`.gitignore` に
`esphome/secrets.yaml` を追加しておくことを推奨します）。

API暗号化キーは以下で生成できます。

```
python3 -c "import secrets, base64; print(base64.b64encode(secrets.token_bytes(32)).decode())"
```

### 2. 書き込み

**初回（USBシリアル書き込みが必要）**

XIAO ESP32C3をUSB-CケーブルでPCに接続し、ESPHome CLIまたはHome Assistant
の「ESPHome」アドオンのダッシュボードから書き込みます。

```
esphome run esphome/pc_power_controller.yaml
```

Home AssistantのESPHomeアドオンを使う場合は、ダッシュボード上で
`pc_power_controller.yaml` の内容を新規デバイスとして貼り付け、
「Install」→「Plug into this computer」を選択してブラウザ経由で書き込みます。

**2回目以降（OTA更新）**

初回書き込みが完了しデバイスがWi-Fiに接続されていれば、以降は
ESPHomeダッシュボード上で「Install」→「Wirelessly」を選ぶだけで
USB接続なしにファームウェアを更新できます。

### 3. Home Assistantへの統合

デバイスがWi-Fiに接続されると、Home Assistant側に自動的に
「pc-power-controller」という名前のデバイスとして検出通知が出ます
（`api:` コンポーネントによるネイティブAPI連携のため、MQTTブローカーは
不要です）。通知から「設定」→追加すると、以下のエンティティが
**1つのデバイスにまとめて**登録されます。

| エンティティ | 種別 | 役割 |
|---|---|---|
| PC電源ボタン | button | 通常操作（電源ON／スリープ移行など）。200msだけリレーを閉じる |
| PC強制電源OFF | button | 強制シャットダウン。5秒間リレーを閉じ続ける（ATX仕様のハード強制OFFを利用） |
| PC電源LED状態 (生値) | binary_sensor | GPIO4の生値（true = LED点灯） |
| PC電源状態 | text_sensor | "on" / "blinking" / "off" の3値にまとめた状態 |

同じYAMLファイル（同じESP32ノード）内で定義したエンティティは、追加設定
なしでHome Assistant上で自動的に1つのデバイスとしてグルーピングされます。
さらに整理したい場合は、HAの「デバイス」ページからこのデバイスに
「エリア」（例：「書斎」「PCデスク」）を割り当てると、ダッシュボードの
自動生成やGoogle Home連携などでも他の部屋別デバイスと混ざらず扱えます。
（エリア割り当てはHA側の設定で、ESPHome側の変更は不要です。）

## 重要: Windows側の電源ボタン設定はスリープにしてください

PLEDの点滅は、一般的なATXマザーボードでは **ACPIスリープ状態(S1〜S3)** を
示す仕様です。点灯/消灯/点滅の対応関係は次の通りです。

| PLED状態 | ACPI電源状態 | 意味 |
|---|---|---|
| 点灯 | S0 | 通常稼働中 |
| 点滅 | S1〜S3 | スリープ中 |
| 消灯 | S5 | シャットダウン（またはコンセント未接続） |

これはOS・BIOSレベルの電源ステートにのみ連動するハードウェア的な仕様で、
「ディスプレイオフ（モニターのDPMSによる省電力）」とは無関係です。
ディスプレイオフはモニター側が単独で画面出力を止めているだけで、PC本体は
S0（フル稼働）のままのため、**電源ボタンの動作をディスプレイオフに設定して
いると、PLEDは常に点灯のままになり、"blinking" 状態が一切観測されません**
（＝本ファームウェアの点滅判定ロジックが機能しなくなります）。

Windowsの設定は以下の手順で「スリープ」に変更してください。

```
コントロールパネル → ハードウェアとサウンド → 電源オプション
→ 「電源ボタンの動作を選択する」
→ 「電源ボタンを押したときの動作」を「スリープ状態」に設定
```

スリープからの復帰失敗（USB機器やGPUドライバとの相性でブラックアウトした
まま戻らない等）はデスクトップPCで一定確率で起こり得るため、導入前に
手動で数回スリープ→復帰を試して安定性を確認しておくことを推奨します。

## Lovelaceカードの設定例

### 強制電源OFFボタンに確認ダイアログを付ける

誤ってタップしただけで強制シャットダウンが走らないよう、`tap_action` に
`confirmation` を設定します（ESPHome側の変更は不要、HAのLovelace設定のみ）。

```yaml
type: button
entity: button.pc_power_controller_pc_forced_power_off
name: "PC強制電源OFF"
icon: mdi:power-off
tap_action:
  action: call-service
  service: button.press
  target:
    entity_id: button.pc_power_controller_pc_forced_power_off
  confirmation:
    text: "強制的に電源を切ります。作業中のデータが失われる可能性があります。よろしいですか？"
```

より確実にしたい場合は、`input_boolean` で「アーム」状態を別途用意し、
アームがONの間だけ強制OFFの自動化が実行できるようにする二段階方式も
考えられますが、個人利用の規模であれば上記の確認ダイアログで十分な
安全マージンになります。

### 電源状態をアイコンで見やすくする

`PC電源状態` (`text_sensor`) の値（"on" / "blinking" / "off"）に応じて
アイコンを切り替える例です。

```yaml
type: entities
entities:
  - entity: text_sensor.pc_power_controller_pc_power_state
    name: "PC電源状態"
    icon: >-
      {% set s = states('text_sensor.pc_power_controller_pc_power_state') %}
      {% if s == 'on' %}
        mdi:desktop-tower-monitor
      {% elif s == 'blinking' %}
        mdi:sleep
      {% else %}
        mdi:desktop-tower-monitor-off
      {% endif %}
```

（テンプレートアイコンを使う場合は、Lovelace UI編集ではなくYAMLモードで
カードを編集する必要があります。）

### デバイス全体をまとめて表示する

個別にエンティティを指定しなくても、HAの「エリアカード」または
「デバイスに紐づくエンティティカード」を使えば、このデバイスに属する
エンティティ（PC電源ボタン・PC強制電源OFF・PC電源LED状態・PC電源状態）を
自動的に列挙して1枚のカードにまとめられます。

## エンティティIDについて

上記のLovelace例中のエンティティID（`button.pc_power_controller_...` など）
は、`esphome.name: pc-power-controller` から自動生成される標準的な命名
パターンです。実際にHAへ追加した後、「開発者ツール」→「状態」で
生成された正確なエンティティIDを確認し、必要に応じて置き換えてください。
