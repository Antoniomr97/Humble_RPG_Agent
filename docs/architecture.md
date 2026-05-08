# 🧱 RPG Agentic 2D — Architecture Overview

Este documento define la arquitectura técnica del proyecto RPG 2D desarrollado en Pygame.

Su objetivo es mantener un diseño modular, escalable y claro desde el inicio, permitiendo crecimiento progresivo del juego sin perder orden ni mantenibilidad.

---

# 🎯 Principios de arquitectura

El proyecto sigue estos principios fundamentales:

- 🧩 Modularidad estricta (cada sistema es independiente)
- 🔁 Separación de lógica y renderizado
- 📦 Código organizado por responsabilidades, no por tipo de archivo
- 🧠 Estado del juego centralizado y controlado
- ⚙️ Sistemas intercambiables y extensibles
- 📉 Evitar dependencias cruzadas entre módulos

---

# 🗂️ Estructura general del proyecto

humble_rpg-project/
│
├── assets/ # Recursos visuales y sonoros
│
├── src/
│ ├── core/ # Motor principal del juego
│ ├── entities/ # Jugador, enemigos, NPCs
│ ├── systems/ # Sistemas del juego (combate, inventario, etc.)
│ ├── states/ # Gestión de pantallas (menu, mapa, combate)
│ ├── ui/ # Interfaz gráfica
│ └── utils/ # Funciones auxiliares
│
├── agents/ # Sistema de agentes (IA de desarrollo)
├── docs/ # Documentación del proyecto
├── tasks/ # Tareas pendientes / roadmap
├── tests/ # Tests futuros
│
├── main.py # Punto de entrada del juego
└── requirements.txt

---

# 🧠 Arquitectura del juego (alto nivel)

El juego se divide en 3 capas principales:

---

## 1. 🎮 Capa de Estados (State Machine)

Responsable de controlar qué pantalla se está mostrando.

Estados principales:

- `CharacterSelectionState`
- `MapState`
- `CombatState`

### Responsabilidades:

- Cambiar entre pantallas
- Mantener flujo del juego
- Delegar lógica a sistemas

---

## 2. ⚙️ Capa de Sistemas (Game Systems)

Contiene la lógica principal del juego.

### Sistemas principales:

#### ⚔️ CombatSystem

- Turnos
- Resolución de acciones
- Daño
- IA enemiga

#### 🧍 CharacterSystem

- Stats del jugador
- Clases
- Progresión básica

#### 🗺️ MapSystem

- Nodos del mapa
- Movimiento entre encuentros
- Generación de combates

#### 🎒 InventorySystem

- Objetos
- Uso en combate

---

## 3. 🎨 Capa de Render/UI

Responsable únicamente de dibujar en pantalla.

- Dibujos de personajes
- Menús
- HUD de combate
- UI del mapa

🚨 IMPORTANTE:  
Esta capa NO contiene lógica del juego.

---

# 🧍 Entidades (Entities)

Las entidades representan objetos del mundo del juego:

- Player
- Enemy
- Boss
- NPC (futuro)

Cada entidad contiene:

- Datos (stats)
- Estado propio
- Referencia mínima a sistemas

---

# 🔁 Flujo del juego

```text
CharacterSelectionState
        ↓
     MapState
        ↓
   CombatState
        ↓
     MapState
        ↓
   (repetición)
        ↓
     Boss Fight
        ↓
     End Game
```
