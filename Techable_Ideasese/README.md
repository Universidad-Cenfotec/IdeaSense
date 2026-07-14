# 🤖 Construye sistemas inteligentes

Universidad Cenfotec. Este proyecto presenta una plataforma web interactiva desarrollada para conectar de forma inalámbrica modelos de Inteligencia Artificial visual con hardware físico.


---

# La Idea Central de la Plataforma Web: **Teachable IdeaSense**

La plataforma **Teachable IdeaSense** funciona como un **centro de control todo en uno**, diseñado para desarrollar proyectos de Inteligencia Artificial de forma sencilla e intuitiva.

En lugar de utilizar múltiples aplicaciones independientes, la plataforma integra en un solo lugar:

- 🤖 Entrenamiento de modelos de IA mediante **Google Teachable Machine**.
- 💻 Programación de la **IdeaBoard** e **IdeaSense**.
- 📷 Ejecución del modelo directamente desde el navegador.
- 📡 Comunicación inalámbrica mediante **Web Bluetooth**.

El flujo general del sistema es el siguiente:

1. **Entrenamiento del modelo**
   - Se crea un modelo de clasificación de imágenes utilizando Teachable Machine.

2. **Procesamiento en el navegador**
   - La plataforma abre la cámara web.
   - Carga el modelo de TensorFlow.js.
   - Ejecuta la clasificación en tiempo real.
   - Envía mediante Bluetooth la etiqueta detectada.

3. **Respuesta física**
   - La IdeaBoard recibe el texto enviado.
   - Una Máquina de Estados escrita en CircuitPython interpreta ese mensaje.
   - La IdeaSense muestra el patrón correspondiente en su matriz de LEDs 5x5.

> ⚠️ **Regla de oro:**  
> El nombre de cada clase del modelo de IA debe coincidir exactamente (incluyendo mayúsculas y minúsculas) con las condiciones definidas en el archivo `code.py`.

---

# Ejemplo práctico: Detector de Gestos con Pulgares

Actualmente la plataforma incluye un laboratorio completamente funcional para reconocer gestos con la mano.

## 🤖 1. El cerebro: Modelo de IA

El modelo fue entrenado para reconocer tres clases:

- `Feliz` 👍
- `Triste` 👎
- `Nada`

La clase **Nada** representa cualquier otra imagen distinta a las anteriores (mano abierta, puño, cámara vacía, etc.).

---

## 💡 2. El cuerpo: Programación de la placa

El programa en CircuitPython utiliza una **Máquina de Estados** con tres estados principales:

- `FELIZ`
- `TRISTE`
- `NADA`

Cada estado posee un patrón binario diferente que dibuja una imagen distinta en la matriz de LEDs de la IdeaSense.

---

## ⚙️ 3. Funcionamiento

Cuando el usuario muestra un pulgar hacia arriba:

1. El navegador detecta la clase **"Feliz"**.
2. Se envía el texto `"Feliz"` mediante Bluetooth.
3. La IdeaBoard cambia automáticamente al estado correspondiente.
4. La IdeaSense muestra una cara feliz.

Todo el proceso ocurre en tiempo real.

---

# 🏗️ Metodología Maker

Una de las ventajas de la plataforma es que no está limitada al detector de pulgares.

Con la misma arquitectura es posible desarrollar proyectos como:

- 📦 Clasificación de objetos
- ✋ Reconocimiento de lenguaje de señas
- 🎨 Detección de colores
- 🔐 Sistemas de acceso
- 🧸 Identificación de juguetes
- 📚 Clasificación de materiales educativos

---

# 1️⃣ Entrenar el modelo de IA (El cerebro)

1. Ingrese desde la plataforma al enlace de **Teachable Machine**.

2. Cree un nuevo:

```
Proyecto de Imagen
→ Modelo de Imagen Estándar
```

3. Cambie el nombre de las clases según su proyecto.

Ejemplo:

- ObjetoA
- ObjetoB
- Nada

> Es importante conservar exactamente esos nombres porque serán utilizados posteriormente en el código de la placa.

4. Capture aproximadamente **100 imágenes por clase** utilizando la webcam.

Se recomienda variar:

- Distancia
- Iluminación
- Fondo
- Ángulo

5. Presione **Entrenar Modelo**.

6. Pruebe el funcionamiento.

7. Finalmente seleccione:

```
Exportar Modelo
→ Upload
```

y copie la URL generada.

---

# 2️⃣ Programar la IdeaBoard (El cuerpo)

Ahora debe modificar el archivo `code.py`.

## Paso 1. Crear un nuevo patrón

```python
NUEVO_ICONO = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1]
]
```

---

## Paso 2. Crear el nuevo estado

```python
def estado_objeto_a():
    global mensaje

    mostrar(NUEVO_ICONO)

    if mensaje == "ObjetoB":
        return "ESTADO_B"

    if mensaje == "Nada":
        return "NADA"

    return "ESTADO_A"
```

---

## Paso 3. Registrar el estado

Dentro de la Máquina de Estados agregar:

```python
sm.add_state("ESTADO_A", estado_objeto_a)
```

Finalmente guardar el archivo.

La placa se reiniciará automáticamente.

---

# 3️⃣ Conectar todo

1. Encienda la IdeaBoard.

2. Abra la plataforma:

👉 **https://universidad-cenfotec.github.io/Libro-de-la-IA/teachable-ideasense/index.html**

3. Pegue la URL del modelo de Teachable Machine.

4. Active la cámara.

5. Presione **Conectar Bluetooth**.

6. Seleccione:

```
IdeaSense
```

7. Comience a probar su modelo mostrando objetos frente a la cámara.

---

# 🛠️ Materiales necesarios

| Cantidad | Componente | Función |
|----------|------------|----------|
| 1 | IdeaBoard | Placa principal con Bluetooth Low Energy (BLE). |
| 1 | IdeaSense | Módulo con matriz LED 5x5 y sensores. |
| 1 | Computadora con webcam | Ejecuta el modelo TensorFlow.js y envía los resultados por Bluetooth. |
| 1 | Cable USB | Alimentación y carga del programa CircuitPython. |

---

# 📂 Contenido del proyecto

```
Proyecto
│
├── README.md
│
├── codigos/
│   ├── index.html
│   ├── code.py
│   ├── statemachine.py
│   └── demás archivos del proyecto
│
└── Modelos/
    ├── Detector de Pulgares
    └── Otros modelos de ejemplo
```

---

# 📚 Tecnologías utilizadas

- IdeaBoard
- IdeaSense
- CircuitPython
- TensorFlow.js
- Google Teachable Machine
- Web Bluetooth API
- HTML5
- JavaScript

---

# 🚀 Resultado

Con esta plataforma es posible desarrollar sistemas inteligentes donde un modelo de Inteligencia Artificial ejecutado directamente desde el navegador interactúa de forma inalámbrica con hardware físico.

La combinación de **Teachable Machine**, **TensorFlow.js**, **Web Bluetooth**, **IdeaBoard** e **IdeaSense** permite construir proyectos educativos y prototipos funcionales de manera sencilla, visual y completamente interactiva.
