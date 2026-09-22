# TREES 4.0.0
[Русская версия](README.ru.md)

A Lua script for Axiom that generates highly configurable trees.

**Donate:** https://www.donationalerts.com/r/rock389

> [!CAUTION]
> **Important:** When copying a preset, delete all existing code first, otherwise the sliders won't update! (may have been fixed in the latest Axiom version, but probably not)

## Block Selection

Unfortunately, there's no proper way to select blocks via buttons, so you'll have to do it via code.

At the beginning of the script there are lines:

- `trunk["blocks"] = {...}` — trunk
- `trunk["bark_blocks"] = {...}` — trunk bark blocks
- `trunk["outside_blocks"] = {...}` — additional blocks* around the trunk
- `branches["blocks"] = {...}` — branches
- `branches["bark_blocks"] = {...}` — branch bark blocks
- `branches["outside_blocks"] = {...}` — additional blocks* around branches
- `leaves["blocks"] = {...}` — leaves
- `leaves["outside_blocks"] = {...}` — outer leaves layer
- `oriented_blocks = {...}` — blocks that need proper orientation (fences, panes, slabs, trapdoors)

*additional blocks are essentially trunk smoothing in certain non-random spots

Instead of `...`, list the blocks separated by commas using `blocks.<block_name>`. Example:

`trunk["blocks"] = {blocks.oak_wood, blocks.spruce_wood}`

If you need to change a block state (e.g. candle count), use `withBlockProperty`:

`candle2 = withBlockProperty(blocks.brown_candle, "candles=2")`

`leaves["outside_blocks"] = {candle2}`

Blocks listed in `oriented_blocks` will automatically connect to adjacent blocks (fences and walls, glass panes, slabs, trapdoors, signs (wall_sign)).

## Parameters

Some parameters are in the code, others are sliders. If you add too many sliders, the interface becomes unusable — this bug can't be fixed (I contacted the mod's developer).

**If an error occurs when spawning a tree, it's most likely because some parameter has a min value greater than its max.**

### Slider Parameters

#### Trunk

| Parameter | Description |
|-----------|-------------|
| `min/max_height` | Trunk height range |
| `min/max_curve` | Trunk tilt angle range (degrees) |
| `min/max_width` | Width of the top and base (block count, not radius) |
| `generate_leaves` | 1 — generate leaves around the trunk, 0 — don't |

#### Branches

| Parameter | Description |
|-----------|-------------|
| `min/max_count` | Number of branches |
| `min/max_length` | Branch length |
| `min/max_curve` | Branch tilt angle (0 — perpendicular, >0 — upward, <0 — downward) |
| `min/max_width` | Width of branch end and start |
| `generate_leaves` | 1 — generate leaves around branches, 0 — don't |

#### Leaves

| Parameter | Description |
|-----------|-------------|
| `density` | Leaves density (0–100%) |
| `outside_density` | Outer leaves layer density (0–100%) |
| `min/max_width` | Leaves thickness (radius) |
| `min_start_height` / `max_start_height` | Range for the minimum leaf spawn height (a value is randomly picked from it) |

### In-Code Parameters
*Parameters with curly brackets, e.g. {1, 2}, mean that 1 is min value and 2 is max value*

#### Trunk

| Parameter | Description |
|-----------|-------------|
| `trunk["count"]` | Minimum and maximum number of trunks |
| `trunk["algorithm"]` | 1 — random (noisy), 2 — smooth |
| `trunk["bark_density"]` | Trunk bark density/frequency (0-100%) |
| `trunk["gradient_mode"]` | 1 — enable gradient mode for trunk blocks, 0 — disable. When gradient mode is on, blocks from `trunk["blocks"]` are not picked randomly but form a gradient |

#### Branches

| Parameter | Description |
|-----------|-------------|
| `branches["algorithm"]` | 1 — random, 2 — smooth |
| `branches["curve_algorithm"]` | 1 — sine curve, 2 — linear |
| `branches["bark_density"]` | Branch bark density/frequency (0-100%) |
| `branches["gradient_mode"]` | 1 — enable gradient mode for branch blocks, 0 — disable. When gradient mode is on, blocks from `branches["blocks"]` are not picked randomly but form a gradient |
| `branches["convexity"]` | 1 — bend away from the trunk, 2 — toward the trunk, 3 — both |
| `branches["branching_count"]` | Minimum and maximum number of sub-branches per branch |
| `branches["branching_length_coef"]` | Length coefficient of sub-branches relative to the branch length |
| `branches["grouping"]` | Minimum and maximum grouping coefficient. A value is picked per branch, and with that chance the branch spawns next to another branch |
| `branches["compression"]` | Branch compression |
| `branches["min_height"]` | Minimum height for branches to appear |
| `branches["max_height_coef"]` | Maximum height coefficient for branches to appear, relative to trunk height |

#### Branches — extra parameters
| Parameter | Description |
|-----------|-------------|
| `branches["enable_vertical_branches_generate_leaves_only"]` | If 1, leaves will only generate around vertical branches |
| `branches["vertical_branches_count_per_branch"]` | Minimum and maximum number of vertical branches per branch |
| `branches["vertical_branches_length"]` | Minimum and maximum vertical branches length |
| `branches["vertical_branches_blocks"]` | Blocks for vertical branches |

#### Leaves

| Parameter | Description |
|-----------|-------------|
| `leaves["start_y"]` | Lower bound of leaves appearance relative to the spawn block (e.g. at 0, leaves only generate in the upper hemisphere) |
| `leaves["end_y"]` | Same, but upper bound of leaves appearance relative to the spawn block |
| `leaves["start_x%"]` | Distance from branch/trunk start in percent, where leaves begin to generate (0 — everywhere, 100 — only the very tip) |
| `leaves["compression"]` | Vertical compression of the leaves sphere (1.0 — sphere, >1 — compressed, <1 — stretched OR, if you prefer, from -1 to 0 — compressed, <-1 — stretched) |
| `leaves["algorithm"]` | Leaves generation algorithm (1–6, see below) |
| `leaves["quality"]` | Generation quality (1–10). Higher value — better quality, but slower generatio, but slower |

### Leaf Generation Algorithms (`leaves["algorithm"]`)

| Value | Description |
|-------|-------------|
| 1 | Simple random selection |
| 2 | Random, but with grouping |
| 3 | The closer to the branch — the higher the chance |
| 4 | Neighbor-based; farther from branches |
| 5 | Neighbor-based; closer to branches (recommended) |
| 6 | Farther from branches; improved algorithm (recommended) |

## Creating Presets

To change a slider's default value, edit the corresponding parameter:

`trunk["min_height"] = $int(Trunk Min Height, 8, 5, 100)$`

Here `8` is the default value.

For parameters without sliders, just change the number directly in the code.

## Block Orientation

Blocks in the `oriented_blocks` list automatically connect to adjacent trunk, branch, and leaves blocks. Supported: fences and walls, glass panes, slabs, trapdoors, and signs (wall_sign).