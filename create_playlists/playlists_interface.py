from abc import ABC, abstractmethod


class PlaylistInterfaces(ABC):
    
    @abstractmethod
    def insert_playlist(name) -> dict:
        pass

    @abstractmethod
    def insert_book_to_playlist(name_playlist, id_playlist, name_book, id_book) -> dict:
        pass