from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.config import settings
from events import create_start_app_handler, create_stop_app_handler
from middlewares import setup_middlewares
from routes import router

# ASCII Art Logo for LlamaCTO
LOGO = """
    __    __                            ______   ______  ____
   / /   / /   ____ _____ ___  ____ _  / ____/  /_  __/ / __ \\
  / /   / /   / __ `/ __ `__ \/ __ `/ / /        / /   / / / /
 / /___/ /___/ /_/ / / / / / / /_/ / / /___     / /   / /_/ / 
/_____/_____/\__,_/_/ /_/ /_/\__,_/  \____/    /_/    \____/  
                                                        
 🦙 LlamaCTO - FastAPI Scaffold v{version}
 Running on: http://{host}:{port}
 Documentation: http://{host}:{port}/docs
"""

def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOC_URL,
        openapi_url=settings.OPENAPI_URL,
    )

    # Set up CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Set up other middlewares
    setup_middlewares(application)

    # Add event handlers
    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    # Add startup logo
    @application.on_event("startup")
    async def display_logo():
        print(LOGO.format(
            version=settings.VERSION,
            host=settings.HOST,
            port=settings.PORT
        ))

    # Include all routes
    application.include_router(router)

    return application

app = get_application() 