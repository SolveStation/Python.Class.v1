# Week 7 – Asynchronous Programming, Background Processing & Caching

## Learning Objectives
- Master Python `asyncio` and `async/await` syntax.
- Implement asynchronous HTTP clients and servers (e.g., FastAPI, aiohttp).
- Design background workers using Celery or simple async tasks.
- Apply caching strategies with Redis or an in‑memory cache.
- Evaluate trade‑offs between synchronous and asynchronous architectures.

## Project Overview
Build a **Note Service** that processes note‑related operations asynchronously:
1. **Async API** – expose endpoints that return responses without blocking the event loop.
2. **Background Tasks** – offload heavy work (e.g., sending email notifications, generating thumbnails) to background workers.
3. **Caching** – cache frequently accessed notes in Redis to reduce database hits.
4. **Rate Limiting** – demonstrate basic rate limiting using an async decorator.

The service will remain lightweight (no external DB required for the demo) but will be structured to swap in PostgreSQL (Week 5) and Redis (Week 8) later.

## Core Features
| Feature | Description |
|---------|-------------|
| **Async Views** | FastAPI routes defined with `async def`; use `await` for I/O operations. |
| **Background Workers** | Use `asyncio.create_task` or Celery for long‑running jobs; expose a `/tasks` endpoint to trigger them. |
| **Cache Layer** | Implement a simple Redis cache (or dict fallback) for note retrieval; include `TTL` handling. |
| **Rate Limiter** | Apply an async rate‑limiting decorator to protect endpoints. |
| **Testing Async Code** | Write unit tests with `pytest-asyncio` for async routes and tasks. |
| **Documentation** | Auto‑generated OpenAPI docs with async operation tags. |

## Project Structure
```
Week7/
├─ app.py                 # FastAPI entry point
├─ main.py                # Application factory and router inclusion
├─ routers/
│   ├─ notes.py           # Async note CRUD endpoints
│   └─ tasks.py           # Background task definitions
├─ cache/
│   └─ redis_client.py    # Redis wrapper (fallback to dict)
├─ models/
│   └─ note.py            # Pydantic models
├─ requirements.txt
└─ spec.md                # This document
```

## Quick Start
1. **Create a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**  
   ```bash
   uvicorn app:app --reload
   ```

4. **Explore the API** – open `http://127.0.0.1:8000/docs` for interactive Swagger UI.

5. **Trigger background tasks** – POST to `/tasks/process-notes` to see async job execution.

## Extensibility
- Persist notes to PostgreSQL (Week 5) and cache results in Redis (Week 8).
- Add WebSocket support for real‑time note updates.
- Implement a full Celery worker for production‑grade background processing.
- Write comprehensive integration tests with `pytest-asyncio`.
- Containerize the service and deploy to a cloud provider (Week 10).
