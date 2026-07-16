# 11 — TESTING AND QA

## Estrategia de calidad

La estrategia de calidad de la propuesta se basa en trazabilidad, evidencia y aceptacion formal. La RFP establece que ningun hito se considera entregado ni habilitado para pago hasta contar con aprobacion escrita de PADF e INCABIDE, y que los modulos de Etapa II requieren pruebas funcionales, UAT y actas de aceptacion parcial. Por ello, la calidad debe gestionarse como un proceso continuo, no como una revision final.

## Niveles de prueba

La solucion debe considerar:

- pruebas unitarias sobre componentes criticos;
- pruebas de integracion entre aplicacion, base de datos, almacenamiento, API y servicios Azure;
- pruebas funcionales por flujo;
- pruebas de seguridad;
- pruebas de roles y permisos;
- pruebas de carga o rendimiento basicas segun alcance validado;
- pruebas de backup y restauracion;
- UAT con usuarios o responsables designados por INCABIDE;
- validacion de evidencias por hito.

## Criterio de no conformidad

Una funcionalidad no se considera aprobada solo porque no genera error, abre correctamente o pasa una prueba aislada. Para marcar `PASS`, debe ser usable, coherente, consistente con el resto del producto, clara, segura, respetar permisos, evitar duplicidad y no introducir deuda tecnica evidente.

Si existe una alternativa claramente mejor dentro del mismo alcance, debe implementarse o documentarse antes de aprobar el entregable.

## Ciclo de mejora continua

Despues de cada correccion se debe:

1. revalidar la pantalla o componente afectado;
2. revalidar el flujo completo;
3. revalidar el modulo;
4. buscar regresiones;
5. buscar oportunidades adicionales de mejora.

Si aparece un nuevo problema, se corrige y se reinicia el ciclo hasta estabilizar el area.

## Matriz requisito-prueba-evidencia

Cada requisito relevante debe conectarse con:

- caso de prueba;
- resultado esperado;
- evidencia;
- responsable;
- estado;
- aprobador.

Esta matriz permite demostrar que la propuesta no responde genericamente a la RFP, sino que construye un mecanismo verificable de cumplimiento.

## Evidencias QA

Las evidencias deben incluir reportes de prueba, capturas, logs, resultados de escaneo, actas UAT, registros de defectos, aprobaciones y checklist de cierre. Para seguridad, deben incluir CVSS, TLS, MFA, backup restaurable y declaracion de ausencia de credenciales en codigo.

## Trazabilidad RFP

Este capitulo cubre QA-001 a QA-029, SEC-027 a SEC-038, FUNC-GEN-007 a FUNC-GEN-009 y criterios de aceptacion de hitos y modulos.

## Informacion pendiente de Justech

Justech debe confirmar:

- metodologia QA real;
- herramientas de pruebas;
- equipo QA asignado;
- plantillas de actas;
- herramientas de seguimiento de defectos;
- evidencia de practicas de calidad si sera mencionada.
