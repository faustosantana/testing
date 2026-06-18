# Justech Audit Log

Módulo de auditoría interna para Odoo que registra cambios críticos en documentos multiempresa.

## Objetivo

Detectar y registrar cambios sensibles en cotizaciones, órdenes de compra, facturas y albaranes. El caso de referencia es una orden con secuencia de una empresa (por ejemplo `CJO-0000525` de Just Office SRL) registrada en otra empresa (JUSTECH S.R.L.), especialmente cuando `company_id` no tiene tracking nativo.

## Instalación

1. Copiar la carpeta `justech_audit_log` al directorio de addons de Odoo.
2. Actualizar la lista de aplicaciones.
3. Instalar **Justech Audit Log** desde Apps.
4. Probar primero en un entorno **staging**. No instalar directamente en producción sin validación.

### Odoo.sh

1. Subir el módulo al repositorio de la rama de staging.
2. Añadir la ruta de addons si aplica.
3. Reiniciar el build de staging.
4. Instalar el módulo desde Apps.

### Servidor propio

```bash
cp -R justech_audit_log /opt/odoo/custom-addons/
# Reiniciar Odoo y actualizar lista de apps
```

## Modelos auditados

| Modelo | Descripción |
|--------|-------------|
| `sale.order` | Cotizaciones / pedidos de venta |
| `purchase.order` | Órdenes de compra |
| `account.move` | Facturas y asientos |
| `stock.picking` | Albaranes |

## Campos auditados

### sale.order
- `company_id`
- `partner_id`
- `state`
- `amount_total`
- `user_id`
- `pricelist_id`

### purchase.order
- `company_id`
- `partner_id`
- `state`
- `amount_total`
- `user_id`

### account.move
- `company_id`
- `partner_id`
- `state`
- `amount_total`
- `move_type`

### stock.picking
- `company_id`
- `partner_id`
- `state`
- `origin`
- `picking_type_id`

## Consulta de logs

Menú: **Ajustes → Técnico → Auditoría Justech**

Solo usuarios administradores (`Administración / Ajustes`) pueden leer los registros.

## Ejemplo JSON-RPC para n8n

Consultar cambios de empresa en pedidos de venta:

```json
{
  "jsonrpc": "2.0",
  "method": "call",
  "params": {
    "service": "object",
    "method": "execute_kw",
    "args": [
      "nombre_base_datos",
      1,
      "api_key_o_password",
      "justech.audit.log",
      "search_read",
      [
        [
          ["model_name", "=", "sale.order"],
          ["technical_field_name", "=", "company_id"]
        ]
      ],
      {
        "fields": [
          "record_name",
          "old_value",
          "new_value",
          "user_id",
          "company_id",
          "change_date"
        ],
        "limit": 50,
        "order": "change_date desc"
      }
    ]
  },
  "id": 1
}
```

Endpoint típico: `https://tu-instancia.odoo.com/jsonrpc`

## Compatibilidad

Probado para Odoo 17/18/19. Usa `@api.model_create_multi` y herencia mixin compatible con versiones recientes.

## Advertencia

Probar siempre en staging antes de producción. El módulo genera un registro por cada campo modificado en cada `write()`, lo que puede incrementar el volumen de datos en entornos con mucha actividad.
