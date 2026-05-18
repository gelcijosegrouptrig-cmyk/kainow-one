class CodeAgent:

    def generate(self, prompt):

        html = f"""
        <div>
            <h1>{prompt}</h1>
        </div>
        """

        return html


if __name__ == "__main__":
    agent = CodeAgent()

    print(
        agent.generate(
            "Landing Page Nike"
        )
    )
