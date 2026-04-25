# Week 4 – Flask Web Server & API Basics

## Learning Objectives
- Understand Flask project structure and routing.
- Build a simple RESTful API with CRUD operations.
- Handle JSON request/response bodies.
- Implement basic error handling and status codes.
- Write basic unit tests for API endpoints.

## Project Overview
Create a lightweight note‑taking API that allows users to:
- Retrieve all notes (`GET /api/notes`)
- Retrieve a single note by ID (`GET /api/notes/<id>`)
- Create a new note (`POST /api/notes`)
- Update an existing note (`PUT /api/notes/<id>`)
- Delete a note (`DELETE /api/notes/<id>`)

The data store will be an in‑memory dictionary that persists only for the lifetime of the application. Future weeks will replace this with a database.

## Core Features
| Feature | Description |
|---------|-------------|
| **Routing** | Define routes for `/api/notes` and `/api/notes/<id>` supporting GET, POST, PUT, DELETE. |
| **JSON Handling** | Parse JSON from requests and return JSON responses with appropriate HTTP status codes. |
| **Error Handling** | Return meaningful error messages for invalid IDs, missing fields, or unsupported methods. |
| **In‑Memory Storage** | Use a Python dict to store notes keyed by a generated ID. |
| **Testing** | Write at least three unit tests covering GET all, POST new, and GET by ID. |

## Project Structure
```
Week4/
├─ app.py            # Main Flask entry point
├─ requirements.txt  # Python dependencies
├─ spec.md           # This specification document
├─ .env              # Environment variables (e.g., FLASK_ENV=development)
├─ routes.py         # Route definitions (optional modularization)
├─ models.py         # Simple Note model / in‑memory storage logic
└─ tests/
   └─ test_app.py   # Unit tests for the API
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

3. **Run the application**  
   ```bash
   flask --app app run
   ```

4. **Test the API**  
   Use `curl`, Postman, or the provided unit tests to interact with the endpoints.

## Extensibility
- Replace the in‑memory store with a PostgreSQL database (Week 5).
- Add authentication (JWT) for protected routes (Week 6).
- Implement async background tasks for note cleanup (Week 7).
- Write comprehensive integration tests and CI/CD pipelines (Weeks 8‑9).
- Build a front‑end client or Dockerize the service for deployment (Week 10).
