# Django Project

A Django web application featuring a blog system with modern web development practices.

## Features

- Blog application with post management
- User authentication and authorization
- Admin interface for content management
- Responsive design
- PostgreSQL database

## Prerequisites

- Python 3.12+
- PostgreSQL 15+
- poetry (Python package manager)
- Git

## Installation

- **1. Clone the repository**

   `git clone https://github.com/SystemSolution21/django_project.git
   cd django_project
   `

- **2. Create virtual environment**

   `python -m venv .venv
   or poetry shell
   (django_project).venv\Scripts\activate
   `

- **3. Install dependencies**

   `pip install -r requirements.txt
   or poetry sync
   `

- **4. Set up environment variables**

   `cp .env.example .env
   #Edit .env with your configuration
   `

- **5. Run migrations**

   `python manage.py migrate
   `

- **6. Create superuser**

   `python manage.py createsuperuser
   `

- **7. Start development server**

   `python manage.py runserver
   `

Visit `http://127.0.0.1:8000/` to view the application.

## Docker Deployment

You can run the application and database using Docker Compose.

1. **Ensure `.env` is configured** with your database credentials.

2. **Build and run the containers:**

      `docker-compose up --build
      `

The application will be available at `http://127.0.0.1:8000/`. The database data will be persisted in a Docker volume.

## Project Structure

```bash
django_project/
├── blog/             # Blog application
│   ├── migrations/       # Database migrations
│   |    ├── __init__.py       # Application package
│   |    └── 0001_initial.py   # Initial migration
|   |
│   ├── static/           # Static files (CSS, JS)
│   |    └── blog/
│   |        └── main.css
│   |        └── script.js
│   |
│   ├── templates/        # Blog templates
│   |    ├── 404.html     # 404 page
│   |    └── blog/
│   |        ├── about.html
│   |        ├── announcements.html
│   |        ├── base.html
│   |        ├── calendar.html
│   |        ├── home.html
│   |        ├── index.html
│   |        ├── latest_posts.html
│   |        ├── post_confirm_delete.html
│   |        ├── post_detail.html
│   |        ├── post_form.html
│   |        ├── resources.html
│   |        └── user_posts.html
│   |
│   ├── __init__.py       # Application package
│   ├── admin.py          # Admin interface configuration
│   ├── apps.py           # Application configuration
│   ├── models.py         # Database models
│   ├── tests.py          # Application tests
│   ├── urls.py           # Application URLs
│   └── views.py          # Application views
|
├── media/           # User uploaded files
│   └── profile_pics/     # User profile pictures
|
├── mysite/          # Main project
│   ├── __init__.py       # Application package
│   ├── asgi.py           # ASGI configuration
│   ├── settings.py       # Application settings
│   ├── urls.py           # Project URLs
│   └── wsgi.py           # WSGI configuration
|
├── productionfiles/   # Production files
|   ├── admin/            # Admin static files
|   ├── blog/            # Blog static files
|   └── staticfiles.json  # Static files manifest
|
├── projectstaticfiles/  # Globally available project static files
|
├── users/             # User authentication application
│   ├── migrations/       # Database migrations
│   |    └── __init__.py   # Initial migration
|   |
│   ├── templates/        # User templates
│   |    └── users/
│   |        ├── login.html
│   |        ├── logout.html
│   |        ├── password_reset_complete.html
│   |        ├── password_reset_confirm.html
│   |        ├── password_reset_done.html
│   |        ├── password_reset.html
│   |        ├── profile.html
│   |        └── register.html
|   |
│   ├── __init__.py       # Application package
│   ├── admin.py          # Admin interface configuration
│   ├── apps.py           # Application configuration
│   ├── forms.py          # User forms
│   ├── models.py         # User models
│   ├── tests.py          # Application tests
│   ├── urls.py           # Application URLs
│   └── views.py          # Application views
|
├── .env                  # Environment variables
├── .env.example          # Environment variables example
├── .gitignore            # Git ignore file
├── .dockerignore         # Docker ignore file
├── DATABASE_OWNERSHIP.md # Database ownership instructions
├── DATABASE.md           # Database setup instructions
├── datadump.json         # Database dump file (if needed for development)
├── django_error.log      # Django error log file
├── Dockerfile            # Docker build file
├── docker-compose.yml    # Docker compose file
├── LICENSE               # License file
├── LINUX_COMMANDS.md     # Linux commands for debugging Docker containers
├── manage.py             # Django management script
├── poetry.lock           # Poetry lock file
├── pyproject.toml        # Poetry project file
└── README.md             # This file
```

## Usage

- **Admin Panel**: Login with superuser credentials.
   Admin button appears in the navbar after login.
- **Blog**: Main blog functionality at `/blog/`
- **API**: RESTful API endpoints (if implemented)

## Development

- **1. Run tests**

   `python manage.py test
   `

- **2. Collect static files**

   `python manage.py collectstatic
   `

- **3. Create new migrations**

   `python manage.py makemigrations
   `

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue in the repository.
