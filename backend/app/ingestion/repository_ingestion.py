from app.integrations.github.github_client import GitHubClient
from app.memory.memory_service import MemoryService


class RepositoryIngestion:
    def __init__(self):
        self.github = GitHubClient()
        self.memory = MemoryService()

    async def ingest_repository(self, owner: str, repo: str):
        repository_id = f"{owner}/{repo}"

        # Get repository information
        repository = await self.github.get_repository(owner, repo)

        # Create Hindsight memory bank
        try:
            await self.memory.create_memory_bank(repository_id)
        except Exception:
            pass

        # Get commits
        commits = await self.github.get_commits(owner, repo)

        processed = 0

        # Store commit history in Hindsight
        for commit in commits:
            commit_data = commit["commit"]

            content = f"""
Repository: {repository_id}

Commit SHA: {commit["sha"]}

Author: {commit_data["author"]["name"]}

Date: {commit_data["author"]["date"]}

Commit Message:
{commit_data["message"]}
"""

            await self.memory.store_memory(
                repository_id,
                content
            )

            processed += 1

        return {
            "repository": repository_id,
            "name": repository["name"],
            "commits_processed": processed
        }