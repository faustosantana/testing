# 03 — BUSINESS PROCESS

## Procesos institucionales cubiertos

La solucion debe representar el ciclo de vida de los bienes bajo custodia de INCABIDE, desde su recepcion hasta su disposicion, con trazabilidad documental, controles de aprobacion y auditoria.

## Mapa de procesos

| Proceso | Objetivo | Modulos relacionados |
| --- | --- | --- |
| Recepcion de activo | Registrar bien recibido con datos minimos, origen e identificador unico. | Registro de Activos |
| Clasificacion y ubicacion | Asignar categoria, subcategoria, provincia, ubicacion y referencia. | Registro, Geolocalizacion |
| Custodia y documentacion | Mantener evidencia multimedia, documentos y estado operativo. | Multimedia, Auditoria |
| Administracion contractual | Gestionar alquileres, clientes, pagos, alertas y documentos. | Contratos y Clientes |
| Venta / subasta | Gestionar disposicion comercial e integracion con sistema de subastas. | Subasta / Ventas |
| Donacion / destruccion / devolucion | Ejecutar disposicion no comercial con flujos legales y evidencia. | Descargo / Donaciones |
| Control de acceso | Administrar roles, permisos y acciones permitidas. | Seguridad Avanzada |
| Reporteria ejecutiva | Proveer indicadores y analisis para toma de decisiones. | Reportes / Analisis |

## Flujo de recepcion de activos

1. Registrar entidad remitente.
2. Capturar datos basicos del activo.
3. Generar identificador unico o QR.
4. Clasificar por tipo de activo.
5. Asociar ubicacion o referencia.
6. Adjuntar evidencia documental o multimedia.
7. Registrar usuario, fecha y accion en auditoria.

## Flujo de contrato y cliente

1. Crear o seleccionar cliente.
2. Asociar activo disponible a contrato.
3. Configurar fechas, condiciones y documentos.
4. Programar alertas de vencimiento y renovacion.
5. Registrar pagos totales o parciales.
6. Generar comprobantes y estados.
7. Monitorear mora, depreciacion y decisiones.

## Flujo de disposicion

1. Seleccionar activo candidato a disposicion.
2. Validar restricciones legales y documentales.
3. Elegir tipo de disposicion: venta, subasta, donacion, destruccion o devolucion.
4. Ejecutar flujo de aprobacion.
5. Registrar transacciones, adjudicaciones o actas.
6. Conciliar informacion financiera si aplica.
7. Cerrar activo con evidencia y auditoria.

## Flujo de aprobacion

```text
Solicitud -> Revision funcional -> Revision legal/administrativa -> Aprobacion -> Ejecucion -> Evidencia -> Cierre
```

## Roles de negocio

| Rol | Uso esperado |
| --- | --- |
| Administracion | Configuracion, usuarios, permisos, integraciones y aprobaciones mayores. |
| Gerente | Supervision operativa, reportes y transacciones dentro de su ambito. |
| Espectador | Consulta y reportes sin modificacion de informacion. |

## Controles de proceso

- listas desplegables para reducir errores;
- catálogos maestros controlados;
- flujos de aprobacion;
- bitacora de cambios;
- evidencia obligatoria en acciones sensibles;
- permisos por modulo y accion;
- reportes de excepciones;
- actas de aceptacion y cierre.

## Informacion pendiente

- catalogos oficiales;
- reglas legales especificas de disposicion;
- responsables de aprobacion;
- integraciones financieras;
- sistema de subastas existente;
- criterios UAT por proceso.
