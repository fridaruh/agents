from swarm import Swarm, Agent
from openai import OpenAI
from typing import Dict
import os
from report_generator import ReportGenerator
from agent_config import (
    risk_agent,
    compliance_agent,
    value_agent,
    timing_agent,
    chain_agent
)
from analysis_functions import TransactionData

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
swarm = Swarm(client=client)

def convert_db_record_to_transaction_data(db_record: Dict) -> TransactionData:
    """Convierte el registro de la base de datos a TransactionData"""
    return TransactionData(
        id=db_record['id'],
        contract_address=db_record['contract_address'],
        event_name=db_record['event_name'],
        from_address=db_record['from_address'],
        transaction_hash=db_record['transaction_hash'],
        block_number=db_record['block_number']
    )
