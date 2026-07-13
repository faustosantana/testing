# REQUISITOS FUNCIONALES Y MODULOS ETAPA II

Fuente: Anexo 2 y Anexo 5 del RFP No. 5801 DRC3P.  
Estado: extraccion funcional para backlog y cumplimiento. No contiene diseno de solucion.

## Inventario de modulos y bloques funcionales

| ID | Modulo / bloque | Duracion de referencia RFP | Participacion pago RFP | Evidencia PDF |
| --- | --- | ---: | ---: | --- |
| MOD-001 | Registro e Ingreso de Activos (mejoras) | 1.5 meses | 7.73% | p.20, L1139-L1156; p.28, L1577-L1600 |
| MOD-002 | Gestion de Contratos y Clientes | 8 meses | 41.22% | p.20, L1157-L1176; p.28-29, L1601-L1638 |
| MOD-003 | Modulo de Subasta / Ventas | 1 mes | 5.15% | p.20, L1177-L1200; p.29, L1639-L1656 |
| MOD-004 | Descargo de Activos / Donaciones | 6.41 meses | 33.02% | p.21, L1210-L1229; p.29-30, L1657-L1684 |
| MOD-005 | Soporte Multilenguaje Espanol/Ingles | 2 meses | 10.30% | p.21, L1230-L1246; p.30, L1685-L1693 |
| MOD-006 | Seguridad y Control de Acceso Avanzado | 0.5 meses | 2.58% | p.21, L1247-L1264; p.30, L1694-L1711 |
| XMOD-001 | Documentacion Multimedia | Dentro de tiempos establecidos | Incluida / item transversal | p.21, L1282-L1286; p.30, L1715-L1720 |
| XMOD-002 | Geolocalizacion de Activos | Dentro de tiempos establecidos | Incluida / item transversal | p.21, L1287-L1290; p.30, L1721-L1724 |
| XMOD-003 | Control y Auditoria del Personal | Dentro de tiempos establecidos | Incluida / item transversal | p.21, L1291-L1295; p.31, L1730-L1734 |
| XMOD-004 | Importacion y Exportacion Masiva de Datos | Dentro de tiempos establecidos | Incluida / item transversal | p.22, L1302-L1306; p.31, L1735-L1739 |
| XMOD-005 | Reportes y Analisis para Toma de Decisiones | Dentro de tiempos establecidos | Incluida / item transversal | p.22, L1307-L1311; p.31, L1740-L1744 |

Total de modulos / bloques funcionales identificados: **11**.

## Requisitos generales de Etapa II

| ID | Requisito trazable | Evidencia PDF | Entregable / respuesta requerida |
| --- | --- | --- | --- |
| FUNC-GEN-001 | Etapa II se ejecutara de forma segmentada segun prioridades de INCABIDE. | p.20, L1129-L1131 | Backlog priorizable por modulo. |
| FUNC-GEN-002 | Propuesta debe detallar costo y tiempo por modulo. | p.20, L1129-L1132 | Matriz economica modular. |
| FUNC-GEN-003 | Antes de cada modulo se deben presentar pantallas, mockups o disenos web navegables. | p.20, L1131-L1133 | Prototipos validados. |
| FUNC-GEN-004 | Mockups/prototipos deben ser validados por INCABIDE antes del desarrollo. | p.20, L1131-L1133; p.22, L1317-L1318 | Acta/evidencia de validacion. |
| FUNC-GEN-005 | Por cada modulo se debe entregar codigo fuente completo en repositorio Git designado por INCABIDE. | p.22, L1318-L1319 | Codigo con historial commits. |
| FUNC-GEN-006 | Por cada modulo se deben entregar especificaciones funcionales aprobadas. | p.22, L1320-L1321 | Casos de uso, flujos, reglas. |
| FUNC-GEN-007 | Por cada modulo se deben ejecutar y aprobar pruebas funcionales, minimo UAT. | p.22, L1322-L1323 | Evidencia UAT. |
| FUNC-GEN-008 | Por cada modulo se debe entregar manual de usuario en espanol con capturas actualizadas. | p.22, L1324 | Manual PDF o en linea. |
| FUNC-GEN-009 | Por cada modulo se debe firmar acta de aceptacion parcial. | p.22, L1325-L1326 | Acta INCABIDE/PADF. |
| FUNC-GEN-010 | Los modulos pueden reordenarse, ejecutarse progresivamente o eliminarse por INCABIDE. | p.21, L1272-L1278; p.24, L1441-L1445 | Plan modular flexible. |

## MOD-001 — Registro e Ingreso de Activos

| ID | Requisito funcional | Evidencia PDF | Entregable / validacion |
| --- | --- | --- | --- |
| FUNC-001 | Identificacion unica de cada activo mediante numeros de serie, codigos de barras o codigos QR. | p.28, L1577-L1582 | Campos/codigos unicos. |
| FUNC-002 | Ingreso detallado de informacion especifica del activo. | p.28, L1580-L1583 | Formulario de activo. |
| FUNC-003 | Capturar valor monetario del activo. | p.28, L1581-L1583 | Campo valor. |
| FUNC-004 | Capturar especificaciones del activo. | p.28, L1581-L1583 | Campos especificaciones. |
| FUNC-005 | Capturar datos del seguro cuando corresponda. | p.28, L1581-L1583 | Campos seguro. |
| FUNC-006 | Capturar programas y requisitos de mantenimiento cuando corresponda. | p.28, L1581-L1583 | Campos mantenimiento. |
| FUNC-007 | Clasificacion y localizacion aplicable a bienes muebles fisicos. | p.28, L1584-L1586 | Clasificacion. |
| FUNC-008 | Para inmuebles usar referencia catastral o direccion. | p.28, L1584-L1586 | Campos inmueble. |
| FUNC-009 | Para activos financieros usar entidad y numero de cuenta o referencia. | p.28, L1584-L1586 | Campos activo financiero. |
| FUNC-010 | Registrar Zona con provincias, ciudades y municipios dominicanos. | p.28, L1586-L1588 | Catalogo geografico. |
| FUNC-011 | Registrar Ubicacion como pasillo y seccion dentro de almacen. | p.28, L1587-L1589 | Campos ubicacion. |
| FUNC-012 | Registrar Categoria: bienes muebles, inmuebles o activos financieros. | p.28, L1588-L1590 | Lista categoria. |
| FUNC-013 | Registrar Subcategoria: casas, apartamentos, vehiculos, ganado, etc. | p.28, L1589-L1590 | Lista subcategoria. |
| FUNC-014 | Campos definidos previamente deben ser listas desplegables. | p.28, L1591-L1593 | Dropdowns. |
| FUNC-015 | Listas desplegables sin posibilidad de variacion para minimizar errores. | p.28, L1591-L1593 | Control de entrada. |
| FUNC-016 | Cada activo debe tener campos predeterminados unicos y no repetitivos. | p.28, L1594-L1598 | Validacion unicidad. |
| FUNC-017 | Identificadores deben combinar valores fijos y variables. | p.28, L1594-L1598 | Regla de codigo. |
| FUNC-018 | Crear lista desplegable de entidades remitentes. | p.28, L1599-L1600 | Catalogo entidades. |
| FUNC-019 | Entidades remitentes incluyen PGR, DGII, DGA, DNCD, entre otras. | p.28, L1599-L1600 | Catalogo inicial. |
| FUNC-020 | Entregar diccionario de datos actualizado con campos nuevos. | p.22, L1328-L1330 | Diccionario de datos. |
| FUNC-021 | Entregar listado de codigos QR de prueba generados y validados. | p.22, L1328-L1330 | Evidencia QR. |

## MOD-002 — Gestion de Contratos y Clientes

| ID | Requisito funcional | Evidencia PDF | Entregable / validacion |
| --- | --- | --- | --- |
| FUNC-022 | Gestionar contratos con terceros y alertas principales. | p.28, L1601-L1604 | Modulo contratos. |
| FUNC-023 | Integrar administracion de clientes. | p.28, L1603-L1606 | Gestion clientes. |
| FUNC-024 | Procesamiento de pagos. | p.28-29, L1603-L1608; L1623-L1625 | Flujo pagos. |
| FUNC-025 | Analisis de depreciacion. | p.28-29, L1603-L1608; L1628-L1631 | Depreciacion. |
| FUNC-026 | Reporteria financiera. | p.28-29, L1603-L1608; L1636-L1638 | Reportes financieros. |
| FUNC-027 | Cliente se define como beneficiario de servicios de alquiler de activos. | p.28, L1605-L1607 | Modelo cliente. |
| FUNC-028 | Control financiero de ingresos y egresos por alquiler. | p.28, L1607-L1608 | Control financiero. |
| FUNC-029 | Canal de comunicacion sistematizado con clientes. | p.28, L1607-L1608 | Comunicaciones. |
| FUNC-030 | Vincular clientes con contratos de alquiler o acuerdos de servicios. | p.28, L1609-L1612 | Vinculacion contrato-cliente. |
| FUNC-031 | Seguimiento a contratos actuales y pasados. | p.28, L1609-L1612 | Historial contratos. |
| FUNC-032 | Recordatorios automatizados de renovacion. | p.28, L1609-L1612 | Alertas renovacion. |
| FUNC-033 | Alertas de vencimiento. | p.28, L1609-L1612 | Alertas vencimiento. |
| FUNC-034 | Creacion automatizada de contratos con plantillas personalizables. | p.28, L1610-L1612 | Plantillas contrato. |
| FUNC-035 | Configuracion de terminos contractuales: inicio, fin y condiciones. | p.28, L1611-L1612 | Campos terminos. |
| FUNC-036 | Alertas en tablero y por correo para notificaciones contractuales. | p.28, L1613-L1615 | Alertas email/tablero. |
| FUNC-037 | Plantillas de correo personalizables. | p.28, L1613-L1615 | Plantillas email. |
| FUNC-038 | Notificaciones periodicas programables a clientes. | p.28, L1613-L1615 | Programacion. |
| FUNC-039 | Almacenamiento seguro de copias digitales de contratos/acuerdos. | p.28, L1616-L1617 | Gestion documental. |
| FUNC-040 | Recuperacion facil y referencia de documentacion. | p.28, L1616-L1617 | Busqueda documental. |
| FUNC-041 | Registro y seguimiento de pagos totales y parciales. | p.29, L1623-L1625 | Registro pagos. |
| FUNC-042 | Generacion automatizada de comprobantes y recibos. | p.29, L1623-L1625 | Comprobantes. |
| FUNC-043 | Integracion con gestion financiera. | p.29, L1623-L1625 | Integracion financiera. |
| FUNC-044 | Estados de cuenta automatizados y en tiempo real. | p.29, L1623-L1625 | Estados cuenta. |
| FUNC-045 | Alertas configurables para pagos atrasados. | p.29, L1626-L1627 | Alertas mora. |
| FUNC-046 | Administracion de planes de pago de clientes en mora. | p.29, L1626-L1627 | Planes pago. |
| FUNC-047 | Metodos de depreciacion personalizables. | p.29, L1628-L1631 | Configuracion depreciacion. |
| FUNC-048 | Monitoreo de valor de mercado con alertas ante cambios significativos. | p.29, L1628-L1631 | Alertas valor. |
| FUNC-049 | Herramientas de apoyo a decision sobre venta o liquidacion anticipada. | p.29, L1628-L1631 | Soporte decision. |
| FUNC-050 | Informes de amortizacion mensuales, trimestrales o anuales. | p.29, L1628-L1631 | Reportes amortizacion. |
| FUNC-051 | Integracion con Inventario, Mantenimiento y Finanzas. | p.29, L1632-L1633 | Integracion modulos. |
| FUNC-052 | Intercambio de datos en tiempo real con modulos integrados. | p.29, L1632-L1633 | Sincronizacion. |
| FUNC-053 | Seguridad del modulo: cifrado de datos. | p.29, L1634-L1635 | Evidencia seguridad. |
| FUNC-054 | Seguridad del modulo: controles de acceso. | p.29, L1634-L1635 | RBAC. |
| FUNC-055 | Cumplimiento de proteccion de datos y normas financieras/auditoria. | p.29, L1634-L1635 | Controles cumplimiento. |
| FUNC-056 | Informes sobre actividad del cliente. | p.29, L1636-L1638 | Reporte cliente. |
| FUNC-057 | Informes sobre estado de contratos. | p.29, L1636-L1638 | Reporte contratos. |
| FUNC-058 | Informes sobre tendencias de pago. | p.29, L1636-L1638 | Reporte pagos. |
| FUNC-059 | Informes sobre metricas financieras. | p.29, L1636-L1638 | Reporte metricas. |
| FUNC-060 | Entregar flujos de aprobacion documentados. | p.22, L1331-L1334 | Documento flujos. |
| FUNC-061 | Entregar informe de prueba de integracion con Inventario y Mantenimiento. | p.22, L1331-L1334 | Informe integracion. |

## MOD-003 — Modulo de Subasta / Ventas

| ID | Requisito funcional | Evidencia PDF | Entregable / validacion |
| --- | --- | --- | --- |
| FUNC-062 | Gestionar ciclo completo de venta o disposicion de activos. | p.20, L1177-L1183; p.29, L1639-L1644 | Modulo gestion venta. |
| FUNC-063 | Integrar sistema de ejecucion de subasta existente de INCABIDE. | p.20, L1184-L1188; p.29, L1640-L1642 | Integracion subasta. |
| FUNC-064 | Complementar el modulo de gestion sin desarrollarlo desde cero. | p.20, L1184-L1188; p.29, L1640-L1642 | Alcance integracion. |
| FUNC-065 | Soportar subastas publicas con ofertas en vivo y subastadores. | p.29, L1645-L1647 | Metodo venta. |
| FUNC-066 | Soportar ofertas selladas confidenciales abiertas a hora predeterminada. | p.29, L1645-L1647 | Metodo venta. |
| FUNC-067 | Soportar procesos competitivos. | p.29, L1645-L1647 | Metodo venta. |
| FUNC-068 | Soportar ventas por lotes. | p.29, L1645-L1647 | Metodo venta. |
| FUNC-069 | Registrar adjudicaciones. | p.29, L1648-L1650 | Registro transaccion. |
| FUNC-070 | Registrar precios finales. | p.29, L1648-L1650 | Registro transaccion. |
| FUNC-071 | Registrar datos del postor ganador. | p.29, L1648-L1650 | Registro transaccion. |
| FUNC-072 | Seguir transaccion desde oferta ganadora hasta pago final y transferencia. | p.29, L1648-L1650 | Seguimiento. |
| FUNC-073 | Procesar pagos y emitir facturas. | p.29, L1648-L1650 | Facturacion. |
| FUNC-074 | Notificar postores sobre estado de oferta. | p.29, L1651-L1652 | Comunicaciones. |
| FUNC-075 | Notificar resultados de subasta. | p.29, L1651-L1652 | Comunicaciones. |
| FUNC-076 | Notificar proximos pasos. | p.29, L1651-L1652 | Comunicaciones. |
| FUNC-077 | Informes de resultados con historial de ofertas, precios y participacion. | p.29, L1653-L1654 | Reporte subasta. |
| FUNC-078 | Analisis de rendimiento. | p.29, L1653-L1654 | Analitica subasta. |
| FUNC-079 | Conciliacion de ingresos con registros financieros. | p.29, L1653-L1654 | Conciliacion. |
| FUNC-080 | Proteger informacion de postores y transacciones. | p.29, L1655-L1656 | Controles seguridad. |
| FUNC-081 | Cumplir requisitos legales/reglamentarios de subastas. | p.29, L1655-L1656 | Control cumplimiento. |
| FUNC-082 | Entregar procedimiento operativo de subasta documentado. | p.22, L1335-L1336 | Procedimiento. |
| FUNC-083 | Entregar informe de conciliacion financiera de prueba. | p.22, L1335-L1336 | Informe conciliacion. |

## MOD-004 — Descargo de Activos / Donaciones

| ID | Requisito funcional | Evidencia PDF | Entregable / validacion |
| --- | --- | --- | --- |
| FUNC-084 | Gestionar liquidacion de activos. | p.21, L1210-L1229; p.29, L1657-L1661 | Flujo liquidacion. |
| FUNC-085 | Gestionar devolucion de activos. | p.21, L1210-L1229; p.29-30, L1657-L1679 | Flujo devolucion. |
| FUNC-086 | Gestionar donacion de activos. | p.21, L1210-L1229; p.29, L1657-L1666 | Flujo donacion. |
| FUNC-087 | Gestionar destruccion de activos. | p.21, L1210-L1229; p.29, L1667-L1671 | Flujo destruccion. |
| FUNC-088 | Verificacion de propietarios. | p.21, L1212-L1216; p.30, L1677-L1679 | Validacion propietario. |
| FUNC-089 | Gestion documental. | p.21, L1212-L1216; p.29, L1662-L1666 | Documentos. |
| FUNC-090 | Cumplimiento ambiental y legal. | p.21, L1212-L1216; p.29-30, L1667-L1681 | Evidencia cumplimiento. |
| FUNC-091 | Flujos de aprobacion. | p.21, L1217-L1222; p.29, L1662-L1666 | Workflow. |
| FUNC-092 | Registros de transferencia. | p.21, L1217-L1222 | Registro transferencia. |
| FUNC-093 | Protocolos de destruccion. | p.21, L1221-L1222; p.29, L1667-L1671 | Protocolo. |
| FUNC-094 | Devolucion a propietarios legitimos. | p.21, L1223-L1225; p.30, L1677-L1679 | Flujo devolucion. |
| FUNC-095 | Donaciones: criterios de elegibilidad por estado, antiguedad, valor o restricciones legales. | p.29, L1662-L1666 | Reglas elegibilidad. |
| FUNC-096 | Donaciones: evaluacion automatizada de elegibilidad. | p.29, L1662-L1666 | Evaluacion automatica. |
| FUNC-097 | Donaciones: solicitudes con aprobacion multinivel. | p.29, L1662-L1666 | Workflow aprobacion. |
| FUNC-098 | Donaciones: formularios, aprobaciones y documentos legales. | p.29, L1662-L1666 | Gestion documental. |
| FUNC-099 | Donaciones: seguimiento de transferencia y confirmacion de recepcion. | p.29, L1662-L1666 | Confirmacion recepcion. |
| FUNC-100 | Destruccion: identificar bienes por criterios legales, seguridad y estado. | p.29, L1667-L1671 | Criterios destruccion. |
| FUNC-101 | Destruccion: protocolos por tipo de activo. | p.29, L1667-L1671 | Protocolo tipo. |
| FUNC-102 | Destruccion: comprobaciones ambientales y legales. | p.29, L1667-L1671 | Checklist cumplimiento. |
| FUNC-103 | Destruccion: gestion de proveedores externos cuando se subcontrate. | p.29, L1667-L1671 | Control proveedor. |
| FUNC-104 | Destruccion: registro de fecha, metodo, personal y razones. | p.29, L1667-L1671 | Registro auditoria. |
| FUNC-105 | Destruccion: generar documentacion legal correspondiente. | p.29, L1667-L1671 | Documento legal. |
| FUNC-106 | Devolucion: protocolos estandarizados. | p.30, L1677-L1679 | Protocolo devolucion. |
| FUNC-107 | Devolucion: gestion de reclamaciones. | p.30, L1677-L1679 | Flujo reclamaciones. |
| FUNC-108 | Devolucion: verificacion de propiedad. | p.30, L1677-L1679 | Validacion propiedad. |
| FUNC-109 | Devolucion: requisitos de documentacion. | p.30, L1677-L1679 | Checklist documentos. |
| FUNC-110 | Devolucion: registro de entrega y recepcion firmada. | p.30, L1677-L1679 | Acta entrega. |
| FUNC-111 | Cumplimiento y auditoria con registros detallados. | p.30, L1680-L1682 | Auditoria. |
| FUNC-112 | Informes sobre ventas, donaciones, destrucciones y devoluciones. | p.30, L1683-L1684 | Reportes disposicion. |
| FUNC-113 | Analisis de datos para mejorar eficiencia de procesos. | p.30, L1683-L1684 | Analitica. |
| FUNC-114 | Entregar protocolo de destruccion documentado. | p.22, L1337-L1340 | Protocolo. |
| FUNC-115 | Entregar evidencia de prueba del flujo completo de devolucion a propietario. | p.22, L1337-L1340 | Evidencia prueba. |

## MOD-005 — Soporte Multilenguaje

| ID | Requisito funcional | Evidencia PDF | Entregable / validacion |
| --- | --- | --- | --- |
| FUNC-116 | Interfaz en espanol e ingles. | p.21, L1230-L1246; p.30, L1685-L1689 | Idiomas. |
| FUNC-117 | Usuario puede cambiar idioma preferido. | p.30, L1685-L1689 | Selector idioma. |
| FUNC-118 | Traducir menus. | p.21, L1237-L1242; p.30, L1687-L1689 | Traducciones. |
| FUNC-119 | Traducir botones. | p.21, L1237-L1242; p.30, L1687-L1689 | Traducciones. |
| FUNC-120 | Traducir instrucciones. | p.21, L1237-L1242; p.30, L1687-L1689 | Traducciones. |
| FUNC-121 | Traducir elementos de navegacion. | p.30, L1687-L1689 | Traducciones. |
| FUNC-122 | Traducir manuales y recursos de ayuda. | p.30, L1687-L1689 | Manuales/ayuda. |
| FUNC-123 | Localizacion cultural de fechas. | p.21, L1233-L1236; p.30, L1692-L1693 | Formato regional. |
| FUNC-124 | Localizacion cultural de moneda. | p.21, L1233-L1236; p.30, L1692-L1693 | Formato moneda. |
| FUNC-125 | Localizacion de entornos regionales. | p.21, L1233-L1236; p.30, L1692-L1693 | Configuracion regional. |
| FUNC-126 | Entrada de datos en espanol. | p.30, L1690-L1691 | Entrada datos. |
| FUNC-127 | Procesar y mostrar correctamente datos en espanol. | p.30, L1690-L1691 | Validacion idioma. |
| FUNC-128 | Entregar archivo de traduccion JSON o equivalente. | p.22, L1341-L1343 | Archivo traduccion. |
| FUNC-129 | Evidencia de cambio de idioma en todas las vistas. | p.22, L1341-L1343 | Prueba idioma. |

## MOD-006 — Seguridad y Control de Acceso Avanzado

| ID | Requisito funcional | Evidencia PDF | Entregable / validacion |
| --- | --- | --- | --- |
| FUNC-130 | Tres niveles de usuario: Administracion, Gerente, Espectador. | p.21, L1247-L1260; p.30, L1694-L1707 | Roles base. |
| FUNC-131 | Permisos personalizables por modulo y accion. | p.21, L1249-L1253; p.30, L1708-L1709 | Matriz permisos. |
| FUNC-132 | Auditoria de actividad. | p.21, L1252-L1259; p.30, L1710-L1711 | Logs auditoria. |
| FUNC-133 | Cifrado. | p.21, L1252-L1253; p.30, L1696-L1698 | Cifrado. |
| FUNC-134 | MFA / 2FA. | p.21, L1252-L1260; p.30, L1696-L1699 | MFA. |
| FUNC-135 | Acceso basado en roles. | p.21, L1249-L1260; p.30, L1696-L1709 | RBAC. |
| FUNC-136 | Administracion: configuracion del sistema. | p.30, L1700-L1702 | Permisos admin. |
| FUNC-137 | Administracion: definicion de flujos de trabajo. | p.30, L1700-L1702 | Permisos admin. |
| FUNC-138 | Administracion: gestion de integraciones. | p.30, L1700-L1702 | Permisos admin. |
| FUNC-139 | Administracion: crear, modificar, eliminar usuarios y asignar roles/permisos. | p.30, L1700-L1702 | Permisos admin. |
| FUNC-140 | Gerente: supervision de operaciones diarias. | p.30, L1703-L1705 | Permisos gerente. |
| FUNC-141 | Gerente: acceso a informes detallados. | p.30, L1703-L1705 | Permisos gerente. |
| FUNC-142 | Gerente: gestion de transacciones dentro de su ambito. | p.30, L1703-L1705 | Permisos gerente. |
| FUNC-143 | Gerente sin configuracion global ni gestion de usuarios. | p.30, L1703-L1705 | Restricciones gerente. |
| FUNC-144 | Espectador: solo lectura a informes y datos relevantes. | p.30, L1706-L1707 | Permisos espectador. |
| FUNC-145 | Espectador sin modificar informacion ni realizar transacciones. | p.30, L1706-L1707 | Restricciones espectador. |
| FUNC-146 | Acciones configurables: ver, crear, editar, eliminar. | p.30, L1708-L1709 | Matriz permisos. |
| FUNC-147 | Autenticacion y autorizacion robustas. | p.30, L1710-L1711 | Control acceso. |
| FUNC-148 | Registros completos de actividad de usuarios. | p.30, L1710-L1711 | Auditoria. |
| FUNC-149 | Entregar matriz de permisos por rol. | p.22, L1344-L1347 | Matriz permisos. |
| FUNC-150 | Entregar informe de prueba de acceso con 2FA/MFA activo. | p.22, L1344-L1347 | Informe MFA. |

## Funciones complementarias transversales

| ID | Funcion | Requisito funcional | Evidencia PDF | Entregable / validacion |
| --- | --- | --- | --- | --- |
| FUNC-151 | Multimedia | Soportar imagenes JPEG/PNG. | p.21, L1282-L1286; p.30, L1715-L1717 | Carga imagenes. |
| FUNC-152 | Multimedia | Soportar videos MP4/AVI. | p.21, L1282-L1286; p.30, L1715-L1717 | Carga videos. |
| FUNC-153 | Multimedia | Soportar audio. | p.30, L1715-L1717 | Carga audio. |
| FUNC-154 | Multimedia | Soportar documentos PDF/DOCX. | p.21, L1282-L1286; p.30, L1715-L1717 | Carga documentos. |
| FUNC-155 | Multimedia | Integrar multimedia en registros de activos y mantenimiento. | p.30, L1715-L1717 | Asociacion registros. |
| FUNC-156 | Multimedia | Almacenamiento seguro. | p.21, L1282-L1286; p.30, L1717-L1720 | Almacenamiento. |
| FUNC-157 | Multimedia | Clasificacion, etiquetado y categorizacion. | p.21, L1282-L1286; p.30, L1717-L1720 | Metadata. |
| FUNC-158 | Multimedia | Busqueda avanzada. | p.21, L1282-L1286; p.30, L1717-L1720 | Busqueda. |
| FUNC-159 | Multimedia | Uso compartido controlado. | p.30, L1717-L1720 | Acceso controlado. |
| FUNC-160 | Multimedia | Auditoria y niveles de confidencialidad por documento. | p.30, L1717-L1720 | Auditoria/confidencialidad. |
| FUNC-161 | Geolocalizacion | Herramientas GPS/GIS para rastreo fisico en territorio dominicano. | p.21, L1287-L1290 | GIS/GPS. |
| FUNC-162 | Geolocalizacion | Mapas de Republica Dominicana. | p.21, L1287-L1290; p.30, L1721-L1724 | Mapa RD. |
| FUNC-163 | Geolocalizacion | Sincronizacion de datos de ubicacion. | p.21, L1287-L1290 | Sincronizacion. |
| FUNC-164 | Geolocalizacion | Monitoreo en tiempo real de ubicacion y movimientos. | p.30, L1721-L1724 | Rastreo. |
| FUNC-165 | Auditoria personal | Monitoreo automatizado de interacciones del personal con activos. | p.21, L1291-L1295; p.31, L1730-L1734 | Monitoreo. |
| FUNC-166 | Auditoria personal | Auditorias periodicas programadas. | p.21, L1291-L1295; p.31, L1730-L1734 | Auditoria. |
| FUNC-167 | Auditoria personal | Flujos de aprobacion para operaciones criticas. | p.21, L1291-L1295; p.31, L1730-L1734 | Workflows. |
| FUNC-168 | Auditoria personal | Registros de actividad. | p.21, L1291-L1295; p.31, L1730-L1734 | Logs. |
| FUNC-169 | Auditoria personal | Tablero personalizable con notificaciones principales. | p.21, L1291-L1295; p.31, L1730-L1734 | Dashboard. |
| FUNC-170 | Import/export | Importacion masiva en CSV. | p.22, L1302-L1306; p.31, L1735-L1739 | Import CSV. |
| FUNC-171 | Import/export | Importacion masiva en Excel. | p.22, L1302-L1306; p.31, L1735-L1739 | Import Excel. |
| FUNC-172 | Import/export | Exportacion en PDF. | p.31, L1735-L1739 | Export PDF. |
| FUNC-173 | Import/export | Validacion y manejo de errores. | p.31, L1735-L1739 | Validacion. |
| FUNC-174 | Import/export | Mapeo e integracion con estructura existente. | p.31, L1735-L1739 | Mapeo. |
| FUNC-175 | Import/export | Exportaciones personalizables. | p.31, L1735-L1739 | Export custom. |
| FUNC-176 | Import/export | Transferencia segura. | p.22, L1302-L1306; p.31, L1735-L1739 | Seguridad transferencia. |
| FUNC-177 | Import/export | Conectividad API para intercambio de datos en tiempo real. | p.22, L1302-L1306; p.31, L1735-L1739 | API. |
| FUNC-178 | Import/export | Control de acceso por roles y registros de auditoria en operaciones masivas. | p.31, L1735-L1739 | RBAC/auditoria. |
| FUNC-179 | Reportes | Informes de inventario. | p.31, L1740-L1744 | Reporte. |
| FUNC-180 | Reportes | Informes de depreciacion. | p.31, L1740-L1744 | Reporte. |
| FUNC-181 | Reportes | Informes de costos de mantenimiento. | p.31, L1740-L1744 | Reporte. |
| FUNC-182 | Reportes | Informes de utilizacion de activos. | p.31, L1740-L1744 | Reporte. |
| FUNC-183 | Reportes | Datos en tiempo real. | p.22, L1307-L1311; p.31, L1740-L1744 | Data realtime. |
| FUNC-184 | Reportes | Plantillas personalizables y herramientas drag-and-drop. | p.31, L1740-L1744 | Report builder. |
| FUNC-185 | Reportes | Graficos de barras, lineas y circulares. | p.22, L1307-L1311; p.31, L1740-L1744 | Visualizaciones. |
| FUNC-186 | Reportes | Exploracion avanzada de datos y filtrado. | p.31, L1740-L1744 | Analitica. |
| FUNC-187 | Reportes | Exportacion PDF, Excel y CSV. | p.22, L1307-L1311; p.31, L1740-L1744 | Exportaciones. |
| FUNC-188 | Reportes | Analisis predictivo y pronostico. | p.22, L1307-L1311; p.31, L1740-L1744 | Predictivo. |
| FUNC-189 | Transversal | Informe de integracion con modulos donde aplique. | p.22, L1348-L1352 | Informe integracion. |
| FUNC-190 | Transversal | Prueba de carga de archivo multimedia. | p.22, L1348-L1352 | Evidencia prueba. |
| FUNC-191 | Transversal | Prueba de reporte exportado en cada formato soportado. | p.22, L1348-L1352 | Evidencia exportacion. |
