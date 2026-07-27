# 🤖 SumoIA - Sumobot Inteligente con BLE, PDI e IdeaSense



Este proyecto presenta una de las tantas aplicaciones de un Sumobot utilizando comunicación **Bluetooth Low Energy (BLE)**, **Máquina de Estados**, control **PDI** e integración con **IdeaSense**.



El objetivo es transformar un robot controlado mediante instrucciones básicas en un sistema más inteligente, capaz de recibir comandos inalámbricos, corregir su trayectoria automáticamente y mostrar información visual mediante una matriz LED.



---



# 💡 Descripción del proyecto



Un Sumobot es una plataforma ideal para aprender robótica porque combina diferentes áreas de la tecnología:



- Programación embebida.

- Control de motores.

- Comunicación inalámbrica.

- Sensores.

- Sistemas inteligentes.

- Inteligencia Artificial.



En este proyecto se desarrollan tres versiones con mismo robot. Cada versión agrega una nueva capacidad:



1. **Control básico mediante BLE.**

2. **Control avanzado con Máquina de Estados y PDI.**

3. **Control con retroalimentación visual utilizando IdeaSense.**



---



# 📂 Estructura del proyecto



```text

SumoIA

│

├── README.md

│

├── 01_control_basico_ble.py

├── 02_sumobot_pdi_estados.py

└── 03_sumobot_ideasense.py



🟢 Código 01: Control básico BLE

Archivo:



01_control_basico_ble.py





Descripción

EL IdeaBoard recibe comandos enviados mediante Bluetooth Low Energy y ejecuta directamente las acciones correspondientes utilizando sus motores.

Los comandos utilizados son:

ComandoAcciónSTOPDetener el robotAVANZARMover hacia adelanteDERECHAGirar hacia la derechaIZQUIERDAGirar hacia la izquierda

Funcionamiento

Usuario

|

|

Bluetooth BLE

|

v

IdeaBoard

|

+------------+

| |

Motor 1 Motor 2



Características



Comunicación inalámbrica BLE.



Control de motores.



Primer acercamiento al manejo del robot.



Base para agregar sistemas más avanzados.

Esta versión permite comprobar que el robot puede recibir instrucciones externas y ejecutar movimientos correctamente.

🟡 Código 02: Sumobot con PDI y Máquina de Estados

Archivo:


02_sumobot_pdi_estados.py


Descripción

Esta versión agrega una arquitectura más avanzada utilizando una Máquina de Estados y un controlador PDI.

Uno de los problemas comunes en robots con motores independientes es que pequeñas diferencias entre los motores provocan que el robot no avance completamente recto.

Para solucionar este problema se incorpora un giroscopio LSM6DS3TRC, el cual permite medir la velocidad angular del robot.

🎯 Control PDI

El controlador PDI utiliza la información del giroscopio para detectar desviaciones durante el movimiento.

Ejemplo:



Dirección deseada:



↑





Dirección real:



↗





Corrección aplicada:



↑



El sistema modifica la velocidad de los motores:



Motor izquierdo = velocidad base + corrección



Motor derecho = velocidad base - corrección



Esto permite que el Sumobot mantenga una trayectoria más estable.

Máquina de Estados

La lógica del robot está organizada mediante diferentes estados:





CALIBRANDO

|

v

DESCONECTADO

|

v

STOP

/ | \

/ | \

v v v



AVANZAR DERECHA IZQUIERDA



|

v



PDI



Estados implementados

EstadoFunciónCALIBRANDOCalcula el error inicial del giroscopioDESCONECTADOMantiene el robot detenido si no existe conexión BLESTOPDetiene motores y reinicia el controlAVANZARMovimiento con corrección PDIDERECHAGiro del robotIZQUIERDAGiro del robot

🔵 Código 03: Sumobot con IdeaSense

Archivo:



03_sumobot_ideasense.py





Descripción

Esta versión agrega una interfaz visual utilizando la matriz LED 5x5 de IdeaSense.

Además de ejecutar el movimiento, el robot muestra una representación gráfica del comando actual.

Esto permite observar fácilmente qué estado está ejecutando el Sumobot.

Patrones visuales

STOP

Representa una señal de detención:



X X

X X

X

X X

X X



AVANZAR

Representa una flecha hacia adelante:



X

XXX

X

X

X



DERECHA

Representa un movimiento hacia la derecha:



X

X

XXXXX

X



IZQUIERDA

Representa un movimiento hacia la izquierda:



X

X

XXXXX

X



Arquitectura completa



Modelo IA / Usuario



|

|

v



Comunicación BLE



|

|

v



IdeaBoard



+-----------+

| |

v v



Motores IdeaSense



|

|

v



Matriz LED 5x5



🤖 Integración con Inteligencia Artificial

El Sumobot puede integrarse con modelos creados mediante Google Teachable Machine.

Un modelo de visión puede reconocer diferentes acciones y enviar comandos mediante Bluetooth.

Ejemplo:





Cámara



|



v



Modelo IA



|



v



Etiqueta detectada



|



v



BLE



|



v



Sumobot



Modelo utilizado:

https://teachablemachine.withgoogle.com/models/xDaPhLJzn/

Clases esperadas:

ClaseAcciónAVANZARMovimiento hacia adelanteDERECHAGiro derechoIZQUIERDAGiro izquierdoSTOPDetener robot

Importante:



Los nombres de las clases del modelo deben coincidir exactamente con los comandos interpretados por la Máquina de Estados.

🚀 ¿Por qué es interesante utilizar un Sumobot de esta manera?

Un Sumobot permite estudiar conceptos que aparecen en robots reales.

Aunque inicialmente parece un robot sencillo, puede convertirse en una plataforma donde se aplican diferentes tecnologías:



Comunicación inalámbrica

BLE permite controlar el robot sin utilizar cables, separando el sistema de decisión del sistema físico.

Control automático

El uso del PDI permite que el robot utilice información del entorno para corregir su comportamiento y mejorar su precisión.

Sistemas inteligentes

Al integrar Inteligencia Artificial, el robot deja de depender únicamente de comandos manuales y puede reaccionar ante información obtenida por una cámara.

Diseño modular

El proyecto está construido por etapas, permitiendo agregar nuevas capacidades:





Sensores adicionales.



Detección de obstáculos.



Visión artificial.



Navegación autónoma.



Estrategias de competencia Sumobot.

🛠️ Hardware utilizado

CantidadComponenteFunción1IdeaBoardControl principal del robot y comunicación BLE1IdeaSenseVisualización mediante matriz LED 5x51LSM6DS3TRCMedición de velocidad angular para control PDI2Motores DCMovimiento del robot1ComputadoraEjecución del modelo IA y comunicación BLE

📚 Tecnologías utilizadas



CircuitPython



Bluetooth Low Energy (BLE)



IdeaBoard



IdeaSense



Máquina de Estados



Control PDI



Google Teachable Machine



TensorFlow.js

✅ Resultado final

El proyecto demuestra la evolución de un robot desde un control básico hasta un sistema inteligente:





Control manual



|



v



Control inalámbrico BLE



|



v



Máquina de Estados



|



v



Corrección automática con PDI



|



v



Integración con IA e IdeaSense



El Sumobot se convierte en una plataforma educativa para experimentar con robótica, programación e inteligencia artificial.

🟢 Código 01: Control básico BLE
Archivo: 01_control_basico_ble.py

Descripción
Esta es la primera versión del Sumobot.
La IdeaBoard recibe comandos enviados mediante Bluetooth Low Energy y ejecuta directamente las acciones correspondientes utilizando sus motores.

Los comandos utilizados son:

Comando	Acción
STOP	Detener el robot
AVANZAR	Mover hacia adelante
DERECHA	Girar hacia la derecha
IZQUIERDA	Girar hacia la izquierda
Funcionamiento
Plaintext
Usuario
   |
   |
 Bluetooth BLE
   |
   v
IdeaBoard
   |
   +------------+
   |            |
Motor 1      Motor 2
Características
Comunicación inalámbrica BLE.

Control de motores.

Primer acercamiento al manejo del robot.

Base para agregar sistemas más avanzados.

Esta versión permite comprobar que el robot puede recibir instrucciones externas y ejecutar movimientos correctamente.

🟡 Código 02: Sumobot con PDI y Máquina de Estados
Archivo: 02_sumobot_pdi_estados.py

Descripción
Esta versión agrega una arquitectura más avanzada utilizando una Máquina de Estados y un controlador PDI.
Uno de los problemas comunes en robots con motores independientes es que pequeñas diferencias entre los motores provocan que el robot no avance completamente recto.
Para solucionar este problema se incorpora un giroscopio LSM6DS3TRC, el cual permite medir la velocidad angular del robot.

🎯 Control PDI
El controlador PDI utiliza la información del giroscopio para detectar desviaciones durante el movimiento.
Ejemplo:

Dirección deseada: ↑

Dirección real: ↗

Corrección aplicada: ↑

El sistema modifica la velocidad de los motores:

Motor izquierdo = velocidad base + corrección

Motor derecho = velocidad base - corrección

Esto permite que el Sumobot mantenga una trayectoria más estable.

Máquina de Estados
La lógica del robot está organizada mediante diferentes estados:

Plaintext
             CALIBRANDO
                  |
                  v
            DESCONECTADO
                  |
                  v
                 STOP
             /     |     \
            /      |      \
           v       v       v
      AVANZAR  DERECHA  IZQUIERDA
             |
             v
             PDI
Estados implementados
Estado	Función
CALIBRANDO	Calcula el error inicial del giroscopio
DESCONECTADO	Mantiene el robot detenido si no existe conexión BLE
STOP	Detiene motores y reinicia el control
AVANZAR	Movimiento con corrección PDI
DERECHA	Giro del robot
IZQUIERDA	Giro del robot
🔵 Código 03: Sumobot con IdeaSense
Archivo: 03_sumobot_ideasense.py

Descripción
Esta versión agrega una interfaz visual utilizando la matriz LED 5x5 de IdeaSense.
Además de ejecutar el movimiento, el robot muestra una representación gráfica del comando actual.
Esto permite observar fácilmente qué estado está ejecutando el Sumobot.

Patrones visuales
STOP (Representa una señal de detención)

Plaintext
X   X
 X X
  X
 X X
X   X
AVANZAR (Representa una flecha hacia adelante)

Plaintext
  X
 XXX
  X
  X
  X
DERECHA (Representa un movimiento hacia la derecha)

Plaintext
   X
   X
XXXXX
   X
IZQUIERDA (Representa un movimiento hacia la izquierda)

Plaintext
 X
 X
XXXXX
 X
Arquitectura completa
Plaintext
        Modelo IA / Usuario
                |
                v
          Comunicación BLE
                |
                v
             IdeaBoard
          +-----------+
          |           |
          v           v
       Motores     IdeaSense
                    |
                    v
              Matriz LED 5x5
🤖 Integración con Inteligencia Artificial
El Sumobot puede integrarse con modelos creados mediante Google Teachable Machine.
Un modelo de visión puede reconocer diferentes acciones y enviar comandos mediante Bluetooth.

Ejemplo de flujo:
Plaintext
Cámara -> Modelo IA -> Etiqueta detectada -> BLE -> Sumobot
Modelo utilizado:
https://teachablemachine.withgoogle.com/models/xDaPhLJzn/

Clases esperadas:

Clase	Acción
AVANZAR	Movimiento hacia adelante
DERECHA	Giro derecho
IZQUIERDA	Giro izquierdo
STOP	Detener robot
⚠️ Importante: Los nombres de las clases del modelo deben coincidir exactamente con los comandos interpretados por la Máquina de Estados.

🚀 ¿Por qué es interesante utilizar un Sumobot de esta manera?
Un Sumobot permite estudiar conceptos que aparecen en robots reales.
Aunque inicialmente parece un robot sencillo, puede convertirse en una plataforma donde se aplican diferentes tecnologías:

Comunicación inalámbrica: BLE permite controlar el robot sin utilizar cables, separando el sistema de decisión del sistema físico.

Control automático: El uso del PDI permite que el robot utilice información del entorno para corregir su comportamiento y mejorar su precisión.

Sistemas inteligentes: Al integrar Inteligencia Artificial, el robot deja de depender únicamente de comandos manuales y puede reaccionar ante información obtenida por una cámara.

Diseño modular: El proyecto está construido por etapas, permitiendo agregar nuevas capacidades:

Sensores adicionales.

Detección de obstáculos.

Visión artificial.

Navegación autónoma.

Estrategias de competencia Sumobot.

🛠️ Hardware utilizado
Cantidad	Componente	Función
1	IdeaBoard	Control principal del robot y comunicación BLE
1	IdeaSense	Visualización mediante matriz LED 5x5
1	LSM6DS3TRC	Medición de velocidad angular para control PDI
2	Motores DC	Movimiento del robot
1	Computadora	Ejecución del modelo IA y comunicación BLE
📚 Tecnologías utilizadas
CircuitPython

Bluetooth Low Energy (BLE)

IdeaBoard

IdeaSense

Máquina de Estados

Control PDI

Google Teachable Machine

TensorFlow.js

✅ Resultado final
El proyecto demuestra la evolución de un robot desde un control básico hasta un sistema inteligente:

Plaintext
Control manual
      |
      v
Control inalámbrico BLE
      |
      v
Máquina de Estados
      |
      v
Corrección automática con PDI
      |
      v
Integración con IA e IdeaSense
El Sumobot se convierte en una plataforma educativa para experimentar con robótica, programación e inteligencia artificial.
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(content)

print("README.md created successfully")


```text?code_stdout&code_event_index=1
README.md created successfully

Your Markdown file is ready

Icono de MD
README
 MD 
Abierto
He formateado la información que enviaste utilizando la sintaxis de Markdown para crear una estructura clara, fácil de leer y profesional para tu repositorio. He añadido tablas, bloques de código para los diagramas y jerarquía con títulos y subtítulos. ¡Listo para ser subido a tu proyecto!




Tus conversaciones de Universidad Cenfotec no se usan para mejorar nuestros modelos. Gemini es una IA y puede cometer errores. Tu privacidad y GeminiSe abre en una ventana nueva

# 🤖 SumoIA - Sumobot Inteligente con BLE, PDI e IdeaSense

Este proyecto presenta la evolución de un Sumobot utilizando **IdeaBoard**, comunicación **Bluetooth Low Energy (BLE)**, **Máquina de Estados**, control **PDI** e integración con **IdeaSense**.

El objetivo es transformar un robot controlado mediante instrucciones básicas en un sistema más inteligente, capaz de recibir comandos inalámbricos, corregir su trayectoria automáticamente y mostrar información visual mediante una matriz LED.

---

# 💡 Descripción del proyecto

Un Sumobot es una plataforma ideal para aprender robótica porque combina diferentes áreas de la tecnología:

- Programación embebida.
- Control de motores.
- Comunicación inalámbrica.
- Sensores.
- Sistemas inteligentes.
- Inteligencia Artificial.

En este proyecto se desarrollan tres versiones del mismo robot. Cada versión agrega una nueva capacidad:

1. **Control básico mediante BLE.**
2. **Control avanzado con Máquina de Estados y PDI.**
3. **Control con retroalimentación visual utilizando IdeaSense.**

---

# 📂 Estructura del proyecto

```text
SumoIA
│
├── README.md
│
├── 01_control_basico_ble.py
├── 02_sumobot_pdi_estados.py
└── 03_sumobot_ideasense.py
```

## 🟢 Código 01: Control básico BLE
**Archivo:** `01_control_basico_ble.py`

### Descripción
Esta es la primera versión del Sumobot.
La IdeaBoard recibe comandos enviados mediante Bluetooth Low Energy y ejecuta directamente las acciones correspondientes utilizando sus motores.

Los comandos utilizados son:

| Comando | Acción |
|---|---|
| STOP | Detener el robot |
| AVANZAR | Mover hacia adelante |
| DERECHA | Girar hacia la derecha |
| IZQUIERDA | Girar hacia la izquierda |

### Funcionamiento
```text
Usuario
   |
   |
 Bluetooth BLE
   |
   v
IdeaBoard
   |
   +------------+
   |            |
Motor 1      Motor 2
```

### Características
- Comunicación inalámbrica BLE.
- Control de motores.
- Primer acercamiento al manejo del robot.
- Base para agregar sistemas más avanzados.

Esta versión permite comprobar que el robot puede recibir instrucciones externas y ejecutar movimientos correctamente.

## 🟡 Código 02: Sumobot con PDI y Máquina de Estados
**Archivo:** `02_sumobot_pdi_estados.py`

### Descripción
Esta versión agrega una arquitectura más avanzada utilizando una Máquina de Estados y un controlador PDI.
Uno de los problemas comunes en robots con motores independientes es que pequeñas diferencias entre los motores provocan que el robot no avance completamente recto.
Para solucionar este problema se incorpora un giroscopio LSM6DS3TRC, el cual permite medir la velocidad angular del robot.

### 🎯 Control PDI
El controlador PDI utiliza la información del giroscopio para detectar desviaciones durante el movimiento.
Ejemplo:

*   Dirección deseada: `↑`
*   Dirección real: `↗`
*   Corrección aplicada: `↑`

El sistema modifica la velocidad de los motores:
*   Motor izquierdo = velocidad base + corrección
*   Motor derecho = velocidad base - corrección

Esto permite que el Sumobot mantenga una trayectoria más estable.

### Máquina de Estados
La lógica del robot está organizada mediante diferentes estados:

```text
             CALIBRANDO
                  |
                  v
            DESCONECTADO
                  |
                  v
                 STOP
             /     |                 /      |                 v       v       v
      AVANZAR  DERECHA  IZQUIERDA
             |
             v
             PDI
```

### Estados implementados
| Estado | Función |
|---|---|
| CALIBRANDO | Calcula el error inicial del giroscopio |
| DESCONECTADO | Mantiene el robot detenido si no existe conexión BLE |
| STOP | Detiene motores y reinicia el control |
| AVANZAR | Movimiento con corrección PDI |
| DERECHA | Giro del robot |
| IZQUIERDA | Giro del robot |

## 🔵 Código 03: Sumobot con IdeaSense
**Archivo:** `03_sumobot_ideasense.py`

### Descripción
Esta versión agrega una interfaz visual utilizando la matriz LED 5x5 de IdeaSense.
Además de ejecutar el movimiento, el robot muestra una representación gráfica del comando actual.
Esto permite observar fácilmente qué estado está ejecutando el Sumobot.

### Patrones visuales

**STOP** (Representa una señal de detención)
```text
X   X
 X X
  X
 X X
X   X
```

**AVANZAR** (Representa una flecha hacia adelante)
```text
  X
 XXX
  X
  X
  X
```

**DERECHA** (Representa un movimiento hacia la derecha)
```text
   X
   X
XXXXX
   X
```

**IZQUIERDA** (Representa un movimiento hacia la izquierda)
```text
 X
 X
XXXXX
 X
```

### Arquitectura completa
```text
        Modelo IA / Usuario
                |
                v
          Comunicación BLE
                |
                v
             IdeaBoard
          +-----------+
          |           |
          v           v
       Motores     IdeaSense
                    |
                    v
              Matriz LED 5x5
```

---

# 🤖 Integración con Inteligencia Artificial
El Sumobot puede integrarse con modelos creados mediante Google Teachable Machine.
Un modelo de visión puede reconocer diferentes acciones y enviar comandos mediante Bluetooth.

### Ejemplo de flujo:
```text
Cámara -> Modelo IA -> Etiqueta detectada -> BLE -> Sumobot
```

**Modelo utilizado:**
https://teachablemachine.withgoogle.com/models/xDaPhLJzn/

**Clases esperadas:**

| Clase | Acción |
|---|---|
| AVANZAR | Movimiento hacia adelante |
| DERECHA | Giro derecho |
| IZQUIERDA | Giro izquierdo |
| STOP | Detener robot |

> ⚠️ **Importante:** Los nombres de las clases del modelo deben coincidir exactamente con los comandos interpretados por la Máquina de Estados.

---

# 🚀 ¿Por qué es interesante utilizar un Sumobot de esta manera?
Un Sumobot permite estudiar conceptos que aparecen en robots reales.
Aunque inicialmente parece un robot sencillo, puede convertirse en una plataforma donde se aplican diferentes tecnologías:

- **Comunicación inalámbrica:** BLE permite controlar el robot sin utilizar cables, separando el sistema de decisión del sistema físico.
- **Control automático:** El uso del PDI permite que el robot utilice información del entorno para corregir su comportamiento y mejorar su precisión.
- **Sistemas inteligentes:** Al integrar Inteligencia Artificial, el robot deja de depender únicamente de comandos manuales y puede reaccionar ante información obtenida por una cámara.
- **Diseño modular:** El proyecto está construido por etapas, permitiendo agregar nuevas capacidades:
    - Sensores adicionales.
    - Detección de obstáculos.
    - Visión artificial.
    - Navegación autónoma.
    - Estrategias de competencia Sumobot.

---

# 🛠️ Hardware utilizado

| Cantidad | Componente | Función |
|:---:|---|---|
| 1 | IdeaBoard | Control principal del robot y comunicación BLE |
| 1 | IdeaSense | Visualización mediante matriz LED 5x5 |
| 1 | LSM6DS3TRC | Medición de velocidad angular para control PDI |
| 2 | Motores DC | Movimiento del robot |
| 1 | Computadora | Ejecución del modelo IA y comunicación BLE |

---

# 📚 Tecnologías utilizadas
- CircuitPython
- Bluetooth Low Energy (BLE)
- IdeaBoard
- IdeaSense
- Máquina de Estados
- Control PDI
- Google Teachable Machine
- TensorFlow.js

---

# ✅ Resultado final
El proyecto demuestra la evolución de un robot desde un control básico hasta un sistema inteligente:

```text
Control manual
      |
      v
Control inalámbrico BLE
      |
      v
Máquina de Estados
      |
      v
Corrección automática con PDI
      |
      v
Integración con IA e IdeaSense
```

El Sumobot se convierte en una plataforma educativa para experimentar con robótica, programación e inteligencia artificial.
