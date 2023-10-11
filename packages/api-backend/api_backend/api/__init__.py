from fastapi import APIRouter
from api_backend.api import users, tips

api_router = APIRouter()

api_router.include_router(users.router, tags=["users"])
api_router.include_router(tips.router, tags=["tips"])
