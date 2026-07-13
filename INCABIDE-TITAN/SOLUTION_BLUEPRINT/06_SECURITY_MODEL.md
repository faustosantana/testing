# 06 — SECURITY MODEL

## Enfoque

El SGB administra informacion sensible sobre procesos penales, personas, bienes incautados y activos bajo custodia. El modelo de seguridad debe ser reforzado, verificable y alineado con los controles exigidos por la RFP.

## Principios

- Zero Trust.
- Minimo privilegio.
- Defensa en profundidad.
- Cifrado por defecto.
- Auditoria completa.
- Secretos fuera del codigo.
- Evidencia verificable para aceptacion.

## Controles de identidad y acceso

| Control | Diseno objetivo |
| --- | --- |
| MFA administrativo | Obligatorio para accesos privilegiados. |
| RBAC | Roles por modulo y accion: ver, crear, editar, eliminar. |
| Separacion de funciones | Administracion, Gerente y Espectador como base. |
| Cuentas de servicio | Privilegios minimos, rotacion y vault. |
| Acceso administrativo | VPN/Bastion/canal seguro segun diseno final. |

## Seguridad de aplicacion

- validacion de entradas;
- proteccion contra OWASP Top 10;
- manejo seguro de sesiones;
- control CSRF y configuraciones seguras Django;
- headers de seguridad;
- registro de eventos sensibles;
- autorizacion a nivel de vista, API y accion;
- escaneo de dependencias;
- prueba de vulnerabilidades antes de produccion.

## Seguridad de datos

| Area | Control |
| --- | --- |
| Datos en transito | TLS/HTTPS. |
| Datos en reposo | Cifrado de base de datos y almacenamiento. |
| Datos sensibles | Minimizacion, acceso por rol y trazabilidad. |
| Credenciales | Vault; nunca en codigo o archivos versionados. |
| Backups | Cifrados, automaticos y restaurables. |
| Auditoria | Logs de accesos, cambios y acciones criticas. |

## Seguridad perimetral y red

- WAF con proteccion OWASP Top 10.
- Firewall y reglas por IP/puerto.
- Red segmentada.
- Acceso administrativo restringido.
- DDoS segun nivel aprobado.
- Monitoreo y alertas.

## Evidencias de seguridad

La solucion debe preparar:

1. Documento de arquitectura de seguridad.
2. Evidencias de configuracion de controles.
3. Informe de vulnerabilidades con CVSS.
4. Reporte TLS/HTTPS con calificacion minima requerida.
5. Informe de prueba MFA.
6. Registro de backup restaurable.
7. Declaracion de no credenciales en codigo.
8. Pentest tercero independiente post-produccion.

## Auditoria

Eventos minimos:

- inicio/cierre de sesion;
- cambios de rol/permisos;
- creacion/modificacion/eliminacion de activos;
- carga/descarga de documentos;
- aprobaciones y rechazos;
- exportaciones masivas;
- cambios contractuales;
- operaciones de disposicion;
- accesos administrativos;
- fallos de autenticacion.

## Riesgos de seguridad a controlar

- credenciales en codigo;
- permisos excesivos;
- APIs sin alcance definido;
- multimedia sin validacion;
- exportaciones masivas no auditadas;
- vulnerabilidades altas/criticas abiertas;
- acceso administrativo no segmentado;
- backups no restaurables.
