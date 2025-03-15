from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f'Server is starting....')
    yield
    print(f"server has stopped working")

VERSION = "v1"

app = FastAPI(
    title="Book API",
    description="A simple API to manage books",
    version=VERSION
)

app.include_router(book_router, prefix=f"/api/{VERSION}/books", tags=["books"])
