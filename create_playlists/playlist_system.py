from config import db, project_dir

import sys
sys.path.insert(1, f"{project_dir}/../create_playlists/")
from playlists_build_database import Playlists, Playlists_Book

from playlists_interface import PlaylistInterfaces

class PlaylistSystem(PlaylistInterfaces):
      
    @staticmethod  
    def insert_playlist(name) -> dict:
        new_data = CreatePlaylist()
        return new_data.insert_playlist(
          name
        )

    @staticmethod 
    def insert_book_to_playlist(name_playlist, id_playlist, name_book, id_book) -> dict:
        new_data = AddBook()
        return new_data.insert_book_to_playlist(
          name_playlist,
          id_playlist,
          name_book,
          id_book,  
      )   

class CreatePlaylist():
    @staticmethod
    def insert_playlist(name) -> dict:
        new_data = {
            "name" : name,
        }
        print(new_data)
        return new_data


class AddBook():
    @staticmethod
    def insert_book_to_playlist(name_playlist, id_playlist, name_book, id_book) -> dict:
      new_data = {
        "name_playlist": name_playlist,
        "id_playlist": id_playlist,
        "name_book": name_book,
        "id_book": id_book,
      }
      print(new_data)
      return new_data