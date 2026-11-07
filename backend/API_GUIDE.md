# CodeMemory FastAPI guide

## Run locally

Open a terminal in the `backend` directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn main:app --reload
```

Add real Hindsight, GitHub, and LLM credentials to `.env` before using endpoints that depend on those services. Never commit `.env`.

- API base URL: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/api/health`

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/api/health` | API health check |
| POST | `/api/chat` | Ask a question about repository history |
| POST | `/api/repositories/connect` | Verify/connect a GitHub repository and create its memory bank |
| POST | `/api/repositories/{owner}/{repo}/ingest` | Import recent commits into repository memory |
| GET | `/api/repositories/{owner}/{repo}/pull-requests` | List recent pull requests |
| POST | `/api/memory/retain` | Store text in repository memory |
| POST | `/api/memory/recall` | Retrieve relevant repository memories |
| POST | `/api/memory/reflect` | Ask Hindsight to reflect on repository memories |

## Example request bodies

### Chat — `POST /api/chat`

```json
{
  "repository_id": "owner/repository",
  "question": "Why was the authentication flow changed?"
}
```

### Connect repository — `POST /api/repositories/connect`

```json
{
  "owner": "owner",
  "repo": "repository"
}
```

### Retain memory — `POST /api/memory/retain`

```json
{
  "repository_id": "owner/repository",
  "content": "The API uses JWT authentication for protected routes."
}
```

### Recall or reflect — `POST /api/memory/recall` or `/api/memory/reflect`

```json
{
  "repository_id": "owner/repository",
  "query": "authentication implementation"
}
```

## Test

From the `backend` directory:

```powershell
pytest -q
```

The included tests cover the root route, health route, and request validation. Integration calls to GitHub, the LLM provider, and Hindsight require valid credentials and are not invoked by these isolated tests.

## Notes

- The API enables CORS for the local Vite/React development origins by default. Set `CORS_ORIGINS` to your frontend origin(s), separated by commas, when deploying.
- The API currently has no user authentication layer. Do not expose it publicly until authentication and authorization are added.
- GitHub and Hindsight errors are translated into HTTP error responses; service credentials remain server-side in environment variables.
