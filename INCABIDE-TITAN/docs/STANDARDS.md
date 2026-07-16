# GUIA DE ESTANDARES — INCABIDE TITAN

## Convencion de nombres

Usar nombres descriptivos, en mayusculas para carpetas principales y con prefijos funcionales cuando aplique.

Formato recomendado:

```text
AREA-TIPO-DESCRIPCION-vX.Y-YYYYMMDD.ext
```

Ejemplos:

- `RFP-MATRIZ-REQUISITOS-v0.1-20260713.md`
- `TEC-OFERTA-TECNICA-v0.1-20260713.md`
- `QA-CHECKLIST-FINAL-v1.0-20260717.md`

## Formato Markdown

- Usar un solo titulo `#` por documento.
- Usar tablas para controles y matrices.
- Mantener secciones breves y trazables.
- Evitar contenido duplicado entre documentos.
- Registrar pendientes con `TODO:` cuando sea necesario.

## Formato de imagenes

- Guardar imagenes en `assets/images/`.
- Usar formatos `png`, `jpg` o `webp`.
- Nombrar con prefijo de area y descripcion.
- Incluir texto alternativo cuando se referencien desde Markdown.

## Formato de diagramas

- Guardar fuentes de diagramas en `assets/diagrams/`.
- Preferir Mermaid para diagramas editables.
- Exportar imagenes finales solo cuando sea necesario.
- Mantener version fuente y version exportada sincronizadas.

## Formato de documentos

- Cada documento debe indicar version, responsable y estado.
- Los documentos finales deben tener revision QA.
- Los documentos administrativos deben conservar evidencia de aprobacion.
- No usar nombres genericos como `final-final` o `version nueva`.

## Formato de commits

Formato:

```text
tipo(area): descripcion breve
```

Tipos recomendados:

- `docs`
- `template`
- `script`
- `chore`
- `qa`

Ejemplos:

- `docs(war-room): update daily bid dashboard`
- `template(qa): add final delivery checklist`
- `script(validation): check required bid folders`

## Formato de versiones

Usar versionado semantico documental:

- `v0.x`: borradores.
- `v1.0`: version aprobada para entrega.
- `v1.x`: correcciones menores posteriores.
- `v2.0`: cambio mayor de alcance o estructura.

## Control de calidad

Antes de declarar un documento como listo:

- Confirmar responsable.
- Confirmar version.
- Revisar ortografia y consistencia.
- Validar trazabilidad con requisitos.
- Confirmar evidencias asociadas.

## Critica tecnica obligatoria antes de iniciar

Antes de comenzar cualquier fase, documento, diseno, arquitectura, demo, mockup, correccion o implementacion, se debe aplicar la regla permanente definida en `docs/TECHNICAL_CRITICAL_REVIEW_RULE.md`.

El equipo debe preguntarse si existe una manera mejor de ejecutar la fase, una arquitectura mas solida, una estrategia mas eficiente, una practica Enterprise superior, riesgo de retrabajo, dependencias no resueltas o puntos que el usuario no esta considerando.

Si existe una alternativa claramente superior, se debe detener la ejecucion, explicar la alternativa, justificarla y esperar aprobacion antes de cambiar el enfoque.

## Criterio de no conformidad

El proyecto adopta el criterio formal de no conformidad definido en `docs/QUALITY_NON_CONFORMITY_CRITERIA.md`.

Ningun entregable debe marcarse `PASS` solo porque no produjo error, abrio correctamente o paso una prueba aislada. Para aprobar, debe ser usable, coherente, consistente, seguro, claro, respetar permisos, evitar duplicidad y no introducir deuda tecnica evidente.

Si existe una alternativa claramente mejor dentro del mismo alcance, debe implementarse o documentarse antes de aprobar el entregable.

## Ciclo de mejora continua

Todo cambio debe aplicar el ciclo definido en `docs/CONTINUOUS_IMPROVEMENT_CYCLE.md`.

Despues de cada correccion se debe revalidar pantalla, flujo completo y modulo; buscar regresiones; y buscar oportunidades adicionales de mejora. Si aparece un nuevo problema, se corrige y se reinicia la revalidacion hasta estabilizar completamente el area.

La auditoria no debe limitarse a los problemas encontrados inicialmente.

## Filosofia de producto

No disenar como un ERP. Disenar como producto Enterprise moderno. Cada pantalla debe cuestionar si puede eliminarse algo, simplificarse, reducir clics, entenderse sin capacitacion, verse mejor, ser mas rapida, mas elegante y parecer desarrollada por Microsoft.
