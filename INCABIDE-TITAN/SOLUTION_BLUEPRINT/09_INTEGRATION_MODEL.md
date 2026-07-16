# 09 — INTEGRATION MODEL

## Objetivo

Definir un modelo de interoperabilidad controlado para el SGB, separando la API obligatoria del SGB de integraciones externas cuyo alcance depende de terceros.

## Principios

- API segura y versionada.
- Integraciones desacopladas.
- Auditoria de intercambios.
- Autenticacion y autorizacion explicitas.
- Separacion entre API base e integraciones opcionales.
- Documentacion tecnica consumible por INCABIDE.

## Componentes de integracion

| Componente | Funcion |
| --- | --- |
| API SGB | Exponer funcionalidades controladas del sistema. |
| API Documentation | Especificacion tecnica, endpoints y reglas de uso. |
| Integration Logs | Registro de solicitudes, respuestas, errores y usuarios/sistemas. |
| Import/Export Engine | Cargas masivas, exportaciones y validaciones. |
| External Connectors | Adaptadores para PGR, subastas u otros sistemas aprobados. |

## API base SGB

La API base debe diseñarse como entregable obligatorio, pero su alcance funcional minimo debe confirmarse con PADF/INCABIDE.

Capacidades recomendadas de alto nivel:

- autenticacion segura;
- versionado;
- control de permisos;
- endpoints por dominios;
- validacion de entrada;
- logs de auditoria;
- documentacion tecnica;
- manejo de errores estandarizado.

## Integracion PGR

La RFP indica que la interconexion efectiva con PGR:

- depende de aprobacion de PGR;
- no tiene fecha fija;
- no esta sujeta a penalidad del proveedor;
- debe cotizarse por separado como item independiente.

Por tanto, el blueprint separa:

1. API SGB obligatoria.
2. Integracion PGR opcional.

## Sistema de subastas existente

La solucion debe integrarse con el sistema de ejecucion de subasta de INCABIDE, sin desarrollarlo desde cero. La integracion depende de:

- documentacion tecnica del sistema existente;
- mecanismo de intercambio;
- API o base de datos disponible;
- reglas de autenticacion;
- flujo de adjudicacion;
- datos de conciliacion.

## Importacion/exportacion

Soporte conceptual:

- CSV;
- Excel;
- PDF/exportaciones;
- validacion y mapeo;
- transferencia segura;
- auditoria;
- control de errores;
- aprobacion antes de cargas productivas.

## Seguridad de integraciones

- TLS;
- autenticacion por token/certificado segun decision;
- scopes o permisos por sistema;
- rate limiting cuando aplique;
- logs de auditoria;
- segregacion de credenciales;
- monitoreo de errores;
- revocacion de accesos.

## Decisiones pendientes

1. Alcance minimo API.
2. Estandar API requerido.
3. Documentacion OpenAPI/Swagger.
4. Sistemas externos ademas de PGR y subastas.
5. Mecanismo tecnico del sistema de subastas.
6. Requisitos de autenticacion externa.
7. Datos permitidos para intercambio.
8. Criterios de aceptacion de integraciones.
