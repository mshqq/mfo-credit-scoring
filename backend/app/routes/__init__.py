from .applications import router as application_router
from .auth import router as auth_router
from .clients import router as clients_router
from .health import router as health_router
from .users import router as users_router

__all__ = [
    "application_router",
    "auth_router",
    "clients_router",
    "health_router",
    "users_router",
]
