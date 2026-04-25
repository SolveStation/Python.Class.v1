# Week 9 – Testing & Deployment

## Learning Objectives
- Write unit, integration, and end‑to‑end tests for Python applications.
- Master pytest fixtures, parameterization, and async testing (`pytest-asyncio`).
- Implement CI/CD pipelines with GitHub Actions or GitLab CI.
- Containerize applications with Docker and Docker Compose.
- Deploy to cloud platforms (AWS, GCP, Azure) or services like Heroku/Render.
- Perform static code analysis, linting, and security scanning.

## Project Overview
Consolidate the code written in Weeks 4‑8 into a unified **Full‑Stack API** that:
1. Exposes all CRUD endpoints for notes (Flask, Django, FastAPI versions).
2. Includes authentication (JWT) and role‑based access control.
3. Implements asynchronous background tasks and caching.
4. Provides comprehensive test coverage (>80%).
5. Is containerized and deployable to a cloud VM or managed service.

## Core Features
| Feature | Description |
|---------|-------------|
| **Test Suite** | - Unit tests for models, serializers, and utilities.<br>- Integration tests for API endpoints using `requests` or FastAPI’s test client.<br>- End‑to‑end tests that simulate a complete user flow. |
| **CI/CD** | - GitHub Actions workflow that runs linting (`flake8`), type checking (`mypy`), tests, and builds Docker images.<br>- Automatic deployment to a staging environment on successful merge. |
| **Dockerization** | - Multi‑stage Dockerfile for each service (Flask, Django, FastAPI).<br>- `docker-compose.yml` to spin up all services (API, PostgreSQL, Redis) together. |
| **Deployment** | - Deploy to a free tier on Render/Heroku or an AWS EC2 instance.<br>- Configure environment variables, HTTPS, and process manager (Gunicorn, Uvicorn). |
| **Quality Gates** | - Enforce code coverage thresholds (`pytest-cov`).<br>- Run security scans (`bandit`, `safety`).<br>- Linting and formatting checks (`black`, `isort`). |

## Project Structure
```
Week9/
├─ docker/
│   ├─ Dockerfile.api          # Multi‑stage build for the API
│   └─ docker-compose.yml      # Orchestrates API, PostgreSQL, Redis
├─ tests/
│   ├─ unit/
│   │   └─ test_models.py
│   ├─ integration/
│   │   └─ test_api.py
│   └─ e2e/
│       └─ test_user_flow.py
├─ .github/
│   └─ workflows/
│       └─ ci.yml              # GitHub Actions CI pipeline
├─ requirements.txt            # Core Python dependencies
├─ requirements.test.txt       # Testing‑specific dependencies
├─ spec.md                     # This specification
├─ main.py                     # Minimal entry‑point for local runs
└─ README.md                   # Project overview and run instructions
```

## Quick Start
1. **Clone the repository** (or copy the Week 4‑8 folders into `Week9`).  
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
5. **Run the test suite**  
   ```bash
   pytest --cov=.
   ```
6. **Build and run with Docker Compose**  
   ```bash
   docker compose up --build
   ```
7. **Access the API** at `http://localhost:8000` (or the port mapped in `docker-compose.yml`).  

## Extensibility
- Add automated deployment to a cloud provider using GitHub Actions secrets.
- Integrate monitoring (Prometheus, Grafana) for production observability.
- Implement canary releases or blue‑green deployments.
- Expand test coverage to include property‑based testing (`hypothesis`).
