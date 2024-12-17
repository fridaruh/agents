from swarm import Agent
from analysis_functions import (
    analyze_risk,
    analyze_compliance,
    analyze_value,
    analyze_timing,
    analyze_chain
)

# Modelo GPT a utilizar
gpt_model = "gpt-4o-mini"

# Configuración de agentes
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

compliance_agent = Agent(
    name="RegulaGuard",
    model=gpt_model,
    temperature=0.4,
    max_tokens=200,
    frequency_penalty=0.5,
    presence_penalty=0.3,
    instructions="Analyze the compliance context based on the sanction flags.",
    functions=[analyze_compliance]
)

value_agent = Agent(
    name="ValueScope",
    model=gpt_model,
    temperature=0.3,
    max_tokens=100,
    frequency_penalty=0.4,
    presence_penalty=0.0,
    instructions="Evaluate the financial risk of each transaction by analyzing the transaction value.",
    functions=[analyze_value]
)

timing_agent = Agent(
    name="ChronoTrace",
    model=gpt_model,
    temperature=0.5,
    max_tokens=150,
    frequency_penalty=0.5,
    presence_penalty=0.3,
    instructions="Analyze the timestamp of each transaction and identify suspicious temporal patterns.",
    functions=[analyze_timing]
)

chain_agent = Agent(
    name="ChainIntel",
    model=gpt_model,
    temperature=0.4,
    max_tokens=120,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    instructions="Identify and provide context on the blockchain network used.",
    functions=[analyze_chain]
)