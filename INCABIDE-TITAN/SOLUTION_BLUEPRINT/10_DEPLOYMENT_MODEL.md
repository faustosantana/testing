# 10 — DEPLOYMENT MODEL

## Objetivo

Definir el modelo de despliegue conceptual para llevar el SGB desde codigo fuente entregado "tal cual" hasta operacion productiva en Azure.

## Flujo de despliegue

```text
Recepcion codigo
  -> Diagnostico tecnico
  -> Ajustes cloud-ready
  -> Contenerizacion
  -> Despliegue QA/UAT
  -> Validacion funcional y seguridad
  -> Despliegue produccion
  -> Evidencias y aceptacion
```

## Ambientes conceptuales

| Ambiente | Proposito | Controles |
| --- | --- | --- |
| Desarrollo | Refactorizacion y pruebas internas. | Acceso restringido, logs, variables separadas. |
| QA/UAT | Validacion PADF/INCABIDE. | Datos controlados, evidencias, UAT. |
| Produccion | Operacion institucional. | TLS, WAF, backups, monitoreo, soporte. |

## Paquetes de despliegue

- imagen de aplicacion;
- configuracion por ambiente;
- scripts de inicializacion;
- migraciones de base de datos;
- configuracion de proxy;
- variables no sensibles;
- runbook de despliegue;
- plan de rollback.

## Health checks

Cada despliegue debe validar:

- aplicacion responde;
- base de datos disponible;
- almacenamiento accesible;
- autenticacion operativa;
- API responde;
- logs fluyen;
- backups configurados;
- certificado TLS activo en produccion.

## Rollback conceptual

1. Identificar version previa estable.
2. Congelar despliegue.
3. Preservar logs y evidencia.
4. Restaurar contenedor/version previa.
5. Validar migraciones reversibles o plan compensatorio.
6. Confirmar health checks.
7. Documentar incidente y acciones.

## Evidencias de despliegue

- capturas o registros de sistema;
- version desplegada;
- resultado de pruebas;
- estado de contenedores;
- estado de base de datos;
- certificado TLS;
- URL productiva;
- aprobacion de responsable.

## Restricciones

El modelo no define SKUs, cantidades de instancias ni topologia final. Eso pertenece a arquitectura Azure detallada posterior.
