# Django DRF Base Template

A production-ready Django REST Framework base template project with authentication, Docker support, Celery, Redis, and comprehensive API documentation. This template is designed to be extended for future projects.

## ⚡ Quick Start

**Fastest way to get started with Docker:**

```bash
# 1. Clone and navigate
git clone <repository-url>
cd dj-template

# 2. Create .env file (copy from .env.example if available)
# Edit .env and set DATABASE_TYPE=postgres for Docker

# 3. Start everything
docker-compose up --build

# 4. Run migrations (in another terminal)
docker-compose exec web python manage.py migrate

# 5. Access the API
# http://localhost:8000/swagger/
```

**For local development without Docker:**

```bash
# 1. Clone and navigate
git clone <repository-url>
cd dj-template

# 2. Install UV (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux

# 3. Install dependencies
uv sync

# 4. Activate virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# 5. Run migrations
cd core
python manage.py migrate

# 6. Start server
python manage.py runserver
```

## 🚀 Features

- **Custom User Model**: Email-based authentication with JWT tokens
- **Django REST Framework**: Full REST API support
- **JWT Authentication**: Secure token-based authentication with SimpleJWT
- **API Documentation**: Swagger/OpenAPI documentation with DRF YASG
- **Docker Support**: Complete Docker and Docker Compose setup
- **UV Package Manager**: Fast Python package management
- **Celery & Redis**: Asynchronous task processing
- **Environment-based Settings**: Separate configurations for local, dev, and production
- **Dynamic Database**: Support for both SQLite and PostgreSQL
- **CORS Support**: Configured for cross-origin requests
- **Database Seeding**: Automated database seeding script

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.13+**
- **UV** (Python package manager) - [Installation Guide](https://github.com/astral-sh/uv)
- **Docker & Docker Compose** (for containerized setup)
- **PostgreSQL** (optional, if not using SQLite)
- **Redis** (optional, if not using Docker)

## 🛠️ Installation

### Option 1: Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd dj-template
   ```

2. **Install UV** (if not already installed)
   ```bash
   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # On Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. **Install dependencies using UV**
   ```bash
   uv sync
   ```

4. **Set up environment variables**
   ```bash
   # The .env file should already exist in the project
   # If not, create one based on the configuration below
   # Make sure to update SECRET_KEY and other sensitive values
   ```

5. **Configure your .env file**

   Edit the `.env` file with your configuration:
   ```env
   # Django Environment
   DJANGO_ENV=local

   # Secret Key (Generate a new one for production!)
   SECRET_KEY=your-secret-key-here

   # Database Configuration
   DATABASE_TYPE=sqlite  # or 'postgres' for PostgreSQL

   # If using PostgreSQL
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=localhost
   DB_PORT=5432

   # Redis Configuration
   REDIS_URL=redis://localhost:6379/0

   # Celery Configuration
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=redis://localhost:6379/0
   ```

6. **Activate the virtual environment**
   ```bash
   # UV creates a virtual environment automatically
   # Activate it:
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

7. **Run migrations**
   ```bash
   cd core
   python manage.py migrate
   ```

8. **Create a superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

   Or use the seed command:
   ```bash
   python manage.py seed_users
   ```

   The seed command supports custom options:
   ```bash
   # Custom email and password
   python manage.py seed_users --email admin@yourdomain.com --password securepass123

   # Force update if user exists
   python manage.py seed_users --force

   # See all options
   python manage.py seed_users --help
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

### Option 2: Docker Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd dj-template
   ```

2. **Create and configure .env file**
   ```bash
   # Create .env file in the root directory
   # Make sure DATABASE_TYPE=postgres for Docker setup
   ```

3. **Build and start containers**
   ```bash
   docker-compose up --build
   ```

   This will start:
   - **Web server** (Django) on port 8000
   - **PostgreSQL database**
   - **Redis server**
   - **Celery worker**
   - **Celery beat** (scheduler)

4. **Run migrations** (first time only)
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create superuser** (optional)
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Access the application**
   - API: http://localhost:8000
   - Swagger UI: http://localhost:8000/swagger/
   - ReDoc: http://localhost:8000/redoc/
   - Admin Panel: http://localhost:8000/admin/

## 📁 Project Structure

```
dj-template/
├── core/                      # Django project root
│   ├── accounts/              # Custom user authentication app
│   │   ├── models.py          # Custom User model
│   │   ├── serializers.py    # User serializers
│   │   ├── views.py          # Authentication views (register, login, logout)
│   │   ├── urls.py           # Account URLs
│   │   └── management/       # Management commands
│   │       └── commands/     # Custom commands
│   │           └── seed_users.py  # Seed initial users command
│   ├── commons/               # Common utilities app (your custom apps go here)
│   ├── core/                  # Django project settings
│   │   ├── settings/          # Environment-based settings
│   │   │   ├── base.py        # Base settings
│   │   │   ├── local.py       # Local development
│   │   │   ├── dev.py         # Development environment
│   │   │   └── prod.py        # Production environment
│   │   ├── utils/             # Utility functions
│   │   │   └── message.py    # Standardized API messages
│   │   ├── celery.py          # Celery configuration
│   │   └── urls.py           # Main URL configuration
│   └── manage.py             # Django management script
├── Dockerfile                 # Docker image definition
├── docker-compose.yml        # Docker Compose configuration
├── entrypoint.sh             # Container entrypoint script
├── pyproject.toml           # Project dependencies (UV)
├── .env                      # Environment variables (not in git)
└── README.md                # This file
```

## 🔧 Configuration

### Environment Variables

The project uses a `.env` file for configuration. Key variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `DJANGO_ENV` | Environment (local/dev/prod) | `local` |
| `SECRET_KEY` | Django secret key | (required) |
| `DATABASE_TYPE` | Database type (sqlite/postgres) | `sqlite` |
| `DB_NAME` | PostgreSQL database name | `postgres` |
| `DB_USER` | PostgreSQL username | `postgres` |
| `DB_PASSWORD` | PostgreSQL password | `postgres` |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |
| `REDIS_URL` | Redis connection URL | `redis://localhost:6379/0` |
| `CELERY_BROKER_URL` | Celery broker URL | `redis://localhost:6379/0` |
| `CELERY_RESULT_BACKEND` | Celery result backend | `redis://localhost:6379/0` |
| `ALLOWED_HOSTS` | Allowed hosts (comma-separated) | `localhost,127.0.0.1` |
| `CORS_ALLOWED_ORIGINS` | CORS origins (comma-separated) | `http://localhost:3000` |
| `JWT_ACCESS_TOKEN_LIFETIME_MINUTES` | JWT access token lifetime | `60` |
| `JWT_REFRESH_TOKEN_LIFETIME_DAYS` | JWT refresh token lifetime | `7` |
| `DRF_PAGE_SIZE` | API pagination size | `20` |
| `LANGUAGE_CODE` | Language code | `en-us` |
| `TIME_ZONE` | Timezone | `UTC` |

### Database Configuration

#### Using SQLite (Default)
```env
DATABASE_TYPE=sqlite
```
No additional configuration needed. Database file will be created at `core/db.sqlite3`.

#### Using PostgreSQL
```env
DATABASE_TYPE=postgres
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

## 🚀 Running the Project

### Local Development

```bash
# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Run migrations
cd core
python manage.py migrate

# Run development server
python manage.py runserver

# Run Celery worker (in separate terminal)
celery -A core worker --loglevel=info

# Run Celery beat (in separate terminal)
celery -A core beat --loglevel=info
```

### Docker

```bash
# Start all services
docker-compose up

# Start in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild containers
docker-compose up --build

# Run management commands
docker-compose exec web python manage.py <command>
```

## 📚 API Endpoints

### Authentication

- **POST** `/api/accounts/register/` - Register a new user
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword",
    "password2": "securepassword",
    "first_name": "John",
    "last_name": "Doe"
  }
  ```

- **POST** `/api/accounts/login/` - Login and get JWT tokens
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```

- **POST** `/api/accounts/logout/` - Logout (requires authentication)
  ```json
  {
    "refresh_token": "your_refresh_token"
  }
  ```

### API Documentation

- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/
- **JSON Schema**: http://localhost:8000/swagger.json

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test accounts

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 🔐 Security Notes

1. **Never commit `.env` file** - It contains sensitive information
2. **Change SECRET_KEY** in production
3. **Use strong passwords** for database and admin users
4. **Enable HTTPS** in production (`SECURE_SSL_REDIRECT=True`)
5. **Configure ALLOWED_HOSTS** properly for production
6. **Review CORS settings** before deploying

## 🛠️ Common Commands

```bash
# Create a new app
python manage.py startapp app_name

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Seed initial users
python manage.py seed_users

# Seed with custom values
python manage.py seed_users --email admin@yourdomain.com --password securepass123

# Force update existing user
python manage.py seed_users --force

# Access Django shell
python manage.py shell

# Access database shell
python manage.py dbshell
```

## 🐳 Docker Commands

```bash
# Build images
docker-compose build

# Start services
docker-compose up

# Stop services
docker-compose down

# View logs
docker-compose logs -f web
docker-compose logs -f celery_worker

# Execute commands in container
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

# Access container shell
docker-compose exec web sh

# Remove volumes (clean database)
docker-compose down -v
```

## 🐛 Troubleshooting

### Database Connection Issues

**Problem**: Cannot connect to PostgreSQL
- Check if PostgreSQL is running
- Verify database credentials in `.env`
- Ensure `DATABASE_TYPE=postgres` is set

**Problem**: SQLite database locked
- Close any other connections to the database
- Restart the development server

### Redis Connection Issues

**Problem**: Celery cannot connect to Redis
- Check if Redis is running: `redis-cli ping`
- Verify `CELERY_BROKER_URL` in `.env`
- For Docker, ensure Redis service is running

### Migration Issues

**Problem**: Migration conflicts
```bash
# Reset migrations (development only!)
python manage.py migrate accounts zero
python manage.py migrate accounts
```

### Port Already in Use

**Problem**: Port 8000 is already in use
```bash
# Use a different port
python manage.py runserver 8001

# Or find and kill the process
lsof -ti:8000 | xargs kill  # macOS/Linux
```

### Docker Issues

**Problem**: Container won't start
```bash
# Check logs
docker-compose logs web

# Rebuild containers
docker-compose down
docker-compose up --build
```

## 📦 Dependencies

Key dependencies (managed by UV):

- **Django 5.2.8+** - Web framework
- **Django REST Framework** - REST API toolkit
- **djangorestframework-simplejwt** - JWT authentication
- **drf-yasg** - API documentation
- **Celery** - Asynchronous task queue
- **Redis** - Message broker and cache
- **Gunicorn** - Production WSGI server
- **psycopg2-binary** - PostgreSQL adapter
- **python-dotenv** - Environment variable management
- **django-cors-headers** - CORS handling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
- Open an issue on GitHub
- Check the API documentation at `/swagger/`
- Review the Django and DRF documentation

## 🎯 Next Steps

After setting up the project:

1. **Customize the User model** if needed (already configured)
2. **Add your apps** to `LOCAL_APPS` in `settings/base.py`
3. **Configure email settings** for production
4. **Set up CI/CD** pipeline
5. **Configure logging** for your environment
6. **Add monitoring** and error tracking
7. **Set up backup** strategy for database

---

**Happy Coding! 🚀**
