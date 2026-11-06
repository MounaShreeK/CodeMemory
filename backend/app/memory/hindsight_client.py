import os
import asyncio
from hindsight_client import Hindsight


class HindsightClient:
    def __init__(self):
        self.client = Hindsight(
            base_url=os.getenv(
                "HINDSIGHT_BASE_URL",
                "https://api.hindsight.vectorize.io"
            ),
            api_key=os.getenv("HINDSIGHT_API_KEY")
        )

    async def create_bank(self, bank_id: str, name: str):
        return await asyncio.to_thread(
            self.client.create_bank,
            bank_id=bank_id,
            name=name
        )

    async def retain(self, bank_id: str, content: str):
        return await self.client.aretain(
            bank_id=bank_id,
            content=content
        )

    async def recall(self, bank_id: str, query: str):
        return await self.client.arecall(
            bank_id=bank_id,
            query=query
        )

    async def reflect(self, bank_id: str, query: str):
        return await self.client.areflect(
            bank_id=bank_id,
            query=query
        )