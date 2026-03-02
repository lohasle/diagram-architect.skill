# C4 Model with PlantUML

## C4 Model Overview

The C4 Model provides four levels of abstraction:

1. **System Context** - System in relation to users and external systems
2. **Container** - Applications, databases, message queues
3. **Component** - Libraries, modules within containers
4. **Code** - Classes, functions (rarely needed)

---

## Setup with C4-PlantUML

### Include Library
```plantuml
@startuml
' Include C4 library from CDN
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml
' Additional includes for other diagrams
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml
@enduml
```

---

## System Context Diagram

### Basic Structure
```plantuml
@startuml C4_Context
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

title System Context Diagram

Person(user, "User", "A customer of the system")
System(system, "E-Commerce Platform", "Allows users to browse and purchase products")
System_Ext(payment, "Payment Gateway", "Processes payments")
System_Ext(email, "Email Service", "Sends notifications")

Rel(user, system, "Uses", "HTTPS")
Rel(system, payment, "Processes payments", "HTTPS")
Rel(system, email, "Sends emails", "SMTP")

@enduml
```

### Key Elements
- `Person(name, label, description)` - User or actor
- `System(name, label, description)` - Your system
- `System_Ext(name, label, description)` - External system
- `Rel(from, to, label, tech)` - Relationship

---

## Container Diagram

### Basic Structure
```plantuml
@startuml C4_Container
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

title Container Diagram

Person(user, "User")

System_Boundary(c1, "E-Commerce Platform") {
    Container(spa, "Web Application", "React", "User interface")
    Container(api, "API Gateway", "Node.js", "REST API")
    Container(orders, "Order Service", "Go", "Handles orders")
    Container(products, "Product Service", "Go", "Product catalog")
    ContainerDb(db, "Database", "PostgreSQL", "Stores data")
    ContainerQueue(queue, "Message Queue", "RabbitMQ", "Async messaging")
}

Rel(user, spa, "Uses", "HTTPS")
Rel(spa, api, "Calls", "HTTPS")
Rel(api, orders, "Routes", "gRPC")
Rel(api, products, "Routes", "gRPC")
Rel(orders, db, "Reads/Writes", "SQL")
Rel(orders, queue, "Publishes", "AMQP")

@enduml
```

### Container Types
- `Container(name, label, technology, description)` - Application
- `ContainerDb(name, label, technology, description)` - Database
- `ContainerQueue(name, label, technology, description)` - Message queue
- `Container_Boundary(name, label)` - Group containers

---

## Component Diagram

### Basic Structure
```plantuml
@startuml C4_Component
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

title Order Service Components

Container(orderSvc, "Order Service", "Go", "Order processing")

ComponentDb(database, "Database", "PostgreSQL", "Orders table")
Component(cache, "Cache", "Redis", "Session cache")
Component(api, "REST API", "Go", "HTTP endpoints")
Component(biz, "Business Logic", "Go", "Order processing")
Component(repo, "Repository", "Go", "Data access")

Rel(api, biz, "Uses", "internal")
Rel(biz, repo, "Uses", "internal")
Rel(repo, database, "Reads/Writes", "SQL")
Rel(api, cache, "Uses", "TCP")

@enduml
```

---

## Deployment Diagram

### Basic Structure
```plantuml
@startuml C4_Deployment
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Deployment.puml

title Deployment Diagram

Deployment_Node(laptop, "Developer Laptop")
Deployment_Node(web, "Web Server", "Ubuntu")
Deployment_Node(db, "Database Server", "CentOS")

Container_Ext(browser, "Browser", "Chrome", on(laptop))
Container(spa, "Web App", "React", on(web))
ContainerDb(postgres, "Database", "PostgreSQL", on(db))

Rel(browser, spa, "HTTPS")
Rel(spa, postgres, "JDBC")

@enduml
```

---

## IoT Architecture Example

```plantuml
@startuml C4_Container_IoT
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

title CMP Platform Architecture

Person(operator, "System Operator")
Person(admin, "Administrator")

System_Boundary(cmp, "CMP Platform") {
    Container(gateway, "Protocol Gateway", "Java/Spring", "Device connection and protocol handling")
    Container(manager, "Network Manager", "Java/Spring", "Device lifecycle management")
    Container(sync, "DMP Sync", "Java/Spring", "Syncs with DMP platform")
    Container(mq, "Message Queue", "RabbitMQ", "Device data messaging")
}

System_Boundary(dmp, "DMP Platform") {
    Container(dmp_api, "DMP API", "Node.js", "Device management API")
    ContainerDb(dmp_db, "DMP Database", "MySQL", "Device and product data")
}

System_Boundary(cloud, "Cloud Platform") {
    System_Ext(iot_cloud, "IoT Cloud", "Device data storage and analytics")
}

Rel(operator, gateway, "Configure", "Web UI")
Rel(admin, manager, "Manage", "Web API")
Rel(gateway, manager, "Device Events", "internal")
Rel(manager, mq, "Publish", "AMQP")
Rel(sync, mq, "Subscribe", "AMQP")
Rel(sync, dmp_api, "Sync Devices", "HTTP/REST")
Rel(mq, iot_cloud, "Forward Data", "MQTT")

@enduml
```

---

## Styling

### Custom Styles
```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

' Custom styling
<style>
person {
    BackgroundColor #3b82f6
    FontColor #ffffff
    BorderColor #1e40af
}
system {
    BackgroundColor #10b981
    FontColor #ffffff
    BorderColor #059669
}
system_db {
    BackgroundColor #f59e0b
    FontColor #ffffff
    BorderColor #d97706
}
</style>

Person(user, "User")
System(sys, "System")
Rel(user, sys, "Uses")

@enduml
```

### Default C4 Colors
- **Person**: `#08427b` (Dark Blue)
- **System**: `#1168bd` (Blue)
- **Container**: `#438dd5` (Light Blue)
- **Component**: `#85bbf0` (Pale Blue)
- **Database**: `#1168bd` (Blue)

---

## Rendering Options

### Via PlantUML JAR
```bash
java -jar plantuml.jar diagram.puml -tsvg
java -jar plantuml.jar diagram.puml -tpng
java -jar plantuml.jar diagram.puml -tpdf
```

### Via kroki.io API
```bash
# Render to SVG
curl -X POST -d "@diagram.puml" https://kroki.io/plantuml/svg

# Render to PNG
curl -X POST -d "@diagram.puml" https://kroki.io/plantuml/png

# Render with C4 library
curl -X POST -d "@diagram.puml" "https://kroki.io/plantuml/svg?include=c4"
```

### Online Renderers
- https://plantuml.com/plantuml/uml/
- https://kroki.io/#plantuml
- https://www.planttext.com/

---

## Best Practices

1. **Start with Context** - Always begin at the system context level
2. **One diagram per level** - Don't mix levels in one diagram
3. **Keep it simple** - Context < 10 elements, Container < 20 elements
4. **Use meaningful labels** - Description should explain the "what", technology the "how"
5. **Include users** - Always show who interacts with the system
6. **Color by type** - Distinguish people, systems, databases visually

---

## Template: IoT Device Platform

```plantuml
@startuml IoT_Platform_Architecture
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

title IoT Device Platform Architecture

' External Users
Person(device_admin, "Device Administrator")
Person(end_user, "End User")
Person(system_user, "System Operator")

' Platform Boundary
System_Boundary(platform, "IoT Platform") {

    ' Edge Layer
    Container_Boundary(edge, "Edge Layer") {
        Container(agent, "Device Agent", "Python", "Runs on devices")
        Container(edge_gw, "Edge Gateway", "Go", "Local device aggregation")
    }

    ' Connection Layer
    Container_Boundary(connection, "Connection Layer") {
        Container(cmp, "CMP", "Java/Spring", "Protocol translation & routing")
        Container(mqtt, "MQTT Broker", "EMQX", "Device messaging")
    }

    ' Management Layer
    Container_Boundary(management, "Management Layer") {
        Container(dmp, "DMP", "Node.js", "Device & product management")
        Container(rules, "Rule Engine", "Go", "Alarm & automation rules")
    }

    ' Data Layer
    Container_Boundary(data, "Data Layer") {
        ContainerDb(mysql, "MySQL", "MySQL 8.0", "Device metadata")
        ContainerDb(tsdb, "TSDB", "InfluxDB", "Time-series data")
        Container(es, "Elasticsearch", "ES 8.x", "Log & event search")
        Container(redis, "Cache", "Redis", "Session & hot data")
    }
}

' External Systems
System_Ext(cloud, "Cloud IoT Hub")
System_Ext(third_party, "Third-party API")

' Relationships
Rel(device_admin, dmp, "Manage Devices", "Web UI")
Rel(end_user, cloud, "View Data", "Web/Mobile")
Rel(system_user, cmp, "Monitor", "Dashboard")

Rel(agent, edge_gw, "Report", "MQTT")
Rel(edge_gw, mqtt, "Publish", "MQTT")
Rel(cmp, mqtt, "Subscribe", "MQTT")

Rel(cmp, dmp, "Sync Devices", "HTTP/REST")
Rel(dmp, mysql, "Device Metadata", "JDBC")
Rel(cmp, tsdb, "Device Data", "InfluxDB API")
Rel(rules, es, "Search Events", "HTTP")
Rel(dmp, redis, "Cache", "TCP")

Rel(mqtt, cloud, "Uplink/Downlink", "MQTT")
Rel(dmp, third_party, "Integration", "HTTP")

@enduml
```
