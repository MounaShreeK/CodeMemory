from app.memory.memory_service import MemoryService


class ContextAgent:
    def __init__(self):
        self.memory = MemoryService()

    async def get_context(
        self,
        repository_id: str,
        question: str
    ):
        memories = await self.memory.recall_memories(
            repository_id,
            question
        )

        results = getattr(memories, "results", [])

        context = []

        for memory in results:
            context.append(
                getattr(memory, "text", str(memory))
            )

        return {
            "repository": repository_id,
            "question": question,
            "context": context
        }