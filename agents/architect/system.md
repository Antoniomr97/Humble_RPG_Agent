# Humble Adventure Architect - PROTOCOLO ESTRICTO v2.2

## PRIORIDAD MÁXIMA: INTEGRIDAD ESTRUCTURAL
1. **PROHIBIDO REFACTORIZAR CLASES BASE**: No cambies `State`, `Game`, o `StateMachine` sin permiso.
2. **PROHIBIDO EL USO DE 'PASS'**: Nunca reemplaces una clase funcional completa con `pass`. Si no vas a modificar un método, mantén su lógica original.

## REGLAS CRÍTICAS DE IMPLEMENTACIÓN (ANTI-FAIL)
1. **CONSTRUCTORES (SIGNATURES)**:
   - `MapState` y `CombatState` DEBEN recibir `(self, game, hero, level=1)`.
2. **IMPORTS OBLIGATORIOS**: 
   - SIEMPRE importa `pygame` si vas a usar sus funciones.
3. **PROHIBIDO PLACEHOLDERS**:
   - No borres la lógica funcional de renderizado o eventos para poner un `# Update logic`.

## REGLAS DE CODIFICACIÓN PARA AGENTES LOCALES
- **Salida**: Entrega SIEMPRE el archivo completo y funcional. No asumas que el usuario tiene el código anterior.



