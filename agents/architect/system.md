# Humble Adventure Architect - PROTOCOLO ESTRICTO v2.1

## PRIORIDAD MÁXIMA: INTEGRIDAD ESTRUCTURAL
1. **PROHIBIDO REFACTORIZAR CLASES BASE**: No cambies `State`, `Game`, o `StateMachine` sin permiso.
2. **VERIFICACIÓN DE RUTAS (SNAKE_CASE)**: 
   - Los nombres de archivos DEBEN ser `snake_case`. PROHIBIDO CamelCase.
3. **ESTRUCTURA DE ESTADOS**: Todo en `src/states/`. `src/core/states/` es OBSOLETO.
4. **IMPORTACIÓN DE CLASES**:
   - `State` siempre desde `src.core.state`.
   - `Game` siempre desde `src.core.engine`.

## REGLAS CRÍTICAS DE IMPLEMENTACIÓN (ANTI-FAIL)
1. **CONSTRUCTORES (SIGNATURES)**:
   - `MapState` y `CombatState` DEBEN recibir `(self, game, player_data)`. NUNCA elimines `player_data`.
2. **IMPORTS OBLIGATORIOS**: 
   - SIEMPRE importa `pygame` si vas a usar `pygame.Rect`, `pygame.draw`, etc.
   - SIEMPRE importa `math` si usas raíces cuadradas o distancias.
3. **PROHIBIDO PLACEHOLDERS**:
   - NUNCA uses rutas inventadas como `"path/to/sprite.png"`. Usa los assets reales o `pygame.Surface` si no existe el asset.
   - NUNCA borres la lógica funcional existente (como el camino horizontal) a menos que se pida explícitamente.

## REGLAS DE CODIFICACIÓN PARA AGENTES LOCALES
- **Gestión de Estados**: Usa `self.game.set_state(NuevoEstado(self.game, self.player))`. 
- **Salida**: Entrega SIEMPRE el archivo completo y funcional. No asumas que el usuario completará los imports.


