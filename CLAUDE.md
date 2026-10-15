# Büyücünün Odası — notes for Claude

A small browser 3D game: a Hogwarts-style tower dormitory, a shared corridor and an open terrace above the clouds.
Everything lives in **one file, `index.html`** (Three.js 0.169 + cannon-es 0.20 from jsDelivr via an import map, no build step).
The UI text is **Turkish**; keep it that way.

## How work arrives here

Change requests are typed into a Claude Code cloud session by **Muse** (Meta's AI agent) on behalf of the owner.
Muse then plays the published build and comes back with feedback in the same session. So for every request:

1. Make the change in `index.html` (and `models/` if an asset is added).
2. Run `python tools/check.py` — it syntax-checks the module script with Node. You cannot open a browser here, so this is the minimum check; re-read the code you touched for runtime mistakes (undefined names, wrong order of declarations, NaN-producing math).
3. Commit with a short Turkish message and **push the current branch**. Any push to any branch triggers `.github/workflows/pages.yml`, which publishes to **https://tanisman441.github.io/buyucu-oda/** in ~1–2 minutes.
4. Reply in Turkish, short, in this shape:
   - **Ne değişti:** 1–3 bullets.
   - **Nasıl denenir:** concrete steps (where to walk, which key, what should happen).
   - **Sürüm:** the short commit sha. The game shows `sürüm <sha> · <dal> · <saat>` in the bottom-right corner, so Muse can confirm the new build loaded (reload with `?v=<sha>` to skip cache).

Keep each change small and testable; if a request is large, split it and say what comes next.

## Code map (`index.html`, sections start with `// ----------------`)

- textures (procedural canvas textures: stone, planks, rug, sky, flame/glow sprites)
- room (walls via `wall()`, window `WIN`, curtains), lights (`sun` follows the player, `hemi`, `winFill`, god-ray `rayMat`)
- furniture (bed, trunk, desk, wand, fireplace `FIRE`, cauldron, bookshelf, banner, rug, floating candles, dust)
- castle (door `doorState`, corridor `CX0..CX1 / CZ0..CZ1`, terrace `TX0..TX1 / TZ0..TZ1`, library east of the corridor (`libDoor`, `LIB_BOOKS`, `CX1+T..LX1 / LZ0..LZ1`), Great Hall south of the corridor (`HALL`, `hallDoor`, `updateHall()`), house dormitory east of the tower room (`DORM`, `dormDoor`, `paintDorm()`, `rest()`), spell-practice targets on the terrace (`dummies`, `hitDummy()`, `updatePractice()`), spell classroom north of the corridor (`CLASS`, `classDoor`, `BOARD_LINES`), owlery in the terrace's north-east corner (`OWL`, `owlDoor`, `owls`, `updateOwls()`; round walls = ring of `box()` colliders + `owlDoorBox`), sky dome, distant towers, clouds) and **`zones` + `walkable()`**: the wizard may only stand inside these rectangles — extend `zones` when adding walkable space (a zone with `gate: <door state>` is only walkable while that door is open), and `box()` adds rectangular obstacles
- sound (`sfx`, all procedural Web Audio, positional; `star`, `fanfare`, `dialog`, `hit`, …; mute button `#snd` / M key, localStorage `buyucu-ses`)
- physics (`world`; meshes tagged with `solid()` become static boxes, `loose(mesh, kg, kind)` or `userData.dynGroup` become movable objects)
- character (KayKit Mage GLB restyled; `wiz.act` animations, `playOnce()` for one-shots)
- collectible stars (`STARS`, `collectStar()`, localStorage `buyucu-yildizlar`)
- composer (bloom, grade), input, quests (`Q`, `setQuest`), interactions (`currentAction()` drives the E key and the bottom hint), lights state (`lights`), spell (force orb), levitation (right-click grab, curtains drag), main loop `frame()`

`window.__dbg` exposes helpers (teleport via `__dbg.wiz.root.position`, `setView`, `frame`, …) for debugging — keep it.

## Rules

- No bundler, no npm install for the game; pin CDN versions exactly.
- Third-party assets must be CC0 or similarly free; record them in `models/CREDITS.txt`.
- Never commit secrets. The repo is public.
