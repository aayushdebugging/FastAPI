from fastapi import FastAPI ,  status
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException
from typing import List


app = FastAPI()

book =[
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Scribner",
        "published_date": "1925-04-10",
        "page_count": 218,
        "language": "English"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count": 281,
        "language": "English"
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg",
        "published_date": "1949-06-08",
        "page_count": 328,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publisher": "T. Egerton",
        "published_date": "1813-01-28",
        "page_count": 279,
        "language": "English"
    },
    {
        "id": 5,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "publisher": "Little, Brown and Company",
        "published_date": "1951-07-16",
        "page_count": 214,
        "language": "English"
    }
]

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

@app.get("/books", response_model=List[Book])
def get_books():
    return book

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for b in book:
        if b["id"] == book_id:
            return b
    raise HTTPException(status_code=404, detail="Book not found")

@app.post('/book', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    
    book.append(new_book)
    return new_book
    

