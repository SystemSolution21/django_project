# PostgreSQL Database Setup

## Connect to PostgreSQL

```bash
psql -U postgres
```

## Create Database and User

```psql
CREATE DATABASE django_mysite_db;
CREATE ROLE django_mysite_user WITH LOGIN PASSWORD 'your_secret_password';
ALTER DATABASE django_mysite_db OWNER TO django_mysite_user;
GRANT ALL PRIVILEGES ON DATABASE django_mysite_db TO django_mysite_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO django_mysite_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO django_mysite_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO django_mysite_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO django_mysite_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO django_mysite_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON FUNCTIONS TO django_mysite_user;
```

## Set Environment Variables

```.env
DB_NAME=django_mysite_db
DB_USER=django_mysite_user
DB_PASSWORD=your_secret_password
DB_HOST=localhost
DB_PORT=5432
```

## Update settings.py

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_mysite_db",
        "USER": "django_mysite_user",
        "PASSWORD": "your_secret_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```

## Run Migrations

```bash
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Start Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the application.

## Workflow for Switch to PostgreSQL from SQLite

### 1. Export data from SQLite

```bash
python manage.py dumpdata --exclude contenttypes --exclude auth.Permission > datadump.json
```

### 2. Switch to PostgreSQL in settings

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_mysite_db",
        "USER": "django_mysite_user",
        "PASSWORD": "your_secret_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### 3. Run migrations to create schema

```bash
python manage.py migrate
```

### 4. Load data

```bash
python manage.py loaddata datadump.json
```

### 5. Create new superuser

```bash
python manage.py createsuperuser
```

### 6. Start development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the application.

## Django Commands

- Use `pgAdmin` to manage PostgreSQL databases
- Use `psql` to connect to PostgreSQL databases
- Use `python manage.py shell` to interact with Django models
- Use `python manage.py test` to run tests
- Use `python manage.py collectstatic` to collect static files
- Use `python manage.py makemigrations` to create new migrations
- Use `python manage.py migrate` to apply migrations
- Use `python manage.py createsuperuser` to create a superuser
- Use `python manage.py runserver` to start the development server
- Use `python manage.py loaddata` to load data
- Use `python manage.py dumpdata` to export data

## Sql Queries

```sql
select *
from (
SELECT DISTINCT ON (author_id) *
FROM blog_post
ORDER BY author_id, date_posted DESC
) as latest
order by date_posted desc;
```
