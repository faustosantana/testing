# 16 — DEVSECOPS

## Objetivo

Diseñar entrega segura para imagenes, configuracion, despliegues, escaneos y evidencias, sin implementar pipelines en esta fase.

## Flujo conceptual

```text
Codigo -> Revision -> Escaneo -> Build imagen -> Scan imagen -> Publicar ACR -> Deploy ambiente -> Pruebas -> Evidencia
```

## Controles

| Control | Objetivo |
| --- | --- |
| SAST | Calidad y vulnerabilidades codigo. |
| Secret scan | Evitar credenciales versionadas. |
| Dependency scan | Vulnerabilidades y licencias. |
| Container scan | Imagenes seguras. |
| IaC scan futuro | Cuando exista Terraform/Bicep. |
| Approval gates | Control antes de produccion. |
| Release notes | Trazabilidad de cambios. |

## Servicios Azure relacionados

- Azure Container Registry.
- Managed Identity.
- Key Vault.
- Defender for Cloud.
- Monitor/Log Analytics.

## Pendiente de validacion

- Herramienta CI/CD.
- Repositorio INCABIDE.
- Politica de ramas.
- Requisitos SBOM.
- Herramienta de escaneo aceptada.
