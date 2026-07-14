# 26 — AZURE ARCHITECTURE DIAGRAMS

## Objetivo

Proveer diagramas tecnicos en Mermaid listos para incorporarse en la propuesta o convertirse posteriormente en diagramas visuales. No son despliegues ni IaC.

## Diagrama 1 — Arquitectura general

```mermaid
flowchart TB
  U[Usuarios INCABIDE / PADF autorizados] --> DNS[DNS institucional]
  DNS --> AFD[Azure Front Door WAF]
  AFD --> AGW[Application Gateway WAF]
  AGW --> ACA[Azure Container Apps - SGB]
  ACA --> PG[(Azure Database for PostgreSQL + PostGIS + unaccent)]
  ACA --> BLOB[(Azure Blob Storage - documentos y multimedia)]
  ACA --> KV[Azure Key Vault]
  ACA --> MON[Azure Monitor / Application Insights]
  MON --> LAW[Log Analytics Workspace]
  LAW --> DEF[Microsoft Defender for Cloud]
  PG --> BCK[Backup / Recovery]
  BLOB --> BCK
```

## Diagrama 2 — Red y seguridad

```mermaid
flowchart LR
  Internet((Internet)) --> AFD[Front Door WAF]
  AFD --> AGW[App Gateway WAF - snet-appgw]
  subgraph VNET[Azure Virtual Network]
    AGW --> ACA[Container Apps internal - snet-containerapps]
    ACA --> PE1[Private Endpoint PostgreSQL]
    ACA --> PE2[Private Endpoint Storage]
    ACA --> PE3[Private Endpoint Key Vault]
    MGMT[VPN/Bastion - snet-management] --> ACA
    FW[Azure Firewall - snet-firewall] --> ACA
    NSG[NSGs por subred] -. controla .- ACA
  end
```

## Diagrama 3 — Identidad y secretos

```mermaid
flowchart TB
  Admin[Administrador] --> Entra[Microsoft Entra ID + MFA]
  Entra --> RBAC[Azure RBAC]
  Entra --> SGBRBAC[Roles SGB]
  ACA[Container Apps] --> MI[Managed Identity]
  MI --> KV[Key Vault]
  KV --> Secrets[Secretos / llaves / cadenas conexion]
  RBAC --> AzureResources[Recursos Azure]
```

## Diagrama 4 — Dev / Test / Prod

```mermaid
flowchart LR
  Repo[Repositorio Git] --> Build[Build / Scan / Package]
  Build --> ACR[Azure Container Registry]
  ACR --> Dev[Dev Environment]
  Dev --> QA[Test/QA Environment]
  QA --> UAT[UAT Environment]
  UAT --> Prod[Production Environment]
  Prod --> Monitor[Monitor + Logs + Alerts]
```

## Diagrama 5 — Observabilidad

```mermaid
flowchart TB
  AFD[Front Door] --> Logs[Log Analytics]
  AGW[Application Gateway] --> Logs
  ACA[Container Apps] --> AppInsights[Application Insights]
  AppInsights --> Logs
  PG[PostgreSQL] --> Monitor[Azure Monitor]
  Blob[Blob Storage] --> Monitor
  KV[Key Vault] --> Monitor
  Monitor --> Alerts[Alertas]
  Logs --> Dashboards[Dashboards operativos]
  Logs --> Defender[Defender for Cloud]
```

## Diagrama 6 — Backup y recuperacion

```mermaid
flowchart LR
  PG[(PostgreSQL)] --> PGB[Backups automaticos]
  Blob[(Blob Storage)] --> BlobRet[Versionado / retencion]
  KV[Key Vault] --> SoftDelete[Soft delete / purge protection]
  ACR[Container Registry] --> ImgRet[Retencion de imagenes]
  PGB --> Restore[Restore test]
  BlobRet --> Restore
  Restore --> DRP[DRP Runbook]
```

## Diagrama 7 — Flujo de solicitud segura

```mermaid
sequenceDiagram
  participant User as Usuario autorizado
  participant DNS as DNS/TLS
  participant AFD as Front Door WAF
  participant AGW as App Gateway WAF
  participant APP as SGB Container App
  participant DB as PostgreSQL
  participant ST as Blob Storage
  participant LOG as Monitor/Logs
  User->>DNS: Accede a dominio SGB
  DNS->>AFD: Resuelve y negocia TLS
  AFD->>AFD: Inspeccion WAF
  AFD->>AGW: Enruta solicitud
  AGW->>AGW: Inspeccion WAF regional
  AGW->>APP: Solicitud autorizada
  APP->>DB: Consulta datos por canal privado
  APP->>ST: Lee/escribe documentos por canal privado
  APP->>LOG: Registra evento y metricas
  APP-->>User: Respuesta segura
```

## Notas

- Los diagramas son proposal-ready, no IaC.
- La topologia final depende de validacion de region, tenant, ambientes, WAF, DDoS y RTO/RPO.
