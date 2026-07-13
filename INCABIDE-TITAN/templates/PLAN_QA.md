# PLANTILLA — PLAN DE QA

| Campo | Valor |
| --- | --- |
| Proyecto | INCABIDE TITAN |
| Responsable QA | TBD |
| Version | v0.1 |
| Estado | Borrador |

## Alcance de QA

- Revision de completitud.
- Revision de consistencia.
- Revision de formato.
- Revision de trazabilidad.
- Revision de evidencias.
- Revision de usabilidad, coherencia y consistencia de producto.
- Revision de permisos, seguridad y separacion de contexto cuando aplique.
- Revision de deuda tecnica, duplicidad y confusion potencial para el usuario.

## Critica tecnica obligatoria antes de iniciar

Antes de comenzar cualquier trabajo, aplicar `docs/TECHNICAL_CRITICAL_REVIEW_RULE.md`.

Preguntar si existe una manera mejor de abordar la fase, una arquitectura mas solida, una estrategia mas eficiente, una practica Enterprise superior, riesgo de retrabajo, dependencias que deban resolverse primero o consideraciones que el usuario no este viendo.

Si existe una alternativa claramente superior, detener la ejecucion, documentar la alternativa y esperar aprobacion antes de cambiar el enfoque.

## Criterio de no conformidad

No marcar `PASS` solo porque una funcionalidad no produjo error, abrio correctamente o paso una prueba aislada.

Una funcionalidad solo puede aprobarse si es usable, coherente, consistente con el producto, tiene buena UX, respeta permisos, respeta multiempresa/multientidad cuando aplique, no introduce deuda tecnica evidente, no duplica capacidades existentes y no genera confusion.

Si existe una alternativa claramente mejor dentro del mismo alcance, debe implementarse o documentarse antes de aprobar.

## Ciclo de mejora continua

Despues de cada correccion:

1. Revalidar la pantalla.
2. Revalidar el flujo completo.
3. Revalidar el modulo.
4. Buscar regresiones.
5. Buscar oportunidades adicionales de mejora.

Si aparece un nuevo problema, debe corregirse y reiniciar el ciclo hasta estabilizar completamente el area. No limitar la auditoria a los problemas encontrados inicialmente.

## Filosofia de producto

No disenar como un ERP. Disenar como un producto Enterprise moderno. Cada pantalla debe evaluarse preguntando si puede eliminarse algo, simplificarse, reducir clics, entenderse sin capacitacion, verse mejor, ser mas rapida, mas elegante y parecer un producto desarrollado por Microsoft.

## Checklist

| ID | Control | Responsable | Estado | Evidencia |
| --- | --- | --- | --- | --- |
| QA-001 | Documento tiene version y responsable | TBD | Pendiente | TBD |
| QA-002 | Documento cumple estandares | TBD | Pendiente | TBD |
| QA-003 | Requisitos estan trazados | TBD | Pendiente | TBD |
| QA-004 | Evidencias estan referenciadas | TBD | Pendiente | TBD |
| QA-005 | No se aprobo solo por ausencia de errores o prueba aislada | TBD | Pendiente | TBD |
| QA-006 | Flujo usable, coherente y consistente con el producto | TBD | Pendiente | TBD |
| QA-007 | Permisos y separacion de contexto validados | TBD | Pendiente | TBD |
| QA-008 | Sin duplicidad ni deuda tecnica evidente | TBD | Pendiente | TBD |
| QA-009 | Alternativas superiores dentro del alcance evaluadas | TBD | Pendiente | TBD |
| QA-010 | Pantalla, flujo completo y modulo revalidados despues de correcciones | TBD | Pendiente | TBD |
| QA-011 | Regresiones buscadas y documentadas | TBD | Pendiente | TBD |
| QA-012 | Oportunidades adicionales de mejora evaluadas | TBD | Pendiente | TBD |
| QA-013 | Experiencia evaluada contra filosofia Enterprise moderna, no ERP | TBD | Pendiente | TBD |
| QA-014 | Critica tecnica previa ejecutada antes de iniciar trabajo | TBD | Pendiente | TBD |
| QA-015 | Alternativas superiores evaluadas antes de ejecutar | TBD | Pendiente | TBD |
| QA-016 | Dependencias y riesgo de retrabajo revisados antes de avanzar | TBD | Pendiente | TBD |
