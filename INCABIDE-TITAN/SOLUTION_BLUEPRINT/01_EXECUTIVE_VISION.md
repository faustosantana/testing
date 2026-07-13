# 01 — EXECUTIVE VISION

## Vision de solucion

INCABIDE necesita transformar el SGB existente en una plataforma institucional segura, gobernable, operable y escalable para administrar bienes incautados, decomisados y en extincion de dominio. La solucion ganadora debe mostrar que Justech entiende que el proyecto no es solo despliegue de software: es una plataforma critica de gobierno digital, datos sensibles, trazabilidad legal, operacion continua y adopcion institucional.

## Resultado objetivo

Una plataforma SGB modernizada sobre Microsoft Azure, basada en Django/Python y PostgreSQL/PostGIS, capaz de:

- operar los modulos existentes del codigo fuente original;
- adaptarse visual y terminologicamente a INCABIDE;
- exponer una API funcional para interoperabilidad;
- incorporar seguridad reforzada;
- preparar la evolucion modular de Etapa II;
- entregar evidencias de aceptacion por hito;
- transferir control operativo a INCABIDE.

## Tesis de valor

La solucion debe diferenciarse por tres atributos:

1. **Control de riesgo**: diagnostico temprano del codigo, trazabilidad de requisitos, QA por evidencias y gestion de penalidades.
2. **Seguridad institucional**: Zero Trust, MFA, cifrado, WAF, backups, monitoreo, pentest y gobierno de credenciales.
3. **Adopcion sostenible**: documentacion, capacitacion, runbooks, soporte y transferencia real de administracion.

## Principios de diseno

| Principio | Aplicacion |
| --- | --- |
| Cloud-ready | Refactorizacion de configuracion, archivos, reportes y geolocalizacion para nube. |
| Security by design | Controles desde infraestructura hasta aplicacion y datos. |
| Evidence-first | Cada hito debe producir evidencia verificable antes de aprobacion. |
| Modularidad | Etapa II separada por modulos contratables y priorizables. |
| Interoperabilidad controlada | API base del SGB separada de integraciones externas opcionales. |
| Operabilidad | Runbooks, monitoreo, alertas y soporte definidos desde el diseno. |
| Transferencia | INCABIDE debe poder operar la plataforma sin dependencia permanente. |

## Alcance funcional de alto nivel

- Registro e ingreso de activos.
- Gestion de contratos y clientes.
- Subasta / ventas integrada a sistema existente.
- Descargo, donaciones, devoluciones y destruccion.
- Multilenguaje.
- Seguridad y control de acceso avanzado.
- Documentacion multimedia.
- Geolocalizacion.
- Auditoria de personal.
- Importacion/exportacion masiva.
- Reportes y analisis para toma de decisiones.

## Indicadores de exito de la solucion

- SGB desplegado y accesible en dominio institucional con TLS.
- Modulos originales visibles y operables.
- API funcional validada.
- Evidencias de seguridad completas.
- Hitos aprobados por escrito.
- Codigo, documentacion, credenciales y runbooks entregados.
- INCABIDE con capacidad de administracion tecnica basica.

## Decisiones pendientes

La vision asume decisiones que deben confirmarse antes de arquitectura detallada:

- region Azure;
- tenant/suscripcion;
- ambientes;
- usuarios y concurrencia;
- volumen de datos y multimedia;
- RTO/RPO;
- alcance minimo API;
- alcance real de subastas;
- identidad institucional;
- criterios de analisis predictivo.
