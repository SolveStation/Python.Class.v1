# Week 10 – Final Capstone Project

## Vision
Build an all‑in‑one **Note‑Taking Platform** that synthesizes everything learned from Weeks 4‑9:

- **Web Servers & APIs** (Flask) – RESTful CRUD for notes.  
- **Databases** (Django + PostgreSQL) – persistent storage with migrations.  
- **Authentication & Authorization** (JWT) – secure user registration, login, and role‑based access.  
- **Asynchronous Programming** (FastAPI) – async endpoints and background workers.  
- **Background Processing & Caching** – Redis‑backed cache and async task queue.  
- **Testing & Deployment** – comprehensive test suite, CI/CD pipelines, Dockerized deployment.

The platform will expose a unified API (`/api/notes`) that serves notes from a PostgreSQL database, protects them with JWT authentication, caches frequent reads, and off‑loads heavy work to background tasks. A Swagger UI will document all endpoints.

## Learning Objectives
- Integrate multiple frameworks (Flask, Django, FastAPI) within a single project.  
- Design a cohesive database schema and handle migrations across frameworks.  
- Implement end‑to‑end security (registration, login, token refresh, role checks).  
- Architect asynchronous processing pipelines with caching layers.  
- Write a full test pyramid (unit → integration → end‑to‑end).  
- Set up CI/CD with GitHub Actions, build Docker images, and deploy to a cloud VM.  
- Document the entire system (API, architecture, deployment) for future maintenance.

## Core Features
| Feature | Description |
|---------|-------------|
| **Unified Note API** | Single `/api/notes` namespace that internally routes to the most appropriate backend (Flask for simple ops, Django for DB‑heavy ops, FastAPI for async ops). |
| **User Management** | Registration, login, password reset, and JWT issuance/refresh. Roles: `user` (default) and `admin` (extra privileges). |
| **Database Layer** | Django ORM models for `Note` and `User`; PostgreSQL as the source of truth. |
| **Async Services** | FastAPI routes for non‑blocking operations; background tasks (e.g., email notifications) executed via `asyncio` or Celery. |
| **Cache** | Redis cache for read‑heavy note retrieval; TTL‑based invalidation on write. |
| **Testing Suite** | - Unit tests for models and utilities.<br>- Integration tests for API endpoints with token auth.<br>- End‑to‑end tests that simulate a full user flow (register → create note → share note). |
| **CI/CD** | GitHub Actions workflow that lints, type‑checks, runs tests, builds Docker images, and pushes to a container registry. |
| **Docker & Deployment** | Multi‑stage Dockerfile for the API, `docker‑compose.yml` to spin up API, PostgreSQL, Redis, and optional Celery worker; deployment instructions for Render/Heroku/AWS. |
| **Documentation** | Auto‑generated OpenAPI docs, architecture diagram, and a `README.md` that explains how to run, test, and deploy the system. |

## Project Structure
```
Week10/
├─ app/
│   ├─ __init__.py
│   ├─ models.py          # Django models (Note, User)
│   ├─ schemas.py         # Pydantic schemas (FastAPI)
│   ├─ auth.py            # JWT utilities, password hashing
│   ├─ cache.py           # Redis wrapper
│   ├─ tasks.py           # Background tasks
│   ├─ routes/
│   │   ├─ api.py         # Main API router (FastAPI)
│   │   ├─ django_views.py# Django viewset (CRUD)
│   │   └─ flask_routes.py# Flask blueprint (simple routes)
│   └─ main.py            # FastAPI app factory
├─ tests/
│   ├─ unit/
│   ├─ integration/
│   └─ e2e/
├─ docker/
│   ├─ Dockerfile.api
│   └─ docker-compose.yml
├─ .github/
│   └─ workflows/
│       └─ ci.yml
├─ requirements.txt
├─ requirements.test.txt
├─ requirements.extra.txt   # optional extras (redis, celery)
├─ spec.md                  # This document
├─ README.md
└─ .env.example
```

## Quick Start
1. **Clone the repository** (or copy the Week 4‑9 folders into `Week10`).  
2. **Create a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. **Install core dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Install test dependencies**  
   ```bash
   pip install -r requirements.test.txt
   ```
5. **Set up environment variables** (copy `.env.example` to `.env` and fill in values).  
6. **Run migrations** (Django)  
   ```bash
   python manage.py migrate
   ```
7. **Start the stack with Docker Compose**  
   ```bash
   docker compose up --build
   ```
8. **Access the API** at `http://localhost:8000` and the Swagger UI at `http://localhost:8000/docs`.  
9. **Run the test suite**  
   ```bash
   pytest --cov=.
   ```

## Extensibility
- Add WebSocket notifications for real‑time updates.  
- Implement a full Celery worker for production‑grade background jobs.  
- Integrate monitoring (Prometheus/Grafana) and logging (ELK stack).  
- Set up automated deployment to a Kubernetes cluster.  
- Expand the test suite with property‑based testing (`hypothesis`).  

## Evaluation Criteria
- **Functionality**: All CRUD operations work under authenticated sessions.  
- **Performance**: Cache hit rate > 70 % in load testing; async tasks complete within SLA.  
- **Reliability**: Test coverage ≥ 80 %; CI pipeline passes on every push.  
- **Security**: No hard‑coded secrets; JWT expiration and refresh handled correctly.  
- **Documentation**: Clear `README`, architecture diagram, and API docs for future developers.
