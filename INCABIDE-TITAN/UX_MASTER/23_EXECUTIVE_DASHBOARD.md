# 23 — EXECUTIVE DASHBOARD

## Objetivo

Dashboard ejecutivo de nivel ministerial para que un Director de INCABIDE entienda la situacion institucional en menos de 30 segundos.

## Preguntas que responde

- ¿Cuantos bienes existen?
- ¿Cual es el valor economico estimado?
- ¿Donde estan los bienes?
- ¿En que estado se encuentran?
- ¿Que alertas requieren accion?
- ¿Cuales son las proximas subastas?
- ¿Que procesos son criticos?
- ¿Como evolucionan los KPIs?

## Layout recomendado

```text
Top: Estado general + fecha de corte + filtros globales
Row 1: Total bienes | Valor economico | Alertas criticas | Procesos pendientes
Row 2: Mapa RD | Bienes por estado
Row 3: Proximas subastas | Procesos criticos
Row 4: Tendencias | Acciones ejecutivas
```

## KPIs principales

| KPI | Visual |
| --- | --- |
| Total de bienes | Card hero. |
| Valor economico | Card hero con tendencia. |
| Bienes por provincia | Mapa + ranking. |
| Bienes por estado | Dona/barra. |
| Alertas criticas | Lista priorizada. |
| Proximas subastas | Agenda compacta. |
| Procesos criticos | Tabla de decision. |
| Cumplimiento operativo | Semaforo. |

## Alertas ejecutivas

| Alerta | Accion |
| --- | --- |
| Bienes sin documentacion obligatoria | Abrir lista filtrada. |
| Contratos por vencer | Abrir contratos criticos. |
| Subasta proxima sin conciliacion | Abrir proceso. |
| Acceso sospechoso | Abrir auditoria. |
| Provincia con acumulacion critica | Abrir mapa filtrado. |

## EXECUTIVE EXPERIENCE

Un Director de INCABIDE debe sentir que el sistema:

1. le da control institucional inmediato;
2. no lo obliga a navegar diez pantallas para entender riesgos;
3. muestra alertas con prioridad real;
4. conecta cada numero con evidencia;
5. permite pasar de vision nacional a expediente especifico;
6. comunica confianza, modernidad y orden;
7. respeta el nivel ejecutivo: menos ruido, mas decision;
8. permite responder ante PADF, autoridades o auditoria con datos.

## Comportamiento ideal

En 30 segundos:

- ve si la operacion esta saludable;
- identifica provincias o procesos con riesgo;
- entiende valor y volumen de bienes;
- abre la alerta mas importante;
- delega o solicita accion.

## Permisos

Perfil ejecutivo con lectura amplia, exportaciones controladas y sin acciones destructivas directas.
