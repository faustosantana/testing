# 13 — TESTING STRATEGY

## Objetivo

Definir una estrategia de pruebas que permita demostrar cumplimiento, reducir rechazos de entregables y generar evidencias para aprobacion PADF/INCABIDE.

## Niveles de prueba

| Nivel | Objetivo |
| --- | --- |
| Pruebas unitarias | Validar funciones y servicios criticos. |
| Pruebas de integracion | Validar interaccion entre aplicacion, base, almacenamiento y API. |
| Pruebas funcionales | Validar flujos de negocio contra requisitos. |
| UAT | Validacion por usuarios o responsables INCABIDE. |
| Pruebas de seguridad | Vulnerabilidades, MFA, TLS, secretos y accesos. |
| Pruebas de rendimiento basicas | Confirmar operacion bajo cargas acordadas. |
| Pruebas de backup/restore | Confirmar restauracion operativa. |

## Matriz requisito-prueba

Cada requisito debe mapearse a:

- ID de requisito;
- caso de prueba;
- datos de prueba;
- resultado esperado;
- evidencia;
- responsable;
- estado;
- aprobador.

## Pruebas por Etapa I

| Hito | Prueba clave |
| --- | --- |
| Hito 1 | Compilacion, ejecucion, dependencias y configuracion cloud-ready. |
| Hito 2 | Branding, terminologia y reportes sin referencias foraneas. |
| Hito 3 | Componentes Azure activos y acceso administrador INCABIDE. |
| Hito 4 | Dominio, TLS, contenedores, API, modulos originales y seguridad. |
| Hito 5 | Procedimientos ejecutables por tecnico INCABIDE. |
| Hito 6 | Transferencia y confirmacion de autonomia. |
| Hito 7 | Constancia y desglose de infraestructura. |
| Hito 8 | Accesos verificados y no retencion de credenciales. |
| Hito 9 | Canales de soporte y SLA verificados. |

## Pruebas por modulo Etapa II

Cada modulo debe entregar:

- mockups validados;
- especificaciones funcionales;
- casos de prueba;
- UAT aprobado;
- manual actualizado;
- acta de aceptacion parcial.

## Evidencias minimas

- capturas;
- logs;
- reportes de prueba;
- actas UAT;
- resultados de escaneo;
- reporte TLS;
- registro de backup;
- checklist de aceptacion;
- firmas o aprobaciones escritas.

## Control de defectos

| Severidad | Definicion |
| --- | --- |
| Critica | Bloquea operacion o seguridad. |
| Alta | Afecta funcionalidad principal o cumplimiento. |
| Media | Afecta flujo secundario con workaround. |
| Baja | Mejora o defecto menor. |

## Criterio de salida

No se debe solicitar aprobacion de un hito o modulo si:

- falta evidencia requerida;
- existen defectos criticos abiertos;
- existen vulnerabilidades altas o criticas abiertas;
- no se ejecuto UAT cuando aplica;
- no hay aprobador definido.
