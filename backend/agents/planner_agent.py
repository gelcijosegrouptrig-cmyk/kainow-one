class PlannerAgent:

    def run(self, prompt):
        return {
            "goal": prompt,
            "tasks": [
                "Criar layout",
                "Criar componentes",
                "Gerar HTML",
                "Gerar CSS",
                "Atualizar preview"
            ]
        }


if __name__ == "__main__":
    agent = PlannerAgent()

    result = agent.run(
        "Criar landing page moderna"
    )

    print(result)
