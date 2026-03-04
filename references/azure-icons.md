# Azure Icon Catalog

Use `@azure:ALIAS` in D2 diagram source to embed Azure service icons as self-contained base64 data URIs.

Icons are stored in `assets/icons/azure/` and automatically resolved by `generate.py`.

## Syntax (D2)

```d2
node-id: Label {
  icon: "@azure:ALIAS"
}
```

D2 renders icon nodes as image shapes. For best results, pair with `shape: image` or omit the shape (D2 auto-infers from icon presence):

```d2
# Recommended: explicit image shape for icon-only nodes
vm1: Web Server {
  icon: "@azure:vm"
  shape: image
}

# Or: icon alongside a shape
gateway: API Gateway {
  icon: "@azure:app-gateway"
  style.fill: "#0078d4"
  style.font-color: white
}
```

---

## Compute

| Alias | Service | Use For |
|-------|---------|---------|
| `vm` | Virtual Machine | Servers, VMs |
| `vm-scale-set` | VM Scale Sets | Auto-scaling server groups |
| `kubernetes` | AKS | Kubernetes clusters |
| `container` | Container Instances | Serverless containers |
| `container-registry` | Container Registry | Docker image registry |
| `app-service` | App Services | Web apps, APIs |
| `function` | Function Apps | Serverless functions |

## Networking

| Alias | Service | Use For |
|-------|---------|---------|
| `vnet` | Virtual Network | VNet boundaries |
| `load-balancer` | Load Balancer | L4 load balancing |
| `app-gateway` | Application Gateway | L7 reverse proxy / WAF |
| `vpn-gateway` | VPN Gateway | Site-to-site VPN |
| `firewall` | Azure Firewall | Network security |
| `traffic-manager` | Traffic Manager | Global DNS routing |
| `front-door` | Front Door / CDN | Global CDN + WAF |
| `dns` | DNS Zones | DNS records |
| `nat-gateway` | NAT Gateway | Outbound NAT |
| `expressroute` | ExpressRoute | Private connectivity |
| `private-endpoint` | Private Endpoint | Private Link endpoint |
| `nsg` | Network Security Group | Subnet/NIC firewall rules |
| `public-ip` | Public IP Address | Public IP resource |
| `route-table` | Route Table | Custom routing (UDR) |
| `bastion` | Azure Bastion | Secure VM access |

## Storage & Databases

| Alias | Service | Use For |
|-------|---------|---------|
| `storage` | Storage Account | Blob, Files, Queues |
| `sql` | Azure SQL Database | Managed SQL |
| `cosmos-db` | Cosmos DB | Multi-model NoSQL |
| `redis` | Azure Cache for Redis | Caching layer |
| `sql-mi` | SQL Managed Instance | Full SQL Server PaaS |
| `postgresql` | Azure Database for PostgreSQL | Managed PostgreSQL |
| `mysql` | Azure Database for MySQL | Managed MySQL |
| `databricks` | Azure Databricks | Spark analytics |
| `synapse` | Azure Synapse Analytics | Data warehouse + analytics |

## Security & Identity

| Alias | Service | Use For |
|-------|---------|---------|
| `key-vault` | Key Vault | Secrets, keys, certs |
| `managed-identity` | Managed Identity | Service-to-service auth |

## Integration & Messaging

| Alias | Service | Use For |
|-------|---------|---------|
| `api-management` | API Management | API gateway / developer portal |
| `service-bus` | Service Bus | Reliable message queuing |
| `event-hub` | Event Hubs | Event streaming / ingestion |

## Monitoring & Operations

| Alias | Service | Use For |
|-------|---------|---------|
| `monitor` | Azure Monitor | Metrics and alerts |
| `app-insights` | Application Insights | APM / distributed tracing |
| `log-analytics` | Log Analytics | Log aggregation and queries |

## AI / ML / IoT

| Alias | Service | Use For |
|-------|---------|---------|
| `openai` | Azure OpenAI | GPT / LLM integration |
| `machine-learning` | Azure ML | ML training and deployment |
| `iot-hub` | IoT Hub | Device-to-cloud messaging |

## Infrastructure

| Alias | Service | Use For |
|-------|---------|---------|
| `subscription` | Azure Subscription | Subscription boundary |

---

## Full D2 Example — Azure Deployment Architecture

```d2
vars: {
  d2-config: {
    layout-engine: elk
  }
}

direction: right

# Subscription boundary
subscription: Azure Subscription {
  icon: "@azure:subscription"
  style.fill: "#f0f9ff"
  style.stroke: "#0078d4"

  # Hub VNet
  hub: Hub VNet {
    icon: "@azure:vnet"
    style.fill: "#e0f2fe"

    fw: Azure Firewall {
      icon: "@azure:firewall"
      shape: image
    }
    vpn: VPN Gateway {
      icon: "@azure:vpn-gateway"
      shape: image
    }
    bastion: Bastion {
      icon: "@azure:bastion"
      shape: image
    }
  }

  # Spoke VNet — App Tier
  spoke-app: App VNet {
    icon: "@azure:vnet"
    style.fill: "#dcfce7"

    agw: App Gateway {
      icon: "@azure:app-gateway"
      shape: image
    }
    aks: AKS Cluster {
      icon: "@azure:kubernetes"
      shape: image
    }
    func: Functions {
      icon: "@azure:function"
      shape: image
    }
  }

  # Spoke VNet — Data Tier
  spoke-data: Data VNet {
    icon: "@azure:vnet"
    style.fill: "#fef3c7"

    sql: Azure SQL {
      icon: "@azure:sql"
      shape: image
    }
    redis: Redis Cache {
      icon: "@azure:redis"
      shape: image
    }
    storage: Storage Account {
      icon: "@azure:storage"
      shape: image
    }
  }

  # Shared Services
  shared: Shared Services {
    kv: Key Vault {
      icon: "@azure:key-vault"
      shape: image
    }
    monitor: Azure Monitor {
      icon: "@azure:monitor"
      shape: image
    }
    apim: API Management {
      icon: "@azure:api-management"
      shape: image
    }
  }
}

# Connections
subscription.hub.vpn -> subscription.hub.fw: Internal
subscription.hub.fw -> subscription.spoke-app.agw: Inspected
subscription.spoke-app.agw -> subscription.spoke-app.aks: HTTP/2
subscription.spoke-app.aks -> subscription.spoke-data.sql: SQL
subscription.spoke-app.aks -> subscription.spoke-data.redis: Cache
subscription.spoke-app.func -> subscription.spoke-data.storage: Blob
subscription.shared.apim -> subscription.spoke-app.aks: API calls
```

---

## How Icons Are Resolved

1. `generate.py` scans the source for `"@azure:ALIAS"` patterns
2. Each alias is looked up in `assets/icons/azure/ALIAS.svg`
3. The SVG is base64-encoded and substituted as a `data:image/svg+xml;base64,...` URI
4. The final HTML is fully self-contained — no network requests needed for icons

## Adding New Icons

Copy any SVG from the source icon library to `assets/icons/azure/` with a kebab-case name:

```bash
cp /path/to/my-service-{hash}.svg \
   /path/to/diagram-architect/assets/icons/azure/my-service.svg
```

Then use `@azure:my-service` in D2 diagrams.
