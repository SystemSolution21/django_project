# PostgreSQL Database Setup

```psql
CREATE DATABASE django_mysite_db;
CREATE ROLE django_mysite_user WITH LOGIN PASSWORD 'django_mysite_password';
ALTER DATABASE django_mysite_db OWNER TO django_mysite_user;
GRANT ALL PRIVILEGES ON DATABASE django_mysite_db TO django_mysite_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO django_mysite_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO django_mysite_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO django_mysite_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO django_mysite_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO django_mysite_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON FUNCTIONS TO django_mysite_user;
```
