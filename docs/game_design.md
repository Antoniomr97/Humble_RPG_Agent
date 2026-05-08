# 🎮 Game Design Document — RPG Agentic 2D

Este documento define el diseño general del juego RPG 2D por turnos desarrollado en Pygame.

Su objetivo es establecer las reglas, sistemas y estructura jugable del proyecto antes de su implementación completa.

---

# 🧭 Visión del juego

El juego es un RPG 2D por turnos en el que el jugador avanza a través de un mapa lineal, enfrentando combates aleatorios hasta llegar a un jefe final.

El enfoque principal es:

- Progresión simple pero significativa
- Combate por turnos estratégico básico
- Exploración lineal tipo “ruta de encuentros”
- Escalabilidad hacia sistemas más complejos

---

# 🧍 Personajes jugables

El jugador puede elegir entre 3 clases:

## 🗡️ Guerrero

- Alta defensa
- Vida elevada
- Daño medio
- Baja velocidad

## 🗡️ Pícaro

- Alta velocidad
- Daño crítico potencial alto (futuro)
- Vida baja
- Defensa media

## 🔮 Mago

- Alto daño
- Vida baja
- Defensa baja
- Potencial de habilidades mágicas (futuro)

---

# 📊 Sistema de estadísticas

Cada entidad tendrá:

- HP (vida)
- ATK (ataque)
- DEF (defensa)
- SPD (velocidad)

---

## 🧮 Valores base sugeridos

### Guerrero

- HP: 120
- ATK: 15
- DEF: 10
- SPD: 5

### Pícaro

- HP: 80
- ATK: 18
- DEF: 6
- SPD: 12

### Mago

- HP: 70
- ATK: 22
- DEF: 4
- SPD: 8

---

# ⚔️ Sistema de combate

El combate es por turnos alternos:

```text id="combatloop"
Jugador → Enemigo → Jugador → Enemigo
```
