# Proyecto 00 — Clasificación de calidad de limones con una CNN

Este proyecto recupera y profesionaliza el notebook académico original del repositorio. El objetivo es clasificar imágenes de limones en **tres categorías de calidad** mediante una red neuronal convolucional.

## 1. Dataset original

El notebook original cargó:

- **2.023 imágenes** para entrenamiento.
- **505 imágenes** para validación.
- **3 clases** de salida.
- Imágenes redimensionadas a **150 × 150 píxeles**.
- Lotes de **32 imágenes**.
- Separación de validación de **20 %**.

## 2. Aumento y preparación de datos

Se aplicaron las siguientes transformaciones durante el entrenamiento:

- normalización de píxeles a escala 0–1;
- rotación aleatoria de hasta 40°;
- desplazamiento horizontal y vertical;
- deformación por shear;
- zoom aleatorio;
- volteo horizontal;
- relleno de bordes mediante el píxel más cercano.

El aumento de datos busca reducir sobreajuste y mejorar la robustez frente a variaciones de posición, tamaño y orientación.

## 3. Arquitectura original

| Etapa | Configuración | Salida aproximada |
|---|---|---:|
| Convolución 1 | 64 filtros, 3 × 3, ReLU | 148 × 148 × 64 |
| Max pooling 1 | 2 × 2 | 74 × 74 × 64 |
| Convolución 2 | 64 filtros, 3 × 3, ReLU | 72 × 72 × 64 |
| Max pooling 2 | 2 × 2 | 36 × 36 × 64 |
| Convolución 3 | 128 filtros, 3 × 3, ReLU | 34 × 34 × 128 |
| Max pooling 3 | 2 × 2 | 17 × 17 × 128 |
| Convolución 4 | 256 filtros, 3 × 3, ReLU | 15 × 15 × 256 |
| Max pooling 4 | 2 × 2 | 7 × 7 × 256 |
| Flatten | Vectorización | 12.544 |
| Dense | 512 neuronas, ReLU | 512 |
| Dropout | 50 % | 512 |
| Salida | 3 neuronas, softmax | 3 clases |

**Parámetros totales:** 6.832.323.  
**Parámetros entrenables:** 6.832.323.

## 4. Configuración de entrenamiento

- Optimizador: `Adam`.
- Función de pérdida: `categorical_crossentropy`.
- Métrica principal: `accuracy`.
- Épocas originales: `5`.

## 5. Resultados originales

| Época | Loss entrenamiento | Accuracy entrenamiento | Loss validación | Accuracy validación |
|---:|---:|---:|---:|---:|
| 1 | 2,5310 | 0,7273 | 0,7090 | 0,8604 |
| 2 | 0,6084 | 0,8302 | 0,4878 | 0,8667 |
| 3 | 0,4629 | 0,8594 | 0,5914 | 0,7896 |
| 4 | 0,5016 | 0,8122 | 0,4878 | 0,8271 |
| 5 | 0,3836 | 0,8759 | 0,3507 | 0,8792 |

El mejor resultado observado fue una **accuracy de validación de 87,92 % en la quinta época**.

## 6. Gráficas recuperadas

El script `plot_original_history.py` reconstruye las dos curvas originales:

1. evolución de accuracy de entrenamiento y validación;
2. evolución de loss de entrenamiento y validación.

Las imágenes se guardan en:

```text
projects/00_clasificacion_limones/figures/
```

## 7. Interpretación profesional

El modelo aprende rápidamente, pero la validación cae en las épocas 3 y 4. Esto puede indicar:

- variabilidad causada por el aumento de datos;
- tamaño limitado del conjunto de validación;
- inicio de sobreajuste;
- tasa de aprendizaje mejorable;
- necesidad de usar `EarlyStopping` y guardar el mejor modelo.

La recuperación posterior en la época 5 muestra que cinco épocas no son suficientes para caracterizar de forma estable la convergencia.

## 8. Mejoras recomendadas

- separar aumento de datos de entrenamiento y validación;
- usar solo normalización en validación;
- agregar `EarlyStopping` y `ModelCheckpoint`;
- usar transferencia de aprendizaje con MobileNetV2 o EfficientNet;
- calcular matriz de confusión y métricas por clase;
- revisar balance de clases;
- documentar nombres exactos de las tres categorías;
- agregar predicciones sobre imágenes individuales;
- convertir el notebook en un pipeline reproducible.

## 9. Limitaciones

Los resultados provienen del notebook original. Las imágenes del dataset y el modelo entrenado no se encuentran versionados en el repositorio, por lo que todavía no se puede reproducir el entrenamiento completo sin recuperar el archivo `archive.zip` utilizado en Colab.
