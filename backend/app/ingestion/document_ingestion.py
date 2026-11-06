from app.memory.memory_service import MemoryService


class DocumentIngestion:
    def __init__(self):
        self.memory = MemoryService()

    async def ingest_document(
        self,
        repository_id: str,
        file_path: str,
        content: str
    ):
        memory_content = f"""
Repository: {repository_id}

Document: {file_path}

Content:
{content}
"""

        await self.memory.store_memory(
            repository_id,
            memory_content
        )

        return {
            "repository": repository_id,
            "file": file_path,
            "status": "stored"
        }