# pc_power_controller — KiCad プロジェクト

ESP32 で PC電源ボタン（PWR_SW）をフォトMOSリレー経由でON/OFFし、PLED（電源LED）の
点灯状態をフォトカプラ経由で監視するための回路の「回路図」と、ユニバーサル基板への
手配線を前提とした「部品配置＋ラッツネスト確認用PCBレイアウト」です。
**銅箔パターンは作成していません**（配線ガイド用途のみ）。

## ファイル構成

```
circuit/
├── pc_power_controller.kicad_sch   回路図
├── pc_power_controller.kicad_pcb   PCBレイアウト（配置のみ、ルーティング無し）
├── pc_power_controller.kicad_pro   プロジェクトファイル
├── sym-lib-table                  プロジェクト用シンボルライブラリテーブル
├── fp-lib-table                   プロジェクト用フットプリントライブラリテーブル
├── Local.kicad_sym                 自作シンボル（4pinオプトカプラ代替 / XIAO ESP32C3）
├── Local.pretty/
│   └── Seeed_XIAO_ESP32C3.kicad_mod  自作フットプリント（XIAO ESP32C3用）
├── pc_power_controller.net         回路図から書き出したネットリスト（参考用）
├── erc_report.txt / erc_report.json  ERC結果
├── pcb_drc.txt                     PCB DRC結果（未配線=ラッツネスト11本を含む）
├── BOM.md                          部品表（秋月電子リンク付き）
├── scripts/
│   ├── gen_sch.py                  回路図生成スクリプト
│   ├── gen_pcb.py                  PCB自動生成スクリプト（KiCad付属pythonで実行）
│   └── gen_ratsnest_svg.py         配置＋ラッツネストのSVG可視化を書き出すスクリプト
└── output/
    └── placement_guide.svg         配置＋ラッツネストの可視化（SVG）
```

## 開き方

1. KiCad 10.0 系で `pc_power_controller.kicad_pro` を開く（プロジェクトマネージャ経由）。
2. 「回路図エディタ」で `pc_power_controller.kicad_sch` を確認できます。
3. 「PCBエディタ」で `pc_power_controller.kicad_pcb` を開くと、部品が配置された状態で、
   配線されていないネットが**ラッツネスト（黄色い破線のエアワイヤー）として自動的に
   表示されます**（KiCadのPCBエディタは接続情報から自動でラッツネストを描画するため、
   ファイルには線そのものは保存されていません）。
   - ラッツネストが表示されない場合は、メニュー「編集」→「ボードの再構築」
     または表示メニューでラッツネスト表示をONにしてください（デフォルトでON）。

## ERC / DRC 結果

- 回路図ERC: **エラー0件**（`erc_report.txt`）。警告は、手作業で構築したため
  ライブラリキャッシュと実ライブラリのシンボル定義が完全一致しない旨の
  `lib_symbol_mismatch` と、汎用シンボルのピン間隔(1.27mm)由来の
  `endpoint_off_grid` のみで、接続には影響しません。
- PCB DRC: **違反0件、未配線アイテム11件**（`pcb_drc.txt`）。この11件が
  そのまま「ラッツネスト」として表示される未配線のネット接続です
  （= 意図的に配線していない状態）。

## 回路構成の要点

- **XIAO ESP32C3 (U3) D1/GPIO3** → R1(330Ω) → TLP225A(F)(U1) → J1 (PWR_SW_HEADER, 2P)
- J2 (PLED_HEADER, 2P) → TLP621-1(U2) → **XIAO ESP32C3 (U3) D2/GPIO4**
  （R2=10kΩでプルアップ）
- GND / 3V3 はすべて U3（XIAO ESP32C3）のGND / 3V3ピンに集約
  （3V3はXIAO本体のレギュレータ出力をそのまま基板側の電源として使う想定）
- D1/D2（GPIO3/GPIO4）を選んでいるのは、GPIO2・GPIO8・GPIO9
  （XIAOのD0・D8・D9）が ESP32-C3 のストラッピングピンで起動時の挙動に
  影響するため、それらを避けたためです。
- U1は当初TLP222AFを想定していましたが**秋月電子で在庫切れのため
  TLP225A(F)に変更**しています（同一パッケージ・同一ピン配置のため
  回路・フットプリントは変更なし）。
- ESP32本体・TLP225A(F)・TLP621-1 は標準ライブラリに厳密一致するシンボルが無いため、
  以下のように代用しています（各シンボルの `Note` プロパティにも明記済み）。
  - **Seeed XIAO ESP32C3**: 自作シンボル (`Local:Seeed_XIAO_ESP32C3`) ＋
    自作フットプリント (`Local:Seeed_XIAO_ESP32C3`、`Local.pretty/` に格納)。
    XIAO本体は基板に直接ハンダ付けせず、2×7・2.54mmピッチの丸ピンICソケット
    経由で着脱する前提のフットプリントです（詳細はBOM.md）。
  - TLP225A(F) / TLP621-1: 自作の汎用4pinオプトカプラシンボル
    (`Local:Optocoupler_Generic_4Pin`、`Local.kicad_sym` に格納) ＋
    フットプリント `Package_DIP:DIP-4_W7.62mm_Socket`（ICソケット実装想定）

## 基板サイズを変更したい場合

想定している基板サイズは **秋月電子 片面ガラス・ユニバーサル基板 Bタイプ (95×72mm)**
です（`BOM.md` 参照）。手持ちの基板サイズが異なる場合は、

1. `circuit/scripts/gen_pcb.py` を開き、冒頭付近の
   ```python
   BOARD_W = 95.0
   BOARD_H = 72.0
   ```
   を実際のサイズ(mm)に書き換える。
2. KiCad付属のPythonでスクリプトを再実行して `.kicad_pcb` を再生成する。
   ```
   "C:\Program Files\KiCad\10.0\bin\python.exe" circuit\scripts\gen_pcb.py
   ```
   （PCBエディタでEdge.Cutsの矩形を直接ドラッグして編集しても構いません）
3. 部品配置がボード外に出ていないか、PCBエディタで確認してください。

## 配置＋ラッツネストの画像（PNG）について

kicad-cli にはラッツネスト（未配線エアワイヤー）を含めてSVG/PNGへ書き出す機能が
無く、ラッツネストはPCBエディタ上でのみ動的に計算・表示される情報のため、
`kicad-cli pcb export svg` 等では再現できません。

代わりに、`circuit/scripts/gen_ratsnest_svg.py` で `.kicad_pcb` の接続情報
（`BuildConnectivity()`）から各ネットの未配線ペアを取得し、独自にラッツネスト線を
描画したSVGを `circuit/output/placement_guide.svg` として生成しています
（黄色の破線 = ラッツネスト）。そのままブラウザ等で開いて確認できます。
PNG化したい場合は、このSVGをブラウザで開いてスクリーンショットを撮るか、
Inkscape等で `placement_guide.svg` → PNG に変換してください。

実際のPCBエディタでの見た目を確認したい場合は、上記「開き方」の手順で
PCBエディタを開いてください（GUI上のラッツネスト表示が最も正確です）。

再生成する場合:
```
"C:\Program Files\KiCad\10.0\bin\python.exe" circuit\scripts\gen_ratsnest_svg.py
```
