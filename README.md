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
   git clone <repository-url>
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
├── blog/                 # Blog application
├── django_project/       # Main project settings
├── static/              # Static files (CSS, JS, images)
├── media/               # User uploaded files
├── templates/           # HTML templates
├── requirements.txt     # Python dependencies
├── manage.py           # Django management script
└── README.md           # This file
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
