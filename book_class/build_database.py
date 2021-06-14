import os
from config import app, db, ma, database_name
from book_class import Book

# Data to initialize database with
BOOK = [
    {'book_id': '1', 'name': 'Cem Anos de Solidão'},
    {'book_id': '2', 'name': 'Em Busca Do Tempo Perdido'},
    {'book_id': '3', 'name': 'O Estrangeiro'},
]

if os.path.exists(database_name):
    os.remove(database_name)

db.create_all()

for book in BOOK:
    book_obj = Book(**book)
    db.session.add(book_obj)

db.session.commit()