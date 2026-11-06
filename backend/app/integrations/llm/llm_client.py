import os
import httpx


class LLMClient:
    def __init__(self):
        self.api_url = os.getenv("LLM_API_URL")
        self.api_key = os.getenv("LLM_API_KEY")
        self.model = os.getenv("LLM_MODEL", "default")

    async def generate(self, prompt: str):
        if not self.api_url or not self.api_key:
            return {
                "text": "LLM configuration is not available.",
                "status": "not_configured"
            }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "prompt": prompt
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.api_url,
                headers=headers,
                json=payload
            )

        response.raise_for_status()

        return {
            "text": response.json(),
            "status": "success"
        }