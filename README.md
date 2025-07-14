# ALX Travel App

A Django-based travel application with REST API, Swagger documentation, and background task processing.

## Features

- Django REST Framework for API development
- Swagger/OpenAPI documentation at `/swagger/`
- MySQL database configuration with environment variables
- CORS headers for cross-origin requests
- Celery for background task processing
- RabbitMQ as message broker

## Project Structure

```
alx_travel_app/
├── alx_travel_app/          # Main Django project
│   ├── __init__.py
│   ├── settings.py          # Django settings with all configurations
│   ├── urls.py              # Main URL configuration with Swagger
│   ├── wsgi.py              # WSGI configuration
│   ├── asgi.py              # ASGI configuration
│   └── celery.py            # Celery configuration
├── listings/                # Django app
│   ├── __init__.py
│   ├── admin.py             # Django admin configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── serializers.py       # REST API serializers
│   ├── views.py             # API views
│   ├── urls.py              # App URL configuration
│   └── tasks.py             # Celery background tasks
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

Copy the example environment file and configure your settings:

```bash
cp .env.example .env
```

Edit `.env` with your actual values:

```env
# Django Settings
SECRET_KEY=your-actual-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DB_NAME=alx_travel_db
DB_USER=root
DB_PASSWORD=your_actual_password
DB_HOST=localhost
DB_PORT=3306

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Celery Settings
CELERY_BROKER_URL=amqp://localhost
CELERY_RESULT_BACKEND=rpc://
```

### 3. Database Setup

Create the MySQL database:

```sql
CREATE DATABASE alx_travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

## API Documentation

### Swagger UI
Access the interactive API documentation at: `http://localhost:8000/swagger/`

### ReDoc
Alternative documentation format at: `http://localhost:8000/redoc/`

## API Endpoints

### Listings API
- `GET /api/listings/` - List all listings
- `POST /api/listings/` - Create a new listing
- `GET /api/listings/{id}/` - Get a specific listing
- `PUT /api/listings/{id}/` - Update a listing
- `DELETE /api/listings/{id}/` - Delete a listing

## Background Tasks

The project includes Celery for background task processing. To start the Celery worker:

```bash
celery -A alx_travel_app worker -l info
```

To start the Celery beat scheduler (for periodic tasks):

```bash
celery -A alx_travel_app beat -l info
```

## Development

### Running Tests
```bash
python manage.py test
```

### Code Quality
```bash
# Install development dependencies
pip install flake8 black isort

# Run code formatting
black .
isort .

# Run linting
flake8
```

## Production Deployment

1. Set `DEBUG=False` in your environment variables
2. Configure proper database credentials
3. Set up a proper web server (nginx, Apache)
4. Use a production WSGI server (gunicorn, uwsgi)
5. Configure Celery with Redis or RabbitMQ
6. Set up proper logging and monitoring

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License.