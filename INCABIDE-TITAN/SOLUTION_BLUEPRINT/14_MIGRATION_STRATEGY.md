# 14 — MIGRATION STRATEGY

## Objetivo

Definir una estrategia conceptual para datos, archivos, configuracion y adopcion del SGB, sin asumir que existe migracion historica hasta que PADF/INCABIDE lo confirme.

## Tipos de migracion posibles

| Tipo | Descripcion | Estado |
| --- | --- | --- |
| Codigo fuente | Recepcion y adaptacion del codigo SGB existente. | Obligatorio |
| Configuracion | Variables, secretos, dominios, certificados y parametros. | Obligatorio |
| Base de datos | Migracion o inicializacion de datos existentes. | Pendiente de confirmar |
| Multimedia | Migracion de documentos, imagenes, videos u otros archivos. | Pendiente de confirmar |
| Catalogos | Provincias, municipios, entidades remitentes, categorias. | Pendiente de confirmar |
| Usuarios | Cuentas, roles y permisos. | Pendiente de confirmar |

## Estrategia para codigo

1. Recibir codigo bajo NDA.
2. Inventariar estructura, dependencias y configuracion.
3. Identificar incompatibilidades cloud.
4. Refactorizar configuraciones sensibles.
5. Contenerizar.
6. Validar ejecucion.
7. Registrar hallazgos y acciones.

## Estrategia para datos

Si existe migracion de datos:

1. Inventario de fuentes.
2. Perfilamiento de calidad.
3. Mapeo a modelo SGB.
4. Reglas de limpieza.
5. Carga de prueba.
6. Validacion de negocio.
7. Carga controlada.
8. Reconciliacion.
9. Evidencia de aprobacion.

## Estrategia para archivos

- inventariar origen;
- validar tipos permitidos;
- calcular volumen;
- definir metadata;
- aplicar controles de confidencialidad;
- cargar a almacenamiento seguro;
- relacionar con registros;
- auditar accesos.

## Migracion de catalogos

Catalogos clave:

- provincias;
- ciudades;
- municipios;
- entidades remitentes;
- tipos de activo;
- categorias;
- subcategorias;
- estados;
- roles;
- permisos.

## Riesgos de migracion

- datos incompletos;
- duplicados;
- inconsistencias de formato;
- archivos corruptos;
- ausencia de catalogos oficiales;
- volumen no dimensionado;
- reglas legales no definidas;
- usuarios sin responsables de validacion.

## Preguntas pendientes

- ¿Existe base productiva actual?
- ¿Que volumen historico debe migrarse?
- ¿Quien depura datos?
- ¿Que catalogos oficiales se entregaran?
- ¿Se requiere migracion completa o carga inicial?
- ¿Que ventana de migracion sera aceptable?
