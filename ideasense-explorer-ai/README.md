 # 🎮 Control, Telemetría e Inteligencia Artificial: IdeaSense Explorer AI

**Universidad CENFOTEC**

Este proyecto ofrece una solución integral web y firmware inalámbrico para transformar la tarjeta **IdeaBoard** y el módulo **IdeaSense Explorer** en un centro de control con telemetría en tiempo real, gamepad físico BLE, simulador de juegos arcade 2D, laboratorio de entrenamiento de modelos IA, registro de experimentos científicos y **monitoreo ambiental aplicable a casos reales como la agricultura inteligente**.

---

## 💡 La Idea Central de la Plataforma Web

La plataforma **IdeaSense Explorer AI** funciona como un **centro de control todo en uno**, accesible directamente desde el navegador en [**IdeaSense Explorer AI Web**](https://universidad-cenfotec.github.io/IdeaSense/ideasense-explorer-ai/codigos/index.html), diseñada para capturar datos de sensores físicamente a 25 Hz (40 ms) e interactuar bidireccionalmente mediante **Web Bluetooth LE (Nordic UART Service)**. Todo vive en un único archivo `index.html`: no requiere servidor, instalación ni cuenta.

En lugar de requerir múltiples programas independientes, la plataforma integra en un solo panel web:

* 📡 **Telemetría en tiempo real:** Lectura continua de acelerómetro, giroscopio, temperatura, humedad y luz.
* 🌱 **Monitoreo ambiental (ejemplo Agro):** Tablero con indicadores grandes, tendencias, rangos configurables, alertas y comparación de mediciones, pensado como ejemplo de cómo llevar IdeaSense a un caso de uso agrícola.
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
   * Muestra tendencias, estados y alertas de las variables ambientales.
3. **Control Bidireccional (Respuesta Física):**
   * Al diseñar un patrón en la matriz 5x5 de la web, se emite una trama `{"cmd": "matrix", "pixels": [...]}`.
   * La IdeaBoard interpreta el comando y enciende los LEDs mediante el controlador HT16K33.

> ⚠️ **Regla de oro:**
> La tasa de refresco por defecto está configurada a **40 ms (25 Hz)** para asegurar un control fluido en los juegos sin saturar el búfer Bluetooth LE. Si modifica la configuración en la pestaña *Configuración*, asegúrese de no usar intervalos menores a 20 ms.

---

## 🌱 Ejemplo de aplicación: monitoreo ambiental para agricultura inteligente

Esta versión incluye un conjunto de vistas que muestran **qué se puede construir con IdeaSense** cuando el objetivo es observar las condiciones del ambiente alrededor de un cultivo. Es un **ejemplo adaptable**: las mismas ideas (medir, visualizar, comparar, registrar, exportar) sirven para invernaderos, viveros, bodegas, aulas o cualquier espacio donde importen la temperatura, la humedad del aire y la luz.

> ⚠️ **Alcance del ejemplo.** Se miden **temperatura, humedad relativa del aire y luz ambiental**. **No se mide humedad del suelo ni se diagnostica la salud de una planta.** La luz se reporta en *cuentas ALS* del sensor LTR-303 (canal CH0), **sin calibrar a lux**. La temperatura puede verse influida por el calor de la propia placa.

### 📊 Dashboard Agro
* Indicadores grandes de **temperatura**, **humedad relativa** y **luz ambiental**, con estado (*bajo / en rango / sobre el rango*) y tendencia por minuto.
* Gráfico histórico en tiempo real (1 muestra por segundo, últimos 5 minutos).
* Estado de la IdeaBoard: conexión BLE, antigüedad de la última lectura y estado de cada sensor.

### 🔍 Transparencia de los datos
Un banner indica siempre el origen de lo que se visualiza:

| Banner | Significado |
| :--- | :--- |
| 🟢 Lecturas reales | Todos los sensores respondieron |
| 🟠 Sensor no detectado | El firmware informa que ese valor es **simulado** |
| 🟠 Modo DEMO | Datos generados por el navegador, **no** provienen de sensores |
| ⚪ Sin verificar | Firmware sin el campo `sim`: no se puede confirmar el origen |

El origen también se guarda en cada fila de los CSV (`origen_datos`).

### 📈 Análisis ambiental
* Mínimo, promedio, máximo y tendencia de cada variable.
* **Rangos configurables** (los valores iniciales son ejemplos de demostración, no recomendaciones agronómicas).
* **Alertas descriptivas** cuando una variable sale o vuelve a su rango.
* **Comparar mediciones:** guarde un punto A y un punto B (por ejemplo, sol vs. sombra) y observe la diferencia (Δ).

### 🧪 Experimentos Agro
Seleccione variables, nombre y anote el experimento, registre (1 muestra/s), consulte el historial y **exporte a CSV** (compatible con Excel y Python).

### 🧠 IA y datos ambientales
Sección **explicativa** sobre el potencial de aplicar Machine Learning a conjuntos de datos ambientales recopilados durante diferentes periodos (patrones día/noche, comparación de zonas, detección de lecturas anómalas, tendencias). **La plataforma no entrena modelos con datos ambientales**; el flujo propuesto es registrar experimentos, exportar el CSV y analizarlo fuera de la página con Python o Excel, validando con referencias de una persona experta.

### 💬 Guion sugerido para una demostración
1. Conectar la IdeaBoard y mostrar el banner verde.
2. Soplar sobre el sensor de humedad (SHT30): la humedad sube.
3. Tapar el sensor de luz (LTR-303): la luz baja.
4. Guardar el punto A (descubierto) y B (tapado) y comparar.
5. Reducir un umbral para provocar una alerta.
6. Registrar 30 s y exportar el CSV.
7. Explicar la sección de IA y datos ambientales.

---

## 🛠️ Funcionalidades y Módulos de la Plataforma

El menú lateral muestra primero las vistas del ejemplo ambiental (*Dashboard Agro, Análisis ambiental, Experimentos Agro, IA y datos ambientales*) y, bajo *IdeaSense original*, los módulos siguientes, que se conservan.

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
Un módulo de Machine Learning pensado para grabar ráfagas de datos del IMU durante 3 segundos y entrenar clasificadores de movimiento directamente en el navegador. Trabaja con **acelerómetro y giroscopio**; no está diseñado para analizar variables ambientales.

1. **Extracción de Características:** Calcula la media ($\mu$) y desviación estándar ($\sigma$) de los 6 ejes de movimiento, generando un vector de 12 dimensiones por muestra:
   $$\vec{V} = [\mu_{ax}, \mu_{ay}, \mu_{az}, \mu_{gx}, \mu_{gy}, \mu_{gz}, \sigma_{ax}, \sigma_{ay}, \sigma_{az}, \sigma_{gx}, \sigma_{gy}, \sigma_{gz}]$$
2. **Clasificación $k$-NN:** Identifica la clase de movimiento más cercana y muestra el nivel de confianza (%).
3. **Exportación a Python:** Permite descargar el modelo entrenado formateado como código `.py` listo para cargarse en CircuitPython.

> ℹ️ Ver *Estado actual y limitaciones conocidas*: en esta versión la captura y la clasificación en vivo del AI Lab están incompletas.

### 5. Experimentos Científicos
Permite seleccionar individualmente los sensores que se desean registrar (Temperatura, Humedad, Luz, Acelerómetro, Giroscopio), iniciar grabaciones de tiempo finito y exportar la serie temporal resultante a archivos `.csv` para análisis en Excel o Python. Para el registro ambiental funcional de la versión actual, use **Experimentos Agro**.

### 6. Visualización 3D
Representa la orientación espacial de la tarjeta en tres dimensiones mediante un cubo 3D interactivo que rota según el cálculo de los ángulos de inclinación (*Pitch* y *Roll*):

$$\text{Roll} = \arctan\left(\frac{A_y}{A_z}\right) \times \frac{180}{\pi}, \quad \text{Pitch} = \arctan\left(\frac{-A_x}{\sqrt{A_y^2 + A_z^2}}\right) \times \frac{180}{\pi}$$

---

## 🧠 1. Entrenar el modelo de IA de Gestos

El módulo **AI Lab** está concebido para crear clasificadores de movimiento personalizados sin necesidad de servidores externos:

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
  "bb": 0,
  "sim": 0
}
```

| Campo | Significado |
| :--- | :--- |
| `t`, `h` | Temperatura (°C) y humedad relativa (%) del SHT30 |
| `l` | Luz ambiental en cuentas ALS (LTR-303, canal CH0), sin calibrar a lux |
| `ax`…`az`, `gx`…`gz` | Acelerómetro (g) y giroscopio (°/s) |
| `ba`, `bb` | Estado de los botones A y B/C |
| `sim` | Bitmask de sensores **no detectados** cuyo valor es simulado: `1` = temp./humedad, `2` = IMU, `4` = luz. `0` = todo real |

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
        "ba": state_a, "bb": state_b,
        "sim": sim["f"]   # 0 = lecturas reales
    }

    payload = json.dumps(telemetry_packet) + "\n"
    uart.write(payload.encode('utf-8'))
```

**Notas del firmware**
* El IMU se lee con `idea.accel` e `idea.gyro` (librería `ideasense`), con respaldo por I2C directo. Si ninguna lectura funciona, se envían ceros y se marca `sim`; no se inventan datos del IMU.
* La librería `IdeaSense` ya abre el bus I2C. Abrir otro con `busio.I2C(...)` produce `IO22 in use`, por lo que el firmware **reutiliza** el bus existente (o `board.I2C()`).
* Al arrancar, la consola serial debe mostrar `[I2C] dispositivos: ['0x29', '0x44', '0x6a', …]` (luz, temp./humedad e IMU).
* Si un sensor no responde, el firmware conserva un valor de respaldo para temperatura/humedad y luz, **pero ahora lo declara en `sim`** para que la interfaz lo advierta.

---

## 🔌 3. Conectar Todo

1. **Cargar el Firmware:** Copie [`codigos/code.py`](codigos/code.py) en la unidad de almacenamiento de la IdeaBoard utilizando [IdeaCode](https://ideacode.crcibernetica.com/) o su editor preferido.
2. **Encender la Placa:** Alimente la IdeaBoard mediante el cable USB.
3. **Abrir la Plataforma Web:** Ingrese a [**IdeaSense Explorer AI**](https://universidad-cenfotec.github.io/IdeaSense/ideasense-explorer-ai/codigos/index.html) desde Chrome o Edge (Web Bluetooth requiere HTTPS o `localhost`). Para uso local: en la carpeta `codigos/` ejecute `python3 -m http.server 8000` y abra `http://localhost:8000`.
4. **Conectar Bluetooth:** Presione el botón **"Conectar IdeaBoard"** en la esquina superior derecha y seleccione el dispositivo `IdeaBoard-Explorer-AI` o `IdeaBoard`.
5. **Comenzar la Interacción:** Visualice las mediciones en *Dashboard Agro*, compárelas en *Análisis ambiental*, registre un experimento, inicie la carrera en *Juegos Web* o explore el resto de módulos.

> 🌐 La página carga Chart.js (v4.4.1), Font Awesome y Google Fonts desde CDN, por lo que el equipo que la abre necesita conexión a internet.

---

## ✅ Pruebas sugeridas

1. Con sensores conectados: banner verde «Lecturas reales».
2. Soplar sobre el SHT30: la humedad sube y la tendencia muestra ▲.
3. Tapar el sensor de luz: el valor baja.
4. Reducir el umbral máximo de temperatura por debajo del valor actual: aparece «Sobre el rango» y una alerta descriptiva.
5. Guardar puntos A y B: la tabla muestra la diferencia.
6. Registrar un experimento de ~30 s y exportar el CSV: la columna `origen_datos` debe indicar `REAL`.
7. Apagar la placa: el estado cambia a «Desconectado».
8. Con un `code.py` anterior (sin `sim`): banner «Sin verificar».
9. Activar el Modo DEMO: banner naranja y `DEMO` en el CSV.

---

## ⚠️ Estado actual y limitaciones conocidas

* **Ejemplo, no producto agronómico:** los rangos por defecto (18–30 °C, 40–80 %, 0–30000 cuentas) son valores de demostración. Cualquier conclusión agronómica requiere más datos, otros sensores (por ejemplo, humedad de suelo, que este kit no incluye) y validación profesional.
* **Luz sin calibrar:** se reporta en cuentas del sensor, no en lux.
* **AI Lab:** en esta versión la captura no almacena las lecturas del IMU y la clasificación k-NN en vivo (clase predicha, confianza y anomalías) no está implementada, por lo que el módulo no es funcional todavía. Se conserva sin cambios.
* **Pestaña *Experimentos* original:** no registra datos; el registro funcional está en *Experimentos Agro*.
* **Modo DEMO:** genera datos simulados en el navegador; siempre se señala con un banner y en los CSV.
* **Persistencia:** los rangos y experimentos se guardan en el navegador (almacenamiento local); el resto de datos vive en memoria durante la sesión.
* **Validación:** probar con la IdeaBoard y los sensores reales antes de cada demostración.

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
    ├── index.html       ← Aplicación Web SPA en un solo archivo (HTML, CSS y JS)
    └── code.py          ← Firmware en CircuitPython 10.x para IdeaBoard
```

| Componente | Archivo / Enlace | Descripción |
| :--- | :--- | :--- |
| 🌐 **Aplicación Web** | [Abrir Plataforma Web](https://universidad-cenfotec.github.io/IdeaSense/ideasense-explorer-ai/codigos/index.html) | Monitoreo ambiental, Gamepad Arcade 2D, AI Lab y Experimentos |
| 💻 **Código Fuente Web** | [`codigos/index.html`](codigos/index.html) | Código HTML5, CSS, JavaScript y Chart.js |
| 🐍 **Firmware Placa** | [`codigos/code.py`](codigos/code.py) | Programa CircuitPython con transmisión BLE |

---

## 📚 Tecnologías Utilizadas

* 🤖 **IdeaBoard & IdeaSense Explorer** (Hardware y Sensores I2C)
* 🐍 **CircuitPython 10.x** (Librerías `ideaboard`, `ideasense`, `adafruit_ble`)
* 📡 **Web Bluetooth API** (Servicio BLE NUS - Nordic UART)
* 📊 **Chart.js** (Gráficos interactivos de telemetría continua)
* 🎨 **Canvas HTML5 2D & WebGL CSS 3D** (Motor del juego Arcade y visualización del cubo 3D)
* 🧠 **JavaScript (ES6+)** (Procesamiento de señales, tendencias, alertas y exportación CSV)

---

## 🚀 Resultado Final

El proyecto **IdeaSense Explorer AI** demuestra la integración entre microcontroladores físicos, conectividad inalámbrica de baja energía (BLE) y aplicaciones web de alto rendimiento. Permite a estudiantes e investigadores convertir la tarjeta IdeaBoard en un gamepad para videojuegos, un registrador de datos científicos, un monitor de condiciones ambientales —con aplicaciones como el ejemplo de agricultura inteligente— o un dispositivo de detección de gestos por Inteligencia Artificial, de forma inalámbrica y directa desde el navegador.
