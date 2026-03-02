# Diagram Engine Selection Guide

## Decision Tree

```
Start
│
├─ Need C4 Architecture Diagram?
│  └─ Yes → PlantUML (C4-PlantUML library)
│  └─ No  → Continue
│
├─ Need Infrastructure/Cloud Layout?
│  └─ Yes → D2 (if CLI installed) OR Mermaid (fallback)
│  └─ No  → Continue
│
├─ Standard Flowchart/Sequence/ER/State?
│  └─ Yes → Mermaid.js (primary choice)
│  └─ No  → Continue
│
└─ Default → Mermaid.js
```

## Engine Comparison

| Feature | Mermaid | D2 | PlantUML |
|---------|---------|-----|----------|
| **Zero Dependency** | ✅ CDN | ❌ CLI required | ❌ JAR or API |
| **Chart Types** | 10+ | 8 | 15+ |
| **Default Styling** | Basic | Beautiful | Enterprise |
| **C4 Support** | Basic | Good | Excellent |
| **Learning Curve** | Low | Low | Medium |
| **Render Speed** | Fast | Fast | Medium |

## Scene Mapping

### Use Mermaid.js for:
- Flowcharts (decision trees, process flows)
- Sequence diagrams (API flows, interactions)
- Entity relationship diagrams (data models)
- State diagrams (state machines)
- Mind maps (brainstorming, hierarchies)
- Gantt charts (timelines, project plans)
- Pie charts (simple data visualization)
- Journey maps (user experience flows)
- Git graphs (branch visualization)

### Use D2 for:
- Infrastructure diagrams (cloud architecture, network topology)
- Complex system layouts (when automatic layout matters)
- When aesthetic quality is priority and CLI is available
- Architecture diagrams that need visual refinement

### Use PlantUML for:
- **C4 Model diagrams** (Context, Container, Component, Code)
- When existing PlantUML code needs to be rendered
- Complex class diagrams
- Activity diagrams (when swimlanes are needed)
- Deployment diagrams

## Quick Reference

### Mermaid CDN
```
https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js
```

### D2 Installation
```bash
# macOS
brew install d2

# Linux
wget https://github.com/terrastruct/d2/releases/download/vX.X.X/d2-vX.X.X-linux-amd64.tar.gz

# Or use kroki.io API
curl -X POST -d "@diagram.d2" https://kroki.io/d2/svg
```

### PlantUML via kroki.io
```bash
curl -X POST -d "@diagram.puml" https://kroki.io/plantuml/svg
```

## Fallback Strategy

When preferred engine is not available:
1. **D2 not installed** → Fall back to Mermaid (translate syntax)
2. **PlantUML not available** → Use Mermaid for basic diagrams, kroki.io for C4
3. **No internet access** → Use CLI tools only (if installed)
