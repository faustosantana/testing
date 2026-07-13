# CRITERIO DE NO CONFORMIDAD — INCABIDE TITAN

## Principio

No se debe marcar una funcionalidad, documento, flujo, pantalla, modulo o entregable como `PASS` solo porque:

- no produjo error;
- abrio correctamente;
- ejecuto una prueba aislada;
- compilo;
- respondio una vez;
- aparenta funcionar en un caso puntual.

El estandar del proyecto no es "funciona". El estandar es excelencia verificable.

## Criterio minimo para PASS

Una funcionalidad solo podra marcarse `PASS` cuando cumpla todos los criterios aplicables:

| Criterio | Pregunta de control |
| --- | --- |
| Usabilidad | ¿Un usuario real puede completarla sin confusion innecesaria? |
| Coherencia | ¿El flujo tiene sentido dentro del proceso institucional? |
| Consistencia | ¿Se comporta igual que patrones equivalentes del producto? |
| UX | ¿La experiencia es clara, ordenada, accesible y accionable? |
| Permisos | ¿Respeta roles, acciones permitidas y restricciones de acceso? |
| Multiempresa / multientidad | ¿Respeta separacion de contexto cuando aplique? |
| Calidad tecnica | ¿No introduce deuda tecnica evidente? |
| No duplicidad | ¿No duplica componentes, campos, reglas o flujos existentes? |
| Claridad | ¿No genera ambiguedad, ruido o interpretaciones incorrectas? |
| Evidencia | ¿Tiene evidencia suficiente para auditoria o aceptacion? |

## Resultado de QA

| Estado | Definicion |
| --- | --- |
| PASS | Cumple los criterios funcionales, tecnicos, UX, seguridad y evidencia aplicables. |
| PASS CON OBSERVACION | Cumple, pero existe mejora menor documentada que no afecta uso, seguridad, consistencia ni aceptacion. |
| FAIL | No cumple uno o mas criterios aplicables. |
| BLOCKED | No puede evaluarse por dependencia externa o informacion faltante. |

## Regla de alternativa superior

Si existe una alternativa claramente mejor dentro del mismo alcance, debe implementarse o documentarse como decision obligatoria antes de aprobar el entregable.

Una alternativa se considera claramente mejor si:

- reduce confusion del usuario;
- mejora seguridad o permisos;
- elimina duplicidad;
- reduce deuda tecnica;
- mejora consistencia del producto;
- facilita auditoria;
- mantiene el mismo alcance contractual.

## No conformidades automaticas

Debe marcarse `FAIL` si ocurre cualquiera de los siguientes casos:

- la funcionalidad opera, pero confunde al usuario;
- el flujo contradice otro modulo;
- permite acciones sin permiso;
- mezcla datos de contextos que deben permanecer separados;
- duplica una funcionalidad existente sin justificacion;
- requiere pasos manuales innecesarios cuando existe patron mejor;
- no deja evidencia suficiente;
- introduce deuda tecnica visible;
- no respeta patrones UX definidos en `UX_MASTER/`;
- no se puede explicar claramente al comite evaluador.

## Aplicacion

Este criterio aplica a:

- propuesta tecnica;
- demo futura;
- mockups futuros;
- arquitectura;
- UX/UI;
- documentos de entrega;
- modulos funcionales;
- pruebas UAT;
- paquetes de evidencia.

## Regla final

No conformarse con "funciona". Buscar excelencia, claridad, seguridad y consistencia institucional.
