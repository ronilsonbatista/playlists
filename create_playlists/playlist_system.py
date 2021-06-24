from config import db, project_dir

import sys
sys.path.insert(1, f"{project_dir}/../create_playlists/")
from playlists_build_database import AddBook, CreatePlaylist
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