# INCABIDE TITAN

Repositorio Enterprise para administrar la licitacion RFP No. 5801 DRC3P de PADF / INCABIDE para Justech SRL.

Este espacio es el Bid Center oficial del proyecto. Su proposito es coordinar, controlar y documentar el trabajo necesario para producir los documentos formales de la propuesta durante un ciclo intensivo de cinco dias, manteniendo trazabilidad, calidad y reutilizacion para futuras licitaciones.

## Objetivo

Construir un entorno profesional de trabajo para la gestion integral de la licitacion INCABIDE TITAN, incluyendo control documental, tareas, riesgos, evidencias, plantillas, automatizacion basica y reglas operativas.

## Alcance

Incluye:

- Organizacion del repositorio de licitacion.
- Gestion del RFP y sus requisitos.
- Control de documentos de propuesta.
- Seguimiento de tareas, riesgos, hitos y decisiones.
- Plantillas reutilizables para entregables.
- Automatizaciones basicas de validacion.
- Evidencias y referencias de soporte.

No incluye en esta fase:

- Desarrollo de la propuesta tecnica.
- Desarrollo de la oferta economica.
- Arquitectura de solucion.
- Diseno Azure.
- Demo funcional.
- Presentaciones finales.

## Entregables del Bid Center

- Estructura Enterprise del repositorio.
- Plan general del proyecto.
- Administrador de tareas.
- Registro de riesgos.
- Dashboard War Room.
- Guia de estandares.
- Plantillas oficiales.
- Scripts de inicializacion y validacion.
- Checklist final base.

## Metodologia de trabajo

La metodologia de esta fase se limita a la administracion del Bid Center:

1. Centralizar todos los insumos oficiales.
2. Registrar requisitos, decisiones, tareas y riesgos.
3. Mantener trazabilidad entre RFP, entregables y evidencias.
4. Trabajar con control de versiones.
5. Validar completitud documental antes de cada cierre diario.

## Cronograma de cinco dias

| Dia | Enfoque de control | Resultado esperado |
| --- | --- | --- |
| Dia 1 | Organizacion, lectura del RFP y matriz de requisitos | Repositorio operativo y requisitos identificados |
| Dia 2 | Produccion controlada de contenidos | Borradores estructurados y dependencias visibles |
| Dia 3 | Integracion, evidencias y revision cruzada | Documentos alineados y brechas registradas |
| Dia 4 | QA documental y preparacion de entrega | Version candidata de entrega |
| Dia 5 | Cierre, aprobaciones y paquete final | Entrega final controlada |

## Reglas de trabajo

- No modificar documentos oficiales sin registrar cambio.
- No incorporar contenido no validado en entregables finales.
- Toda decision relevante debe registrarse en el War Room.
- Toda tarea debe tener responsable, estado y dependencia cuando aplique.
- Toda evidencia debe almacenarse en `99_EVIDENCE/`.
- Los documentos finales deben pasar por QA antes de entrega.

## Estandares

Los estandares se mantienen en `docs/STANDARDS.md` e incluyen:

- Convencion de nombres.
- Formato Markdown.
- Formato de imagenes y diagramas.
- Formato de documentos.
- Formato de commits.
- Versionado documental.

## Estructura del repositorio

```text
INCABIDE-TITAN/
├── 00_WAR_ROOM/
├── 01_RFP/
├── 02_REQUIREMENTS/
├── 03_PROPOSAL/
├── 04_AZURE/
├── 05_DEMO/
├── 06_PRESENTATION/
├── 07_COSTS/
├── 08_REFERENCES/
├── 09_TEAM/
├── 10_LEGAL/
├── 11_DELIVERY/
├── 99_EVIDENCE/
├── assets/
├── docs/
├── scripts/
└── templates/
```

## Flujo de trabajo

1. Registrar insumos en la carpeta correspondiente.
2. Convertir requisitos en tareas y dependencias.
3. Usar plantillas oficiales para nuevos documentos.
4. Guardar evidencias y referencias con nombres normalizados.
5. Ejecutar validaciones antes de cada cierre.
6. Actualizar dashboard, tareas, riesgos y changelog.

## Estado inicial

Fase 0 completada cuando la estructura, documentos de control, plantillas y scripts basicos esten creados y validados.
