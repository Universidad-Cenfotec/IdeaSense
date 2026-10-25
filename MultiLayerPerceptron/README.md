# Perceptrón Multicapa para CircuitPython con ulab

**Autoría:** Tomás de Camino Beck, Ph.D. — Universidad CENFOTEC

## Archivos

| Archivo | Para qué sirve |
| :--- | :--- |
| [`mlp.py`](mlp.py) | Librería `FastMLP`. Copiarla a la tarjeta como `/lib/mlp.py`. |
| [`xor_training.py`](xor_training.py) | Entrena la red con la función XOR en la tarjeta y guarda los pesos en `/xor.nn`. |
| [`xor_load.py`](xor_load.py) | Carga `/xor.nn` y muestra las predicciones, sin volver a entrenar. |
| [`Perceptron_Multicapa_4clases.ipynb`](Perceptron_Multicapa_4clases.ipynb) | Notebook de Google Colab: entrena un MLP `[18, 12, 4]` para 4 gestos del acelerómetro con NumPy y exporta los pesos en un formato que `FastMLP.load()` puede leer en la tarjeta. |

## Cómo ejecutar el ejemplo XOR

1. Abrir [IdeaCode](https://ideacode.crcibernetica.com/) y conectar la IdeaBoard.
2. Guardar `mlp.py` en la tarjeta como `/lib/mlp.py`.
3. Ejecutar `xor_training.py`: imprime las épocas y al final las predicciones (valores cercanos a 0, 1, 1, 0).
4. Ejecutar `xor_load.py` para comprobar que la red guardada se recupera.

> ℹ️ `save()` escribe un archivo en la tarjeta. Si aparece `OSError: [Errno 30] Read-only filesystem`, la memoria no está habilitada para escritura desde el programa; consulte la documentación de CircuitPython sobre `storage.remount()` en `boot.py`. También se puede entrenar en el notebook de Colab y copiar el archivo de pesos a la tarjeta con IdeaCode.

---

Este proyecto implementa un perceptrón multicapa sencillo para ejecutarse en una placa ESP32 con CircuitPython. Está pensado para proyectos educativos donde se desea comprender cómo funciona una red neuronal desde sus componentes básicos, pero aprovechando `ulab` para acelerar algunas operaciones numéricas.

## Objetivo

El objetivo de esta librería es permitir crear, entrenar, guardar y cargar una red neuronal pequeña directamente en un microcontrolador.

La librería puede utilizarse para proyectos como:

- Clasificación de gestos usando un acelerómetro
- Reconocimiento de patrones simples
- Experimentos educativos de aprendizaje automático
- Demostraciones de redes neuronales en sistemas embebidos

## Requisitos

La placa debe tener CircuitPython instalado con soporte para `ulab`.

El código utiliza:

```python
from ulab import numpy as np
import math
import random
````

## Clase principal

La clase principal es:

```python
FastMLP
```

Esta clase representa una red neuronal multicapa completamente conectada.

## Crear una red

Para crear una red se indica la arquitectura como una lista.

```python
from mlp import FastMLP

net = FastMLP([30, 16, 4], learning_rate=0.05)
```

Esta arquitectura significa:

```text
30 entradas
16 neuronas ocultas
4 salidas
```

En un proyecto de reconocimiento de gestos, las 30 entradas podrían corresponder a 10 lecturas del acelerómetro, cada una con tres valores:

```text
ax, ay, az
```

## Inicialización

Cuando se crea la red, se generan automáticamente los pesos y sesgos.

```python
self.weights = []
self.biases = []
```

Los pesos se inicializan con valores aleatorios entre -1 y 1.

```python
random.uniform(-1.0, 1.0)
```

Cada conexión entre capas tiene una matriz de pesos, y cada capa de salida tiene un vector de sesgos.

## Función de activación

La red utiliza la función sigmoide.

```python
def sigmoid(self, x):
```

La sigmoide convierte cada valor de entrada en un número entre 0 y 1.

```text
0 significa baja activación
1 significa alta activación
```

Para evitar errores numéricos, el código limita valores muy grandes o muy pequeños.

```python
if v > 20:
    result[i] = 1.0

elif v < -20:
    result[i] = 0.0
```

## Derivada de la sigmoide

Durante el entrenamiento se necesita calcular cuánto debe cambiar cada peso. Para eso se usa la derivada de la sigmoide.

```python
def dsigmoid(self, y):
    result[i] = y[i] * (1.0 - y[i])
```

Esta derivada se usa durante backpropagation.

## Propagación hacia adelante

La función `forward()` pasa los datos por toda la red.

```python
def forward(self, x):
```

Primero recibe un vector de entrada.

Luego, para cada capa, calcula:

```python
z = np.dot(W, a) + b
```

Esto significa:

```text
entrada × pesos + sesgo
```

Después aplica la función sigmoide:

```python
a = self.sigmoid(z)
```

La función devuelve una lista con todas las activaciones de la red. Esto es necesario para poder entrenar después con backpropagation.

## Predicción

La función `predict()` permite obtener la salida de la red.

```python
def predict(self, inputs):
```

Ejemplo:

```python
salida = net.predict([0.1, 0.4, 0.8])
```

En una red de cuatro salidas, el resultado puede verse así:

```text
[0.02, 0.91, 0.10, 0.05]
```

La salida más alta representa la clase predicha.

## Entrenamiento

La función principal de aprendizaje es:

```python
def train(self, inputs, targets):
```

Recibe dos valores:

```python
inputs
```

que son las entradas de la red, y:

```python
targets
```

que son las salidas esperadas.

Por ejemplo, para clasificar cuatro gestos:

```python
LEFT  = [1, 0, 0, 0]
RIGHT = [0, 1, 0, 0]
UP    = [0, 0, 1, 0]
DOWN  = [0, 0, 0, 1]
```

Si una muestra corresponde al gesto `LEFT`, se entrena así:

```python
net.train(vector_gesto, LEFT)
```

## Error de salida

Durante el entrenamiento se calcula la diferencia entre la salida esperada y la salida producida por la red.

```python
error = y - output
```

Luego se calcula el delta de salida.

```python
delta_out[i] = error[i] * output[i] * (1.0 - output[i])
```

Este valor indica cuánto debe corregirse cada neurona de salida.

## Backpropagation

Después de calcular el error de salida, el código propaga ese error hacia atrás.

```python
for layer in range(len(self.weights) - 2, -1, -1):
```

Esto permite ajustar también los pesos de las capas ocultas.

La propagación se hace manualmente, sin usar `np.transpose()`, porque algunas versiones de `ulab` en CircuitPython no incluyen esa función.

## Actualización de pesos

Una vez calculados los deltas, la red actualiza sus pesos.

```python
self.weights[layer][neuron][k] += (
    self.learning_rate
    * delta[neuron]
    * a_prev[k]
)
```

El parámetro `learning_rate` controla qué tan grandes son los cambios en cada entrenamiento.

Un valor alto aprende más rápido, pero puede ser inestable.

Un valor bajo aprende más lento, pero puede ser más estable.

## Seleccionar la clase ganadora

La función `argmax()` devuelve la posición del valor más alto en un vector.

```python
def argmax(self, vector):
```

Ejemplo:

```python
salida = net.predict(vector_gesto)
clase = net.argmax(salida)
```

Si la salida fue:

```text
[0.1, 0.8, 0.2, 0.05]
```

entonces:

```text
clase = 1
```

## Guardar la red entrenada

La función `save()` permite guardar los pesos y sesgos en un archivo local del ESP32.

```python
net.save("/modelo.txt")
```

Esto permite conservar una red ya entrenada aunque la placa se reinicie.

El archivo guarda:

* cantidad de matrices de pesos
* matrices de pesos
* sesgos

## Cargar una red entrenada

Para cargar una red guardada:

```python
net.load("/modelo.txt")
```

Esto reemplaza los pesos y sesgos actuales por los valores almacenados en el archivo.

Uso típico:

```python
net = FastMLP([30, 16, 4])
net.load("/modelo.txt")
```

## Ejemplo mínimo

```python
from mlp import FastMLP

net = FastMLP([2, 4, 1], learning_rate=0.3)

datos = [
    ([0, 0], [0]),
    ([0, 1], [1]),
    ([1, 0], [1]),
    ([1, 1], [0])
]

for epoch in range(5000):
    for x, y in datos:
        net.train(x, y)

print(net.predict([0, 0]))
print(net.predict([0, 1]))
print(net.predict([1, 0]))
print(net.predict([1, 1]))
```

## Ejemplo para gestos

Una red para gestos con acelerómetro podría definirse así:

```python
net = FastMLP([30, 16, 4], learning_rate=0.05)
```

Cada gesto puede representarse con una ventana de 10 muestras:

```text
ax1, ay1, az1,
ax2, ay2, az2,
...
ax10, ay10, az10
```

Eso produce 30 entradas.

Las salidas pueden representar:

```text
0 = izquierda
1 = derecha
2 = arriba
3 = abajo
```

## Limitaciones

Esta implementación está diseñada para redes pequeñas.

No incluye:

* optimizadores avanzados
* softmax
* regularización
* batches
* normalización automática
* manejo seguro de archivos corruptos

Es una implementación educativa, suficientemente simple para entender cómo una red neuronal aprende, pero funcional para experimentos pequeños en un ESP32.

## Recomendación

Para reconocimiento de gestos, es importante normalizar los datos del acelerómetro antes de entrenar.

Por ejemplo:

```python
ax = ax / 20.0
ay = ay / 20.0
az = az / 20.0
```

```

