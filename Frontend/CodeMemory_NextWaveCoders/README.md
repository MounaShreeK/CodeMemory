# CodeMemory — NextWaveCoders

**Team workspace branding: NextWaveCoders**

**AI-Powered Code Archaeology and Developer Knowledge Preservation**

This repository contains the CodeMemory frontend in `frontend/`. The structure follows the folder layout supplied by the team. The workspace and sidebar use **NextWaveCoders** branding. Both the left workspace sidebar and the main content panel have independent vertical scrolling on desktop.

## Run frontend
```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```
Open the local URL printed by Vite (normally `http://localhost:5173`).

## Frontend pages
- `/` — Home / product introduction
- `/dashboard` — workspace overview
- `/chat` — ask questions about code history and retained knowledge
- `/repositories` — connect and sync repositories
- `/memories` — search retained decisions, fixes, patterns and cautions
- `/settings` — backend and integration status

## API integration

This ZIP contains the frontend project only. A separate backend service is required for live repository syncing, chat, and Hindsight memory operations. The included demo mode uses sample data.
Default API base: `http://localhost:8000/api/v1`

Expected endpoints:
- `GET /health`
- `GET /dashboard/summary`
- `GET /repositories`
- `POST /repositories/connect` with `{ "repository_url": "..." }`
- `POST /repositories/{repository_id}/sync`
- `GET /memories`
- `POST /chat` with `{ "message": "...", "repository_id": null }`

`VITE_DEMO_MODE=true` supplies sample data when the backend is unavailable. Set it to `false` once backend endpoints are implemented and tested.

## Hindsight and Band AI
Hindsight Memory is a backend integration: Retain stores useful development context, Recall retrieves relevant memories, and Reflect synthesizes context. The UI is prepared to display memory evidence and citations; the actual memory operations must run on the backend.

Band AI Desktop is treated as an external hackathon-required tool/workflow, not a browser-side React dependency. Follow the event's exact requirements and do not expose its credentials in frontend code.

Never commit `.env`, API keys, GitHub tokens, or provider secrets.
