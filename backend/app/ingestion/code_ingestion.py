from app.memory.memory_service import MemoryService


class CodeIngestion:
    def __init__(self):
        self.memory = MemoryService()

    async def ingest_code(
        self,
        repository_id: str,
        file_path: str,
        code: str
    ):
        content = f"""
Repository: {repository_id}

File: {file_path}

Code:
{code}
"""

        await self.memory.store_memory(
            repository_id,
            content
        )

        return {
            "repository": repository_id,
            "file": file_path,
            "status": "stored"
        }