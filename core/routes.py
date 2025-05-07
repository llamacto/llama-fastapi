from app.core.config import get_settings
from app.core.router_registry import registry

settings = get_settings()

# Register all route modules
def register_routes():
    """Register all API route modules"""
    (registry
        # Auth routes
        .register(
            prefix=f"{settings.API_V1_STR}/auth",
            tags=["auth"],
            module_path="app.modules.auth.api"
        )
        # User module routes
        .register(
            prefix=f"{settings.API_V1_STR}/users",
            tags=["users"],
            module_path="app.modules.user.api"
        )
        # Health check routes
        .register(
            prefix="",  # No prefix for health checks
            tags=["health"],
            module_path="app.modules.health.api"
        )
    )

    return registry 