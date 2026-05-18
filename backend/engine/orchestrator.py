from agents.planner_agent import PlannerAgent
from agents.code_agent import CodeAgent


class Orchestrator:

    def __init__(self):
        self.planner = PlannerAgent()
        self.coder = CodeAgent()

    def execute(self, prompt):

        plan = self.planner.run(prompt)

        print("PLANO:")
        print(plan)

        html = self.coder.generate(prompt)

        return {
            "plan": plan,
            "html": html
        }


if __name__ == "__main__":

    orchestrator = Orchestrator()

    result = orchestrator.execute(
        "Landing page moderna da Nike"
    )

    print(result)
