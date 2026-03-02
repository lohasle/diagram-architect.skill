# diagram-architect.skill

**中文** · [English](README.md)

一个用于 **Claude Code** 的生产级架构图生成技能。通过自然语言描述，自动生成美观的自包含 HTML 图表文件——内置 5 套专业主题、交互式缩放/导出控件，零运行时依赖。

## 能做什么

安装后，该技能让 Claude Code 能理解"画一张 XX 架构图"这类请求，选择合适的图表类型和主题，自动写出可在浏览器直接打开的 `.html` 文件。

---

## 四类 AI 架构图示例

以下四个示例覆盖 AI 系统最常见的架构描述场景，验证了技能在不同架构维度下的表现。

---

### 1. 应用架构

**描述什么**：从客户端到 LLM 服务的完整分层，展示 RAG 问答平台各层组件及交互关系。
**适用场景**：系统设计评审、技术方案讨论、新人 Onboarding 文档。

**Prompt 示例：**
```
画一个 RAG 问答平台的应用架构图，使用 Tech 主题
```

**图表代码：**
```mermaid
flowchart LR
    subgraph CLIENT["客户端层"]
        WEB["Web 应用"]:::c
        SDK["API 客户端"]:::c
    end
    subgraph APP["应用层"]
        GW["API 网关"]:::a
        PM["Prompt 管理"]:::a
        SM["会话管理"]:::a
    end
    subgraph AI["AI 服务"]
        LLM["LLM 服务"]:::ai
        EMB["Embedding"]:::ai
        RAG["RAG 引擎"]:::ai
    end
    subgraph DATA["数据层"]
        VDB[("向量数据库")]:::d
        DOCS[("文档存储")]:::d
        CACHE[("Redis 缓存")]:::d
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

**验证说明：**

| 维度 | 结果 |
|------|------|
| 分层清晰度 | ✅ 4 层（客户端 → 应用 → AI 服务 → 数据）逻辑隔离 |
| 关键路径 | ✅ 用户请求 → API 网关 → RAG 引擎 → LLM 完整可追踪 |
| 数据流向 | ✅ 向量化、存储、缓存的写入/读取方向正确 |
| 适用主题 | Tech（紫色系）突显 AI 产品属性 |

---

### 2. 数据架构

**描述什么**：数据从采集、处理到 RAG 检索生成的全链路流转，展示每个阶段的处理逻辑和存储目标。
**适用场景**：数据治理设计、ETL 流程规划、数据团队对齐。

**Prompt 示例：**
```
生成 AI 知识库系统的数据处理流水线架构图
```

**图表代码：**
```mermaid
flowchart LR
    subgraph SRC["数据源"]
        PDF["PDF 文档"]:::s
        DB["结构化数据库"]:::s
        WEB["网页内容"]:::s
    end
    subgraph ETL["数据处理"]
        PARSE["解析提取"]:::p
        CHUNK["语义切分"]:::p
        EMBED["向量化"]:::p
    end
    subgraph STORE["存储层"]
        VDB[("向量数据库")]:::st
        OBJ[("对象存储 OSS")]:::st
        META[("元数据 MySQL")]:::st
    end
    subgraph SERVE["检索生成"]
        SEARCH["语义检索 Top-K"]:::sv
        RERANK["重排序 Cross-Encoder"]:::sv
        GEN["LLM 生成回答"]:::sv
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

**验证说明：**

| 维度 | 结果 |
|------|------|
| 数据流向 | ✅ 从左至右，单向流动，无回路 |
| 分阶段处理 | ✅ ETL 三步（解析 → 切分 → 向量化）清晰展开 |
| 存储目标明确 | ✅ 向量、原始文本、元数据分别写入不同存储 |
| 检索链路 | ✅ 双阶段检索（召回 + 重排序）符合 RAG 最佳实践 |

---

### 3. 部署架构

**描述什么**：生产环境下 AI 推理服务的完整部署拓扑，从边缘 CDN 到 GPU 计算集群及运维监控。
**适用场景**：运维架构设计、容量规划、安全评审、上线 Checklist。

**Prompt 示例：**
```
画出生产环境 AI 推理服务的部署架构图，包含 GPU 集群和运维监控层
```

**图表代码：**
```mermaid
flowchart TD
    USERS["用户 / 客户端"]:::u
    subgraph EDGE["边缘层"]
        CDN["CDN 加速"]:::e
        WAF["WAF 防火墙"]:::e
    end
    subgraph PLATFORM["接入层"]
        LB["负载均衡 Nginx"]:::p
        GW["API 网关 Kong"]:::p
    end
    subgraph COMPUTE["计算层"]
        APP["应用服务 x3"]:::c
        GPU["GPU 推理集群 A100"]:::gpu
        WORKER["异步 Worker"]:::c
    end
    subgraph INFRA["存储层"]
        VDB[("向量数据库")]:::d
        RDS[("MySQL RDS")]:::d
        REDIS[("Redis Cluster")]:::d
    end
    subgraph OPS["运维层"]
        MON["Prometheus 监控"]:::o
        LOG["ELK 日志系统"]:::o
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

**验证说明：**

| 维度 | 结果 |
|------|------|
| 流量路径 | ✅ 用户 → CDN → WAF → LB → 网关 完整链路 |
| 高可用设计 | ✅ 应用服务 ×3 副本，GPU 集群独立扩展 |
| 监控覆盖 | ✅ 虚线表示监控采集链路，区别于业务数据链路 |
| 存储隔离 | ✅ 向量/关系/缓存三种存储各司其职 |

---

### 4. 模块架构

**描述什么**：AI Agent 框架中各核心模块的组成与依赖关系，展示 Agent 核心、模型层、记忆层和工具层的职责划分。
**适用场景**：模块设计文档、接口规范制定、代码架构评审。

**Prompt 示例：**
```
绘制 AI Agent 框架的模块架构图，使用 Dark Mode 主题
```

**图表代码：**
```mermaid
flowchart LR
    subgraph AGENT["Agent 核心"]
        PLAN["任务规划"]:::core
        EXEC["任务执行"]:::core
        CTX["上下文管理"]:::core
    end
    subgraph MODELS["模型层"]
        LLM["语言模型 LLM"]:::model
        EMB["嵌入模型 Embedding"]:::model
        VISION["视觉模型 Vision"]:::model
    end
    subgraph MEMORY["记忆层"]
        SHORT["短期记忆 会话上下文"]:::mem
        LONG["长期记忆 向量存储"]:::mem
        KG["实体记忆 知识图谱"]:::mem
    end
    subgraph TOOLS["工具层"]
        SEARCH["搜索工具"]:::tool
        CODE["代码执行沙箱"]:::tool
        API["外部 API 调用"]:::tool
    end
    AGENT --> MODELS
    AGENT --> MEMORY
    AGENT --> TOOLS
    classDef core fill:#7c3aed,stroke:#6d28d9,color:#fff
    classDef model fill:#0ea5e9,stroke:#0284c7,color:#fff
    classDef mem fill:#10b981,stroke:#059669,color:#fff
    classDef tool fill:#f59e0b,stroke:#d97706,color:#fff
```

**验证说明：**

| 维度 | 结果 |
|------|------|
| 模块职责清晰 | ✅ 4 个子系统各自内聚，边界明确 |
| 依赖方向 | ✅ Agent 核心为统一入口，单向依赖三层 |
| 扩展性 | ✅ 工具层和模型层均可独立水平扩展 |
| 适用主题 | Dark Mode 适合开发者文档和 IDE 环境 |

---

## 功能特性

| 特性 | 说明 |
|------|------|
| **图表类型** | 流程图、时序图、ER 图、状态图、类图、思维导图、甘特图、C4 架构图 |
| **渲染引擎** | Mermaid.js（CDN 零依赖）、D2（kroki.io API）、PlantUML/C4（kroki.io API） |
| **主题系统** | Corporate、Dark Mode、Minimal、Tech、Warm — 运行时切换，无需重新生成 |
| **交互控件** | 缩放（25%–300%）、鼠标拖拽平移、触控拖拽、键盘快捷键 |
| **导出格式** | SVG 矢量图、2× Retina PNG、打印优化布局 |
| **输出格式** | 单个自包含 `.html` 文件，无需服务器，任意浏览器打开 |

## 安装方法

### 方式一：安装 `.skill` 文件（推荐）

```bash
# 下载最新版本
curl -L https://github.com/lohasle/diagram-architect.skill/releases/latest/download/diagram-architect.skill \
  -o ~/.claude/skills/diagram-architect.skill
# Claude Code 下次启动时自动识别，无需额外配置
```

### 方式二：Git Clone 源目录

```bash
cd ~/.claude/skills
git clone https://github.com/lohasle/diagram-architect.skill.git diagram-architect

# 后续更新
cd diagram-architect && git pull
```

## 主题系统

| 主题 | 主色调 | 适用场景 |
|------|--------|----------|
| **Corporate** | 藏青 `#1e3a5a` | 企业架构、B2B 文档、技术评审 |
| **Dark Mode** | 深灰 `#1e293b` | 开发者文档、API 规范、IDE 截图 |
| **Minimal** | 灰色 `#374151` | 白皮书、学术材料、正式报告 |
| **Tech** | 紫色 `#7c3aed` | AI 产品、SaaS、技术博客 |
| **Warm** | 琥珀 `#92400e` | 教程、培训材料、友好文档 |

生成的 HTML 文件内置主题切换按钮，运行时切换无需重新生成。

## 引擎选择

```
需要 C4 架构图？       → PlantUML（通过 kroki.io）
基础设施 / 云部署图？  → D2（通过 kroki.io 或本地 CLI）
其他所有图表类型？      → Mermaid.js（CDN，零依赖）✓ 默认
```

## 快捷键（在生成的 HTML 中）

| 快捷键 | 操作 |
|--------|------|
| `Ctrl/Cmd +` | 放大 |
| `Ctrl/Cmd -` | 缩小 |
| `Ctrl/Cmd 0` | 重置视图 |
| `Ctrl/Cmd P` | 打印 |

## 项目结构

```
diagram-architect/
├── SKILL.md                       # Claude Code 技能定义文件
├── assets/
│   └── templates/
│       └── diagram.html           # 自包含 HTML 模板（含 Mermaid.js CDN）
├── references/
│   ├── engine-selection.md        # 引擎选择决策树
│   ├── mermaid-patterns.md        # Mermaid 语法与示例
│   ├── d2-patterns.md             # D2 语法与基础设施图案例
│   ├── plantuml-c4.md             # C4 模型与 PlantUML
│   ├── design-principles.md       # 图表设计原则与反模式
│   └── themes.md                  # 5 套主题的颜色定义
└── scripts/
    └── render.py                  # D2/PlantUML → SVG（通过 kroki.io API）
```

## 依赖要求

- **Claude Code** v2.0+（支持 skills 功能）
- **浏览器** — 任意现代浏览器均可查看生成的 HTML
- **D2/PlantUML 渲染**（可选）：`pip install requests`

## 许可证

MIT

---

> 为 [Claude Code](https://claude.ai/code) 构建 · 基于 [Mermaid.js](https://mermaid.js.org)、[D2](https://d2lang.com)、[PlantUML](https://plantuml.com)、[kroki.io](https://kroki.io)
