# 🤖 SumoIA - Control Inteligente de un Sumobot

Este ejemplo muestra cómo integrar un **Sumobot** con **Google Teachable Machine**, **Bluetooth Low Energy (BLE)** y **CircuitPython** para controlar el robot mediante un modelo de Inteligencia Artificial.

A partir de un modelo entrenado, el navegador reconoce una acción, envía el nombre de la clase por Bluetooth y el robot ejecuta el movimiento correspondiente.

---

# 📂 Contenido

```text
SumoIA
│
├── README.md
├── 01_control_basico_ble.py
├── 02_sumobot_pdi_estados.py
└── 03_sumobot_ideasense.py
```

### 🟢 01 - Control básico BLE
Versión inicial del proyecto.

- Comunicación mediante Bluetooth Low Energy.
- Control directo de los motores.
- Comandos:
  - `STOP`
  - `AVANZAR`
  - `DERECHA`
  - `IZQUIERDA`

Ideal para comprender cómo controlar el robot desde una aplicación externa.

---

### 🟡 02 - Máquina de Estados + PDI

Agrega una arquitectura más robusta utilizando una **Máquina de Estados** y un controlador **PDI**.

El PDI utiliza el giroscopio para corregir pequeñas desviaciones durante el avance, permitiendo que el robot mantenga una trayectoria mucho más estable.

Estados principales:

- CALIBRANDO
- DESCONECTADO
- STOP
- AVANZAR
- DERECHA
- IZQUIERDA

---

### 🔵 03 - IdeaSense

Extiende el ejemplo anterior incorporando la placa **IdeaSense**.

Mientras el robot se mueve, la matriz LED 5×5 muestra el estado actual mediante símbolos sencillos:

- ✖ STOP
- ↑ AVANZAR
- → DERECHA
- ← IZQUIERDA

Esto proporciona retroalimentación visual del comportamiento del robot.

---

## 🤖 Integración con Google Teachable Machine

Este ejemplo fue diseñado para utilizarse junto con la plataforma **Teachable IdeaSense**, la cual ejecuta un modelo de **Google Teachable Machine** directamente desde el navegador y envía la clase detectada al Sumobot mediante Bluetooth Low Energy (BLE).

### 🌐 Plataforma web

Utiliza la siguiente aplicación para cargar el modelo y controlar el robot:

**https://universidad-cenfotec.github.io/Libro-de-la-IA/teachable-ideasense/index.html**

### 🧠 Modelo utilizado

El modelo de ejemplo incluido en este proyecto puede encontrarse en:

**https://teachablemachine.withgoogle.com/models/xDaPhLJzn/**

Las clases del modelo son:

| Clase | Acción |
|--------|--------|
| AVANZAR | El robot avanza |
| DERECHA | Giro a la derecha |
| IZQUIERDA | Giro a la izquierda |
| STOP | Detiene el robot |

> ⚠️ **Importante:** Los nombres de las clases del modelo deben coincidir exactamente con los comandos utilizados en los programas de CircuitPython.

### 🔄 Reentrenar el modelo

La precisión del robot depende directamente de la calidad del modelo de Inteligencia Artificial. Si las clasificaciones no son correctas o el robot responde de forma inesperada, se recomienda abrir el archivo del proyecto (`.tm`) incluido en la carpeta modelo, cargarlo nuevamente en **Google Teachable Machine** y realizar un nuevo entrenamiento con más imágenes o ejemplos de mejor calidad.

De esta manera es posible mejorar el desempeño del sistema sin necesidad de modificar el código del Sumobot.

---

# 🛠️ Hardware utilizado

- IdeaBoard
- IdeaSense (solo en el ejemplo 03)
- Giroscopio LSM6DS3TRC(solo en el ejemplo 02)
- Motores DC
- Computadora con Bluetooth

---

# 📚 Tecnologías

- CircuitPython
- Bluetooth Low Energy (BLE)
- Google Teachable Machine
- TensorFlow.js
- Máquina de Estados
- Control PDI

---

# 🚀 Resultado

Este ejemplo muestra cómo un modelo de Inteligencia Artificial puede controlar un robot físico mediante Bluetooth, evolucionando desde un control básico hasta una solución más completa con corrección automática de trayectoria y retroalimentación visual utilizando IdeaSense.
