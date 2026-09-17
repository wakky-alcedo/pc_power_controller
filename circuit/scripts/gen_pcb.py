# Run with KiCad's bundled python: "C:/Program Files/KiCad/10.0/bin/python.exe" gen_pcb.py
import pcbnew

FP_ROOT = "C:/Program Files/KiCad/10.0/share/kicad/footprints"
LOCAL_FP_ROOT = r"C:\userfile\circuit\pc_power_controller\circuit\Local.pretty"
OUT_PCB = r"C:\userfile\circuit\pc_power_controller\circuit\pc_power_controller.kicad_pcb"

board = pcbnew.BOARD()
board.SetFileName(OUT_PCB)

mm = pcbnew.FromMM

# ---- Board outline: 95 x 72 mm rectangle on Edge.Cuts ----
# NOTE: change BOARD_W / BOARD_H below if your universal prototyping board
# (e.g. Akizuki "B" type) has different actual dimensions.
BOARD_W = 95.0
BOARD_H = 72.0
ORIGIN = (10.16, 10.16)  # top-left corner of the board outline in mm (4 x 2.54mm)

corners = [
    (ORIGIN[0], ORIGIN[1]),
    (ORIGIN[0] + BOARD_W, ORIGIN[1]),
    (ORIGIN[0] + BOARD_W, ORIGIN[1] + BOARD_H),
    (ORIGIN[0], ORIGIN[1] + BOARD_H),
]
for i in range(4):
    seg = pcbnew.PCB_SHAPE(board)
    seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
    seg.SetStart(pcbnew.VECTOR2I(mm(corners[i][0]), mm(corners[i][1])))
    nxt = corners[(i + 1) % 4]
    seg.SetEnd(pcbnew.VECTOR2I(mm(nxt[0]), mm(nxt[1])))
    seg.SetLayer(pcbnew.Edge_Cuts)
    seg.SetWidth(mm(0.15))
    board.Add(seg)


def load_fp(lib_dir, fp_name):
    lib_path = f"{FP_ROOT}/{lib_dir}.pretty"
    fp = pcbnew.FootprintLoad(lib_path, fp_name)
    if fp is None:
        raise RuntimeError(f"footprint not found: {lib_dir}:{fp_name}")
    return fp


def load_local_fp(fp_name):
    fp = pcbnew.FootprintLoad(LOCAL_FP_ROOT, fp_name)
    if fp is None:
        raise RuntimeError(f"local footprint not found: {fp_name}")
    return fp


def place(fp, ref, value, x, y, rot_deg=0.0):
    fp.SetReference(ref)
    fp.SetValue(value)
    fp.SetPosition(pcbnew.VECTOR2I(mm(ORIGIN[0] + x), mm(ORIGIN[1] + y)))
    fp.SetOrientationDegrees(rot_deg)
    board.Add(fp)
    return fp


def get_net(name):
    ni = board.FindNet(name)
    if ni is None:
        ni = pcbnew.NETINFO_ITEM(board, name)
        board.Add(ni)
    return ni


def assign(fp, pad_number, net_name):
    pad = fp.FindPadByNumber(pad_number)
    if pad is None:
        raise RuntimeError(f"pad {pad_number} not found on {fp.GetReference()}")
    pad.SetNet(get_net(net_name))


# ---- Placement plan (mm, relative to board ORIGIN) ----
# Layout mirrors a hand-wired universal-board build: sockets for the two
# optocouplers grouped together in the middle, headers (J1/J2) pushed to the
# board edges for easy hand wiring, resistors alongside their associated
# optocoupler, and the Seeed XIAO ESP32C3 module (on 2x7 female headers)
# placed centrally so both R1 and R2/U2 are within easy reach of its D1/D2 pins.

# Control path (top row): XIAO D1/GPIO3 -> R1 -> U1(TLP225A(F) socket) -> J1 (PWR_SW_HEADER, edge)
# All x,y offsets below are exact multiples of 2.54mm so every pad lands on
# a standard perfboard hole.
R1 = place(load_fp("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"),
           "R1", "330", 25.4, 12.7)
U1 = place(load_fp("Package_DIP", "DIP-4_W7.62mm_Socket"),
           "U1", "TLP225A(F)", 45.72, 12.7)
J1 = place(load_fp("Connector_PinHeader_2.54mm", "PinHeader_1x02_P2.54mm_Vertical"),
           "J1", "PWR_SW_HEADER", 88.9, 12.7, rot_deg=90)

# Monitor path (second row): J2 (PLED_HEADER, edge) -> U2(TLP621-1 socket) -> R2 pull-up
J2 = place(load_fp("Connector_PinHeader_2.54mm", "PinHeader_1x02_P2.54mm_Vertical"),
           "J2", "PLED_HEADER", 7.62, 30.48, rot_deg=90)
U2 = place(load_fp("Package_DIP", "DIP-4_W7.62mm_Socket"),
           "U2", "TLP621-1", 45.72, 30.48)
R2 = place(load_fp("Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"),
           "R2", "10k", 68.58, 30.48)

# Seeed XIAO ESP32C3, mounted on 2x7 2.54mm female headers soldered to the
# universal board (pads sized for standard header sockets, not castellation).
U3 = place(load_local_fp("Seeed_XIAO_ESP32C3"),
           "U3", "Seeed_XIAO_ESP32C3", 17.78, 53.34)

# ---- Net assignments (mirrors the schematic connectivity) ----
assign(U3, "5", "GPIO_CTRL")   # D1/GPIO3 -> R1
assign(R1, "2", "GPIO_CTRL")
assign(R1, "1", "R1_U1")
assign(U1, "1", "R1_U1")
assign(U1, "2", "GND")
assign(U1, "3", "PWR_SW_A")
assign(U1, "4", "PWR_SW_B")
assign(J1, "1", "PWR_SW_A")
assign(J1, "2", "PWR_SW_B")

assign(J2, "1", "PLED_A")
assign(J2, "2", "PLED_B")
assign(U2, "1", "PLED_A")
assign(U2, "2", "PLED_B")
assign(U2, "3", "GND")
assign(U2, "4", "GPIO_MON")
assign(R2, "2", "GPIO_MON")
assign(R2, "1", "3V3")
assign(U3, "6", "GPIO_MON")    # D2/GPIO4 <- R2 / U2 collector

assign(U3, "2", "GND")         # XIAO GND
assign(U3, "3", "3V3")         # XIAO 3V3 (module's own regulator output)
# XIAO pins 1 (5V), 4, 7-14 are intentionally left with no net (unused).

board.BuildConnectivity()
pcbnew.SaveBoard(OUT_PCB, board)
print("Saved", OUT_PCB)
print("Ratsnest edges (unrouted):", board.GetConnectivity().GetRatsnestForItem if False else "see GUI")
