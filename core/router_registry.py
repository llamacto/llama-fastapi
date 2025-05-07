from fastapi import APIRouter, FastAPI
from typing import List, Dict
from dataclasses import dataclass
from importlib import import_module
import logging

logger = logging.getLogger(__name__)


@dataclass
class RouteModule:
    """Route module configuration"""
    prefix: str
    tags: List[str]
    module_path: str
    router_name: str = "router"  # Default router variable name in modules


class RouterRegistry:
    """Elegant router registration manager"""
    def __init__(self):
        self._routes: Dict[str, RouteModule] = {}

    def register(self, prefix: str, tags: List[str], module_path: str) -> 'RouterRegistry':
        """Register a new route module"""
        self._routes[module_path] = RouteModule(
            prefix=prefix,
            tags=tags,
            module_path=module_path
        )
        return self  # Enable method chaining

    def include_in_app(self, app: FastAPI) -> None:
        """Include all registered routes in the FastAPI application"""
        for module_path, route_config in self._routes.items():
            try:
                # Dynamically import the module
                module = import_module(module_path)
                router = getattr(module, route_config.router_name, None)
                
                if not isinstance(router, APIRouter):
                    logger.error(f"No valid router found in module: {module_path}")
                    continue

                # Include the router in the app
                app.include_router(
                    router,
                    prefix=route_config.prefix,
                    tags=route_config.tags
                )
                logger.info(f"Successfully registered routes from: {module_path}")
                
            except Exception as e:
                logger.error(f"Failed to register routes from {module_path}: {str(e)}")


# Create a global registry instance
registry = RouterRegistry() 