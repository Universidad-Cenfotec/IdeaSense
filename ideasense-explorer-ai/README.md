# 🎮 Control, Telemetría e Inteligencia Artificial: IdeaSense Explorer AI

**Universidad CENFOTEC**

Este proyecto ofrece una solución integral web y firmware inalámbrico para transformar la tarjeta **IdeaBoard** y el módulo **IdeaSense Explorer** en un centro de control con telemetría en tiempo real, gamepad físico BLE, simulador de juegos arcade 2D, laboratorio de entrenamiento de modelos IA y sistema de registro de experimentos científicos.

---

## 💡 La Idea Central de la Plataforma Web

La plataforma **IdeaSense Explorer AI** funciona como un **centro de control todo en uno**, accesible directamente desde el navegador en [**IdeaSense Explorer AI Web**](https://universidad-cenfotec.github.io/IdeaSense/ideasense-explorer-ai/codigos/index.html), diseñada para capturar datos de sensores físicamente a 25 Hz (40 ms) e interactuar bidireccionalmente mediante **Web Bluetooth LE (Nordic UART Service)**.

En lugar de requerir múltiples programas independientes, la plataforma integra en un solo panel web:

* 📡 **Telemetría en tiempo real:** Lectura continua de acelerómetro, giroscopio, temperatura, humedad y luz.
* 🎮 **Gamepad Inalámbrico Arcade:** Uso de los botones físicos de la tarjeta (`idea.held`) para controlar juegos en canvas 2D.
* 🧠 **Laboratorio de Inteligencia Artificial:** Captura de gestos, extracción de características de 12 dimensiones, clasificación $k$-NN y detección de anomalías.
* 💡 **Control de Matriz LED 5x5:** Diseñador interactivo que transmite gráficos bidireccionalmente a la placa.
* 📊 **Laboratorio de Experimentos:** Registro selectivo de variables ambientales y exportación directa de conjuntos de datos en CSV.

### Flujo general del sistema

1. **Captura y Transmisión de Telemetría (Hardware):**
   * La IdeaBoard lee los sensores I2C (LSM6DS, SHT30, LTR-303) y los botones físicos (`idea.held[0]`, `idea.held[1]`/`idea.held[2]`).
   * Transmite empaquetados JSON a 25 Hz por Bluetooth LE.
2. **Procesamiento y Control Visual (Navegador):**
   * La aplicación recibe las tramas JSON mediante la Web Bluetooth API.
   * Modula en vivo gráficos dinámicos de movimiento y métricas ambientales.
   * Transfiere el estado de los botones físicos al motor de físicas 2D (esquivar obstáculos en la carrera).
   * Clasifica gestos IMU mediante el algoritmo $k$-NN en tiempo real.
3. **Control Bidireccional (Respuesta Física):**
   * Al diseñar un patrón en la matriz 5x5 de la web, se emite una trama `{"cmd": "matrix", "pixels": [...]}`.
   * La IdeaBoard interpreta el comando y enciende los LEDs mediante el controlador HT16K33.

> ⚠️ **Regla de oro:**
> La tasa de refresco por defecto está configurada a **40 ms (25 Hz)** para asegurar un control fluido en los juegos sin saturar el búfer Bluetooth LE. Si modifica la configuración en la pestaña *Settings*, asegúrese de no usar intervalos menores a 20 ms.

---

## 🛠️ Funcionalidades y Módulos de la Plataforma

### 1. Dashboard (Panel Principal)
Supervisión global con lectura instantánea de métricas clave, estado de entrenamiento del modelo de IA, resumen dinámico de aceleración ($A_x, A_y, A_z$) y monitoreo en vivo de los botones físicos **A** y **B/C**.

### 2. Explorer & Matriz LED 5x5
Visualización numérica detallada de los datos del acelerómetro ($g$) y giroscopio ($dps$). Incluye una cuadrícula interactiva de 5x5 píxeles donde el usuario puede activar LEDs haciendo clic y enviarlos en tiempo real a la matriz física de la placa.

**Comando JSON enviado a la tarjeta:**
```json
{
  "cmd": "matrix",
  "pixels": [0,1,0,1,0, 1,1,1,1,1, 1,1,1,1,1, 0,1,1,1,0, 0,0,1,0,0]
}
```

### 3. Juegos Web (Gamepad Arcade 2D)
Simulador de carreras 2D renderizado en un Canvas HTML5. La posición del vehículo se controla mediante los botones físicos integrados en la tarjeta IdeaBoard.

* 🕹️ **Botón A (`idea.held[0]`):** Desplaza el vehículo hacia la izquierda.
* 🕹️ **Botón B / C (`idea.held[1]` / `idea.held[2]`):** Desplaza el vehículo hacia la derecha.
* ⌨️ **Teclado de respaldo:** Teclas `Flecha Izquierda` y `Flecha Derecha` para pruebas sin hardware.

### 4. AI Lab (Laboratorio de Inteligencia Artificial)
Un módulo autónomo de Machine Learning que graba ráfagas de datos del IMU durante 3 segundos para entrenar clasificadores de movimiento directamente en el navegador.

1. **Extracción de Características:** Calcula la media ($\mu$) y desviación estándar ($\sigma$) de los 6 ejes de movimiento, generando un vector de 12 dimensiones por muestra:
   $$\vec{V} = [\mu_{ax}, \mu_{ay}, \mu_{az}, \mu_{gx}, \mu_{gy}, \mu_{gz}, \sigma_{ax}, \sigma_{ay}, \sigma_{az}, \sigma_{gx}, \sigma_{gy}, \sigma_{gz}]$$
2. **Clasificación $k$-NN:** Identifica la clase de movimiento más cercana y muestra el nivel de confianza (%).
3. **Exportación a Python:** Permite descargar el modelo entrenado formateado como código `.py` listo para cargarse en CircuitPython.

### 5. Experimentos Científicos
Permite seleccionar individualmente los sensores que se desean registrar (Temperatura, Humedad, Luz, Acelerómetro, Giroscopio), iniciar grabaciones de tiempo finito y exportar la serie temporal resultante a archivos `.csv` para análisis en Excel o Python.

### 6. Visualización 3D
Representa la orientación espacial de la tarjeta en tres dimensiones mediante un cubo 3D interactivo que rota según el cálculo de los ángulos de inclinación (*Pitch* y *Roll*):

$$\text{Roll} = \arctan\left(\frac{A_y}{A_z}\right) \times \frac{180}{\pi}, \quad \text{Pitch} = \arctan\left(\frac{-A_x}{\sqrt{A_y^2 + A_z^2}}\right) \times \frac{180}{\pi}$$

---

## 🧠 1. Entrenar el modelo de IA de Gestos

El módulo **AI Lab** permite crear clasificadores de movimiento personalizados sin necesidad de servidores externos:

1. **Seleccionar o crear una clase:** Elija una categoría como `Reposo`, `Inclinacion`, `Movimiento` o agregue una propia.
2. **Capturar muestras:** Presione `Capturar (3s)` y realice el movimiento continuo con la tarjeta IdeaBoard frente a usted.
3. **Entrenar el modelo:** Una vez capturadas al menos 2 muestras por clase, presione `Entrenar Modelo`.
4. **Clasificación en Vivo:** Realice los movimientos grabados y observe cómo el sistema clasifica el gesto en tiempo real mostrando el nivel de confianza.
5. **Exportar a la Placa:** Haga clic en `Descargar .py` para obtener la estructura de datos lista para CircuitPython.

---

## 💻 2. Programar la IdeaBoard (CircuitPython)

El programa cargado en la tarjeta (`code.py`) lee periódicamente el hardware y transmite empaquetados JSON a través del servicio BLE NUS.

**Estructura del empaquetado JSON de telemetría:**
```json
{
  "t": 23.5,
  "h": 50.2,
  "l": 310,
  "ax": 0.015,
  "ay": -0.021,
  "az": 0.982,
  "gx": 0.1,
  "gy": -0.2,
  "gz": 0.0,
  "ba": 1,
  "bb": 0
}
```

**Código base de lectura y transmisión (`code.py`):**
```python
def send_telemetry():
    t, h = read_environment_sensors()
    ax, ay, az, gx, gy, gz = read_motion_sensors()
    lux = read_light_sensor()

    state_a = 1 if (idea and hasattr(idea, 'held') and idea.held[0]) else 0
    state_b = 1 if (idea and hasattr(idea, 'held') and len(idea.held) > 1 and idea.held[1]) else 0

    telemetry_packet = {
        "t": round(t, 1), "h": round(h, 1), "l": int(lux),
        "ax": round(ax, 3), "ay": round(ay, 3), "az": round(az, 3),
        "gx": round(gx, 1), "gy": round(gy, 1), "gz": round(gz, 1),
        "ba": state_a, "bb": state_b
    }

    payload = json.dumps(telemetry_packet) + "\n"
    uart.write(payload.encode('utf-8'))
```

---

## 🔌 3. Conectar Todo

1. **Cargar el Firmware:** Copie [`codigos/code.py`](codigos/code.py) en la unidad de almacenamiento de la IdeaBoard utilizando [IdeaCode](https://ideacode.crcibernetica.com/) o su editor preferido.
2. **Encender la Placa:** Alimente la IdeaBoard mediante el cable USB.
3. **Abrir la Plataforma Web:** Ingresa a [**IdeaSense Explorer AI**](https://universidad-cenfotec.github.io/IdeaSense/ideasense-explorer-ai/codigos/index.html) desde Chrome o Edge.
4. **Conectar Bluetooth:** Presione el botón **"Conectar IdeaBoard"** en la esquina superior derecha y seleccione el dispositivo `IdeaBoard-Explorer-AI` o `IdeaBoard`.
5. **Comenzar la Interacción:** Inicie la carrera en la pestaña *Juegos Web*, visualice las curvas en *Dashboard* o entrene un gesto en *AI Lab*.

---

## 🛠️ Materiales Necesarios

| Cantidad | Componente | Función |
| :---: | :--- | :--- |
| **1** | IdeaBoard | Placa principal con microcontrolador ESP32 y Bluetooth LE. |
| **1** | IdeaSense Explorer | Módulo con sensores IMU (LSM6DS), Temp/Hum (SHT30), Luz (LTR-303) y Matriz LED (HT16K33). |
| **1** | Computadora / Tablet | Ejecuta la aplicación web SPA con soporte Web Bluetooth (Chrome/Edge). |
| **1** | Cable USB | Alimentación eléctrica y transferencia del programa CircuitPython. |

---

## 📂 Contenido de la Carpeta

```text
ideasense-explorer-ai
├── README.md            ← Documentación detallada de la herramienta
└── codigos
    ├── index.html       ← Aplicación Web SPA (Dashboard, Gamepad 2D, AI Lab, Experimentos)
    └── code.py          ← Firmware en CircuitPython 9.x para IdeaBoard
```

| Componente | Archivo / Enlace | Descripción |
| :--- | :--- | :--- |
| 🌐 **Aplicación Web** | [Abrir Plataforma Web](https://universidad-cenfotec.github.io/IdeaSense/ideasense-explorer-ai/codigos/index.html) | Dashboard, Gamepad Arcade 2D, AI Lab y Experimentos |
| 💻 **Código Fuente Web** | [`codigos/index.html`](codigos/index.html) | Código HTML5, JavaScript y Chart.js |
| 🐍 **Firmware Placa** | [`codigos/code.py`](codigos/code.py) | Programa CircuitPython 9.x con transmisión BLE |

---

## 📚 Tecnologías Utilizadas

* 🤖 **IdeaBoard & IdeaSense Explorer** (Hardware y Sensores I2C)
* 🐍 **CircuitPython 9.x** (Librerías `ideaboard`, `ideasense`, `adafruit_ble`)
* 📡 **Web Bluetooth API** (Servicio BLE NUS - Nordic UART)
* 📊 **Chart.js** (Gráficos interactivos de telemetría continua)
* 🎨 **Canvas HTML5 2D & WebGL CSS 3D** (Motor del juego Arcade y visualización del cubo 3D)
* 🧠 **JavaScript (ES6+)** (Clasificador $k$-NN local y procesamiento de señales)

---

## 🚀 Resultado Final

El proyecto **IdeaSense Explorer AI** demuestra la integración entre microcontroladores físicos, conectividad inalámbrica de baja energía (BLE) y aplicaciones web de alto rendimiento. Permite a estudiantes e investigadores convertir la tarjeta IdeaBoard en un gamepad para videojuegos, un registrador de datos científicos o un dispositivo de detección de gestos por Inteligencia Artificial de forma inalámbrica y directa desde el navegador.
