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
