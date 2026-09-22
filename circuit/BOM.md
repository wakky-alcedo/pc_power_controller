# BOM (部品表) — pc_power_controller

回路図上の部品と、秋月電子通商での購入先候補です。

| リファレンス | 部品 | 値 / 仕様 | 個数 | 秋月電子 通販コード | リンク |
|---|---|---|---|---|---|
| U3 | Seeed Studio XIAO ESP32C3 | メイン基板側は本機に実装しない前提（2x7 2.54mmピッチのピンソケット経由で着脱） | 1 | 117454 | https://akizukidenshi.com/catalog/g/g117454/ |
| U1 | フォトMOSリレー **TLP225A(F)** | 60V 0.5A, DIP4（TLP222AFの後継/在庫あり品。ピン配置同一のため回路・フットプリントはそのまま流用可） | 1 | 112192 | https://akizukidenshi.com/catalog/g/g112192/ |
| U2 | フォトカプラ TLP621-1 | 赤外LED+フォトトランジスタ, DIP4 | 1 | 107442 | https://akizukidenshi.com/catalog/g/g107442/ |
| U1, U2 用 | 丸ピンICソケット (4P) | DIP-4対応 | 2 | 114240 | https://akizukidenshi.com/catalog/g/g114240/ |
| U3 用 | 丸ピンIC用ソケット (1×40, 切断して2×7として使用) | XIAO ESP32C3実装用（2列×7pin分に切断） | 1 | 101591 | https://akizukidenshi.com/catalog/g/g101591/ |
| R1 | カーボン抵抗 1/4W 330Ω | 330Ω (5%) | 1（100本入り袋を購入） | 125331 | https://akizukidenshi.com/catalog/g/g125331/ |
| R2 | カーボン抵抗 1/4W 10kΩ | 10kΩ (5%) | 1（100本入り袋を購入） | 125103 | https://akizukidenshi.com/catalog/g/g125103/ |
| J1, J2 | ピンヘッダー 1×40 (2.54mmピッチ、切断して2P×2箇所に使用) | PWR_SW_HEADER / PLED_HEADER | 1本（40P、切って4ピン分に使用） | 100167 | https://akizukidenshi.com/catalog/g/g100167/ |
| — | 片面ガラス・ユニバーサル基板 Bタイプ (95×72mm) | 2.54mmピッチ | 1 | 100518 | https://akizukidenshi.com/catalog/g/g100518/ |

## 補足・変更履歴

- **TLP222AF は在庫切れのため TLP225A(F) に変更しました。** 同じ東芝製フォトMOSリレー
  (60V/0.5A, DIP4)で、ピン配置・パッケージが同一のため回路図・フットプリント・
  配線は変更していません（`U1` の `Value` プロパティのみ更新）。
- **ESP32本体は Seeed Studio XIAO ESP32C3 を使用します。** 本基板には
  XIAO本体を直接ハンダ付けせず、丸ピンICソケット(1×40)を2列×7pinに切って
  ソケット実装し、そこにXIAOを挿す前提です（着脱・書き込み用USB接続がしやすいため）。
  - 使用ピン: **D1 (GPIO3)** をリレー制御出力(R1へ)、**D2 (GPIO4)** をPLED監視入力
    (R2プルアップ・U2コレクタへ)に割り当てています。GPIO2/GPIO8/GPIO9
    (D0/D8/D9) はESP32-C3のストラッピングピンのため未使用のまま空けています。
  - 5V(Pin14)は未使用（USB給電のみで運用する場合は接続不要）。GND(Pin13)・
    3V3(Pin12)は基板上のGND/3V3レールに接続されます。XIAOの実物理ピン配列は
    左列(USB側から)がD0〜D6、右列がD7〜D10・3V3・GND・5Vの順（5V/GND/3V3が
    左列先頭ではない点に注意）。詳細はREADME.mdの「XIAOのピン配置」参照。
- R1・R2 は100本入り袋単位でしか販売されていないため、1本のみ必要な場合も袋ごと購入します。
- ユニバーサル基板の実際の手持ちサイズが異なる場合は、`circuit/scripts/gen_pcb.py`
  内の `BOARD_W` / `BOARD_H` を変更し、`.kicad_pcb` を再生成してください
  （詳細はREADME参照）。

秋月電子の商品ページ内容（価格・在庫・仕様）は変更される場合があります。
発注前に最新情報を各リンクで確認してください。
