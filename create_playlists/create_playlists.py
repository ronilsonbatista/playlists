import os.path
from config import app, db, ma, database_file, project_dir
from flask import jsonify, render_template, request
from dateutil import parser

import sys
sys.path.insert(1, f"{project_dir}/../services/")
from ServiceMapping import BookServiceHandler

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
    id_playlist = db.Column(db.String(256), nullable=False)
    name_book = db.Column(db.String(256), nullable=False)
    id_book = db.Column(db.String(256), nullable=False)

class PlaylistsBookSchema(ma.SQLAlchemyAutoSchema):
    submitted = ma.Nested(Playlists_Book, many=True)
    class Meta:
        model = Playlists_Book

all_playlists_book_schema = PlaylistsBookSchema(many = True)

@app.route("/api/create/playlist", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/submitt/new/playlist", methods=["POST"])
def post_playlists():
    new_data = {
        "name" : request.form["name"],
    }

    submitted = Playlists(**new_data)
    db.session.add(submitted)
    db.session.commit()
    return "Salvo com Sucesso"


@app.route("/api/remove/playlist/", methods=["GET"])
def romeve_playlists():

    result = Playlists.query.all()

    return render_template("remove_playlists.html",
                           list=result)

@app.route("/api/remove", methods=["POST"])
def post_remove():

    id = int(request.form["remove_id"])
    
    user = Playlists.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return "OK"
    
@app.route("/api/playlist/list", methods=["GET"])
def submitted_list():
    result = Playlists.query.all()
    return jsonify(all_playlists_schema.dump(result))

@app.route("/api/playlist/new/book", methods=["GET"])
def new_book():
   
    result = Playlists.query.all()

    return render_template("insert_playlists.html",
                           list=result)

@app.route("/api/add/book", methods=["POST"])
def post_add_book():

    id_playlist_ = request.form["id_playlist"]
    name_playlist_ = request.form["name_playlist"]
    result = BookServiceHandler().get()
    
    return render_template("add_playlist.html",
                           list=result, 
                           id_playlist = id_playlist_,
                           name_playlist = name_playlist_)

@app.route("/api/add/book", methods=["POST"])
def post_book():    

    new_data = {
        "name_playlist": request.form["name_playlist"],
        "id_playlist": request.form["id_playlist"],
        "name_book": request.form["name_book"],
        "id_book": request.form["id_book"],
    }

    submitted = Playlists_Book(**new_data)
    db.session.add(submitted)
    db.session.commit()
    return "Salvo com Sucesso"

@app.route("/api/playlist/book/list", methods=["GET"])
def list_book_playlist():
    result = Playlists_Book.query.all()
    return jsonify(all_playlists_book_schema.dump(result))

if __name__ == "__main__":
    if not os.path.exists(database_file):
        db.create_all()
    app.run(host="0.0.0.0", port=11231, debug=True)