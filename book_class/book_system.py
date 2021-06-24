
from config import project_dir
from config import db, ma

import sys
sys.path.insert(1, f"{project_dir}/../book_class/")
from book_database import Book, BookSchema
from book_interface import BookInterfaces

class BookSystem(BookInterfaces):
      
    @staticmethod
    def insert_book(titulo, isbn, autor, genero) -> bool:
        if titulo==None or isbn==None or autor==None or genero == None: 
            return False

        new_data = {
            "titulo": titulo,
            "isbn": isbn,
            "autor": autor,
            "genero": genero,
        }

        submitted = Book(**new_data)
        db.session.add(submitted)
        db.session.commit()
        return True
           
    @staticmethod
    def remove_book(remove_id) -> bool:
        if remove_id==None:
            return False

        id = Book.query.get(remove_id)
        db.session.delete(id)
        db.session.commit()
        return True

    @staticmethod
    def update_book(id, titulo, isbn, autor, genero) -> bool:
        if id==None or titulo==None or isbn==None or autor==None or genero == None: 
            return False

        book = Book.query.get(id)
        book.titulo = titulo
        book.isbn = isbn
        book.autor = autor
        book.genero = genero
        db.session.commit()

