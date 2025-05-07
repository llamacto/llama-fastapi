# FastAPI Scaffold

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
- Database migrations with Alembic (optional)

## Project Structure

```
├── app/
│   ├── main.py               # FastAPI application entry point
│   ├── core/                 # Core functionality
│   │   ├── config.py        # Configuration settings
│   │   ├── security.py      # Security utilities
│   ├── db/                  # Database
│   │   ├── session.py      # Database session
│   │   ├── base.py         # SQLAlchemy base
│   ├── middlewares/        # Middleware components
│   │   ├── logging.py      # Logging middleware
│   ├── modules/            # Feature modules
│   │   ├── user/          # User module
│   │   │   ├── api.py     # API endpoints
│   │   │   ├── models.py  # Database models
│   │   │   ├── schemas.py # Pydantic schemas
│   │   │   ├── services.py # Business logic
│   ├── utils/             # Utility functions
│   ├── events/            # Application events
│       ├── startup.py     # Startup events
│       ├── shutdown.py    # Shutdown events
├── tests/                 # Test files
├── .env                  # Environment variables
├── requirements.txt      # Project dependencies
```

## Getting Started

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
4. Set up your environment variables in `.env`
5. Run the application:
   ```bash
   uvicorn app.main:app --reload
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