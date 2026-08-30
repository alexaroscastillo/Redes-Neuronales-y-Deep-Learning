# Hoja de ruta del portafolio

## Fase 1 — Recuperación y orden

- Conservar el notebook académico original.
- Documentar el entorno de ejecución.
- Separar notebooks exploratorios de código reutilizable.
- Agregar control de versiones limpio y estructura estándar.

## Fase 2 — Proyecto industrial principal

### Predicción de fallas en equipos industriales

**Pregunta de negocio:** ¿qué activos presentan mayor riesgo de falla y con cuánta anticipación puede detectarse?

**Variables candidatas:**

- temperatura;
- vibración RMS y picos;
- corriente;
- tensión;
- potencia activa y reactiva;
- factor de potencia;
- velocidad;
- presión;
- horas de operación;
- mantenimientos previos;
- estado o modo operacional.

**Modelos:**

1. Regresión logística como línea base.
2. Random Forest o Gradient Boosting.
3. Red neuronal multicapa.
4. Autoencoder para anomalías, cuando no existan suficientes etiquetas.

**Métricas:**

- recall de fallas;
- precision;
- F1;
- PR-AUC;
- matriz de confusión;
- costo esperado de falsos negativos y falsos positivos.

**Entregables:**

- notebook de exploración;
- pipeline de entrenamiento;
- modelo versionado;
- reporte técnico;
- resumen ejecutivo;
- demostración mediante Streamlit o API.

## Fase 3 — Proyectos complementarios

1. Pronóstico de consumo energético industrial.
2. Detección de anomalías en transformadores o motores.
3. Predicción del índice energético de hornos.
4. Visión computacional para inspección de componentes.
5. Asistente RAG para normas y manuales de ingeniería.

## Fase 4 — Publicación profesional

- README individual por proyecto.
- Diagramas de arquitectura.
- Resultados cuantitativos verificables.
- Capturas o demostraciones.
- Licencia y referencias de datos.
- Perfil de GitHub y LinkedIn alineados con el portafolio.

## Criterio de terminado

Un proyecto solo se considera terminado cuando otra persona puede:

1. comprender el problema;
2. instalar el entorno;
3. ejecutar el código;
4. reproducir las métricas;
5. entender las limitaciones;
6. evaluar su utilidad industrial.
