# DEMO MASTER PLAN — INCABIDE TITAN

## Proposito

Disenar completamente la demo que se presentara al comite evaluador de PADF/INCABIDE, sin desarrollar pantallas, frontend, backend, infraestructura ni datos reales.

La demo debe mostrar el SGB como una plataforma Enterprise moderna que acompana el ciclo completo de vida de un bien: recepcion, registro, clasificacion, custodia, evidencia, decision, disposicion, auditoria y reporte ejecutivo.

## Critica tecnica obligatoria

| Pregunta | Decision |
| --- | --- |
| ¿Existe una mejor manera de hacer esta fase? | Si: disenar la demo como historia operativa de un bien, no como recorrido aislado por pantallas. |
| ¿Hay riesgo de retrabajo? | Si: si se crean pantallas antes de aprobar flujo, datos ficticios, roles y narrativa. |
| ¿Hay dependencias que resolver primero? | Si: aprobacion de flujo, alcance de pantallas, tono ejecutivo y datos ficticios permitidos. |
| ¿Se requiere detener el enfoque? | No. El enfoque narrativo cumple el objetivo y evita construir demo prematuramente. |

## Principios de la demo

- No usar datos reales.
- No simular capacidades fuera de la RFP.
- No prometer integracion PGR como entregable fijo.
- Mostrar seguridad, permisos y auditoria.
- Mostrar valor ejecutivo en menos de 30 segundos.
- Mostrar que el sistema es usable, moderno y trazable.
- Evitar apariencia de ERP.
- Presentar una historia clara, no una lista de funcionalidades.

## Audiencia

| Audiencia | Que necesita ver |
| --- | --- |
| Comite PADF | Cumplimiento, control, evidencia, seguridad y viabilidad. |
| Direccion INCABIDE | Visibilidad ejecutiva, alertas, valor y decisiones. |
| Equipo TI INCABIDE | Arquitectura operable, seguridad, monitoreo y soporte. |
| Usuarios funcionales | Registro facil, expediente claro y flujos de trabajo. |
| Auditoria / Legal | Trazabilidad, cadena de custodia, documentos y permisos. |

## Historia de la demo

**Titulo narrativo:** "De la recepcion del bien a la decision institucional".

La demo inicia con un Director de INCABIDE que necesita entender la situacion nacional de bienes bajo custodia. Desde el Dashboard Ejecutivo identifica una alerta critica: un bien de alto valor en Santo Domingo requiere completar documentacion y preparar decision de disposicion. El recorrido baja del nivel ejecutivo al expediente del bien, muestra su caso, documentos, ubicacion, cadena de custodia y auditoria. Luego un usuario administrador demuestra permisos, seguridad y configuracion basica. Finalmente se presenta el flujo de subasta/disposicion y se cierra con reportes ejecutivos.

## Usuarios de demostracion

| Usuario demo | Rol | Permisos mostrados | Proposito |
| --- | --- | --- | --- |
| `director.incabide.demo` | Ejecutivo | Lectura ejecutiva, dashboards, reportes, drill-down | Mostrar decision en 30 segundos. |
| `admin.sgb.demo` | Administrador | Usuarios, roles, configuracion, auditoria, catalogos | Mostrar control institucional. |
| `operador.activos.demo` | Operador | Registro, edicion controlada, documentos, custodia | Mostrar flujo operativo. |
| `auditor.demo` | Auditor | Timeline, auditoria, exportaciones controladas | Mostrar trazabilidad y cumplimiento. |

## Datos ficticios

Todos los datos son ficticios y deben marcarse como datos de demostracion.

| Entidad | Dato ficticio |
| --- | --- |
| Caso | `CASO-INC-2026-00428` |
| Bien principal | Vehiculo SUV blindado, placa ficticia `DEMO-7421` |
| Codigo SGB | `SGB-RD-000128` |
| Entidad remitente | PGR Demo |
| Provincia | Santo Domingo |
| Municipio | Distrito Nacional |
| Estado | En custodia - documentacion pendiente |
| Valor estimado | Usar etiqueta `Valor estimado demo`, sin monto real si no se aprueba |
| Responsable | Operador Demo |
| Documento | Acta de recepcion demo, fotografias demo, referencia judicial demo |
| Alerta | Documentacion pendiente para proceso de disposicion |
| Subasta demo | Lote demo `SUB-DEMO-2026-03` |

## Flujo maestro de la demo

| Paso | Pantalla | Usuario | Objetivo | Mensaje al comite |
| --- | --- | --- | --- | --- |
| 1 | Login / acceso seguro | Ejecutivo | Mostrar acceso controlado. | El sistema protege acceso y separa roles. |
| 2 | Dashboard Ejecutivo | Ejecutivo | Ver estado nacional en 30 segundos. | La Direccion entiende volumen, valor, estados, provincias y alertas. |
| 3 | Drill-down de alerta | Ejecutivo | Abrir lista filtrada desde alerta critica. | Los KPIs llevan a evidencia, no son graficas decorativas. |
| 4 | Expediente de Bien | Ejecutivo / Operador | Ver resumen completo del activo. | Cada bien tiene expediente unico y trazable. |
| 5 | Registro / edicion controlada | Operador | Mostrar datos estructurados y catalogos. | Se reducen errores con listas, validaciones y campos guiados. |
| 6 | Centro Documental | Operador | Adjuntar y clasificar evidencia. | Documentos y multimedia quedan vinculados al expediente. |
| 7 | Mapa Geografico | Ejecutivo | Ver ubicacion territorial. | INCABIDE puede supervisar bienes por provincia y municipio. |
| 8 | Cadena de Custodia | Auditor | Ver movimientos y responsables. | La custodia queda documentada y verificable. |
| 9 | Timeline / Auditoria | Auditor | Reconstruir historia del bien. | Cada accion relevante deja evidencia. |
| 10 | Subasta / Disposicion | Gerente / Operador | Preparar lote demo o proceso de disposicion. | La disposicion se gestiona con controles y aprobaciones. |
| 11 | Usuarios y permisos | Administrador | Mostrar roles, MFA/2FA conceptual y permisos. | No todos ven ni hacen lo mismo. |
| 12 | Reportes | Ejecutivo | Mostrar reporte ejecutivo y exportacion controlada. | La plataforma convierte operacion en decision. |
| 13 | Monitoreo / salud conceptual | Admin/TI | Mostrar estado de plataforma como concepto demo. | El sistema se opera, monitorea y respalda. |
| 14 | Cierre ejecutivo | Ejecutivo | Resumir beneficios. | Trazabilidad, seguridad, visibilidad y control institucional. |

## Pantallas requeridas para demo

| Pantalla | Objetivo | Informacion principal | Acciones | KPIs / alertas | Permisos |
| --- | --- | --- | --- | --- | --- |
| Login / seleccion rol | Mostrar seguridad inicial. | Usuario, rol, entorno demo. | Iniciar sesion. | Alerta MFA conceptual. | Todos segun rol. |
| Dashboard Ejecutivo | Decision rapida. | Total bienes, estados, provincias, alertas, subastas. | Filtrar, abrir KPI, abrir alerta. | Bienes, valor demo, alertas, proximas subastas. | Ejecutivo lectura. |
| Dashboard Operativo | Priorizar trabajo. | Pendientes, vencimientos, aprobaciones, bienes recientes. | Asignar, revisar, abrir expediente. | Pendientes, bloqueados, vencidos. | Gerente/admin. |
| Registro de Casos | Crear contexto legal. | Caso, entidad remitente, tipo penal, imputados demo. | Crear, guardar borrador, asociar bien. | Caso incompleto. | Operador autorizado. |
| Expediente de Bien | Vista 360 del activo. | Codigo, estado, ubicacion, valor demo, documentos, timeline. | Editar, adjuntar, solicitar aprobacion. | Documentos faltantes, estado. | Segun rol. |
| Centro Documental | Gestionar evidencia. | Documentos, tipo, confidencialidad, version. | Cargar, clasificar, ver, auditar. | Documento faltante. | Por confidencialidad. |
| Mapa Geografico | Visualizar ubicacion. | Provincia, municipio, clusters demo, estados. | Filtrar, abrir bien. | Bienes por provincia. | Lectura segun rol. |
| Cadena de Custodia | Evidenciar movimientos. | Origen, receptor, fecha, evidencia. | Registrar movimiento demo, exportar acta demo. | Movimiento sin firma. | Auditor/operador. |
| Timeline | Reconstruir historia. | Eventos, usuarios, cambios, documentos. | Filtrar, abrir evento. | Eventos criticos. | Auditor/gerente. |
| Subastas | Mostrar disposicion. | Lote, activos, estado, fecha demo. | Crear lote demo, revisar, cerrar demo. | Proximas subastas. | Gerente/admin. |
| Auditoria | Control de acciones. | Usuario, accion, fecha, recurso, IP demo. | Filtrar, investigar. | Accesos fallidos demo. | Auditor/admin. |
| Usuarios | Gestionar permisos. | Usuarios, roles, estado MFA, permisos. | Crear usuario demo, asignar rol. | Admin sin MFA. | Admin. |
| Configuracion | Mostrar catalogos. | Provincias, entidades remitentes, categorias. | Editar catalogo demo. | Catalogo incompleto. | Admin/config. |
| Reportes | Mostrar decision. | Reportes guardados, graficas, tabla. | Ejecutar, exportar demo. | Exportacion sensible. | Segun reporte. |

## Escenarios de demostracion

### Escenario 1 — Decision ejecutiva en 30 segundos

**Actor:** Director INCABIDE.  
**Objetivo:** identificar situacion general y alerta prioritaria.  
**Recorrido:** Login -> Dashboard Ejecutivo -> alerta critica -> expediente.  
**Mensaje:** la direccion no necesita navegar todo el sistema para entender riesgos.

### Escenario 2 — Registro controlado de un bien

**Actor:** Operador de activos.  
**Objetivo:** registrar un bien recibido con catalogos y evidencia.  
**Recorrido:** Casos -> Nuevo caso -> Registrar bien -> Adjuntar documento -> Guardar.  
**Mensaje:** el sistema reduce errores y crea trazabilidad desde el primer registro.

### Escenario 3 — Custodia y auditoria

**Actor:** Auditor.  
**Objetivo:** reconstruir movimientos y decisiones.  
**Recorrido:** Expediente -> Cadena de Custodia -> Timeline -> Auditoria.  
**Mensaje:** cada accion relevante tiene responsable, fecha y evidencia.

### Escenario 4 — Disposicion / subasta

**Actor:** Gerente operativo.  
**Objetivo:** preparar un bien para lote o proceso de disposicion.  
**Recorrido:** Expediente -> Validacion documental -> Subastas -> Lote demo -> Reporte.  
**Mensaje:** la disposicion final se gobierna con controles y aprobaciones.

### Escenario 5 — Administracion y seguridad

**Actor:** Administrador SGB.  
**Objetivo:** mostrar roles, permisos y configuracion.  
**Recorrido:** Usuarios -> Roles -> Permisos -> Auditoria de cambio.  
**Mensaje:** el sistema respeta permisos y deja evidencia de cambios.

## Guion de demostracion recomendado

Duracion objetivo: aproximadamente 15 minutos.

| Minuto | Pantalla | Que explicar | Beneficio a destacar | Pregunta probable | Respuesta sugerida |
| --- | --- | --- | --- | --- | --- |
| 0-1 | Apertura / entorno demo | Aclarar que son datos ficticios y que la demo sigue el ciclo de vida de un bien. | Transparencia y control del alcance. | ¿Son datos reales? | No. Son datos ficticios preparados para demostrar flujos. |
| 1-3 | Dashboard Ejecutivo | Mostrar bienes, estados, provincias, alertas y proximas subastas. | Decision ejecutiva en menos de 30 segundos. | ¿Puede un director llegar al detalle? | Si, cada KPI permite drill-down a evidencia. |
| 3-4 | Drill-down de alerta | Abrir una alerta critica y navegar a lista filtrada. | Los indicadores no son decorativos; guian accion. | ¿Como se priorizan alertas? | Por estado, criticidad y reglas funcionales configurables. |
| 4-6 | Expediente de Bien | Mostrar codigo, caso, estado, ubicacion, documentos y resumen. | Expediente unico y trazable. | ¿Todo queda en un solo lugar? | El expediente consolida datos, evidencia, timeline y custodia. |
| 6-7 | Registro / edicion controlada | Mostrar catalogos, campos obligatorios y validaciones. | Menos errores y mas consistencia. | ¿Se evita captura libre? | Se usan catalogos y validaciones donde la RFP lo requiere. |
| 7-8 | Centro Documental | Mostrar documentos, tipos, confidencialidad y version. | Evidencia vinculada al activo. | ¿Se auditan descargas? | Las acciones sensibles deben quedar auditadas. |
| 8-9 | Mapa Geografico | Mostrar provincia/municipio y acceso a expediente. | Supervision territorial. | ¿Que mapas se usaran? | Proveedor/fuente pendiente de validacion con INCABIDE. |
| 9-10 | Cadena de Custodia | Mostrar movimientos, responsables y evidencia. | Trazabilidad legal-operativa. | ¿Se puede reconstruir un traslado? | Si, con eventos, responsables, fechas y documentos. |
| 10-11 | Timeline / Auditoria | Filtrar eventos por usuario, fecha y accion. | Auditoria accionable. | ¿Quien hizo que cambio? | El timeline muestra usuario, accion, fecha y recurso. |
| 11-12 | Subastas / Disposicion | Mostrar lote demo y estado de proceso. | Disposicion gobernada. | ¿PGR esta integrado? | La API base es obligatoria; PGR es opcional y depende de aprobacion externa. |
| 12-13 | Usuarios y permisos | Mostrar roles y permisos conceptuales. | Seguridad por rol. | ¿Todos pueden editar? | No. Las acciones dependen de rol y permiso. |
| 13-14 | Reporte Ejecutivo | Mostrar reporte y exportacion controlada. | Operacion convertida en decision. | ¿Se puede exportar todo? | Exportaciones sensibles deben controlarse y auditarse. |
| 14-15 | Cierre | Resumir trazabilidad, seguridad, visibilidad y control. | Valor institucional. | ¿Que sigue? | Aprobar alcance de demo futura: prototipo, clickable o funcional. |

## Navegacion demo

```text
Login Ejecutivo
  -> Dashboard Ejecutivo
  -> Alerta critica
  -> Expediente de Bien
  -> Documentos
  -> Mapa
  -> Cadena de Custodia
  -> Timeline
  -> Subasta / Disposicion
  -> Reportes
  -> Cambio a Admin
  -> Usuarios / Permisos
  -> Auditoria
  -> Cierre Ejecutivo
```

## Datos ficticios requeridos

| Categoria | Datos necesarios |
| --- | --- |
| Casos | 5 casos demo con estados distintos. |
| Bienes | 20 bienes demo en distintas categorias. |
| Provincias | 6 provincias demo con distribucion territorial. |
| Documentos | 8 documentos demo con niveles de confidencialidad. |
| Usuarios | 4 usuarios demo por rol. |
| Subastas | 3 lotes demo: programado, en revision, cerrado. |
| Auditoria | 20 eventos demo. |
| Reportes | 5 reportes demo. |
| Alertas | 6 alertas demo: critica, vencimiento, documento faltante, seguridad. |

## Dataset ficticio sugerido

| Codigo | Tipo | Provincia | Estado | Alerta |
| --- | --- | --- | --- | --- |
| SGB-RD-000128 | Vehiculo | Santo Domingo | En custodia | Documentacion pendiente |
| SGB-RD-000129 | Inmueble | Santiago | En revision | Valor pendiente |
| SGB-RD-000130 | Activo financiero | Distrito Nacional | Bloqueado | Requiere aprobacion |
| SGB-RD-000131 | Vehiculo | La Altagracia | Preparado para subasta | Subasta proxima |
| SGB-RD-000132 | Inmueble | Puerto Plata | Donacion en revision | Documento legal faltante |

## Reglas de datos demo

- Usar nombres ficticios.
- No usar casos reales.
- No usar direcciones exactas reales.
- No usar placas reales.
- No usar documentos reales.
- No usar montos reales si no se aprueban.
- Marcar visualmente "Datos de demostracion".

## Historia verbal del presentador

1. "Comenzamos en la vista de direccion: INCABIDE ve el estado nacional de sus bienes."
2. "Una alerta ejecutiva nos lleva a un bien especifico."
3. "Este expediente concentra datos, documentos, ubicacion, estado y auditoria."
4. "El operador registra y completa informacion usando catalogos y validaciones."
5. "El auditor puede reconstruir toda la historia del bien."
6. "Cuando llega la disposicion, el sistema conserva aprobaciones y evidencia."
7. "El administrador controla usuarios, roles y permisos."
8. "La institucion termina con visibilidad, trazabilidad y seguridad."

## Criterios de exito de la demo

- El comite entiende el valor en los primeros 2 minutos.
- La demo muestra el ciclo de vida completo de un bien.
- No parece ERP ni formulario generico.
- Se evidencian permisos y auditoria.
- Se muestra Azure/operacion solo de forma conceptual, no como despliegue.
- No se prometen integraciones no aprobadas.
- Se evita cualquier dato real.
- Cada pantalla tiene proposito narrativo.

## Riesgos de la demo

| Riesgo | Mitigacion |
| --- | --- |
| Parecer mockup sin profundidad | Mostrar datos, estados, auditoria y decisiones. |
| Demasiadas pantallas | Mantener recorrido de 15-20 minutos. |
| Prometer funcionalidades fuera de alcance | Alinear con RFP y marcar conceptual cuando aplique. |
| Usar datos sensibles reales | Dataset completamente ficticio. |
| Confundir PGR con API obligatoria | Separar integracion PGR como opcional/pendiente. |
| No mostrar seguridad | Incluir usuarios, roles, auditoria y MFA conceptual. |

## Dependencias antes de desarrollar demo

- Aprobar flujo maestro.
- Aprobar pantallas incluidas.
- Aprobar dataset ficticio.
- Definir si se hara demo clickable, prototipo visual o demo funcional.
- Definir herramienta de prototipado.
- Definir estilo visual final.
- Definir alcance de Azure/monitoreo en demo.
- Definir presentador y guion final.

## Fuera de alcance en esta fase

- No desarrollar frontend.
- No crear backend.
- No crear base de datos.
- No desplegar Azure.
- No crear Docker Compose.
- No generar mockups visuales.
- No usar datos reales.

## Proxima decision requerida

Fausto debe aprobar:

1. historia central de la demo;
2. pantallas incluidas;
3. roles demo;
4. dataset ficticio;
5. duracion objetivo;
6. tipo de demo futura: prototipo, demo clickable o demo funcional.
