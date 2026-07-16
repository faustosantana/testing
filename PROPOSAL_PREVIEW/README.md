# PROPOSAL PREVIEW

Vista navegable local de la propuesta tecnica INCABIDE TITAN usando MkDocs Material.

## Instalacion

```bash
python3 -m pip install --user -r PROPOSAL_PREVIEW/requirements.txt
```

## Sincronizar capitulos

```bash
python3 PROPOSAL_PREVIEW/sync_proposal_docs.py
```

## Ejecutar localmente

```bash
export PATH="$HOME/.local/bin:$PATH"
mkdocs serve --config-file PROPOSAL_PREVIEW/mkdocs.yml --dev-addr 127.0.0.1:8000
```

## Exportar a PDF

Abrir la opcion **Exportar / imprimir PDF** en la navegacion lateral o visitar:

```text
http://127.0.0.1:8000/print_page/
```

Luego usar la funcion de impresion del navegador y seleccionar "Guardar como PDF".
