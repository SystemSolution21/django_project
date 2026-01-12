# Database Ownership in PostgreSQL

1. **Administrative control**: The owner can drop the database, alter its properties, and has implicit privileges
2. **Default privileges**: When the owner creates new objects, they automatically own them
3. **Security**: Non-owners cannot perform certain administrative operations even with granted privileges
4. **Django migrations**: Django typically expects the database user to own the database for seamless migrations and schema changes

## Database Level vs Django Application Level

**`django_mysite_user` (PostgreSQL database user):**

- Database-level user for PostgreSQL
- Used by Django to connect to the database
- Configured in `mysite/settings.py` as `DB_USER`
- Handles all database operations (CREATE, READ, UPDATE, DELETE)
- Never logs into Django admin or website

**`createsuperuser` (Django application user):**

- Application-level user stored in the database
- Created with `python manage.py createsuperuser`
- Stored in Django's `auth_user` table inside `django_mysite_db`
- Used to log into Django admin interface and website
- Has Django permissions (staff, superuser, etc.)

## The Relationship

```bash
PostgreSQL Database (django_mysite_db)
├── Owned by: django_mysite_user (DB user)
└── Contains Django tables:
    └── auth_user table
        └── Contains: superuser created by createsuperuser
```

## Workflow Example

1. **Database connection**: Django uses `django_mysite_user` credentials to connect to PostgreSQL
2. **User authentication**: When someone logs into the Django site, Django queries the `auth_user` table (using the `django_mysite_user` connection) to verify the login
3. **Admin access**: The superuser created by `createsuperuser` can access `/admin/` interface

## Key Point

- `django_mysite_user` = Database access credentials (never changes)
- Django superuser = Website admin account (can have multiple, can be changed)

They work together but serve completely different purposes in the application stack.
