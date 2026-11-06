from app.agents.context_agent import ContextAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.code_memory_agent import CodeMemoryAgent


class AgentOrchestrator:
    def __init__(self):
        self.context_agent = ContextAgent()
        self.decision_agent = DecisionAgent()
        self.code_memory_agent = CodeMemoryAgent()

    async def process(
        self,
        repository_id: str,
        question: str
    ):
        context_result = await self.context_agent.get_context(
            repository_id,
            question
        )

        decision = await self.decision_agent.analyze(
            question,
            context_result["context"]
        )

        if decision["decision"] == "insufficient_context":
            return {
                "answer": "I could not find enough repository history to answer this question.",
                "context": [],
                "decision": decision
            }

        answer = await self.code_memory_agent.answer(
            repository_id,
            question
        )

        return {
            "answer": answer["answer"],
            "context": context_result["context"],
            "decision": decision
        }