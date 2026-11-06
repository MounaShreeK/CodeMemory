import os
import httpx


class GitHubClient:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")

    def _headers(self):
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    async def get_repository(self, owner: str, repo: str):
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"

        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=self._headers()
            )

        response.raise_for_status()
        return response.json()

    async def get_commits(self, owner: str, repo: str, limit: int = 20):
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/commits"

        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=self._headers(),
                params={"per_page": limit}
            )

        response.raise_for_status()
        return response.json()

    async def get_pull_requests(self, owner: str, repo: str):
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/pulls"

        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=self._headers(),
                params={
                    "state": "all",
                    "per_page": 20
                }
            )

        response.raise_for_status()
        return response.json()