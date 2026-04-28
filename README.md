# IdeaSense

Repositorio de documentos y ejemplos IdeaBoard-IdeaSense

<p align="center">
  <img src="https://github.com/Universidad-Cenfotec/IdeaSense/blob/main/images/IdeaSense.png" 
       alt="IdeaSense" 
       width="700">
</p>

## Comparación con Micro:bit 

| Criterio | micro:bit | IdeaBoard \+ IdeaSense |
| :---- | :---- | :---- |
| **Nivel de diseño** | Dispositivo educativo cerrado-curado | Plataforma modular (board \+ sensores desacoplados) |
| **Procesador** | Nordic nRF52 (limitado) | ESP32 (alto rendimiento, dual core, WiFi/BLE) |
| **Sensores integrados** | Acelerómetro, brújula, temperatura | Acelerómetro \+ Giroscópio, expandible a múltiples sensores externos |
| **Matriz LED** | 5x5 integrada | 5x5 integrada (equivalente funcional) |
| **Botones** | 2 botones | 3 botones (A, B, C) → más grados de interacción |
| **Arquitectura de hardware** | Monolítica | Distribuida (board \+ módulos) |
| **Extensibilidad física** | Limitada (edge connector) | Alta (conectores dedicados, cables, sensores externos) |
| **Modelo de programación** | Bloques \+ MicroPython | Bloques \+ Python (pero adaptable) |
| **Control del stack** | Parcial (dependes de ecosistema BBC/Microsoft) | Total (hardware \+ firmware \+ plataforma) |
| **Conectividad** | BLE (limitada), radio propietario | WiFi \+ BLE \+ ESPNOW → integración real con IoT y servicios |
| **Uso en investigación** | Bajo | Alto (puede integrarse en pipelines reales) |
| **Capacidad de IA** | Muy limitada | Integrable (LLMs locales, APIs, edge AI) |
| **Modelo pedagógico implícito** | Aprender conceptos | Construir sistemas \+ experimentar |
| **Tipo de usuario que forma** | Usuario guiado | Constructor / diseñador de sistemas |
| **Apertura real** | Parcial (reference design) | Total |
| **Escalabilidad de proyectos** | Baja | Alta (de prototipo a sistema funcional) |
