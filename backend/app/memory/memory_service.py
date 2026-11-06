from app.memory.hindsight_client import HindsightClient


class MemoryService:
    def __init__(self):
        self.hindsight = HindsightClient()

    def _bank_id(self, repository_id: str) -> str:
        return "repo-" + repository_id.replace("/", "-")

    async def create_memory_bank(self, repository_id: str):
        bank_id = self._bank_id(repository_id)

        return await self.hindsight.create_bank(
            bank_id=bank_id,
            name=f"CodeMemory - {repository_id}"
        )

    async def store_memory(self, repository_id: str, content: str):
        bank_id = self._bank_id(repository_id)

        return await self.hindsight.retain(
            bank_id=bank_id,
            content=content
        )

    async def recall_memories(self, repository_id: str, query: str):
        bank_id = self._bank_id(repository_id)

        return await self.hindsight.recall(
            bank_id=bank_id,
            query=query
        )

    async def reflect(self, repository_id: str, question: str):
        bank_id = self._bank_id(repository_id)

        return await self.hindsight.reflect(
            bank_id=bank_id,
            query=question
        )