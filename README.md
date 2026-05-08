# 🧭 RPG Agentic 2D (Pygame)

Este sistema permite que el desarrollo del juego pueda ser asistido por IA local, donde cada agente tiene un rol específico dentro del ciclo de desarrollo.

Este proyecto es un RPG 2D por turnos desarrollado en Python utilizando Pygame.  
El objetivo principal no es solo crear un videojuego, sino también servir como laboratorio de aprendizaje para sistemas modulares y agentes de desarrollo asistido.

A lo largo del desarrollo, el proyecto irá evolucionando desde un prototipo simple hacia un RPG completo con combate por turnos, progresión de mapa y sistemas expansibles.

---

# 🎯 Visión del proyecto

El juego representa una aventura clásica de RPG en 2D donde el jugador progresa a través de encuentros, combates y decisiones simples.

La prioridad inicial es:

- Construir primero la lógica del juego
- Mantener una arquitectura modular
- Usar representaciones simples (rectángulos, UI básica)
- Iterar progresivamente hacia un juego completo

---

# 🎮 Estructura del juego

El juego está dividido en **3 pantallas principales**:

---

## 🧍 Pantalla 1 — Selección de personaje

El jugador elige entre tres clases disponibles:

- 🗡️ Guerrero
- 🗡️ Pícaro
- 🔮 Mago

Cada personaje está representado inicialmente con un rectángulo.

Debajo de cada uno se mostrará:

- Estadísticas básicas (vida, ataque, defensa, velocidad)
- Descripción narrativa del personaje (lore), que será expandida posteriormente

Esta pantalla define el inicio de la aventura del jugador.

---

## 🗺️ Pantalla 2 — Mapa de progreso

El jugador avanza a través de un mapa lineal representado por:

- Una línea horizontal
- Círculos distribuidos a lo largo del recorrido

Cada círculo representa un encuentro:

- Combate aleatorio
- Evento prediseñado

### Mecánicas:

- El jugador puede moverse hacia la izquierda o derecha
- Avanza o retrocede entre nodos del mapa
- Selecciona el próximo encuentro

El objetivo es llegar al final del recorrido.

---

## ⚔️ Pantalla 3 — Sistema de combate

Sistema de combate por turnos entre el jugador y enemigos.

### Mecánicas básicas:

- Turnos alternos (jugador → enemigo)
- Acciones disponibles:
  - Atacar
  - Defender
  - Usar objetos
  - Huir

### Características del sistema:

- Representación visual simple con rectángulos
- Sistema inicialmente minimalista
- Evolución progresiva hacia mecánicas más complejas

---

## 👑 Jefe final

El recorrido contiene:

- 5 combates en total
- El último combate es un boss fijo

El resto de encuentros son aleatorios entre enemigos prediseñados.

---

# 🧱 Filosofía de desarrollo

Este proyecto prioriza:

- ✔️ Primero lógica, después estética
- ✔️ Arquitectura modular desde el inicio
- ✔️ Sistemas independientes por carpeta
- ✔️ Iteración constante
- ✔️ Preparación para integración con agentes de IA

---

# 🤖 Enfoque agentic (futuro del proyecto)

Este proyecto está diseñado para integrarse con un sistema de agentes locales que ayudarán en:

- Arquitectura del código
- Diseño de sistemas
- Refactorización
- Implementación de features
- Revisión de calidad

Esto permitirá simular un entorno de desarrollo asistido por IA local.
El Agent Runner actúa como orquestador del sistema, conectando los agentes con el modelo local de Ollama y permitiendo ejecutar flujos completos de desarrollo de forma automatizada.

# ⚡ Flujo de desarrollo con agentes

El flujo ideal de trabajo del sistema es:

1. El Architect define estructura y diseño del sistema
2. El Gameplay Agent implementa la funcionalidad en código
3. El Reviewer valida, corrige y optimiza el resultado
4. El Executor aplica los cambios directamente al proyecto

Este ciclo permite un desarrollo iterativo y asistido por IA local.

---

# 📁 Estructura esperada del proyecto

humble_rpg-project/
│
├── assets/
├── src/
│ ├── entities/
│ ├── systems/
│ ├── states/
│ └── utils/
│
├── agents/
├── docs/
├── tasks/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md

---

# 🚀 Estado actual del proyecto

- [x] Entorno WSL configurado
- [x] Python + Pygame instalado
- [x] Ollama funcionando
- [x] Modelo coder operativo
- [x] Primer ciclo agentic completo funcionando (Architect → Gameplay → Reviewer → Executor)
- [ ] Arquitectura del juego completa
- [ ] Sistema de combate implementado
- [ ] Integración con agentes

---

# 🧠 Objetivo final

Construir un RPG 2D funcional mientras se aprende:

- Arquitectura de software real
- Diseño de sistemas modulares
- Flujo de trabajo con agentes de IA
- Desarrollo iterativo profesional

---

# 📌 Nota final

Este proyecto no busca ser solo un juego, sino un entorno de aprendizaje progresivo donde la complejidad se construye de forma controlada y entendible.

Este proyecto está diseñado para ejecutarse localmente con modelos LLM mediante Ollama, por lo que requiere entorno local (WSL recomendado) y no depende de APIs externas.
