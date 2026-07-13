# 10 — MODULES UX

## Pantallas maestras

Cada pantalla se describe como especificacion de experiencia, no como mockup ni desarrollo.

| Pantalla | Objetivo | Usuario | Informacion principal | Acciones | KPIs | Alertas | Permisos | Flujo de navegacion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dashboard Ejecutivo | Dar vision ministerial en menos de 30 segundos. | Director, alta direccion | total bienes, valor, mapa, estados, alertas, subastas, procesos criticos | filtrar, abrir detalle, exportar resumen, ver alerta | total bienes, valor, provincias, estados, alertas, subastas | criticas institucionales | direccion/espectador autorizado | Inicio > Dashboard Ejecutivo > Detalle KPI |
| Dashboard Operativo | Priorizar trabajo diario. | Gerente, supervisor | tareas, aprobaciones, vencimientos, bienes recientes | asignar, aprobar, revisar, filtrar | pendientes, vencidos, nuevos, bloqueados | vencimientos, documentos faltantes | gerente/admin | Inicio > Operativo > Lista filtrada |
| Registro de Casos | Crear y consultar casos vinculados a bienes. | Operador, gerente | numero caso, fiscalia, tipo penal, imputados, estado | crear caso, editar, asociar bien, adjuntar | casos activos, pendientes, nuevos | casos incompletos | crear/editar segun rol | Casos > Lista > Nuevo/Detalle |
| Expediente de Bien | Concentrar informacion completa del bien. | Operador, gerente, auditor | codigo, categoria, estado, ubicacion, valor, documentos, timeline | editar, mover, adjuntar, aprobar, exportar | valor, dias en estado, documentos, alertas | documentacion faltante, vencimientos | por rol y accion | Bienes > Lista > Expediente |
| Linea de Tiempo | Reconstruir historia del caso o bien. | Auditor, gerente | eventos, fechas, usuarios, documentos, cambios | filtrar, exportar, abrir evento | eventos criticos, aprobaciones, cambios | eventos sospechosos | auditor/gerente/admin | Expediente > Timeline |
| Cadena de Custodia | Evidenciar movimientos y responsables. | Auditor, legal, operador | origen, traslado, receptor, fechas, evidencia | registrar movimiento, validar, exportar acta | movimientos, pendientes firma, inconsistencias | ruptura o falta firma | roles autorizados | Expediente > Custodia |
| Mapa Geografico | Visualizar bienes por territorio. | Director, gerente, operador | provincia, municipio, clusters, categorias, estados | filtrar, abrir bien, cambiar capa | bienes por provincia, valor territorial, alertas | provincias con riesgo | lectura segun rol | Mapa > Provincia > Bien |
| Subastas | Gestionar disposicion por subasta/venta. | Gerente, operador, auditor | lotes, fechas, postores, estado, conciliacion | crear lote, publicar, cerrar, conciliar | proximas, valor, adjudicadas, pendientes | subasta sin conciliacion | gerente/admin | Subastas > Proceso > Lote |
| Reportes | Consultar, filtrar y exportar informacion. | Todos segun permiso | reportes guardados, filtros, graficas, tablas | crear, ejecutar, exportar, programar | reportes usados, exportaciones | exportacion sensible | permisos por reporte | Reportes > Categoria > Resultado |
| Auditoria | Supervisar accesos y acciones sensibles. | Auditor, seguridad, admin | eventos, usuario, accion, IP, fecha, recurso | filtrar, investigar, exportar | accesos fallidos, cambios, exportaciones | patron anomalo | auditor/admin | Auditoria > Eventos > Detalle |
| Usuarios | Administrar identidades, roles y MFA. | Administrador | usuarios, roles, estado MFA, actividad | crear, desactivar, asignar rol, reset MFA | usuarios activos, MFA pendiente, privilegios | admin sin MFA | admin | Usuarios > Lista > Perfil |
| Configuracion | Gestionar catalogos y parametros. | Administrador funcional | catalogos, entidades, provincias, categorias, integraciones | editar catalogo, importar, activar | catalogos incompletos, cambios | cambio sensible | admin/config | Configuracion > Catalogo |
| Centro Documental | Gestionar documentos y multimedia. | Operador, auditor, gerente | documentos, tipo, confidencialidad, relacion, version | cargar, clasificar, ver, descargar | documentos, pendientes, confidenciales | archivo sensible o faltante | por confidencialidad | Documentos > Biblioteca > Detalle |

## Detalle por pantalla

### Dashboard Ejecutivo

- **Objetivo:** visibilidad institucional inmediata.
- **Usuario:** Director de INCABIDE, alta direccion, PADF autorizado.
- **Informacion principal:** KPIs agregados, mapa, alertas, subastas, procesos criticos.
- **Acciones:** abrir detalle, descargar resumen, filtrar por periodo/provincia/estado.
- **Permisos:** lectura ejecutiva; sin edicion directa.
- **Flujo:** Inicio -> KPI -> lista filtrada -> expediente.

### Registro de Casos

- **Objetivo:** iniciar trazabilidad legal-operativa.
- **Usuario:** operador autorizado.
- **Informacion principal:** datos del caso, fiscalia remitente, imputados, etapa, documentos.
- **Acciones:** guardar borrador, validar, asociar bienes, adjuntar evidencia.
- **Alertas:** campos obligatorios faltantes, duplicado potencial.
- **Flujo:** Casos -> Nuevo caso -> Asociar bienes -> Confirmar.

### Expediente de Bien

- **Objetivo:** pagina unica del activo.
- **Usuario:** operador, gerente, auditor.
- **Informacion principal:** resumen, estado, ubicacion, valor, documentos, timeline, custodia.
- **Acciones:** editar segun permisos, cambiar estado, adjuntar, exportar, solicitar aprobacion.
- **Alertas:** falta evidencia, estado vencido, permiso insuficiente.
- **Flujo:** Bienes -> Lista -> Expediente -> Secciones.

### Cadena de Custodia

- **Objetivo:** proteger trazabilidad de movimientos.
- **Usuario:** operador, auditor, legal.
- **Informacion principal:** quien entrega, quien recibe, fecha, ubicacion, evidencia.
- **Acciones:** registrar movimiento, validar firma, adjuntar acta, exportar.
- **Alertas:** movimiento sin receptor, falta firma, inconsistencia.

### Mapa Geografico

- **Objetivo:** entender distribucion territorial.
- **Usuario:** director, gerente, operador.
- **Informacion principal:** bienes por provincia, valor, estado, tipo.
- **Acciones:** filtrar, abrir cluster, abrir expediente, exportar vista.
- **KPIs:** provincias con mas bienes, valor por provincia, alertas territoriales.

### Centro Documental

- **Objetivo:** concentrar evidencias y documentos.
- **Usuario:** operador, auditor, gerente.
- **Informacion principal:** documentos por expediente, tipo, version, confidencialidad.
- **Acciones:** cargar, clasificar, reemplazar version, descargar, auditar.
- **Permisos:** segun rol, confidencialidad y relacion con expediente.
