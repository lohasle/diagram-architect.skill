# diagram-architect.skill

**[中文](README.zh.md)** · English

A production-grade diagram generation skill for **Claude Code**. Describe your architecture in plain text and get a beautiful, self-contained HTML file — 5 professional themes, interactive zoom/export controls, zero runtime dependencies.

## What It Does

Once installed, the skill lets Claude Code understand requests like "draw an XX architecture diagram", choose the right diagram type and theme, and automatically write a `.html` file you can open directly in any browser.

---

## 4 AI Architecture Examples

The following four examples cover the most common AI system architecture scenarios, demonstrating the skill across different architectural dimensions.

---

### 1. Application Architecture

**What it shows**: Complete layering from client to LLM service, illustrating each layer's components and interactions in a RAG Q&A platform.
**Use cases**: System design reviews, technical proposal discussions, new-hire onboarding documentation.

**Prompt example:**
```
Draw an application architecture diagram for a RAG Q&A platform, using Tech theme
```

**Diagram code:**
```mermaid
flowchart LR
    subgraph CLIENT["Client Layer"]
        WEB["Web App"]:::c
        SDK["API Client"]:::c
    end
    subgraph APP["Application Layer"]
        GW["API Gateway"]:::a
        PM["Prompt Manager"]:::a
        SM["Session Manager"]:::a
    end
    subgraph AI["AI Services"]
        LLM["LLM Service"]:::ai
        EMB["Embedding"]:::ai
        RAG["RAG Engine"]:::ai
    end
    subgraph DATA["Data Layer"]
        VDB[("Vector DB")]:::d
        DOCS[("Document Store")]:::d
        CACHE[("Redis Cache")]:::d
    end
    CLIENT --> GW
    GW --> PM
    GW --> SM
    PM --> LLM
    SM --> LLM
    RAG --> LLM
    EMB --> VDB
    RAG --> VDB
    RAG --> DOCS
    LLM --> CACHE
    classDef c fill:#3b82f6,stroke:#1e40af,color:#fff
    classDef a fill:#7c3aed,stroke:#6d28d9,color:#fff
    classDef ai fill:#10b981,stroke:#059669,color:#fff
    classDef d fill:#f59e0b,stroke:#d97706,color:#fff
```

**Validation:**

| Dimension | Result |
|-----------|--------|
| Layer clarity | ✅ 4 layers (Client → App → AI Services → Data) logically isolated |
| Critical path | ✅ User request → API Gateway → RAG Engine → LLM fully traceable |
| Data flow | ✅ Vectorization, storage, and cache read/write directions correct |
| Recommended theme | Tech (purple) highlights AI product identity |

---

### 2. Data Architecture

**What it shows**: Full data journey from ingestion and processing to RAG retrieval and generation, illustrating processing logic and storage targets at each stage.
**Use cases**: Data governance design, ETL pipeline planning, data team alignment.

**Prompt example:**
```
Generate a data processing pipeline architecture diagram for an AI knowledge base system
```

**Diagram code:**
```mermaid
flowchart LR
    subgraph SRC["Data Sources"]
        PDF["PDF Documents"]:::s
        DB["Structured Database"]:::s
        WEB["Web Content"]:::s
    end
    subgraph ETL["Data Processing"]
        PARSE["Parse & Extract"]:::p
        CHUNK["Semantic Chunking"]:::p
        EMBED["Vectorization"]:::p
    end
    subgraph STORE["Storage Layer"]
        VDB[("Vector Database")]:::st
        OBJ[("Object Storage OSS")]:::st
        META[("Metadata MySQL")]:::st
    end
    subgraph SERVE["Retrieval & Generation"]
        SEARCH["Semantic Retrieval Top-K"]:::sv
        RERANK["Re-ranking Cross-Encoder"]:::sv
        GEN["LLM Answer Generation"]:::sv
    end
    SRC --> ETL
    PARSE --> CHUNK
    CHUNK --> EMBED
    EMBED --> VDB
    PARSE --> OBJ
    CHUNK --> META
    VDB --> SEARCH
    SEARCH --> RERANK
    RERANK --> GEN
    classDef s fill:#1e3a5a,stroke:#1e40af,color:#fff
    classDef p fill:#7c3aed,stroke:#6d28d9,color:#fff
    classDef st fill:#f59e0b,stroke:#d97706,color:#fff
    classDef sv fill:#10b981,stroke:#059669,color:#fff
```

**Validation:**

| Dimension | Result |
|-----------|--------|
| Data flow direction | ✅ Left to right, unidirectional, no cycles |
| Stage separation | ✅ ETL three steps (parse → chunk → vectorize) clearly laid out |
| Storage targets explicit | ✅ Vectors, raw text, and metadata written to separate stores |
| Retrieval pipeline | ✅ Two-stage retrieval (recall + re-ranking) follows RAG best practices |

---

### 3. Deployment Architecture

**What it shows**: Complete production deployment topology for an AI inference service, from edge CDN to GPU compute cluster and operations monitoring.
**Use cases**: Operations architecture design, capacity planning, security review, go-live checklist.

**Prompt example:**
```
Draw a deployment architecture diagram for a production AI inference service, including GPU cluster and operations monitoring layer
```

**Diagram code:**
```mermaid
flowchart TD
    USERS["Users / Clients"]:::u
    subgraph EDGE["Edge Layer"]
        CDN["CDN Acceleration"]:::e
        WAF["WAF Firewall"]:::e
    end
    subgraph PLATFORM["Ingress Layer"]
        LB["Load Balancer Nginx"]:::p
        GW["API Gateway Kong"]:::p
    end
    subgraph COMPUTE["Compute Layer"]
        APP["App Service x3"]:::c
        GPU["GPU Inference Cluster A100"]:::gpu
        WORKER["Async Worker"]:::c
    end
    subgraph INFRA["Storage Layer"]
        VDB[("Vector Database")]:::d
        RDS[("MySQL RDS")]:::d
        REDIS[("Redis Cluster")]:::d
    end
    subgraph OPS["Operations Layer"]
        MON["Prometheus Monitoring"]:::o
        LOG["ELK Logging"]:::o
    end
    USERS --> CDN --> WAF --> LB --> GW
    GW --> APP
    GW --> WORKER
    APP --> GPU
    APP --> VDB
    APP --> RDS
    APP --> REDIS
    WORKER --> VDB
    GPU -.-> MON
    APP -.-> LOG
    classDef u fill:#6366f1,stroke:#4f46e5,color:#fff
    classDef e fill:#0ea5e9,stroke:#0284c7,color:#fff
    classDef p fill:#7c3aed,stroke:#6d28d9,color:#fff
    classDef c fill:#1e3a5a,stroke:#1e40af,color:#fff
    classDef gpu fill:#ef4444,stroke:#dc2626,color:#fff
    classDef d fill:#f59e0b,stroke:#d97706,color:#fff
    classDef o fill:#10b981,stroke:#059669,color:#fff
```

**Validation:**

| Dimension | Result |
|-----------|--------|
| Traffic path | ✅ Users → CDN → WAF → LB → Gateway complete chain |
| High availability | ✅ App service ×3 replicas, GPU cluster scales independently |
| Monitoring coverage | ✅ Dashed lines denote monitoring collection, distinct from data flow |
| Storage isolation | ✅ Vector / relational / cache stores each serve dedicated roles |

---

### 4. Module Architecture

**What it shows**: Core module composition and dependencies within an AI Agent framework, illustrating responsibility boundaries across Agent Core, Model Layer, Memory Layer, and Tools Layer.
**Use cases**: Module design documents, interface specification, code architecture review.

**Prompt example:**
```
Draw an AI Agent framework module architecture diagram using Dark Mode theme
```

**Diagram code:**
```mermaid
flowchart LR
    subgraph AGENT["Agent Core"]
        PLAN["Task Planning"]:::core
        EXEC["Task Execution"]:::core
        CTX["Context Management"]:::core
    end
    subgraph MODELS["Model Layer"]
        LLM["Language Model LLM"]:::model
        EMB["Embedding Model"]:::model
        VISION["Vision Model"]:::model
    end
    subgraph MEMORY["Memory Layer"]
        SHORT["Short-term Memory (Session Context)"]:::mem
        LONG["Long-term Memory (Vector Store)"]:::mem
        KG["Entity Memory (Knowledge Graph)"]:::mem
    end
    subgraph TOOLS["Tools Layer"]
        SEARCH["Search Tool"]:::tool
        CODE["Code Execution Sandbox"]:::tool
        API["External API Call"]:::tool
    end
    AGENT --> MODELS
    AGENT --> MEMORY
    AGENT --> TOOLS
    classDef core fill:#7c3aed,stroke:#6d28d9,color:#fff
    classDef model fill:#0ea5e9,stroke:#0284c7,color:#fff
    classDef mem fill:#10b981,stroke:#059669,color:#fff
    classDef tool fill:#f59e0b,stroke:#d97706,color:#fff
```

**Validation:**

| Dimension | Result |
|-----------|--------|
| Module responsibility | ✅ 4 subsystems each cohesive with clear boundaries |
| Dependency direction | ✅ Agent Core is the single entry point, one-way dependency on three layers |
| Extensibility | ✅ Tools Layer and Model Layer can scale horizontally and independently |
| Recommended theme | Dark Mode suits developer docs and IDE environments |

---

### 5. Azure Deployment Architecture (with Cloud Icons)

**What it shows**: Production Hub-Spoke network topology on Azure with real service icons — VNet boundaries, Firewall, AKS, App Gateway, Key Vault, SQL, Redis and more.
**Use cases**: Cloud architecture reviews, infrastructure planning, network security design, Azure adoption documentation.

**Prompt example:**
```
Draw an Azure Hub-Spoke deployment architecture diagram with network security and shared services
```

**Result:**

![Azure Hub-Spoke Deployment Architecture with Icons](assets/screenshots/azure-icons-demo.png)

**Key feature:** Use `@azure:ALIAS` in D2 source — `generate.py` automatically embeds the SVG as a base64 data URI, keeping the HTML fully self-contained with no internet dependency for icons.

```d2
hub: Hub VNet {
  icon: "@azure:vnet"

  fw: Firewall {
    icon: "@azure:firewall"
    shape: image
  }
  vpn: VPN Gateway {
    icon: "@azure:vpn-gateway"
    shape: image
  }
}

spoke: App Spoke {
  aks: AKS Cluster {
    icon: "@azure:kubernetes"
    shape: image
  }
}
```

**43 built-in Azure icons** — see [references/azure-icons.md](references/azure-icons.md) for the full catalog.

---

## Features

| Feature | Description |
|---------|-------------|
| **Diagram Types** | Flowchart, Sequence, ER, State, Class, Mind Map, Gantt, C4 Architecture |
| **Rendering Engines** | Mermaid.js (CDN, zero dependencies), D2 (kroki.io API), PlantUML/C4 (kroki.io API) |
| **Azure Cloud Icons** | 43 built-in Azure service icons — use `@azure:ALIAS` in D2 diagrams, auto-embedded as base64 |
| **Theme System** | Corporate, Dark Mode, Minimal, Tech, Warm — runtime switching, no re-generation needed |
| **Interactive Controls** | Zoom (25%–300%), drag-to-pan (mouse + touch), keyboard shortcuts |
| **Export Formats** | SVG vector, 2× Retina PNG, print-optimized layout |
| **Output Format** | Single self-contained `.html` file, no server required, opens in any browser |

## Installation

### Option 1: Install `.skill` file (Recommended)

```bash
# Download the latest release
curl -L https://github.com/lohasle/diagram-architect.skill/releases/latest/download/diagram-architect.skill \
  -o ~/.claude/skills/diagram-architect.skill
# Claude Code auto-discovers it on next launch — no further configuration needed
```

### Option 2: Clone from Git

```bash
cd ~/.claude/skills
git clone https://github.com/lohasle/diagram-architect.skill.git diagram-architect

# Update later with:
cd diagram-architect && git pull
```

## Theme System

| Theme | Primary Color | Best For |
|-------|---------------|----------|
| **Corporate** | Navy `#1e3a5a` | Enterprise architecture, B2B docs, technical reviews |
| **Dark Mode** | Slate `#1e293b` | Developer docs, API specs, IDE screenshots |
| **Minimal** | Gray `#374151` | White papers, academic materials, formal reports |
| **Tech** | Purple `#7c3aed` | AI products, SaaS platforms, tech blogs |
| **Warm** | Amber `#92400e` | Tutorials, training materials, approachable docs |

Generated HTML files include a built-in theme switcher — change themes at runtime without re-generating.

## Engine Selection

```
Need a C4 architecture diagram?      → PlantUML (via kroki.io)
Infrastructure / cloud deployment?   → D2 (via kroki.io or local CLI)
All other diagram types?             → Mermaid.js (CDN, zero dependencies) ✓ default
```

## Keyboard Shortcuts (in generated HTML)

| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd +` | Zoom in |
| `Ctrl/Cmd -` | Zoom out |
| `Ctrl/Cmd 0` | Reset view |
| `Ctrl/Cmd P` | Print |

## Project Structure

```
diagram-architect/
├── SKILL.md                       # Claude Code skill definition
├── assets/
│   ├── icons/
│   │   └── azure/                 # 43 Azure service SVG icons (vm, kubernetes, vnet, ...)
│   ├── screenshots/               # Demo screenshots
│   └── templates/
│       └── diagram.html           # Self-contained HTML template (includes Mermaid.js CDN)
├── references/
│   ├── engine-selection.md        # Engine selection decision tree
│   ├── mermaid-patterns.md        # Mermaid syntax and examples
│   ├── d2-patterns.md             # D2 syntax and infrastructure diagram examples
│   ├── plantuml-c4.md             # C4 model and PlantUML
│   ├── azure-icons.md             # Azure icon catalog (@azure:ALIAS usage)
│   ├── design-principles.md       # Diagram design principles and anti-patterns
│   └── themes.md                  # Color definitions for all 5 themes
└── scripts/
    ├── generate.py                # Generate HTML from template; resolves @azure: icons
    └── render.py                  # D2/PlantUML → SVG (via kroki.io API)
```

## Requirements

- **Claude Code** v2.0+ (skills feature support)
- **Browser** — any modern browser to view generated HTML
- **D2/PlantUML rendering** (optional): `pip install requests`

## License

MIT

---

> Built for [Claude Code](https://claude.ai/code) · Powered by [Mermaid.js](https://mermaid.js.org), [D2](https://d2lang.com), [PlantUML](https://plantuml.com), [kroki.io](https://kroki.io)
