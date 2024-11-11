## version python 3.10

from swarm import Swarm, Agent
from openai import OpenAI
from typing import List, Dict
from dataclasses import dataclass
import os
from report_generator import ReportGenerator

# Initialize OpenAI client first, then pass to Swarm
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
swarm = Swarm(client=client)

gpt_model = "gpt-4o-mini"

@dataclass
class TransactionData:
    """Structure for holding transaction data"""
    value: float
    timestamp: str
    chain_id: str
    flags: List[str]

def analyze_risk(context_variables: Dict, transaction: TransactionData) -> str:
    """Analyze risk level based on transaction flags"""
    return f"Risk analysis completed for transaction with {len(transaction.flags)} flags"

def analyze_compliance(context_variables: Dict, transaction: TransactionData) -> str:
    """Analyze compliance implications of transaction flags"""
    return f"Compliance analysis completed for flags: {', '.join(transaction.flags)}"

def analyze_value(context_variables: Dict, transaction: TransactionData) -> str:
    """Analyze transaction value against AML thresholds"""
    return f"Value analysis completed for amount: {transaction.value}"

def analyze_timing(context_variables: Dict, transaction: TransactionData) -> str:
    """Analyze transaction timing patterns"""
    return f"Timing analysis completed for timestamp: {transaction.timestamp}"

def analyze_chain(context_variables: Dict, transaction: TransactionData) -> str:
    """Analyze blockchain network specifics"""
    return f"Chain analysis completed for ID: {transaction.chain_id}"

# Create agents with proper configuration
risk_agent = Agent(
    name="RiskSense",
    model=gpt_model,
    instructions="Interpret the overall risk level based on interaction flags provided.",
    functions=[analyze_risk]
)

compliance_agent = Agent(
    name="RegulaGuard",
    model=gpt_model,
    instructions="Analyze the compliance context based on the sanction flags.",
    functions=[analyze_compliance]
)

value_agent = Agent(
    name="ValueScope",
    model=gpt_model,
    instructions="Evaluate the financial risk of each transaction by analyzing the transaction value.",
    functions=[analyze_value]
)

timing_agent = Agent(
    name="ChronoTrace",
    model=gpt_model,
    instructions="Analyze the timestamp of each transaction and identify suspicious temporal patterns.",
    functions=[analyze_timing]
)

chain_agent = Agent(
    name="ChainIntel",
    model=gpt_model,
    instructions="Identify and provide context on the blockchain network used.",
    functions=[analyze_chain]
)

def generate_insight(analyses: List[str]) -> str:
    """Consolidate analyses into a final report"""
    return "\n".join(analyses)

insight_agent = Agent(
    name="InsightGen",
    model=gpt_model,
    instructions="Consolidate findings from all agents into a cohesive report.",
    functions=[generate_insight]
)

def generate_structured_report(analyses: List[str]) -> str:
    """Genera un reporte estructurado con secciones definidas"""
    return "\n".join(analyses)

reporter_agent = Agent(
    name="ReportStructurer",
    model=gpt_model,
    instructions="""Estructura el reporte final en el siguiente formato:
    # Reporte de Análisis de Transacción
    
    ## Resumen Ejecutivo
    [Resumen breve de los hallazgos principales]
    
    ## Detalles del Análisis
    ### Análisis de Riesgo
    [Detalles del análisis de riesgo]
    
    ### Análisis de Cumplimiento
    [Detalles del análisis de cumplimiento]
    
    ### Análisis de Valor
    [Detalles del análisis de valor]
    
    ### Análisis Temporal
    [Detalles del análisis temporal]
    
    ### Análisis de Cadena
    [Detalles del análisis de cadena]
    
    ## Conclusiones y Recomendaciones
    [Conclusiones finales y acciones recomendadas]
    """,
    functions=[generate_structured_report]
)

#### Orchestration ####

def analyze_transaction(transaction: TransactionData):
    """Run the complete analysis pipeline for a transaction with error handling"""
    context_vars = {"transaction": transaction}
    
    # Initialize messages
    messages = [{"role": "user", "content": "Begin transaction analysis"}]
    
    # Run each agent in sequence with error handling
    agents = [risk_agent, compliance_agent, value_agent, timing_agent, chain_agent, insight_agent, reporter_agent]
    analyses = []
    
    try:
        for agent in agents:
            response = swarm.run(
                agent=agent,
                messages=messages,
                context_variables=context_vars,
                max_turns=3  # Limit turns for each agent
            )
            analyses.append(response.messages[-1]["content"])
            messages = response.messages
    except Exception as e:
        return f"Error during analysis: {str(e)}"
    
    return analyses[-1]  # Return the final structured report

def main():
    # Example transaction data
    sample_transaction = TransactionData(
        value=1000000,
        timestamp="2024-03-15T14:30:00Z",
        chain_id="1",
        flags=["USDT_SANCTION", "TORNADO_CASH"]
    )
    
    # Run analysis
    report = analyze_transaction(sample_transaction)
    print("Generated AML Report:")
    print(report)

# Implementación de create_analysis_input
def create_analysis_input(tx_data: dict) -> TransactionData:
    """Convert raw transaction data into a structured TransactionData instance"""
    return TransactionData(
        value=float(tx_data['value']),
        timestamp=tx_data['timestamp'],
        chain_id=tx_data['chain_id'],
        flags=tx_data.get('flags', [])  # Asume una lista vacía si 'flags' no está presente
    )

def generate_pdf_report(analyses: List[str]) -> str:
    """Convert analysis report to PDF with markdown formatting"""
    report_content = analyses[0]  # Tomamos el reporte consolidado del insight_agent
    generator = ReportGenerator()
    return generator.generate_pdf(report_content)

if __name__ == "__main__":
    main()
