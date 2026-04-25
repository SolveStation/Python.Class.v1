# Week 5 – Databases (Django + PostgreSQL)

## Learning Objectives
- Understand Django ORM and model definitions.
- Set up PostgreSQL database connections.
- Perform CRUD operations using Django models.
- Implement relationships and migrations.
- Write unit tests for database interactions.

## Project Overview
Extend the Week 4 note‑taking API into a Django project that persists data in PostgreSQL. Provide the same CRUD endpoints for notes, but backed by a relational database instead of an in‑memory dict.

## Core Features
| Feature | Description |
|---------|-------------|
| **Model** | Define a `Note` model with fields: `id`, `title`, `content`, `created_at`. |
| **Database** | Use PostgreSQL via `psycopg2`; configure connection in `settings.py`. |
| **ORM** | Use Django ORM for create, read, update, delete operations. |
| **Migrations** | Generate and apply migrations for schema changes. |
| **Serializers** | (Optional) Use Django REST framework serializers for JSON output. |
| **Testing** | Write tests that cover model creation, query filtering, and migration integrity. |

## Project Structure
```
Week5/
├─ django_project/
│  ├─ manage.py
│  ├─ config/
│  │   ├─ __init__.py
│  │   ├─ settings.py
│  │   └─ urls.py
│  ├─ notes/
│  │   ├─ migrations/
│  │   ├─ __init__.py
│  │   ├─ models.py
│  │   ├─ serializers.py
│  │   ├─ views.py
│  │   └─ tests.py
│  └─ requirements.txt
├─ spec.md
└─ requirements.txt
```

## Quick Start
1. **Create a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**  
   ```bash
   pip install -r django_project/requirements.txt
   ```

3. **Apply migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the development server**  
   ```bash
   python manage.py runserver
   ```

5. **Test the API** (using curl, Postman, or the Django admin) at `http://127.0.0.1:8000/api/notes/`.

## Extensibility
- Add authentication (JWT) in Week 6.
- Implement async background tasks for heavy DB operations in Week 7.
- Write integration tests with Django’s test framework in Week 9.
- Deploy to a cloud PostgreSQL instance and configure CI/CD pipelines in Week 10.
