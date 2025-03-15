from fastapi import APIRouter, status, HTTPException
from typing import List
from src.books.schemas import Book, BookUpdateModel
from src.books.book_data import book

book_router = APIRouter()

@book_router.get("/", response_model=List[Book])
def get_books():
    return book

@book_router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    for b in book:
        if b["id"] == book_id:
            return b
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    if new_book.get("id") is None:
        new_book["id"] = max((b["id"] for b in book), default=0) + 1
    book.append(new_book)
    return new_book

@book_router.patch("/{book_id}")
async def update_a_book(book_id: int, book_data: BookUpdateModel) -> dict:
    for b in book:
        if b["id"] == book_id:
            b["title"] = book_data.title
            b["author"] = book_data.author
            b["publisher"] = book_data.publisher
            b["page_count"] = book_data.page_count
            b["language"] = book_data.language
            return b
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.delete("/{book_id}")
async def delete_a_book(book_id: int) -> dict:
    for b in book:
        if b["id"] == book_id:
            book.remove(b)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
