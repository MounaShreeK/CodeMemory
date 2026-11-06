from app.memory.memory_service import MemoryService
from app.integrations.llm.llm_client import LLMClient
from app.integrations.llm.prompt_templates import MEMORY_QUESTION_PROMPT


class ChatService:
    def __init__(self):
        self.memory = MemoryService()
        self.llm = LLMClient()

    async def answer_question(self, repository_id: str, question: str):

        # Retrieve relevant memories from Hindsight
        memories = await self.memory.recall_memories(
            repository_id,
            question
        )

        memory_results = []

        results = getattr(memories, "results", [])

        for memory in results:
            memory_results.append({
                "type": getattr(memory, "type", "memory"),
                "text": getattr(memory, "text", str(memory))
            })

        # Prepare memories for the LLM
        memory_text = "\n".join(
            item["text"] for item in memory_results
        )

        prompt = MEMORY_QUESTION_PROMPT.format(
            memories=memory_text,
            question=question
        )

        # Generate answer using LLM
        response = await self.llm.generate(prompt)

        return {
            "answer": response["text"],
            "memories": memory_results
        }