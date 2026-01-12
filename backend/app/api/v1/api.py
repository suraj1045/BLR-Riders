from fastapi import APIRouter
from app.api.v1.endpoints import auth, rides, learning, chatbot

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(rides.router, prefix="/rides", tags=["rides"])
api_router.include_router(learning.router, prefix="/learning", tags=["learning"])
api_router.include_router(chatbot.router, prefix="/chatbot", tags=["chatbot"])