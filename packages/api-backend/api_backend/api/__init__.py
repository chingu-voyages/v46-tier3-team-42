from fastapi import APIRouter
from api_backend.api import users

api_router = APIRouter()

api_router.include_router(users.router, tags=["users"])
