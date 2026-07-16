# 09 — CONTAINER PLATFORM

## Objetivo

Ejecutar el SGB contenerizado en Azure, cumpliendo el requisito de Docker y permitiendo operacion segura.

## Opcion recomendada conceptual

Azure Container Apps + Azure Container Registry, `PENDIENTE DE VALIDACION` con PADF/INCABIDE.

## Justificacion

La RFP permite VM o servicio gestionado configurado para ejecutar contenedores Docker. Container Apps reduce operacion comparado con VM, soporta despliegue de contenedores y puede integrarse con red, identidad y observabilidad.

## Componentes

| Componente | Objetivo | Dependencias | Riesgo | Criticidad |
| --- | --- | --- | --- | --- |
| Azure Container Apps | Ejecutar aplicacion Django/API. | Imagen, red, secretos. | Aprobacion pendiente. | Alta |
| Azure Container Registry | Guardar imagenes privadas. | Pipeline/identidad. | Imagenes vulnerables. | Media |
| Managed Identity | Acceso a Key Vault/Storage. | Entra ID. | Compatibilidad app. | Alta |
| Environment variables | Config no sensible. | Separacion ambientes. | Secretos mal ubicados. | Alta |
| Health probes | Verificar salud. | Endpoints app. | Falsos positivos. | Media |

## Alternativas

- VM con Docker y proxy inverso: alineacion literal con partes de la RFP, mayor operacion.
- AKS: potente pero mas complejo.
- App Service for Containers: alternativa gestionada viable, pendiente de validacion.

## Pendiente de validacion

- Servicio gestionado aceptado.
- Necesidad explicita de Docker Compose en entrega vs ejecucion productiva.
- Estrategia de proxy inverso.
- Escalado esperado.
- Ambientes.
