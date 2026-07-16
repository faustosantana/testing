# scripts

Automatizaciones basicas del Bid Center INCABIDE TITAN.

## Scripts disponibles

- `init_project.sh`: confirma estructura base y crea carpetas faltantes.
- `validate_structure.sh`: valida carpetas, archivos y plantillas requeridas.
- `check_missing_documents.sh`: reporta documentos operativos esperados que aun no existen.
- `generate_checklist.sh`: genera un checklist de estado en `11_DELIVERY/`.

Ejecutar desde la raiz del proyecto:

```bash
bash scripts/validate_structure.sh
```
