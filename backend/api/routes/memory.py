import logging

import httpx
from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_memory_service
from app.memory.memory_service import MemoryService
from app.schemas.api_schemas import MemoryQueryRequest, MemoryRetainRequest

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/memory", tags=["Memory"])


def _to_jsonable(value):
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, list):
        return [_to_jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _to_jsonable(item) for key, item in value.items()}
    if hasattr(value, "model_dump"):
        return value.model_dump()
    if hasattr(value, "dict"):
        return value.dict()
    if hasattr(value, "__dict__"):
        return {key: _to_jsonable(item) for key, item in vars(value).items() if not key.startswith("_")}
    return str(value)


def _service_error(exc: Exception) -> HTTPException:
    if isinstance(exc, (httpx.RequestError, httpx.HTTPStatusError)):
        return HTTPException(status_code=503, detail="The Hindsight memory service is unavailable or rejected the request.")
    return HTTPException(status_code=500, detail="Memory operation failed.")


@router.post("/retain", summary="Store information in repository memory")
async def retain_memory(
    payload: MemoryRetainRequest,
    memory: MemoryService = Depends(get_memory_service),
):
    try:
        result = await memory.store_memory(payload.repository_id, payload.content)
        return {"status": "stored", "repository": payload.repository_id, "result": _to_jsonable(result)}
    except Exception as exc:
        logger.exception("Could not retain repository memory")
        raise _service_error(exc) from exc


@router.post("/recall", summary="Search repository memories")
async def recall_memory(
    payload: MemoryQueryRequest,
    memory: MemoryService = Depends(get_memory_service),
):
    try:
        result = await memory.recall_memories(payload.repository_id, payload.query)
        return {"repository": payload.repository_id, "memories": _to_jsonable(result)}
    except Exception as exc:
        logger.exception("Could not recall repository memory")
        raise _service_error(exc) from exc


@router.post("/reflect", summary="Generate a reflection from repository memories")
async def reflect_memory(
    payload: MemoryQueryRequest,
    memory: MemoryService = Depends(get_memory_service),
):
    try:
        result = await memory.reflect(payload.repository_id, payload.query)
        return {"repository": payload.repository_id, "reflection": _to_jsonable(result)}
    except Exception as exc:
        logger.exception("Could not reflect on repository memory")
        raise _service_error(exc) from exc
