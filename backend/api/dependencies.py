"""Dependency providers for API route handlers."""

from app.agents.agent_orchestrator import AgentOrchestrator
from app.integrations.github.github_client import GitHubClient
from app.memory.memory_service import MemoryService
from app.services.repository_service import RepositoryService


def get_agent_orchestrator() -> AgentOrchestrator:
    return AgentOrchestrator()


def get_github_client() -> GitHubClient:
    return GitHubClient()


def get_memory_service() -> MemoryService:
    return MemoryService()


def get_repository_service() -> RepositoryService:
    return RepositoryService()
