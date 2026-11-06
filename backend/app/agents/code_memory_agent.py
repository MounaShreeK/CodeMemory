from app.memory.memory_service import MemoryService
from app.integrations.llm.llm_client import LLMClient
from app.integrations.llm.prompt_templates import MEMORY_QUESTION_PROMPT


class CodeMemoryAgent:
    def __init__(self):
        self.memory = MemoryService()
        self.llm = LLMClient()

    async def answer(
        self,
        repository_id: str,
        question: str
    ):
        memories = await self.memory.recall_memories(
            repository_id,
            question
        )

        results = getattr(memories, "results", [])

        memory_text = "\n".join(
            getattr(memory, "text", str(memory))
            for memory in results
        )

        prompt = MEMORY_QUESTION_PROMPT.format(
            memories=memory_text,
            question=question
        )

        response = await self.llm.generate(prompt)

        return {
            "answer": response["text"],
            "memories": memory_text
        }