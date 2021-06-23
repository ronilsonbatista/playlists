from abc import ABC, abstractmethod

class BookInterfaces(ABC):
    
    @abstractmethod
    def insert_book(titulo, isbn, autor, genero) -> dict:
        pass

    @abstractmethod
    def romove_book(id) -> dict:
        pass
    