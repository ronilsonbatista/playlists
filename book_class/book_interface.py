from abc import ABC, abstractmethod
from config import project_dir

import sys
sys.path.insert(1, f"{project_dir}/../book_class/")
from book_database import BookSchema

class BookInterfaces(ABC):

    @abstractmethod
    def insert_book(titulo, isbn, autor, genero) -> bool:
        pass

    def romove_book(remove_id) -> bool:
        pass
    