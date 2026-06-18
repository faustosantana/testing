# Justech Global Audit Log

Auditoría global configurable para entornos Odoo multiempresa.

## Objetivo

Registrar quién creó, modificó o eliminó documentos y registros en Odoo, incluyendo valor anterior, valor nuevo, fecha, usuario, empresa, modelo y documento.

Empresas de referencia:
- JUSTECH S.R.L.
- Just Office SRL
- PlugSafe SRL
- Omni Solutions SRL

## Instalación

1. Copiar `justech_global_audit_log` al directorio de addons custom.
2. Reiniciar Odoo o reconstruir la rama en Odoo.sh.
3. Actualizar lista de aplicaciones.
4. Instalar **Justech Global Audit Log** desde Apps.

### Odoo.sh

1. Subir el módulo al repositorio de la rama staging.
2. Verificar que la ruta de addons incluya el módulo.
3. Instalar desde Apps en staging.

### Servidor propio

```bash
cp -R justech_global_audit_log /opt/odoo/custom-addons/
# Reiniciar servicio Odoo
```

## Configuración

Menú: **Ajustes → Técnico → Auditoría Global Justech → Reglas**

- Cada regla define un modelo auditado.
- Solo las reglas **activas** generan logs.
- No auditar todos los modelos por defecto: activar solo lo necesario.

### Modelos auditados por defecto

| Modelo | Descripción |
|--------|-------------|
| sale.order | Pedidos de venta |
| purchase.order | Pedidos de compra |
| account.move | Facturas y asientos |
| stock.picking | Albaranes |
| res.partner | Contactos |
| product.template | Plantillas de producto |
| product.product | Variantes de producto |
| account.payment | Pagos |
| crm.lead | Oportunidades CRM |
| project.task | Tareas de proyecto |

## Cómo agregar nuevos modelos

1. Ir a **Reglas**.
2. Crear una regla nueva.
3. Seleccionar el modelo en `ir.model`.
4. Activar la regla.

Modelos soportados adicionalmente (ejemplos):
- stock.move
- helpdesk.ticket (requiere módulo helpdesk instalado)
- hr.employee (requiere módulo hr instalado)
- hr.expense (requiere módulo hr_expense instalado)

Modelos excluidos por diseño:
- justech.audit.log
- justech.audit.rule

## Consulta de logs

Menú: **Ajustes → Técnico → Auditoría Global Justech → Logs**

Filtros disponibles:
- Modelo, documento, usuario, empresa
- Tipo de operación (create, write, unlink)
- Campo, fecha
- Cambios de empresa / cliente
- Eliminaciones

## JSON-RPC para n8n

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
          ["field_name", "=", "company_id"],
          ["operation_type", "=", "write"]
        ]
      ],
      {
        "fields": [
          "record_name",
          "old_value",
          "new_value",
          "user_id",
          "company_id",
          "change_date",
          "ip_address"
        ],
        "limit": 100,
        "order": "change_date desc"
      }
    ]
  },
  "id": 1
}
```

Endpoint: `https://tu-instancia.odoo.com/jsonrpc`

## Seguridad

- Solo administradores (`Administración / Ajustes`) pueden ver logs.
- Los logs son de solo lectura en interfaz y permisos.
- Las reglas solo las gestionan administradores.

## Performance

- Solo se auditan modelos con regla activa.
- Campos técnicos ruidosos ignorados: write_date, write_uid, create_date, create_uid, message_ids, activity_ids, __last_update.
- Los logs se crean con `sudo()` sin alterar documentos originales.
- Evitar activar reglas en modelos transaccionales de alto volumen sin necesidad.

## Advertencia

Probar siempre en **staging** antes de producción. La auditoría global puede generar un volumen importante de registros según la actividad del sistema.

## Compatibilidad

Diseñado para Odoo 17/18/19.
