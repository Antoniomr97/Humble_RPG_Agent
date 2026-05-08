# 🤖 Agent System — RPG Agentic 2D

Este sistema define cómo los agentes locales (basados en LLMs como Ollama) colaboran en el desarrollo del proyecto.

---

# 🧠 Arquitectura de agentes

El sistema se divide en 3 agentes principales:

---

## 🏗️ Architect Agent

Responsable de:

- Diseñar arquitectura del código
- Definir sistemas y módulos
- Proponer refactors estructurales
- Mantener coherencia global

📂 Input:

- docs/\*.md
- estructura del repo

📤 Output:

- propuestas de arquitectura
- cambios estructurales
- diseño de sistemas

---

## 🎮 Gameplay Agent

Responsable de:

- Implementar mecánicas del juego
- Escribir lógica de sistemas
- Crear entidades y comportamiento
- Implementar features jugables

📂 Input:

- combat_system.md
- game_design.md
- architecture.md

📤 Output:

- código Python
- sistemas funcionales
- nuevas mecánicas

---

## 🔍 Reviewer Agent

Responsable de:

- Revisar código generado
- Detectar errores lógicos
- Proponer mejoras
- Validar coherencia con arquitectura

📂 Input:

- código generado
- logs de ejecución

📤 Output:

- feedback estructurado
- correcciones
- mejoras

---

# 🔁 Flujo de trabajo

```text
Architect → Gameplay → Reviewer → Gameplay (iteración)
```
