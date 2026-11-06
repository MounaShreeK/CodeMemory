from app.memory.memory_service import MemoryService


class ChatService:
    def __init__(self):
        self.memory = MemoryService()

    async def answer_question(self, repository_id: str, question: str):
        memories = await self.memory.recall_memories(
            repository_id,
            question
        )

        response = await self.memory.reflect(
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

        answer = getattr(response, "text", str(response))

        return {
            "answer": answer,
            "memories": memory_results
        }