import uuid

def u():
    return str(uuid.uuid4())

out = []
def w(s=""):
    out.append(s)

w('(kicad_sch (version 20250114) (generator "kicad-manual") (generator_version "10.0")')
w()
w(f'  (uuid {u()})')
w()
w('  (paper "A3")')
w()
w('  (lib_symbols')

# Device:R
w('''    (symbol "Device:R" (pin_numbers hide) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 2.032 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "R" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "" (at -1.778 0 90)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Datasheet" "~" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54)
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
      )
      (symbol "R_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 0 -3.81 90) (length 1.27)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
      )
    )''')

# Connector_Generic:Conn_01x01
w('''    (symbol "Connector_Generic:Conn_01x01" (pin_names (offset 1.016) hide) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 2.54 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Conn_01x01" (at 0 -2.54 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Datasheet" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "Conn_01x01_0_1"
        (rectangle (start -1.27 1.27) (end 1.27 -1.27)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
      )
      (symbol "Conn_01x01_1_1"
        (pin passive line (at -5.08 0 0) (length 3.81)
          (name "Pin_1" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
      )
    )''')

# Connector_Generic:Conn_01x02
w('''    (symbol "Connector_Generic:Conn_01x02" (pin_names (offset 1.016) hide) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 3.81 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Conn_01x02" (at 0 -3.81 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Datasheet" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "Conn_01x02_0_1"
        (rectangle (start -1.27 2.54) (end 1.27 -3.81)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
      )
      (symbol "Conn_01x02_1_1"
        (pin passive line (at -5.08 0 0) (length 3.81)
          (name "Pin_1" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at -5.08 -2.54 0) (length 3.81)
          (name "Pin_2" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
      )
    )''')

# Custom generic 4-pin optocoupler (used for TLP222AF / TLP621-1 substitution)
w('''    (symbol "Local:Optocoupler_Generic_4Pin" (pin_names (offset 1.016) hide) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 3.81 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Optocoupler_Generic_4Pin" (at 0 -3.81 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Datasheet" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "Optocoupler_Generic_4Pin_0_1"
        (rectangle (start -3.81 3.175) (end 3.81 -3.175)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
        (polyline
          (pts (xy -1.905 -0.635) (xy 1.905 0.635))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
      )
      (symbol "Optocoupler_Generic_4Pin_1_1"
        (pin passive line (at -5.08 2.54 0) (length 2.54)
          (name "1" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at -5.08 -2.54 0) (length 2.54)
          (name "2" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 5.08 2.54 180) (length 2.54)
          (name "3" (effects (font (size 1.27 1.27))))
          (number "3" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 5.08 -2.54 180) (length 2.54)
          (name "4" (effects (font (size 1.27 1.27))))
          (number "4" (effects (font (size 1.27 1.27))))
        )
      )
    )''')

# power:GND
w('''    (symbol "power:GND" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -6.35 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Value" "GND" (at 0 -3.81 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Datasheet" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "GND_0_1"
        (polyline
          (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
      )
      (symbol "GND_1_1"
        (pin power_in line (at 0 0 270) (length 0) hide
          (name "GND" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
      )
    )''')

# power:+3V3
w('''    (symbol "power:+3V3" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 3.556 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Value" "+3V3" (at 0 3.556 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Datasheet" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "+3V3_0_1"
        (polyline
          (pts (xy -0.762 1.27) (xy 0 2.54))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (polyline
          (pts (xy 0 0) (xy 0 2.54))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (polyline
          (pts (xy 0 2.54) (xy 0.762 1.27))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
      )
      (symbol "+3V3_1_1"
        (pin power_in line (at 0 0 90) (length 0) hide
          (name "+3V3" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
      )
    )''')

# power:PWR_FLAG
w('''    (symbol "power:PWR_FLAG" (power) (pin_names (offset 0)) (in_bom yes) (on_board no)
      (property "Reference" "#FLG" (at 0 1.905 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Value" "PWR_FLAG" (at 0 3.81 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Datasheet" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "PWR_FLAG_0_0"
        (pin power_out line (at 0 0 90) (length 0) hide
          (name "pwr" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
      )
      (symbol "PWR_FLAG_0_1"
        (circle (center 0 1.905) (radius 0.635)
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (polyline
          (pts (xy 0 1.27) (xy 0 0))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (polyline
          (pts (xy 0 2.54) (xy -1.016 3.81))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (polyline
          (pts (xy 0 2.54) (xy 1.016 3.81))
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
      )
    )''')

# Local:Seeed_XIAO_ESP32C3 (14-pin module). Pin numbering/positions match the
# REAL physical silkscreen layout confirmed from Seeed's own pinout docs:
# left column, top-to-bottom (near the USB-C connector at the top): D0, D1,
# D2, D3, D4, D5, D6 (pins 1-7); right column, bottom-to-top: D7, D8, D9,
# D10, 3V3, GND, 5V (pins 8-14). Note 5V/GND/3V3 are NOT the first pins next
# to the USB connector -- they're clustered at the far end of the right
# column, directly across from D0-D2.
w('''    (symbol "Local:Seeed_XIAO_ESP32C3" (pin_names (offset 1.016) hide) (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 10.16 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Seeed_XIAO_ESP32C3" (at 0 -10.16 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Datasheet" "" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "Seeed_XIAO_ESP32C3_0_1"
        (rectangle (start -7.62 8.89) (end 7.62 -8.89)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
      )
      (symbol "Seeed_XIAO_ESP32C3_1_1"
        (pin bidirectional line (at -10.16 7.62 0) (length 2.54)
          (name "D0/GPIO2" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at -10.16 5.08 0) (length 2.54)
          (name "D1/GPIO3" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at -10.16 2.54 0) (length 2.54)
          (name "D2/GPIO4" (effects (font (size 1.27 1.27))))
          (number "3" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at -10.16 0 0) (length 2.54)
          (name "D3/GPIO5" (effects (font (size 1.27 1.27))))
          (number "4" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at -10.16 -2.54 0) (length 2.54)
          (name "D4/GPIO6" (effects (font (size 1.27 1.27))))
          (number "5" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at -10.16 -5.08 0) (length 2.54)
          (name "D5/GPIO7" (effects (font (size 1.27 1.27))))
          (number "6" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at -10.16 -7.62 0) (length 2.54)
          (name "D6/GPIO21" (effects (font (size 1.27 1.27))))
          (number "7" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at 10.16 -7.62 180) (length 2.54)
          (name "D7/GPIO20" (effects (font (size 1.27 1.27))))
          (number "8" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at 10.16 -5.08 180) (length 2.54)
          (name "D8/GPIO8" (effects (font (size 1.27 1.27))))
          (number "9" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at 10.16 -2.54 180) (length 2.54)
          (name "D9/GPIO9" (effects (font (size 1.27 1.27))))
          (number "10" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at 10.16 0 180) (length 2.54)
          (name "D10/GPIO10" (effects (font (size 1.27 1.27))))
          (number "11" (effects (font (size 1.27 1.27))))
        )
        (pin power_out line (at 10.16 2.54 180) (length 2.54)
          (name "3V3" (effects (font (size 1.27 1.27))))
          (number "12" (effects (font (size 1.27 1.27))))
        )
        (pin power_in line (at 10.16 5.08 180) (length 2.54)
          (name "GND" (effects (font (size 1.27 1.27))))
          (number "13" (effects (font (size 1.27 1.27))))
        )
        (pin power_in line (at 10.16 7.62 180) (length 2.54)
          (name "5V" (effects (font (size 1.27 1.27))))
          (number "14" (effects (font (size 1.27 1.27))))
        )
      )
    )''')

w('  )')
w()

instances = []  # (reference, order_num) for symbol_instances section

def add_symbol(lib_id, ref, value, at, rot, pins_map, footprint="", extra_props=None, in_bom=True, on_board=True, mirror=None):
    """pins_map: dict pin_number -> uuid"""
    uid = u()
    lines = []
    mirror_s = f" (mirror {mirror})" if mirror else ""
    lines.append(f'  (symbol (lib_id "{lib_id}") (at {at[0]} {at[1]} {rot}){mirror_s} (unit 1)')
    lines.append(f'    (in_bom {"yes" if in_bom else "no"}) (on_board {"yes" if on_board else "no"})')
    lines.append(f'    (uuid {uid})')
    lines.append(f'    (property "Reference" "{ref}" (at {at[0]} {at[1]-2.54} 0)')
    lines.append('      (effects (font (size 1.27 1.27)))')
    lines.append('    )')
    lines.append(f'    (property "Value" "{value}" (at {at[0]} {at[1]+2.54} 0)')
    lines.append('      (effects (font (size 1.27 1.27)))')
    lines.append('    )')
    fp_hide = ' hide' if footprint == "" else ''
    lines.append(f'    (property "Footprint" "{footprint}" (at {at[0]} {at[1]} 0)')
    lines.append(f'      (effects (font (size 1.27 1.27)){fp_hide})')
    lines.append('    )')
    lines.append(f'    (property "Datasheet" "" (at {at[0]} {at[1]} 0)')
    lines.append('      (effects (font (size 1.27 1.27)) hide)')
    lines.append('    )')
    if extra_props:
        for pname, pval in extra_props:
            lines.append(f'    (property "{pname}" "{pval}" (at {at[0]} {at[1]} 0)')
            lines.append('      (effects (font (size 1.27 1.27)) hide)')
            lines.append('    )')
    for pnum in pins_map:
        lines.append(f'    (pin "{pnum}" (uuid {pins_map[pnum]}))')
    lines.append('  )')
    w('\n'.join(lines))
    w()
    instances.append((ref, uid))
    return uid

# ---- Component placements ----
# All coordinates below are chosen so that every PIN (not necessarily every
# component's own "at" origin) lands on an exact multiple of 2.54mm -- that's
# what ERC's connection-grid check and clean hand-wiring both care about.
# Device:R's pin offset (+-3.81mm = 1.5 grid squares) means an R symbol's own
# origin unavoidably sits at a half-grid (odd x1.27mm) position for its pins
# to hit the 2.54mm grid; every other symbol here (Optocoupler, Connector,
# XIAO, power) has pin offsets that are themselves exact 2.54mm multiples, so
# their own origins land on-grid too.

# CONTROL PATH (XIAO D1/GPIO3 -> R1 -> U1(TLP225A(F)) -> J1 PWR_SW_HEADER)
R1_pos = (38.1, 34.29)
p_R1_1 = u(); p_R1_2 = u()
add_symbol("Device:R", "R1", "330", R1_pos, 0,
           {"1": p_R1_1, "2": p_R1_2}, footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal")

U1_pos = (53.34, 33.02)
p_U1_1 = u(); p_U1_2 = u(); p_U1_3 = u(); p_U1_4 = u()
add_symbol("Local:Optocoupler_Generic_4Pin", "U1", "TLP225A(F)", U1_pos, 0,
           {"1": p_U1_1, "2": p_U1_2, "3": p_U1_3, "4": p_U1_4},
           footprint="Package_DIP:DIP-4_W7.62mm_Socket",
           extra_props=[("Note", "Substitute: generic 4-pin optocoupler symbol / DIP-4 socket footprint. TLP225A(F) PhotoMOS relay (pin-compatible replacement for TLP222AF, which is out of stock)")])

J1_pos = (63.5, 30.48)
p_J1_1 = u(); p_J1_2 = u()
add_symbol("Connector_Generic:Conn_01x02", "J1", "PWR_SW_HEADER", J1_pos, 0,
           {"1": p_J1_1, "2": p_J1_2}, footprint="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical")

GND1_pos = (48.26, 40.64)
p_GND1 = u()
add_symbol("power:GND", "#PWR01", "GND", GND1_pos, 0, {"1": p_GND1}, in_bom=False, on_board=False)

# MONITOR PATH (PLED_HEADER J2 -> U2(TLP621-1) -> GND / GPIO_MON, R2 pullup to 3V3)
J2_pos = (25.4, 20.32)
p_J2_1 = u(); p_J2_2 = u()
add_symbol("Connector_Generic:Conn_01x02", "J2", "PLED_HEADER", J2_pos, 0,
           {"1": p_J2_1, "2": p_J2_2}, footprint="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical")

U2_pos = (25.4, 22.86)
p_U2_1 = u(); p_U2_2 = u(); p_U2_3 = u(); p_U2_4 = u()
add_symbol("Local:Optocoupler_Generic_4Pin", "U2", "TLP621-1", U2_pos, 0,
           {"1": p_U2_1, "2": p_U2_2, "3": p_U2_3, "4": p_U2_4},
           footprint="Package_DIP:DIP-4_W7.62mm_Socket",
           extra_props=[("Note", "Substitute: generic 4-pin optocoupler symbol / DIP-4 socket footprint for TLP621-1")])

GND2_pos = (30.48, 15.24)
p_GND2 = u()
add_symbol("power:GND", "#PWR02", "GND", GND2_pos, 0, {"1": p_GND2}, in_bom=False, on_board=False)

R2_pos = (88.9, 34.29)
p_R2_1 = u(); p_R2_2 = u()
add_symbol("Device:R", "R2", "10k", R2_pos, 0,
           {"1": p_R2_1, "2": p_R2_2}, footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal")

PWR3V3_1_pos = (88.9, 25.4)  # above R2 pin1 -- must NOT share y with the
                              # GPIO_MON stub on R2 pin2, or the straight
                              # vertical wire down to it would electrically
                              # merge the two nets
p_3V3_1 = u()
add_symbol("power:+3V3", "#PWR03", "+3V3", PWR3V3_1_pos, 0, {"1": p_3V3_1}, in_bom=False, on_board=False)

# Seeed XIAO ESP32C3 module (U3). D1/GPIO3 drives the control path, D2/GPIO4
# reads the monitor path. Both are ordinary GPIOs on the C3 (no ADC/strapping
# concerns); GPIO2/GPIO8/GPIO9 (D0/D8/D9) are avoided since those are strapping
# pins on ESP32-C3.
XIAO_pos = (15.24, 35.56)
xiao_pins = {str(i): u() for i in range(1, 15)}
add_symbol("Local:Seeed_XIAO_ESP32C3", "U3", "Seeed_XIAO_ESP32C3", XIAO_pos, 0,
           xiao_pins, footprint="Local:Seeed_XIAO_ESP32C3",
           extra_props=[("Note", "Seeed Studio XIAO ESP32C3, mounted on 2x7 2.54mm female headers. Pin2=D1/GPIO3 (relay control out), Pin3=D2/GPIO4 (PLED monitor in). Pin order matches Seeed's real silkscreen: left column D0-D6 (pins 1-7), right column D7-D10,3V3,GND,5V (pins 8-14)")])

GND3_pos = (25.4, 30.48)  # coincides with XIAO pin13 (GND)
p_GND3 = u()
add_symbol("power:GND", "#PWR04", "GND", GND3_pos, 0, {"1": p_GND3}, in_bom=False, on_board=False)

PWR3V3_2_pos = (25.4, 33.02)  # coincides with XIAO pin12 (3V3)
p_3V3_2 = u()
add_symbol("power:+3V3", "#PWR05", "+3V3", PWR3V3_2_pos, 0, {"1": p_3V3_2}, in_bom=False, on_board=False)

# PWR_FLAG on the GND net only: GND's pin type is power_in, so it still needs
# an explicit "this net is externally driven" marker for ERC. +3V3 does NOT
# get one here -- XIAO pin 3 is itself typed power_out (the module's own
# regulator supplies this rail), so it already satisfies ERC as the driver;
# adding a PWR_FLAG (also power_out) on top of it trips a power_out-vs-
# power_out conflict.
PWRFLAG1_pos = GND3_pos
p_pf1 = u()
add_symbol("power:PWR_FLAG", "#FLG01", "PWR_FLAG", PWRFLAG1_pos, 0, {"1": p_pf1}, in_bom=False, on_board=False)

# ---- Wires ----
def wire(p1, p2):
    w(f'  (wire (pts (xy {p1[0]} {p1[1]}) (xy {p2[0]} {p2[1]}))')
    w('    (stroke (width 0) (type default))')
    w(f'    (uuid {u()})')
    w('  )')
    w()

def label(text, pos):
    w(f'  (label "{text}" (at {pos[0]} {pos[1]} 0)')
    w('    (effects (font (size 1.27 1.27)) (justify left))')
    w(f'    (uuid {u()})')
    w('  )')
    w()

def no_connect(pos):
    w(f'  (no_connect (at {pos[0]} {pos[1]})')
    w(f'    (uuid {u()})')
    w('  )')
    w()

# Pin absolute coords for rotation-0 placements: KiCad's schematic canvas uses
# a Y-down page, so a pin defined at local (px,py) maps to (compX+px, compY-py)
# even with zero symbol rotation. All transforms below apply that Y flip.
def pin_abs(pos, rel):
    return (pos[0] + rel[0], pos[1] - rel[1])

R1_p1 = pin_abs(R1_pos, (0, 3.81)); R1_p2 = pin_abs(R1_pos, (0, -3.81))
U1_p1 = pin_abs(U1_pos, (-5.08, 2.54)); U1_p2 = pin_abs(U1_pos, (-5.08, -2.54))
U1_p3 = pin_abs(U1_pos, (5.08, 2.54)); U1_p4 = pin_abs(U1_pos, (5.08, -2.54))
J1_p1 = pin_abs(J1_pos, (-5.08, 0)); J1_p2 = pin_abs(J1_pos, (-5.08, -2.54))

J2_p1 = pin_abs(J2_pos, (-5.08, 0)); J2_p2 = pin_abs(J2_pos, (-5.08, -2.54))
U2_p1 = pin_abs(U2_pos, (-5.08, 2.54)); U2_p2 = pin_abs(U2_pos, (-5.08, -2.54))
U2_p3 = pin_abs(U2_pos, (5.08, 2.54)); U2_p4 = pin_abs(U2_pos, (5.08, -2.54))
R2_p1 = pin_abs(R2_pos, (0, 3.81)); R2_p2 = pin_abs(R2_pos, (0, -3.81))

# XIAO pin absolute positions (left pins 1-7 point left/angle0, right pins
# 8-14 point right/angle180 -- direction doesn't affect the Y-flip transform)
XIAO_pin = {}
left_rel_y = {1: 7.62, 2: 5.08, 3: 2.54, 4: 0, 5: -2.54, 6: -5.08, 7: -7.62}
right_rel_y = {8: -7.62, 9: -5.08, 10: -2.54, 11: 0, 12: 2.54, 13: 5.08, 14: 7.62}
for n, ry in left_rel_y.items():
    XIAO_pin[n] = pin_abs(XIAO_pos, (-10.16, ry))
for n, ry in right_rel_y.items():
    XIAO_pin[n] = pin_abs(XIAO_pos, (10.16, ry))

def route(p1, p2):
    """Route a possibly-bent wire: horizontal from p1 then vertical into p2.
    Only used for short local stubs to a power symbol (never for inter-
    component signal runs -- those all go through stub_label() instead so
    the diagram doesn't have long wires criss-crossing the page)."""
    if p1[0] == p2[0] or p1[1] == p2[1]:
        wire(p1, p2)
    else:
        bend = (p2[0], p1[1])
        wire(p1, bend)
        wire(bend, p2)

def stub_label(pin, direction, text):
    """Draw a short (1 grid step) stub outward from `pin` in `direction`
    (dx, dy each in {-1, 0, 1}) and place a same-named label at its end.
    Every signal connection between two components uses this instead of a
    direct wire, so nets are joined by label text rather than long routed
    wires across the page."""
    end = (pin[0] + direction[0] * 2.54, pin[1] + direction[1] * 2.54)
    wire(pin, end)
    label(text, end)

# ---- Control path: XIAO D1/GPIO3 -> R1 -> U1(TLP225A(F)) -> J1 (PWR_SW_HEADER) ----
stub_label(XIAO_pin[2], (-1, 0), "GPIO_CTRL")
stub_label(R1_p2, (0, 1), "GPIO_CTRL")

stub_label(R1_p1, (0, -1), "CTRL_R1_U1")
stub_label(U1_p1, (-1, 0), "CTRL_R1_U1")

route(U1_p2, GND1_pos)

stub_label(U1_p3, (1, 0), "PWR_SW_A")
stub_label(J1_p1, (-1, 0), "PWR_SW_A")
stub_label(U1_p4, (1, 0), "PWR_SW_B")
stub_label(J1_p2, (-1, 0), "PWR_SW_B")

# ---- Monitor path: J2 (PLED_HEADER) -> U2(TLP621-1) -> GND / XIAO D2/GPIO4 (+ R2 pull-up) ----
stub_label(J2_p1, (-1, 0), "PLED_A")
stub_label(U2_p1, (-1, 0), "PLED_A")
stub_label(J2_p2, (-1, 0), "PLED_B")
stub_label(U2_p2, (-1, 0), "PLED_B")

route(U2_p3, GND2_pos)

stub_label(U2_p4, (1, 0), "GPIO_MON")
stub_label(R2_p2, (0, 1), "GPIO_MON")
stub_label(XIAO_pin[3], (-1, 0), "GPIO_MON")

route(R2_p1, PWR3V3_1_pos)

# XIAO bulk GND / 3V3 (power symbols placed exactly at the pins, no wire needed)
# (implicit connection: GND3_pos == XIAO_pin[13], PWR3V3_2_pos == XIAO_pin[12])

# Unused XIAO pins: D0(1), D3(4), D4(5), D5(6), D6(7), D7(8), D8(9), D9(10), D10(11), 5V(14)
for n in (1, 4, 5, 6, 7, 8, 9, 10, 11, 14):
    no_connect(XIAO_pin[n])

w('  (sheet_instances')
w('    (path "/" (page "1"))')
w('  )')
w(')')
w()

with open(r"C:\userfile\circuit\pc_power_controller\circuit\pc_power_controller.kicad_sch", "w", encoding="utf-8") as f:
    f.write('\n'.join(out))

print("wrote schematic, symbols:", len(instances))
