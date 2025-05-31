# LlamaCTO FastAPI Scaffold

A modern, production-ready FastAPI project scaffold with a well-organized structure and common features.

## Features

- FastAPI framework with modern Python type hints
- SQLAlchemy ORM with PostgreSQL
- JWT authentication
- Pydantic models for request/response validation
- Modular project structure
- Logging middleware
- CORS middleware
- Environment variable configuration
- Database migrations with Alembic

## Project Structure

```
├── app/                # Business logic modules
│   ├── user/           # User module
│   ├── auth/           # Authentication module
│   └── article/        # Article module
├── config/             # Configuration
├── database/           # Database migrations and sessions
├── middleware/         # Middleware components
├── routes/             # API routes
├── .env                # Environment variables (create from template below)
├── main.py             # Application entry point
└── README.md           # This file
```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```
# Application
APP_NAME=LlamaCTO
APP_ENV=local
APP_DEBUG=true
APP_URL=http://localhost:8000
APP_KEY=your-app-key-here

# Server
SERVER_HOST=0.0.0.0
SERVER_PORT=8000

# Database
DB_CONNECTION=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=llama_fastapi
DB_USERNAME=postgres
DB_PASSWORD=your_password_here

# JWT
JWT_SECRET=your-jwt-secret-key-here-please-change-in-production
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# Logging
LOG_LEVEL=debug
```

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your environment variables (see template above)
5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## API Documentation

Once the application is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

- Follow PEP 8 style guide
- Write tests for new features
- Update documentation as needed

## License

MIT 

## API Specification (Enterprise Mainstream Style)

- All endpoints use the unified prefix: `/v1/xxx`, deployed under the domain `api.xxx.com`
- Example: `https://api.xxx.com/v1/auth/login`
- Do not use the `/api` path prefix, keep it clean and simple
- Recommended endpoint style:
  - `POST   /v1/auth/login`
  - `POST   /v1/auth/register`
  - `GET    /v1/user/profile`
  - `POST   /v1/article/create`
  - `GET    /v1/article/list`
  - `GET    /v1/health`

### Unified Response Structure

All endpoints return the following structure:

```json
{
  "code": 200,
  "msg": "success",
  "data": { ... }
}
```
- `code`: Business status code, 200 for success, others for errors
- `msg`: Message description
- `data`: Business data object

### Error Response Example
```json
{
  "code": 400,
  "msg": "Email already registered",
  "data": null
}
```

### Version Management
- For future versions, use `/v2/xxx` directly, no need for `/api` prefix 