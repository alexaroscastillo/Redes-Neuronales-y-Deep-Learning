# Proyecto 01 — Predicción de fallas en equipos industriales

## 1. Contexto

Las fallas inesperadas generan pérdidas de producción, costos de mantenimiento correctivo y riesgos operacionales. Este proyecto construirá un modelo que priorice activos según su probabilidad de falla.

## 2. Objetivo técnico

Desarrollar y comparar modelos de clasificación capaces de identificar equipos con riesgo elevado de falla.

## 3. Objetivo operacional

Reducir fallas no planificadas sin saturar al equipo de mantenimiento con falsas alarmas.

## 4. Criterios de éxito iniciales

- superar el modelo ingenuo y la regresión logística base;
- maximizar recall sin deteriorar de manera inaceptable la precision;
- reportar PR-AUC cuando exista desbalance de clases;
- traducir errores del modelo a impacto operacional;
- evitar fuga temporal o de información.

## 5. Flujo de trabajo

1. Definición del activo y horizonte de predicción.
2. Revisión de calidad y trazabilidad de datos.
3. Análisis exploratorio.
4. División temporal o estratificada, según corresponda.
5. Modelo base.
6. Modelos de árbol.
7. Red neuronal.
8. Calibración y selección de umbral.
9. Interpretabilidad.
10. Evaluación económica.
11. Demostración y documentación.

## 6. Datos

El repositorio no debe almacenar información industrial confidencial. Se trabajará inicialmente con datos públicos o sintéticos y luego se documentará cómo adaptar el pipeline a datos reales.

## 7. Riesgos técnicos

- pocas fallas etiquetadas;
- clases altamente desbalanceadas;
- sensores con ruido o interrupciones;
- cambios en los modos de operación;
- variables registradas después de ocurrida la falla;
- métricas altas que no generan valor operacional.

## 8. Próximo entregable

Crear un dataset sintético reproducible, entrenar una línea base y generar el primer reporte de métricas.
