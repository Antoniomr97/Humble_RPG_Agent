# ⚔️ Combat System — RPG Agentic 2D

Este documento define el sistema de combate del RPG 2D desarrollado en Pygame.

El objetivo es establecer una base clara, extensible y predecible para el combate por turnos, priorizando primero la lógica sobre la representación visual.

---

# 🎯 Objetivo del sistema

El sistema de combate debe:

- Gestionar combates por turnos
- Resolver acciones entre jugador y enemigo
- Aplicar daño y efectos
- Determinar victoria o derrota
- Mantener independencia del sistema de renderizado

---

# 🧠 Filosofía del combate

El combate está diseñado bajo estos principios:

- ⚖️ Simplicidad inicial (MVP jugable)
- 🔁 Turnos alternos claros
- 📦 Lógica desacoplada de UI
- 🧩 Extensible a futuro (skills, buffs, IA avanzada)
- 🎮 Legible y predecible para el jugador

---

# 🔁 Flujo general del combate

```text id="combatflow"
Start Combat
    ↓
Player Turn
    ↓
Enemy Turn
    ↓
Check Win Condition
    ↓
Repeat until end
```
