# 24 — EXECUTIVE SUMMARY

La arquitectura Azure Enterprise propuesta para el SGB de INCABIDE responde a los requisitos centrales de la RFP: Microsoft Azure como plataforma obligatoria, ejecucion de contenedores Docker, PostgreSQL 14+ con PostGIS y unaccent, almacenamiento de medios, dominio personalizado con TLS, seguridad reforzada, monitoreo, backups cifrados, DRP, WAF, DDoS, VPN, MFA, RBAC, auditoria y soporte operacional.

La arquitectura recomendada se organiza en capas: entrada segura, red segmentada, identidad, plataforma de contenedores, base de datos, almacenamiento, secretos, seguridad, observabilidad y continuidad. El diseno prioriza servicios gestionados cuando reducen carga operacional y mejoran seguridad, pero marca como `PENDIENTE DE VALIDACION` las decisiones que dependen de PADF/INCABIDE: region, tenant, ambientes, nivel de alta disponibilidad, RTO/RPO, WAF, DDoS, VPN, retencion y dimensionamiento.

El enfoque propuesto protege a INCABIDE porque evita exponer datos y servicios innecesariamente, centraliza identidad y auditoria, separa redes, usa acceso privado a datos, mantiene secretos fuera del codigo, incorpora monitoreo y alertas, y establece backups restaurables. Tambien prepara evidencias requeridas por la RFP para aprobacion de hitos.

Esta fase no implementa infraestructura ni define costos. Establece una arquitectura defendible y una matriz de decisiones para que la propuesta posterior pueda calcular, justificar y comprometer la solucion de forma responsable.
