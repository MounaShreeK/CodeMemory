import logging
import json

import httpx
from fastapi import APIRouter, Depends, HTTPException

from app.agents.agent_orchestrator import AgentOrchestrator
from api.dependencies import get_agent_orchestrator
from schemas.api_schemas import ChatRequest, ChatResponse

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse, summary="Ask a question about a repository")
async def chat(
    payload: ChatRequest,
    agent: AgentOrchestrator = Depends(get_agent_orchestrator),
):
    try:
        result = await agent.process(payload.repository_id, payload.question)
        answer = result.get("answer", "")
        if isinstance(answer, dict):
            answer = (
                answer.get("text")
                or answer.get("answer")
                or answer.get("content")
                or answer.get("response")
                or json.dumps(answer, ensure_ascii=False)
            )
        return ChatResponse(
            answer=str(answer),
            context=result.get("context", []),
            decision=result.get("decision", {}),
        )
    except httpx.HTTPStatusError as exc:
        logger.exception("Upstream service rejected the chat request")
        raise HTTPException(
            status_code=502,
            detail=f"An upstream service returned HTTP {exc.response.status_code}.",
        ) from exc
    except (httpx.RequestError, RuntimeError) as exc:
        logger.exception("Chat request could not reach a required service")
        raise HTTPException(status_code=503, detail="A required service is unavailable.") from exc
    except Exception as exc:
        logger.exception("Unexpected chat error")
        raise HTTPException(status_code=500, detail="Unable to process the chat request.") from exc
