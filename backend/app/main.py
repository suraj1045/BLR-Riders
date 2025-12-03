from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings

def create_application() -> FastAPI:
    """Create and configure the FastAPI application"""
    app = FastAPI(
        title=settings.APP_NAME,
        description="BLR Riders - Intelligent Rider Companion App",
        version="0.1.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
    )

    # CORS middleware configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, replace with your frontend URL
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routers
    from .api.v1.api import api_router
    app.include_router(api_router, prefix="/api/v1")

    @app.get("/api/healthcheck")
    async def health_check():
        return {"status": "ok", "app": settings.APP_NAME}

    return app

# Create the FastAPI application
app = create_application()