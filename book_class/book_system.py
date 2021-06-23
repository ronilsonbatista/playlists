from book_class.book_database import RemoveBook
from config import db, project_dir

import sys
sys.path.insert(1, f"{project_dir}/../create_playlists/")
from book_database import InsertBook, RemoveBook
from book_interface import BookInterfaces

class PlaylistSystem(BookInterfaces):
      
    @staticmethod  
    def insert_book(titulo, isbn, autor, genero) -> bool:
        insertBook = InsertBook()
        insertBook = insertBook.insert_book(
            titulo,
            isbn,
            autor,
            genero 
        )

        if insertBook==False:
            return False

        if insertBook==True:
            return True
        
    @staticmethod 
    def romove_book(id) -> bool:
        romove_book = RemoveBook()
        romove_book.remove_book(id)

        if romove_book==False:
            return False

        if romove_book==True:
            return True

