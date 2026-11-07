import logging

import httpx
from fastapi import APIRouter, Depends, HTTPException, Path

from api.dependencies import get_github_client, get_repository_service
from app.integrations.github.github_client import GitHubClient
from schemas.api_schemas import RepositoryConnectRequest
from app.services.repository_service import RepositoryService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/repositories", tags=["Repositories"])


def _upstream_error(exc: Exception) -> HTTPException:
    if isinstance(exc, httpx.HTTPStatusError):
        status = exc.response.status_code
        if status == 404:
            return HTTPException(status_code=404, detail="GitHub repository was not found.")
        if status == 401 or status == 403:
            return HTTPException(status_code=502, detail="GitHub rejected the request. Check token permissions or rate limits.")
        return HTTPException(status_code=502, detail=f"GitHub returned HTTP {status}.")
    if isinstance(exc, httpx.RequestError):
        return HTTPException(status_code=503, detail="GitHub could not be reached.")
    return HTTPException(status_code=500, detail="Repository operation failed.")


@router.post("/connect", summary="Connect a GitHub repository")
async def connect_repository(
    payload: RepositoryConnectRequest,
    service: RepositoryService = Depends(get_repository_service),
):
    try:
        return await service.connect_repository(payload.owner, payload.repo)
    except Exception as exc:
        logger.exception("Could not connect repository %s/%s", payload.owner, payload.repo)
        raise _upstream_error(exc) from exc


@router.post("/{owner}/{repo}/ingest", summary="Import recent GitHub commits into repository memory")
async def ingest_repository_commits(
    owner: str = Path(..., min_length=1, max_length=100),
    repo: str = Path(..., min_length=1, max_length=100),
    service: RepositoryService = Depends(get_repository_service),
):
    try:
        return await service.ingest_commits(owner, repo)
    except Exception as exc:
        logger.exception("Could not ingest commits for %s/%s", owner, repo)
        raise _upstream_error(exc) from exc


@router.get("/{owner}/{repo}/pull-requests", summary="List repository pull requests")
async def list_pull_requests(
    owner: str = Path(..., min_length=1, max_length=100),
    repo: str = Path(..., min_length=1, max_length=100),
    github: GitHubClient = Depends(get_github_client),
):
    try:
        pull_requests = await github.get_pull_requests(owner, repo)
        return {
            "repository": f"{owner}/{repo}",
            "count": len(pull_requests),
            "pull_requests": [
                {
                    "number": item.get("number"),
                    "title": item.get("title"),
                    "state": item.get("state"),
                    "url": item.get("html_url"),
                    "created_at": item.get("created_at"),
                    "updated_at": item.get("updated_at"),
                }
                for item in pull_requests
            ],
        }
    except Exception as exc:
        logger.exception("Could not list pull requests for %s/%s", owner, repo)
        raise _upstream_error(exc) from exc
