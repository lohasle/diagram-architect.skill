# diagram-architect.skill

A **Claude Code skill** for production-grade diagram generation. Creates beautiful, self-contained HTML files from text descriptions — with professional themes, interactive controls, and zero runtime dependencies.

## What It Does

When installed, this skill teaches Claude Code to generate architecture diagrams, flowcharts, sequence diagrams, and more as polished HTML files that open in any browser.

```
User: "Draw the CMP IoT platform architecture"
Claude: → Generates architecture.html with interactive diagram
         → 5 professional themes switchable at runtime
         → Export to SVG/PNG with one click
```

## Features

| Feature | Details |
|---------|---------|
| **Diagram Types** | Flowchart, Sequence, ER, State, Class, Mind Map, Gantt, C4 Architecture |
| **Rendering Engines** | Mermaid.js (CDN, zero-dep), D2 (via kroki.io), PlantUML/C4 (via kroki.io) |
| **Themes** | Corporate, Dark Mode, Minimal, Tech, Warm |
| **Interactive** | Zoom (25%–300%), drag-to-pan, theme switcher, keyboard shortcuts |
| **Export** | SVG vector, PNG raster (2x retina), Print |
| **Output** | Single self-contained `.html` file, no server required |
| **Mobile** | Touch drag-to-pan, responsive controls |

## Installation

### Option 1: Install `.skill` file (recommended)

1. Download [`diagram-architect.skill`](https://github.com/lohasle/diagram-architect.skill/releases/latest)
2. Place it in your Claude Code skills directory:
   ```bash
   cp diagram-architect.skill ~/.claude/skills/
   ```
3. Claude Code auto-discovers it on next launch.

### Option 2: Clone the source directory

```bash
cd ~/.claude/skills
git clone https://github.com/lohasle/diagram-architect.skill.git diagram-architect
```

## Usage

Once installed, just describe what you need in plain language:

```
"Draw a system architecture for our e-commerce platform"
"Create a sequence diagram for the OAuth login flow"
"Generate an ER diagram for the orders database"
"Make a C4 container diagram for the IoT edge service"
"Draw a deployment flowchart using the Dark Mode theme"
```

Claude selects the right engine and theme automatically, or you can specify:

```
"Draw the data pipeline architecture using the Tech theme"
"Create a sequence diagram in Dark Mode"
```

## Themes

| Theme | Primary Color | Best For |
|-------|--------------|----------|
| **Corporate** | Navy `#1e3a5a` | Enterprise, B2B docs |
| **Dark Mode** | Slate `#1e293b` | Developer docs, APIs |
| **Minimal** | Gray `#374151` | White papers, academic |
| **Tech** | Purple `#7c3aed` | Startups, AI/ML |
| **Warm** | Amber `#92400e` | Tutorials, education |

All themes are switchable at runtime in the generated HTML — no re-generation needed.

## Keyboard Shortcuts (in generated HTML)

| Key | Action |
|-----|--------|
| `Ctrl/Cmd +` | Zoom in |
| `Ctrl/Cmd -` | Zoom out |
| `Ctrl/Cmd 0` | Reset view |
| `Ctrl/Cmd P` | Print |

## Skill Structure

```
diagram-architect/
├── SKILL.md                       # Claude Code skill definition
├── assets/
│   └── templates/
│       └── diagram.html           # Self-contained HTML template
├── references/
│   ├── engine-selection.md        # When to use which engine
│   ├── mermaid-patterns.md        # Mermaid syntax & examples
│   ├── d2-patterns.md             # D2 syntax & infrastructure patterns
│   ├── plantuml-c4.md             # C4 model with PlantUML
│   ├── design-principles.md       # Quality guidelines & anti-patterns
│   └── themes.md                  # 5 theme definitions & color palettes
└── scripts/
    └── render.py                  # D2/PlantUML → SVG via kroki.io API
```

## Engine Selection Guide

```
Need C4 Architecture? → PlantUML (via kroki.io)
Infrastructure/Cloud? → D2 (via kroki.io or local CLI)
Everything else?      → Mermaid.js (CDN, zero dependency) ✓ default
```

## Requirements

- **Claude Code** v2.0+ with skills support
- **Browser** — any modern browser to view generated HTML
- **For D2/PlantUML**: `pip install requests` (for `scripts/render.py`)

## Example Output

The generated HTML includes:

- Diagram rendered via Mermaid.js
- Header with title, subtitle, and all controls
- 5 theme swatches (click to switch)
- Zoom in/out/reset buttons + mouse wheel zoom
- Drag-to-pan (mouse and touch)
- Export SVG / Export PNG buttons
- Print-optimized stylesheet
- Footer with theme name

## License

MIT

---

> Built for [Claude Code](https://claude.ai/code) · Powered by [Mermaid.js](https://mermaid.js.org), [D2](https://d2lang.com), [PlantUML](https://plantuml.com), [kroki.io](https://kroki.io)
