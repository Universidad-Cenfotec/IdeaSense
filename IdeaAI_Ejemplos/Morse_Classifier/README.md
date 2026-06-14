# 📟 Morse_Classifier: Traductor Morse con Inteligencia Artificial (CircuitPython)

Este proyecto es un sistema interactivo de **Edge AI** desarrollado bajo el ecosistema de **CircuitPython**. Utiliza los sensores integrados de movimiento (acelerómetro y giroscopio de la placa IdeaSense / IdeaBoard) para capturar gestos físicos del usuario, clasificarlos en tiempo real como "puntos" o "rayas" de código Morse mediante una red neuronal embebida, y traducirlos a caracteres alfabéticos.

El proyecto destaca por ejecutar el modelo de Machine Learning directamente en el hardware (TinyML) y gestionar un sistema de archivos local para almacenar las palabras traducidas.

---

## 🧠 Flujo de Trabajo y Entrenamiento (CRCibernetica IdeaAI)

El corazón de la clasificación no se programó a mano con reglas fijas (`if/else`), sino que se obtuvo mediante un pipeline de Inteligencia Artificial:

1. **Captura de Datos:** Se utilizó la plataforma **CRCibernetica IdeaAI** para recolectar muestras reales de los sensores en dos estados: **"Golpe-Punto"** (movimientos rápidos y secos) y **"Nada-Raya"** (movimientos prolongados o estáticos).
2. **Extracción de Características:** Cada ráfaga de movimiento se dividió en ventanas de tiempo de **25 lecturas (WINDOW = 25)**. Para cada ventana, la plataforma calculó métricas estadísticas complejas (medias, desviaciones estándar, valores mínimos/máximos y cruces por cero).
3. **Entrenamiento del Modelo:** **IdeaAI** entrenó una red neuronal densa (Multilayer Perceptron). Los parámetros de normalización (`NORM_MEAN`, `NORM_STD`), los pesos de las capas (`W1`, `W2`) y los sesgos (`B1`, `B2`) resultantes fueron exportados directamente a código de Python e integrados en este script para ejecutarse de forma local y nativa en el microcontrolador.

---

## 🚀 Características Principales del Sistema

- **TinyML / Edge AI:** Clasificación local instantánea sin necesidad de conexión a Internet ni servidores externos.
- **Diccionario Alfabético Corregido:** Menú por consola ordenado de forma estrictamente alfabética (**A-Z**) invirtiendo la indexación de símbolos Morse para una lectura limpia.
- **Interfaz y Feedback Visual:** Animaciones dedicadas en la matriz LED interna para confirmar aciertos (`✓`), marcar errores de secuencia (`X`) y dibujar las letras de la palabra final.
- **Persistencia en Almacenamiento Flash:** Registro automático de las traducciones en un archivo local `registro_morse.csv`.
- **Freno Antirrebote:** Implementación de lógica de software por banderas para mitigar la alta velocidad del bucle principal y evitar registros duplicados o corruptos al presionar los botones.

# 📟 Edge-Morse-Classifier: Traductor Morse con Inteligencia Artificial (CircuitPython)

Este proyecto es un sistema interactivo de **Edge AI** desarrollado bajo el ecosistema de **CircuitPython**. Utiliza los sensores integrados de movimiento (acelerómetro y giroscopio) de la placa para capturar gestos físicos del usuario, clasificarlos en tiempo real como "puntos" o "rayas" de código Morse mediante una red neuronal embebida, y traducirlos a caracteres alfabéticos.

El proyecto destaca por ejecutar el modelo de Machine Learning directamente en el hardware (TinyML), optimizar la lectura de botones por software y gestionar un sistema de archivos local para almacenar las palabras traducidas de forma persistente.

---

## 🧠 Flujo de Trabajo y Entrenamiento (CRCibernetica IdeaAI)

El corazón de la clasificación no se programó a mano con reglas fijas (`if/else`), sino que se obtuvo mediante un pipeline de Inteligencia Artificial:

1. **Captura de Datos:** Se utilizó la plataforma **CRCibernetica IdeaAI** para recolectar muestras reales de los sensores en dos estados: **"Golpe-Punto"** (movimientos rápidos y secos) y **"Nada-Raya"** (movimientos prolongados o estáticos).
2. **Extracción de Características:** Cada ráfaga de movimiento se dividió en ventanas de tiempo de **25 lecturas (WINDOW = 25)**. Para cada ventana, la plataforma calculó métricas estadísticas complejas (medias, desviaciones estándar, valores mínimos/máximos y cruces por cero).
3. **Entrenamiento del Modelo:** **IdeaAI** entrenó una red neuronal densa (Multilayer Perceptron). Los parámetros de normalización (`NORM_MEAN`, `NORM_STD`), los pesos de las capas (`W1`, `W2`) y los sesgos (`B1`, `B2`) resultantes fueron exportados directamente a código de Python e integrados en este script para ejecutarse de forma local y nativa en el microcontrolador.

---

## 🚀 Características Principales del Sistema

- **TinyML / Edge AI:** Clasificación local instantánea sin necesidad de conexión a Internet ni servidores externos.
- **Diccionario Alfabético Corregido:** Menú por consola ordenado de forma estrictamente alfabética (**A-Z**) invirtiendo la indexación de símbolos Morse para una lectura limpia.
- **Interfaz y Feedback Visual:** Animaciones dedicadas en la matriz LED interna para confirmar aciertos (`✓`), marcar errores de secuencia (`X`) y dibujar las letras de la palabra final.
- **Persistencia en Almacenamiento Flash:** Registro automático de las traducciones en un archivo local `registro_morse.csv`.
- **Freno Antirrebote:** Implementación de lógica de software por banderas para mitigar la alta velocidad del bucle principal y evitar registros duplicados o corruptos al presionar los botones.

---

## 📁 Estructura del Repositorio y Descripción de Archivos

Para mantener el proyecto organizado y facilitar su mantenimiento, los archivos se dividen de la siguiente manera en el repositorio:

```text
Morse_Classifier/
├── README.md               <-- Documentación principal del proyecto
└── traductor_morse/        <-- Subcarpeta con el software del sistema
    ├── Morce_Interface.py  <-- Script unificado de ejecución en la placa
    └── modelo_IA.py  <-- Respaldo de los datos puros del modelo de IA

---
