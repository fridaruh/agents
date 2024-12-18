from swarm import Swarm, Agent
from openai import OpenAI
from typing import Dict
from dataclasses import dataclass
from typing import List
import os
from conexion_datos import get_record_by_address
from datetime import datetime

### pip3 install git+https://github.com/openai/swarm.git
### pip3 install openai==1.55.3

client = Swarm()
gpt_model = "gpt-4o-mini"
fecha_generacion = str(datetime.now())

@dataclass
class TransactionData:
    """Structure for holding blockchain transaction data"""
    id: int
    contract_address: str
    event_name: str
    from_address: str
    transaction_hash: str
    block_number: int
    value: float = 0.0
    timestamp: str = ""
    chain_id: str = "1"
    flags: List[str] = None
    tornado_cash: int = 0

def analyze_risk(context_variables: Dict, transaction: TransactionData) -> str:
    """Analyze risk level based on transaction data"""
    risk_factors = [
        f"Contract interaction with {transaction.contract_address}",
        f"Event type: {transaction.event_name}",
        f"Tornado Cash: Found in block {transaction.block_number}" if transaction.tornado_cash == 1 else ""
    ]
    return f"Risk analysis completed for transaction {transaction.transaction_hash}:\n" + "\n".join(risk_factors)

risk_agent = Agent(
    name="RiskSense",
    model=gpt_model,
    temperature=0.3,
    max_tokens=150,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    instructions="Interpret the overall risk level based on interaction flags provided.",
    functions=[analyze_risk]
)

results_agent = Agent(
    name="Summarize",
    model=gpt_model,
    temperature=0.4,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    instructions="""
    You are a blockchain transaction analysis agent. Your task is to generate a detailed risk analysis report in Spanish based on the provided transaction data. Follow this specific format and guidelines:

Always start with a header section containing:
Wallet address as "Wallet: {from_address}"
Risk level assessment based on detected flags


If Tornado Cash interaction is detected ({tornado_cash} > 0):
Set risk level as "Alto"
Include a "Resumen de Interacciones y Sanciones" section
Highlight Tornado Cash interaction as a significant money laundering risk
Mention WhirlCheck as detection source


Always conclude with "Recomendaciones":

Set review priority based on risk level
Suggest specific actions based on findings
For high-risk cases, recommend monitoring and regulatory notification
For Tornado Cash interactions, recommend transaction blocking

Format requirements:

Use bullet points (•) for main sections
Use asterisks (*) for headers
Bold section titles using **
Maintain consistent indentation
Keep language formal but clear
Include specific transaction details when available

The report should be actionable, professional, and focus on risk assessment and compliance implications of the analyzed transactions.
"""
)

def analyze_wallet(from_address: str):
    """Función para analizar una wallet específica"""
    try:
        resultado = get_record_by_address('tornado', from_address)
        
        if resultado:
            # Convertir el resultado a un formato que el agente pueda procesar
            response = client.run(
                agent=results_agent,
                messages=[{
                    "role": "user", 
                    "content": f"Registro encontrado en la tabla tornado cash: {resultado}"
                }]
            )
            
            return response.messages[-1]["content"]
        else:
            return "No se encontró el registro en la tabla tornado cash"
            
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"

