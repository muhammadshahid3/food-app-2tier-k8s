# Food Management System

A Django 5 CRUD application for managing food price records with image uploads, Bootstrap 5 styling, modal-based forms, and admin support. It runs with SQLite by default and can use MySQL in production.

## Features
- Responsive landing page with Bootstrap 5
- Modal-based add and update forms
- MySQL-backed food storage with Django ORM
- Image upload support
- Delete confirmation modal
- Success and error messages
- Django admin integration

## Setup Instructions

### 1. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure the database
The included configuration runs locally with SQLite without additional setup. To use MySQL, create a database:
```sql
CREATE DATABASE food_management_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Copy the example environment file and update values as needed:
```bash
cp .env.example .env
```

For MySQL, set `DB_ENGINE=mysql` and provide the MySQL credentials in `.env`.

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Run with Docker

Docker Compose starts two containers: `app` (Django) and `mysql` (database).
This setup is intended for local development.

```bash
docker compose up --build
```

Then open http://127.0.0.1:8000/. Migrations run automatically when the app
container starts. Stop the stack with `docker compose down`; add `-v` only if
you also want to remove the database volume.
