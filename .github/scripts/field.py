"""Animated contribution-field SVG: a pixel combine harvests the graph, or a pig eats it."""
import json, sys

data = json.load(open(sys.argv[1]))
mode, out = sys.argv[2], sys.argv[3]
light = len(sys.argv) > 4 and sys.argv[4] == "light"
cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
total = cal["totalContributions"]
LEVEL = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
weeks = cal["weeks"]
NC = len(weeks)

CELL, GAP, OX, OY = 12, 3, 24, 22
STEP = CELL + GAP
W, H = OX * 2 + NC * STEP - GAP, OY + 7 * STEP + 8
if light:
    BG, DIRT, INK = "#F3F5FB", "#E1E6F5", "#4A5580"
    CROP = {1: "#BFE6CF", 2: "#7FCFA0", 3: "#2FA86A", 4: "#E8A317"}
    STUBBLE = "#CFC8B0"
else:
    BG, DIRT, INK = "#0A1033", "#141C4A", "#8D98BF"
    CROP = {1: "#1F5C3F", 2: "#2E8B57", 3: "#4FD18B", 4: "#FFC857"}
    STUBBLE = "#3B3524"
T_MOVE, T = 40.0, 46.0
dt = T_MOVE / (7 * NC)

COMBINE = ["....OO......", "...OWWO.....", "..OOOOOO..Y.", ".OOOOOOOOYYY",
           "OOOOOOOOOYYY", "OOOOOOOOOYYY", ".KK....KK...", ".KK....KK..."]
PIG = ["..P......P..", "..PPPPPPPP..", ".PPPPPPPPPP.", ".PPEPPPPEPP.",
       ".PPPPSSPPPP.", ".PPPPSSPPPP.", "..PPPPPPPP..", "..OOOOOOOO..", "..PP....PP.."]
PAL = {"O": "#F76900", "W": "#FFC857", "Y": "#FFC857", "K": "#C9D1F0",
       "P": "#F4A3A3", "E": "#0B1238", "S": "#E36B7A"}
sprite = COMBINE if mode == "combine" else PIG
PX = 3
sw, sh = len(sprite[0]) * PX, len(sprite) * PX

def t_of(r, c):
    pos = c if r % 2 == 0 else NC - 1 - c
    return (r * NC + pos) * dt

def pct(t): return f"{t / T * 100:.3f}%"

rects, styles = [], []
for c, wk in enumerate(weeks):
    for day in wk["contributionDays"]:
        r = day["weekday"]
        lvl = LEVEL[day["contributionLevel"]]
        x, y = OX + c * STEP, OY + r * STEP
        if lvl == 0:
            rects.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{DIRT}"/>')
            continue
        after = STUBBLE if mode == "combine" else DIRT
        k = f"c{c}_{r}"
        t = t_of(r, c) + dt * 0.5
        styles.append(f"@keyframes {k}{{0%,{pct(t)}{{fill:{CROP[lvl]}}}{pct(t + 0.05)},96%{{fill:{after}}}100%{{fill:{CROP[lvl]}}}}}")
        rects.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{CROP[lvl]}" style="animation:{k} {T}s linear infinite"/>')

# sprite path: serpentine across rows
frames = []
for r in range(7):
    y = OY + r * STEP + CELL / 2
    for c in ([0, NC - 1] if r % 2 == 0 else [NC - 1, 0]):
        x = OX + c * STEP + CELL / 2
        sx = 1 if r % 2 == 0 else -1
        frames.append((t_of(r, c), x, y, sx))
kf = []
for t, x, y, sx in frames:
    kf.append(f"{pct(t)}{{transform:translate({x:.1f}px,{y:.1f}px) scaleX({sx});opacity:1}}")
last = frames[-1]
kf.append(f"{pct(T_MOVE + 0.6)}{{transform:translate({last[1]-60:.1f}px,{last[2]:.1f}px) scaleX(-1);opacity:0}}")
kf.append(f"100%{{transform:translate({frames[0][1]:.1f}px,{frames[0][2]:.1f}px) scaleX(1);opacity:0}}")
styles.append("@keyframes drive{" + "".join(kf) + "}")

px = []
for j, row in enumerate(sprite):
    for i, ch in enumerate(row):
        if ch != ".":
            px.append(f'<rect x="{i*PX - sw/2}" y="{j*PX - sh/2}" width="{PX}" height="{PX}" fill="{PAL[ch]}"/>')

label = "harvesting the contribution graph" if mode == "combine" else "the pig eats the contribution graph"
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">
<style>
text{{font-family:"JetBrains Mono","SFMono-Regular",Consolas,monospace;font-size:13px}}
.bot{{animation:drive {T}s linear infinite;shape-rendering:crispEdges}}
{chr(10).join(styles)}
@media (prefers-reduced-motion:reduce){{rect,.bot{{animation:none!important}}}}
</style>
<rect width="{W}" height="{H}" rx="10" fill="{BG}"/>
{"".join(rects)}
<g class="bot">{"".join(px)}</g>
</svg>'''
open(out, "w", encoding="utf-8").write(svg)
print(mode, len(svg), "bytes")
