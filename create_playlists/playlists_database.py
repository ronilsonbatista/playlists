import os.path
from config import app, db, ma, database_file, project_dir
from flask import jsonify, render_template, request
from dateutil import parser



class Playlists(db.Model):
    __tablename__ = "create_playlists_"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

class PlaylistsSchema(ma.SQLAlchemyAutoSchema):
    submitted = ma.Nested(Playlists, many=True)
    class Meta:
        model = Playlists

all_playlists_schema = PlaylistsSchema(many = True)

class Playlists_Book(db.Model):
    __tablename__ = "create_playlists_book_"
    id = db.Column(db.Integer, primary_key=True)
    name_playlist = db.Column(db.String(256), nullable=False)
    id_playlist = db.Column(db.Integer, nullable=False)
    name_book = db.Column(db.String(256), nullable=False)
    id_book = db.Column(db.Integer, nullable=False)

class PlaylistsBookSchema(ma.SQLAlchemyAutoSchema):
    submitted = ma.Nested(Playlists_Book, many=True)
    class Meta:
        model = Playlists_Book

all_playlists_book_schema = PlaylistsBookSchema(many = True)