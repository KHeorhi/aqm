from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.services import queue_manager
from src.router import api_router


@asynccontextmanager
async def lifespan(_application: FastAPI):
    await queue_manager.create_queue()
    yield
    await queue_manager.shutdown_queue()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['GET', 'POST'],
    allow_credentials=True,
)

app.include_router(api_router)
