import os.path
from config import db, ma

# Criando tabelas 
class Playlists(db.Model):
    __tablename__ = "create_playlists_"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

class Playlists_Book(db.Model):
    __tablename__ = "create_playlists_book_"
    id = db.Column(db.Integer, primary_key=True)
    name_playlist = db.Column(db.String(256), nullable=False)
    id_playlist = db.Column(db.Integer, nullable=False)
    name_book = db.Column(db.String(256), nullable=False)
    id_book = db.Column(db.Integer, nullable=False)


# Tratando Exibição dos json
class PlaylistsSchema(ma.SQLAlchemyAutoSchema):
    submitted = ma.Nested(Playlists, many=True)
    class Meta:
      model = Playlists


class PlaylistsBookSchema(ma.SQLAlchemyAutoSchema):
    submitted = ma.Nested(Playlists_Book, many=True)
    class Meta:
        model = Playlists_Book

# Preparando modelo com dados
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

class Submitted():

    @staticmethod
    def insert_book(dict) -> bool:
        submitted = Playlists(**dict)
        db.session.add(submitted)
        db.session.commit()
        return True

    @staticmethod
    def insert_book(dict) -> bool:
        submitted = Playlists_Book(**dict)
        db.session.add(submitted)
        db.session.commit()
        return True
