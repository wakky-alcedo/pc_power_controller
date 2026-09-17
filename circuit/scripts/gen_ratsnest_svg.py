import pcbnew

PCB_PATH = r"C:\userfile\circuit\pc_power_controller\circuit\pc_power_controller.kicad_pcb"
SVG_PATH = r"C:\userfile\circuit\pc_power_controller\circuit\output\placement_guide.svg"

board = pcbnew.LoadBoard(PCB_PATH)
board.BuildConnectivity()

to_mm = pcbnew.ToMM

# Board outline bbox from Edge.Cuts
minx = miny = 1e9
maxx = maxy = -1e9
for shape in board.GetDrawings():
    if shape.GetLayer() == pcbnew.Edge_Cuts:
        bb = shape.GetBoundingBox()
        minx = min(minx, to_mm(bb.GetLeft()))
        maxx = max(maxx, to_mm(bb.GetRight()))
        miny = min(miny, to_mm(bb.GetTop()))
        maxy = max(maxy, to_mm(bb.GetBottom()))

pad_by_net = {}
fp_boxes = []
for fp in board.GetFootprints():
    bb = fp.GetBoundingBox()
    fp_boxes.append({
        "ref": fp.GetReference(),
        "value": fp.GetValue(),
        "x": to_mm(bb.GetLeft()),
        "y": to_mm(bb.GetTop()),
        "w": to_mm(bb.GetWidth()),
        "h": to_mm(bb.GetHeight()),
    })
    for pad in fp.Pads():
        net = pad.GetNetname()
        if not net:
            continue
        pos = pad.GetPosition()
        pad_by_net.setdefault(net, []).append((to_mm(pos.x), to_mm(pos.y)))

ratsnest_lines = []
for net, pts in pad_by_net.items():
    if len(pts) < 2:
        continue
    for i in range(len(pts) - 1):
        ratsnest_lines.append((pts[i], pts[i + 1]))

# ---- Build SVG ----
PAD = 8
SCALE = 6
W = (maxx - minx + 2 * PAD) * SCALE
H = (maxy - miny + 2 * PAD) * SCALE


def tx(x):
    return (x - minx + PAD) * SCALE


def ty(y):
    return (y - miny + PAD) * SCALE


parts = []
parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" '
             f'viewBox="0 0 {W:.0f} {H:.0f}">')
parts.append(f'<rect x="0" y="0" width="{W:.0f}" height="{H:.0f}" fill="#1e1e1e"/>')

# Board outline
parts.append(f'<rect x="{tx(minx):.1f}" y="{ty(miny):.1f}" '
             f'width="{(maxx-minx)*SCALE:.1f}" height="{(maxy-miny)*SCALE:.1f}" '
             f'fill="#0a3d0a" stroke="#ffcc00" stroke-width="2"/>')

# Footprint outlines + labels
for b in fp_boxes:
    parts.append(f'<rect x="{tx(b["x"]):.1f}" y="{ty(b["y"]):.1f}" '
                 f'width="{b["w"]*SCALE:.1f}" height="{b["h"]*SCALE:.1f}" '
                 f'fill="#3a5f8a" stroke="#a0c0e0" stroke-width="1.5" opacity="0.85"/>')
    cx = tx(b["x"] + b["w"] / 2)
    cy = ty(b["y"] + b["h"] / 2)
    parts.append(f'<text x="{cx:.1f}" y="{cy-4:.1f}" fill="#ffffff" font-size="13" '
                 f'font-family="monospace" text-anchor="middle">{b["ref"]}</text>')
    parts.append(f'<text x="{cx:.1f}" y="{cy+11:.1f}" fill="#dddddd" font-size="10" '
                 f'font-family="monospace" text-anchor="middle">{b["value"]}</text>')

# Ratsnest (unrouted airwires)
for (x1, y1), (x2, y2) in ratsnest_lines:
    parts.append(f'<line x1="{tx(x1):.1f}" y1="{ty(y1):.1f}" x2="{tx(x2):.1f}" y2="{ty(y2):.1f}" '
                 f'stroke="#ffe066" stroke-width="1.5" stroke-dasharray="4,3"/>')

parts.append(f'<text x="{10*SCALE:.0f}" y="{H-10:.0f}" fill="#888888" font-size="11" '
             f'font-family="monospace">Yellow dashed = ratsnest (unrouted). No copper traces present.</text>')
parts.append('</svg>')

with open(SVG_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(parts))

print("wrote", SVG_PATH, "footprints:", len(fp_boxes), "ratsnest edges:", len(ratsnest_lines))
