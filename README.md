# Django Project

A Django web application featuring a blog system with modern web development practices.

## Features

- Blog application with post management
- User authentication and authorization
- Admin interface for content management
- Responsive design
- SQLite database (development)

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/SystemSolution21/django_project.git
   cd django_project
   ```

2. **Create virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**

   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` to view the application.

## Project Structure

```project structure
django_project/
├── blog/             # Blog application
│   ├── migrations/       # Database migrations
│   |    ├── __init__.py       # Application package
│   |    └── 0001_initial.py   # Initial migration
|   |
│   ├── static/           # Static files (CSS, JS)
│   |    └── blog/
│   |        └── main.css
│   |
│   ├── templates/        # Blog templates
│   |    └── blog/
│   |        ├── about.html
│   |        ├── base.html
│   |        └── home.html
│   |
│   ├── __init__.py       # Application package
│   ├── admin.py          # Admin interface configuration
│   ├── apps.py           # Application configuration
│   ├── models.py         # Database models
│   ├── tests.py          # Application tests
│   ├── urls.py           # Application URLs
│   └── views.py          # Application views
|
├── mysite/          # Main project settings
│   ├── __init__.py       # Application package
│   ├── asgi.py           # ASGI configuration
│   ├── settings.py       # Django settings
│   ├── urls.py           # Project URLs
│   └── wsgi.py           # WSGI configuration
|
├── users/             # User authentication application
│   ├── migrations/       # Database migrations
│   |    └── __init__.py   # Initial migration
|   |
│   ├── templates/        # User templates
│   |    └── users/
│   |        ├── login.html
│   |        ├── logout.html
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
├── db.sqlite3            # SQLite database
├── LICENSE               # License file
├── manage.py             # Django management script
├── poetry.lock           # Poetry lock file
├── pyproject.toml        # Poetry project file
└── README.md             # This file
```

## Usage

- **Admin Panel**: Visit `/admin/` to manage content
- **Blog**: Main blog functionality at `/blog/`
- **API**: RESTful API endpoints (if implemented)

## Development

1. **Run tests**

   ```bash
   python manage.py test
   ```

2. **Collect static files**

   ```bash
   python manage.py collectstatic
   ```

3. **Create new migrations**

   ```bash
   python manage.py makemigrations
   ```

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
