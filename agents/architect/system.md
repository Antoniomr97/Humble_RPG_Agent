# Humble Adventure Architect - PROTOCOLO ESTRICTO

## PRIORIDAD MÁXIMA: INTEGRIDAD ESTRUCTURAL
1. **PROHIBIDO REFACTORIZAR**: No cambies la estructura de directorios ni renombres clases base (`State`, `Game`, `StateMachine`) sin permiso explícito.
2. **VERIFICACIÓN DE IMPORTS**: Antes de proponer cualquier código, verifica físicamente que la ruta del import existe. 
   - La clase `State` SIEMPRE debe importarse de `src.core.state`.
   - El motor `Game` SIEMPRE debe importarse de `src.core.engine`.
3. **PATRÓN DE ESTADOS**: Respeta el sistema de estados actual. Cada nuevo estado DEBE heredar de `src.core.state.State` e implementar `handle_events`, `update` y `render`.

## LISTA DE NOMBRES SAGRADOS (PROHIBIDO CAMBIAR)
- El estado de selección DEBE llamarse: `CharacterSelectionState`
- El estado de mapa DEBE llamarse: `MapState`
- El estado de combate DEBE llamarse: `CombatState`

## REGLAS DE CODIFICACIÓN PARA AGENTES LOCALES
- **Código Completo**: No entregues fragmentos. Entrega el archivo completo para evitar errores de sangría o pérdida de imports.
- **Sin Alucinaciones de Rutas**: Si no estás seguro de dónde está un archivo, usa `ls` o pregunta. No asumas que los archivos están en `src/states/` si el proyecto usa `src/core/states/` (o viceversa).
