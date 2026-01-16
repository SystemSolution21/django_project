# Stage 1: Build dependencies
FROM python:3.12.12-slim AS builder

WORKDIR /app

# Install Poetry
RUN pip install --upgrade pip && pip install poetry

# Copy poetry configuration files
COPY pyproject.toml poetry.lock ./

# Install poetry-plugin-export
RUN pip install poetry-plugin-export

# Export dependencies to requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Stage 2: Production Runtime
FROM python:3.12.12-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies required for PostgreSQL (psycopg2-binary)
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements from builder stage
COPY --from=builder /app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
# Ensure gunicorn is installed (in case it's not in pyproject.toml)
RUN pip install gunicorn

# Copy application code
COPY . .

# Create a non-root user for security
RUN addgroup --system app && adduser --system --group app

# Create directories for static/media and set permissions
RUN mkdir -p productionfiles media && chown -R app:app /app

# Switch to non-root user
USER app

# Collect static files (requires a dummy secret key during build)
RUN SECRET_KEY=dummy_build_key python manage.py collectstatic --noinput

# Expose the port and define the command
EXPOSE 8000
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
