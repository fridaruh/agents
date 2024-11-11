import openai_swarm as swarm

# Definimos los agentes con sus configuraciones específicas
agents_config = [
    {
        "name": "RiskSense",
        "instruction": "Interpret the overall risk level based on interaction flags provided (e.g., Tornado Cash, USDT/USDC sanctions, OFAC sanction). Prioritize cases with multiple high-risk indicators and assign a final risk rating on a scale of 1 to 100. Output the calculated risk level and a priority recommendation.",
        "temperature": 0.3,
        "max_tokens": 150,
        "frequency_penalty": 0.5,
        "presence_penalty": 0
    },
    {
        "name": "RegulaGuard",
        "instruction": "Analyze the compliance context based on the sanction flags (USDT sanction, USDC sanction, OFAC sanction). For each flagged interaction, provide a brief explanation of its compliance impact and regulatory implications. Emphasize cases that directly violate AML regulations and recommend actions.",
        "temperature": 0.4,
        "max_tokens": 200,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.3
    },
    {
        "name": "ValueScope",
        "instruction": "Evaluate the financial risk of each transaction by analyzing the transaction value. Compare the value against predefined AML thresholds and identify transactions that exceed critical limits. If the transaction value is high, highlight its significance and recommend additional scrutiny.",
        "temperature": 0.3,
        "max_tokens": 100,
        "frequency_penalty": 0.4,
        "presence_penalty": 0
    },
    {
        "name": "ChronoTrace",
        "instruction": "Analyze the timestamp of each transaction and identify any suspicious temporal patterns, such as repeated transactions within a short time frame. Contextualize these findings to indicate whether they suggest unusual activity. Provide a chronological summary if relevant.",
        "temperature": 0.5,
        "max_tokens": 150,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.3
    },
    {
        "name": "ChainIntel",
        "instruction": "Identify and provide context on the blockchain network used (based on Chain ID). Highlight any specific risks associated with transactions on this network and suggest considerations for AML compliance specific to this blockchain.",
        "temperature": 0.4,
        "max_tokens": 120,
        "frequency_penalty": 0.5,
        "presence_penalty": 0
    },
    {
        "name": "InsightGen",
        "instruction": "Consolidate findings from all agents into a cohesive generative report. Summarize the risk level, compliance implications, financial significance, temporal patterns, and blockchain context. Provide a comprehensive yet concise report with recommendations for next steps in compliance actions. Ensure the report is clear and actionable for end-users.",
        "temperature": 0.6,
        "max_tokens": 500,
        "frequency_penalty": 0.6,
        "presence_penalty": 0
    }
]

# Inicializamos Swarm y creamos los agentes
def create_agents():
    agent_instances = []
    for config in agents_config:
        agent = swarm.Agent(
            name=config["name"],
            instruction=config["instruction"],
            temperature=config["temperature"],
            max_tokens=config["max_tokens"],
            frequency_penalty=config["frequency_penalty"],
            presence_penalty=config["presence_penalty"]
        )
        agent_instances.append(agent)
    return agent_instances

# Función para ejecutar los agentes y generar el reporte
def run_swarm():
    agents = create_agents()
    # Ejecuta Swarm con los agentes configurados
    swarm_response = swarm.run(agents)
    return swarm_response

# Ejecutamos el sistema y mostramos el resultado
if __name__ == "__main__":
    report = run_swarm()
    print("Generative AML Report:")
    print(report)
