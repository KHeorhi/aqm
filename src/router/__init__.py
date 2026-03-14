from fastapi import APIRouter
from src.router.add_task import router as router_add_task


api_router = APIRouter()

api_router.include_router(router_add_task)
