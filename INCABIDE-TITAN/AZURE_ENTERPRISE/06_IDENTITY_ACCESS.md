# 06 — IDENTITY ACCESS

## Objetivo

Definir identidad, acceso administrativo, MFA, RBAC y minimo privilegio.

## Modelo propuesto

| Area | Diseno |
| --- | --- |
| Identidad cloud | Microsoft Entra ID. |
| Administradores | MFA obligatorio. |
| Aplicacion a recursos | Managed Identity hacia Key Vault, Storage y base de datos cuando aplique. |
| Permisos Azure | RBAC por rol operativo. |
| Usuarios SGB | PENDIENTE DE VALIDACION: Entra ID/SSO o usuarios gestionados por aplicacion. |

## Roles Azure conceptuales

- Owner limitado a responsables autorizados.
- Contributor para operacion controlada.
- Reader para auditoria/consulta.
- Key Vault Secrets User para identidades gestionadas.
- Monitoring Reader para soporte.
- Security Reader para revision.

## Acceso administrativo

Debe realizarse por VPN/Bastion/canal seguro. No se deben exponer puertos administrativos directamente a Internet.

## Riesgos

- tenant no definido;
- exceso de privilegios;
- cuentas compartidas;
- MFA no aplicado;
- credenciales retenidas por proveedor;
- falta de proceso de baja de usuarios.

## Alternativas

| Alternativa | Uso |
| --- | --- |
| Entra ID SSO para usuarios SGB | Preferible si INCABIDE lo aprueba. |
| Usuarios locales en Django | Puede ser transitorio, requiere MFA/controles segun alcance. |
| Service principal | Alternativa si Managed Identity no es viable. |

## Pendiente de validacion

- Tenant INCABIDE o proveedor.
- SSO Entra ID para usuarios finales.
- Politica MFA.
- Proceso de entrega/verificacion de credenciales.
