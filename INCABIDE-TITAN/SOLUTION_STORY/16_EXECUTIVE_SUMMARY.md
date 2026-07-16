# 16 — EXECUTIVE SUMMARY

INCABIDE requiere una plataforma tecnologica moderna para gestionar integralmente bienes incautados, decomisados y en extincion de dominio. La RFP identifica un SGB existente desarrollado en Django/Python con PostgreSQL, entregado en su estado actual, que debe ser adaptado, personalizado, desplegado en Microsoft Azure y preparado para evolucionar por modulos.

La solucion propuesta se concibe como una transformacion institucional del SGB: de una plataforma existente con limitaciones tecnicas y funcionales hacia un sistema seguro, trazable, operable y preparado para la toma de decisiones. El objetivo no es solo poner una aplicacion en produccion; es construir una plataforma que acompañe todo el ciclo de vida de un bien bajo custodia.

Desde que un bien llega a INCABIDE, el sistema debe registrar su origen, caso, entidad remitente, categoria, ubicacion, documentos y evidencia. Durante la custodia, cada movimiento, cambio de estado, documento, aprobacion y accion relevante debe quedar registrado en una linea de tiempo auditable. Cuando el bien avanza hacia subasta, donacion, devolucion, destruccion o cierre, el sistema debe sostener el flujo con permisos, controles, documentos y evidencia.

Para la Direccion, el SGB debe ofrecer una vision ejecutiva clara: total de bienes, valor economico estimado, distribucion por provincia, bienes por estado, alertas criticas, proximas subastas y procesos que requieren atencion. Para los operadores, debe simplificar el registro y seguimiento. Para auditores, debe permitir reconstruir decisiones. Para TI, debe entregar una plataforma documentada, monitoreada, respaldada y transferible.

La Etapa I se enfoca en diagnosticar y adaptar el codigo fuente existente, corregir dependencias, preparar el sistema para nube, aplicar identidad visual y terminologia INCABIDE, desplegar en Azure, contenerizar, publicar en dominio institucional, entregar documentacion tecnica, capacitar al equipo y activar soporte. La Etapa II permite evolucionar el sistema mediante modulos priorizables: registro de activos, contratos y clientes, subastas/ventas, descargo/donaciones, multilenguaje, seguridad avanzada y funciones transversales como multimedia, geolocalizacion, importacion/exportacion y reportes.

La seguridad es un eje central. La RFP exige controles reforzados: cifrado, MFA, RBAC, WAF, DDoS, gestion segura de secretos, monitoreo, backups cifrados, DRP, escaneos y pentest. La narrativa de solucion convierte esos requisitos en una plataforma verificable, donde cada hito genera evidencias y cada decision queda sustentada.

El resultado esperado es un SGB institucionalmente confiable: visible para la direccion, util para los equipos operativos, auditable para cumplimiento, seguro para datos sensibles y operable para INCABIDE. La propuesta debe construirse sobre esta historia: transformar la administracion de bienes en un proceso digital trazable, seguro y orientado a decisiones.
