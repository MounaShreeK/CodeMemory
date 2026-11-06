from app.integrations.github.github_client import GitHubClient
from app.memory.memory_service import MemoryService


class RepositoryService:
    def __init__(self):
        self.github = GitHubClient()
        self.memory = MemoryService()

    async def connect_repository(self, owner: str, repo: str):
        repository = await self.github.get_repository(owner, repo)

        repository_id = f"{owner}/{repo}"

        try:
            await self.memory.create_memory_bank(repository_id)
        except Exception:
            pass

        return {
            "id": repository_id,
            "name": repository["name"],
            "full_name": repository["full_name"],
            "description": repository.get("description"),
            "url": repository["html_url"]
        }

    async def ingest_commits(self, owner: str, repo: str):
        repository_id = f"{owner}/{repo}"

        commits = await self.github.get_commits(owner, repo)

        processed = 0

        for commit in commits:
            commit_data = commit["commit"]

            content = f"""
Repository: {repository_id}
Commit SHA: {commit["sha"]}
Author: {commit_data["author"]["name"]}
Date: {commit_data["author"]["date"]}

Commit message:
{commit_data["message"]}
"""

            await self.memory.store_memory(
                repository_id,
                content
            )

            processed += 1

        return {
            "repository": repository_id,
            "commits_processed": processed
        }