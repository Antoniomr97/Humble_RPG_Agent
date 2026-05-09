# Humble Adventure Architect - PROTOCOLO ESTRICTO v2.0

## PRIORIDAD MÁXIMA: INTEGRIDAD ESTRUCTURAL
1. **PROHIBIDO REFACTORIZAR CLASES BASE**: No cambies `State`, `Game`, o `StateMachine` sin permiso.
2. **VERIFICACIÓN DE RUTAS (SNAKE_CASE)**: 
   - Los nombres de archivos DEBEN ser `snake_case` (ej. `map_state.py`).
   - PROHIBIDO crear archivos CamelCase (ej. `MapState.py`).
   - PROHIBIDO crear archivos con el mismo nombre en diferentes directorios.
3. **ESTRUCTURA DE ESTADOS**:
   - Todos los estados del juego DEBEN estar en `src/states/`.
   - `src/core/states/` es una ruta OBSOLETA. No la uses.
4. **IMPORTACIÓN DE CLASES**:
   - `State` siempre desde `src.core.state`.
   - `Game` siempre desde `src.core.engine`.

## LISTA DE NOMBRES SAGRADOS
- Estado de selección: `CharacterSelectionState` (en `src/states/character_selection.py`)
- Estado de mapa: `MapState` (en `src/states/map_state.py`)
- Estado de combate: `CombatState` (en `src/states/combat_state.py`)

## REGLAS DE CODIFICACIÓN PARA AGENTES LOCALES
- **Gestión de Estados**: Usa `self.game.set_state(NuevoEstado(self.game, ...))`. No uses `self.manager` ni Enums para transiciones de estado.
- **Sin Alucinaciones de Filenames**: Nunca uses un bloque de código como nombre de archivo. Verifica siempre el path antes de escribir.
- **Limpieza**: Si detectas archivos duplicados o con nombres incorrectos (CamelCase), bórralos o informa inmediatamente.

