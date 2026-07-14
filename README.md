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

## Estructura

```text
.
├── legacy/                         # Trabajo académico original
├── notebooks/                      # Análisis y experimentos reproducibles
├── src/                            # Código reutilizable
├── data/                           # Instrucciones de datos; no almacenar datos sensibles
├── models/                         # Modelos exportados; normalmente fuera de Git
├── reports/                        # Resultados, gráficos y memorias técnicas
├── docs/                           # Documentación y hoja de ruta
├── tests/                          # Pruebas automatizadas
├── requirements.txt
└── README.md
```

## Proyecto inicial

### Predicción de fallas en equipos industriales

**Problema:** estimar la probabilidad de falla de un activo usando variables operacionales como temperatura, vibración, corriente, potencia y horas de servicio.

**Resultado esperado:**

- pipeline reproducible de preparación de datos;
- modelo base y red neuronal;
- métricas técnicas y de negocio;
- interpretación de variables;
- reporte ejecutivo orientado a mantenimiento;
- API o aplicación demostrativa.

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

Portafolio en reconstrucción. La primera fase ordena el repositorio, conserva el notebook original y prepara un proyecto industrial demostrable.

## Autor

**Alex Aros Castillo**  
Ingeniería eléctrica · Inteligencia artificial aplicada · Energía · Mantenimiento predictivo
