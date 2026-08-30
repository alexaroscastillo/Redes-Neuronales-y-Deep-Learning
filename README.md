# Portafolio Profesional de Inteligencia Artificial Aplicada a Ingeniería

Portafolio técnico de **Alex Aros**, Ingeniero Eléctrico, orientado a machine learning, deep learning, mantenimiento predictivo, energía y aplicaciones industriales.

## Objetivo

Transformar ejercicios académicos en proyectos reproducibles, documentados y conectados con problemas reales de ingeniería.

## Líneas de trabajo

1. Fundamentos de redes neuronales.
2. Machine learning para datos industriales.
3. Series temporales y pronóstico energético.
4. Detección de anomalías y mantenimiento predictivo.
5. Visión computacional para inspección industrial.
6. IA generativa y asistentes para ingeniería.

## Proyectos del portafolio

### Proyecto 00 — Clasificación de calidad de limones

Recuperación profesional del proyecto académico original mediante una CNN para clasificación de imágenes en tres clases.

Incluye:

- explicación del dataset y aumento de datos;
- arquitectura completa de la red;
- tabla de resultados por época;
- gráficas visibles de accuracy y loss;
- análisis técnico de convergencia y sobreajuste;
- plan de modernización con transferencia de aprendizaje.

[Ver Proyecto 00 — Clasificación de limones](projects/00_clasificacion_limones/README.md)

### Proyecto 01 — Predicción de fallas en equipos industriales

**Problema:** estimar la probabilidad de falla de un activo usando variables operacionales como temperatura, vibración, corriente, potencia y horas de servicio.

**Resultado esperado:**

- pipeline reproducible de preparación de datos;
- modelo base y red neuronal;
- métricas técnicas y de negocio;
- interpretación de variables;
- reporte ejecutivo orientado a mantenimiento;
- API o aplicación demostrativa.

[Ver Proyecto 01 — Predicción de fallas](projects/01_prediccion_fallas/README.md)

## Estructura

```text
.
├── projects/                        # Proyectos completos del portafolio
├── notebooks/                       # Análisis y experimentos reproducibles
├── src/                             # Código reutilizable
├── data/                            # Instrucciones de datos; no almacenar datos sensibles
├── models/                          # Modelos exportados; normalmente fuera de Git
├── reports/                         # Resultados, gráficos y memorias técnicas
├── docs/                            # Documentación y hoja de ruta
├── tests/                           # Pruebas automatizadas
├── requirements.txt
└── README.md
```

## Metodología profesional

Cada proyecto incluirá:

- definición del problema y criterio de éxito;
- análisis exploratorio;
- separación correcta de entrenamiento, validación y prueba;
- modelo base antes de usar deep learning;
- control de fuga de información;
- métricas apropiadas al riesgo operacional;
- reproducibilidad mediante semillas y dependencias;
- conclusiones, limitaciones y próximos pasos.

## Ejecución local

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

En Linux o macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Estado

Portafolio en reconstrucción. Ya se recuperó y documentó el proyecto original de visión computacional, y se está desarrollando el primer proyecto industrial de mantenimiento predictivo.

## Autor

**Alex Aros Castillo**  
Ingeniería eléctrica · Inteligencia artificial aplicada · Energía · Mantenimiento predictivo
