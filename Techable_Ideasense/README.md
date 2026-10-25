# 🤖 Construye sistemas inteligentes: Teachable IdeaSense

**Universidad CENFOTEC** · Fiorella Pérez y Tomás de Camino Beck, Ph.D.

 Este proyecto presenta una plataforma web interactiva desarrollada para conectar de forma inalámbrica modelos de Inteligencia Artificial visual con hardware físico.

---

## 💡 La Idea Central de la Plataforma Web

La plataforma **Teachable IdeaSense** funciona como un **centro de control todo en uno**, diseñado para desarrollar proyectos de Inteligencia Artificial de forma sencilla e intuitiva.

En lugar de utilizar múltiples aplicaciones independientes, la plataforma integra en un solo lugar:

*   🤖 **Entrenamiento de modelos de IA** mediante Google Teachable Machine.
*   💻 **Programación** de la IdeaBoard e IdeaSense.
*   📷 **Ejecución del modelo** directamente desde el navegador.
*   📡 **Comunicación inalámbrica** mediante Web Bluetooth.

### Flujo general del sistema

1. **Entrenamiento del modelo:** Se crea un modelo de clasificación de imágenes utilizando Teachable Machine.
2. **Procesamiento en el navegador:**
   * La plataforma abre la cámara web.
   * Carga el modelo de TensorFlow.js.
   * Ejecuta la clasificación en tiempo real.
   * Envía mediante Bluetooth la etiqueta detectada.
3. **Respuesta física:**
   * La IdeaBoard recibe el texto enviado.
   * Una Máquina de Estados escrita en CircuitPython interpreta ese mensaje.
   * La IdeaSense muestra el patrón correspondiente en su matriz de LEDs 5x5.

> ⚠️ **Regla de oro:**
> El nombre de cada clase del modelo de IA debe coincidir exactamente (incluyendo mayúsculas y minúsculas) con las condiciones definidas en el archivo `code.py`.

---

## 🛠️ Ejemplos de Implementación

### Ejemplo 01: Detector de Gestos con Pulgares
Este ejemplo demuestra cómo conectar un modelo de IA visual con un dispositivo físico. El sistema reconoce gestos realizados con la mano mediante una cámara y genera una respuesta visual utilizando la matriz LED.

*   **Clase Feliz (👍):** El usuario realiza un gesto con el pulgar hacia arriba. El modelo envía la etiqueta `Feliz`.
*   **Clase Triste (👎):** El usuario realiza un gesto con el pulgar hacia abajo. El modelo envía la etiqueta `Triste`.
*   **Clase Nada:** Cualquier imagen diferente a los gestos entrenados (mano abierta, cámara vacía, etc.). El modelo envía la etiqueta `Nada`.

**Programación de la placa (CircuitPython):**
```python
FELIZ = [
    [0,1,0,1,0],
    [0,1,0,1,0],
    [1,0,0,0,1],
    [0,1,1,1,0],
    [0,0,0,0,0]
]

def estado_feliz():
    global mensaje
    mostrar(FELIZ)

    if mensaje == "Triste":
        return "TRISTE"
    if mensaje == "Nada":
        return "NADA"

    return "FELIZ"
```

### Ejemplo 02: Clasificador de Números
El objetivo es que el usuario pueda mostrar un número frente a la cámara y que la placa responda mostrando el número detectado en su matriz LED.

*   **Clases del modelo:** `Uno`, `Dos`, `Tres` y `Nulo` (categoría de seguridad para cuando no hay un número claro).
*   **Estados en CircuitPython:** `UNO`, `DOS`, `TRES`, `NULO`.

**Ejemplo de patrón LED:**
```python
UNO = [
    [0,0,1,0,0],
    [0,1,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0]
]
```

### Ejemplo 03: Detector de Objeto con Confirmación Visual
Enfocado en la detección de un objeto específico (por ejemplo, un carrito) y su confirmación visual utilizando símbolos.

*   **Clases del modelo:** `Carrito` y `Nulo`.
*   **Estados de la Máquina:** `CHECK` (✔ Objeto detectado) y `NULO` (✖ Objeto no detectado).

**Patrones LED utilizados:**
```python
CHECK = [
    [0,0,0,0,1],
    [0,0,0,1,0],
    [1,0,1,0,0],
    [0,1,0,0,0],
    [0,0,0,0,0]
]

X = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1]
]
```

---

## 🧠 1. Entrenar el modelo de IA (El cerebro)

Todos los ejemplos siguen el mismo proceso de entrenamiento utilizando **Google Teachable Machine**.

1. **Crear el proyecto:** Ingresa a Google Teachable Machine y selecciona `Proyecto de Imagen` → `Modelo de Imagen Estándar`.
2. **Crear las clases:** Define las clases asegurándote de que coincidan exactamente con tu código en CircuitPython.
3. **Capturar imágenes:** Se recomiendan aproximadamente **100 imágenes por clase**, variando distancia, posición, iluminación y fondo.
4. **Entrenar el modelo:** Presiona `Entrenar Modelo`.
5. **Probar el modelo:** Verifica que las predicciones sean correctas frente a la cámara.
6. **Exportar:** Selecciona `Exportar Modelo` → `Upload` y copia la URL generada. Esta se utilizará en la plataforma Teachable IdeaSense.

---

## 💻 2. Programar la IdeaBoard (El cuerpo)

El programa desarrollado en CircuitPython recibe mensajes mediante Bluetooth (BLE), interpreta la etiqueta mediante una Máquina de Estados y muestra una respuesta en la matriz LED de la IdeaSense (5x5).

*   `1` = LED encendido.
*   `0` = LED apagado.

**Antes de ejecutar:**

1. Abrir [IdeaCode](https://ideacode.crcibernetica.com/) y conectar la IdeaBoard.
2. Copiar [`lib/statemachine.py`](../lib/statemachine.py) a la tarjeta como `/lib/statemachine.py`.
3. Pegar el código del ejemplo y guardarlo como `code.py`. La tarjeta se anuncia por Bluetooth con el nombre **IdeaSense**.

> Si Chrome no encuentra el dispositivo, verifique que el `boot.py` de la tarjeta contenga `supervisor.runtime.ble_workflow = False` (así viene de fábrica en la IdeaBoard) y que ningún otro programa esté conectado a ella.

---

## 🔌 3. Conectar Todo

1. **Encender la IdeaBoard:** Conecta la placa mediante USB (debe tener el código CircuitPython cargado).
2. **Abrir la plataforma:** Ingresa a [Teachable IdeaSense](https://universidad-cenfotec.github.io/Libro-de-la-IA/teachable-ideasense/index.html).
3. **Cargar el modelo de IA:** Pega la URL generada por Teachable Machine.
4. **Activar la cámara:** Concede permisos a la plataforma en tu navegador.
5. **Conectar Bluetooth:** Presiona `Conectar Bluetooth` y selecciona tu dispositivo **IdeaSense**.
6. **Realizar pruebas:** Muestra los objetos o gestos frente a la cámara y observa la reacción de la placa.

---

## 🛠️ Materiales Necesarios

| Cantidad | Componente | Función |
| :---: | :--- | :--- |
| **1** | IdeaBoard | Placa principal con conectividad Bluetooth Low Energy (BLE). |
| **1** | IdeaSense | Módulo de expansión con matriz LED 5x5 y sensores. |
| **1** | Computadora | Ejecuta TensorFlow.js, cámara web y procesa el modelo de IA. |
| **1** | Cable USB | Alimentación eléctrica y carga del programa CircuitPython. |

---

## 📂 Contenido del Proyecto

```text
Techable_Ideasense
│
├── README.md
├── codigos
│   ├── index.html        ← versión local de la plataforma Teachable IdeaSense
│   ├── Ejemplo01.py      ← pulgares: Feliz / Triste / Nada
│   ├── Ejemplo02.py      ← números: Uno / Dos / Tres / Nulo
│   └── Ejemplo03.py      ← detector de objeto: Carrito / Nulo
├── modelos
│   └── modelos.md        ← enlaces a los modelos de Teachable Machine
└── SumoIA                ← Sumobot controlado por IA (ver su README)
```

| Ejemplo | Código | Modelo de Teachable Machine | Clases |
| :--- | :--- | :--- | :--- |
| 01 · Pulgares | [`Ejemplo01.py`](codigos/Ejemplo01.py) | [8PFBVe19l](https://teachablemachine.withgoogle.com/models/8PFBVe19l/) | `Feliz`, `Triste`, `Nada` |
| 02 · Números | [`Ejemplo02.py`](codigos/Ejemplo02.py) | [DxmCUv-np](https://teachablemachine.withgoogle.com/models/DxmCUv-np/) | `Uno`, `Dos`, `Tres`, `Nulo` |
| 03 · Objeto | [`Ejemplo03.py`](codigos/Ejemplo03.py) | [iIaAJedxa](https://teachablemachine.withgoogle.com/models/iIaAJedxa/) | `Carrito`, `Nulo` |

> Los tres programas usan la máquina de estados [`lib/statemachine.py`](../lib/statemachine.py). Cópiela a la tarjeta como `/lib/statemachine.py` antes de ejecutarlos.

> Si el modelo de ejemplo no reconoce bien sus objetos, entrene uno propio con las **mismas clases** y pegue su URL en la plataforma.

---

## 📚 Tecnologías Utilizadas

*   🤖 IdeaBoard & IdeaSense (Hardware)
*   🐍 CircuitPython
*   🧠 TensorFlow.js
*   🤖 Google Teachable Machine
*   📡 Web Bluetooth API
*   🌐 HTML5 & JavaScript

---

## 🚀 Resultado Final

La plataforma **Teachable IdeaSense** permite crear sistemas inteligentes donde un modelo de Inteligencia Artificial ejecutado directamente desde el navegador se comunica con hardware físico de forma inalámbrica. Es ideal para construir proyectos educativos y prototipos funcionales de manera sencilla, visual e intuitiva.
