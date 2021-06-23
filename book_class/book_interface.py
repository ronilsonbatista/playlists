from abc import ABC, abstractmethod
from config import project_dir

import sys
sys.path.insert(1, f"{project_dir}/../book_class/")
from book_database import BookSchema

class BookInterfaces(ABC):

    # @abstractmethod
    # def romove_book(id) -> bool:
    #     pass
    
    @abstractmethod
    def insert_book(titulo, isbn, autor, genero) -> bool:
        pass

    @abstractmethod
    def list_book() -> BookSchema:
        pass