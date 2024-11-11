# Sistema de Análisis de Transacciones con Agentes Inteligentes

## Descripción General
Este sistema implementa un enfoque de análisis multi-agente para evaluar transacciones blockchain, utilizando diferentes agentes especializados que trabajan en conjunto para generar un reporte comprehensivo de análisis AML (Anti-Money Laundering).

## Arquitectura de Agentes

### 1. Agentes de Análisis Primario
- **RiskSense**: Evalúa el nivel general de riesgo basado en flags de interacción
- **RegulaGuard**: Analiza el contexto de cumplimiento normativo y sanciones
- **ValueScope**: Examina los riesgos financieros basados en el valor de la transacción
- **ChronoTrace**: Identifica patrones temporales sospechosos
- **ChainIntel**: Proporciona contexto sobre la red blockchain utilizada

### 2. Agentes de Consolidación
- **InsightGen**: Consolida los hallazgos de todos los agentes
- **ReportStructurer**: Estructura el reporte final en un formato estandarizado

## Flujo de Trabajo

1. **Entrada de Datos**
   - Se recibe una transacción en formato `TransactionData`
   - Incluye: valor, timestamp, ID de cadena y flags

2. **Proceso de Análisis**
   ```
   Transacción → Análisis Primario → Consolidación → Reporte Estructurado
   ```

3. **Estructura del Reporte Final**
   - Resumen Ejecutivo
   - Detalles del Análisis
     - Análisis de Riesgo
     - Análisis de Cumplimiento
     - Análisis de Valor
     - Análisis Temporal
     - Análisis de Cadena
   - Conclusiones y Recomendaciones

## Características Principales

- **Análisis Multi-perspectiva**: Cada agente se especializa en un aspecto específico
- **Manejo de Errores**: Sistema robusto con manejo de excepciones
- **Configuración Flexible**: Parámetros ajustables por agente
- **Generación de PDF**: Capacidad de exportar reportes en formato PDF

## Uso
```
Ejemplo de uso básico
transaction = TransactionData(
value=1000000,
timestamp="2024-03-15T14:30:00Z",
chain_id="1",
flags=["USDT_SANCTION", "TORNADO_CASH"]
)
report = analyze_transaction(transaction)
```


## Requisitos

- Python 3.10+
- OpenAI API key
- Dependencias:
  - openai
  - swarm
  - report_generator

## Configuración

1. Configure la variable de entorno para la API key de OpenAI:

```
export OPENAI_API_KEY="your_openai_api_key"
```

2. Instale las dependencias:
```
pip install -r requirements.txt
```

## Notas de Implementación

- Los agentes utilizan el modelo "gpt-4o-mini"
- Cada agente tiene configuraciones específicas de temperatura y tokens
- El sistema incluye límites de intentos (max_turns) para prevenir bucles infinitos

## Contribución

Las contribuciones son bienvenidas. Por favor, asegúrese de:
1. Crear un fork del repositorio
2. Crear una rama para su feature
3. Enviar un pull request con sus cambios

## Licencia

