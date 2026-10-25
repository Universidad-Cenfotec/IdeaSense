# Ejemplos con IdeaAI

Clasificadores de gestos creados con **[IdeaAI](https://ideaai.crcibernetica.com/)**, la plataforma web de CRCibernética para grabar datos del acelerómetro y el giroscopio de la IdeaSense, entrenar una red neuronal en el navegador y exportarla como `code.py`.

Los modelos exportados no necesitan librerías de aprendizaje automático: los pesos de la red quedan escritos como listas de Python y la predicción se hace con sumas y multiplicaciones (`extract_features()`, `dense()`, `predict()`).

| Ejemplo | Qué hace | Clases |
| :--- | :--- | :--- |
| [`MotionSense.py`](MotionSense.py) | Distingue si la tarjeta está quieta o en movimiento y muestra una carita en la matriz. | `Calma`, `Movimiento` |
| [`Morse_Classifier/`](Morse_Classifier/) | Traductor de código Morse: cada gesto se clasifica como punto o raya y se arman letras y palabras. | `Golpe-Punto`, `Nada-Raya` |

## Flujo de trabajo

1. **Grabar** ejemplos de cada gesto en IdeaAI con la tarjeta conectada por USB.
2. **Entrenar** el modelo y probarlo en vivo en la misma página.
3. **Exportar** el `code.py` generado y abrirlo en [IdeaCode](https://ideacode.crcibernetica.com/).
4. **Ejecutar** en la tarjeta: el programa toma ventanas de 25 lecturas del IMU, calcula características y predice la clase.

## Cómo funciona el modelo exportado

```text
25 lecturas × 6 ejes (ax, ay, az, gx, gy, gz)
        │
        ▼
extract_features(): por eje → media, desviación, mínimo, máximo, cruces por cero  (30 valores)
        │  normalización con NORM_MEAN y NORM_STD
        ▼
dense(W1, B1, ReLU) → dense(W2, B2) → clase con el valor más alto
```

Para entrenar una red **dentro** de la tarjeta en lugar de en el navegador, ver [`MultiLayerPerceptron`](../MultiLayerPerceptron/).
