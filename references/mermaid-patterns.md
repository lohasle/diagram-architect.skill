# Mermaid Diagram Patterns

## Flowchart

### Basic Structure
```mermaid
flowchart TD
    A[Start] --> B{Decision?}
    B -->|Yes| C[Action]
    B -->|No| D[Alternative]
    C --> E[End]
    D --> E
```

### Direction
- `TD` = Top-Down
- `LR` = Left-Right
- `BT` = Bottom-Top
- `RL` = Right-Left

### Node Shapes
```
[Text]          Rectangle
(Text)          Rounded
([Text])        Stadium
{Text}          Diamond
[[Text]]        Subroutine
[(Text)]        Cylinder (database)
((Text))        Circle
>Text]          Flag
```

### Styling
```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#1e3a5a', 'edgeLabelBackground':'#ffffff'}}}%%
flowchart LR
    A[Start] --> B[Process]
    B --> C[End]

    style A fill:#3b82f6,stroke:#1e40af,color:#fff
    style B fill:#10b981,stroke:#059669,color:#fff
    style C fill:#f59e0b,stroke:#d97706,color:#fff
```

### Grouping
```mermaid
flowchart TD
    subgraph Group1 [User Layer]
        A[Frontend] --> B[Mobile App]
    end
    subgraph Group2 [Backend Layer]
        C[API Gateway] --> D[Service]
    end
    Group1 --> Group2
```

---

## Sequence Diagram

### Basic Structure
```mermaid
sequenceDiagram
    participant User as User
    participant API as API Gateway
    participant DB as Database

    User->>API: Request
    API->>DB: Query
    DB-->>API: Result
    API-->>User: Response
```

### Messages
- `->>`  Synchronous request
- `-->>` Synchronous response
- `->`   Asynchronous message
- `-->`  Asynchronous response
- `--`   Dotted line (no response)

### Activations and Loops
```mermaid
sequenceDiagram
    participant Client
    participant Server

    Client->>+Server: Request
    loop Retry
        Server->>Server: Process
    end
    Server-->>-Client: Response
```

### Grouping
- `rect` - Group with box
- `alt/else` - Conditional blocks
- `opt` - Optional block
- `loop` - Loop block
- `par/and` - Parallel execution

---

## Entity Relationship Diagram

### Basic Structure
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        uuid id PK
        string email UK
        string name
        timestamp created_at
    }
    ORDER {
        uuid id PK
        uuid customer_id FK
        enum status
        decimal total
    }
```

### Cardinalities
- `||--||`  One to One
- `||--o{`  One to Many (optional)
- `||--|{`  One to Many (required)
- `}o--||`  Many to One (optional)
- `}|--||`  Many to One (required)
- `}o--o{`  Many to Many (both optional)
- `}|--|{`  Many to Many (both required)

---

## State Diagram

### Basic Structure
```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Pending: submit()
    Pending --> Approved: approve()
    Pending --> Rejected: reject()
    Rejected --> Draft: revise()
    Approved --> Published: publish()
    Published --> [*]
```

### Choices
```mermaid
stateDiagram-v2
    [*] --> Active
    Active --> Check: action()
    Check --> Success: pass()
    Check --> Failed: fail()
    Success --> [*]
    Failed --> Active: retry()
```

---

## Class Diagram

### Basic Structure
```mermaid
classDiagram
    class User {
        +String id
        +String email
        +String name
        +create()
        +update()
        +delete()
    }

    class Order {
        +String id
        +Date createdAt
        +Status status
        +process()
        +cancel()
    }

    User "1" --> "*" Order : places
```

### Visibility
- `+`  Public
- `-`  Private
- `#`  Protected
- `~`  Package

### Relationships
- `-->`   Association (general)
- `*--`   Composition (owns)
- `o--`   Aggregation (has)
- `<|--`  Inheritance (extends)
- `..|>`  Implementation (implements)
- `..>`   Dependency (uses)

---

## Mind Map

### Basic Structure
```mermaid
mindmap
  root((Project))
    Backend
      API
      Database
      Services
    Frontend
      React
      Components
      State
    DevOps
      CI/CD
      Monitoring
```

---

## Gantt Chart

### Basic Structure
```mermaid
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Design
    Research      :a1, 2024-01-01, 5d
    Wireframes    :after a1, 3d
    section Development
    Backend       :2024-01-10, 10d
    Frontend      :2024-01-15, 8d
    section Testing
    QA Testing    :after dev, 5d
```

---

## Quality Examples

### Bad: Too Many Nodes
```mermaid
flowchart TD
    A-->B-->C-->D-->E-->F-->G-->H-->I-->J-->K-->L-->M-->N-->O-->P-->Q-->R-->S-->T
```

### Good: Logical Grouping
```mermaid
flowchart TD
    subgraph Input [Input Layer]
        A[A] --> B[B] --> C[C]
    end
    subgraph Process [Processing]
        D[D] --> E[E] --> F[F]
    end
    subgraph Output [Output Layer]
        G[G] --> H[H]
    end
    Input --> Process --> Output
```

### Excellent: Clear Labels + Visual Hierarchy
```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#1e3a5a', 'primaryTextColor': '#ffffff', 'edgeLabelBackground':'#f1f5f9'}}}%%
flowchart LR
    subgraph CLIENT["Client Side"]
        WEB["Web App<br/><span style='font-size:10px'>React 18</span>"]:::client
        MOBILE["Mobile App<br/><span style='font-size:10px'>React Native</span>"]:::client
    end

    subgraph EDGE["Edge Layer"]
        GW["API Gateway<br/><span style='font-size:10px'>Kong</span>"]:::edge
        CDN["CDN<br/><span style='font-size:10px'>CloudFlare</span>"]:::edge
    end

    subgraph CORE["Core Services"]
        AUTH["Auth Service"]:::service
        USER["User Service"]:::service
        ORDER["Order Service"]:::service
    end

    subgraph DATA["Data Layer"]
        PG[(PostgreSQL)]:::data
        REDIS[(Redis)]:::data
        S3[(S3)]:::data
    end

    WEB --> GW
    MOBILE --> CDN --> GW
    GW --> AUTH
    GW --> USER
    GW --> ORDER
    AUTH --> REDIS
    USER --> PG
    ORDER --> PG
    ORDER --> S3

    classDef client fill:#3b82f6,stroke:#1e40af,color:#fff
    classDef edge fill:#8b5cf6,stroke:#7c3aed,color:#fff
    classDef service fill:#10b981,stroke:#059669,color:#fff
    classDef data fill:#f59e0b,stroke:#d97706,color:#fff
```

## Theme Variables Reference

```javascript
{
  primaryColor: '#1e3a5a',
  primaryTextColor: '#ffffff',
  primaryBorderColor: '#1e40af',
  lineColor: '#5c6370',
  secondaryColor: '#f0f0f0',
  tertiaryColor: '#e8e8e8',
  background: '#ffffff',
  edgeLabelBackground: '#f1f5f9',
  actorBkg: '#3b82f6',
  actorBkgColor: '#3b82f6',
  actorTextColor: '#ffffff',
  actorBorder: '#1e40af',
  labelBoxBkgColor: '#3b82f6',
  labelTextColor: '#ffffff',
  noteBkgColor: '#fef3c7',
  noteTextColor: '#92400e',
  noteBorderColor: '#d97706'
}
```
