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
    id_playlist = db.Column(db.Integer, nullable=False)
    name_book = db.Column(db.String(256), nullable=False)
    id_book = db.Column(db.Integer, nullable=False)

class PlaylistsBookSchema(ma.SQLAlchemyAutoSchema):
    submitted = ma.Nested(Playlists_Book, many=True)
    class Meta:
        model = Playlists_Book

all_playlists_book_schema = PlaylistsBookSchema(many = True)

# Criar coleção
@app.route("/api/criar/colecao", methods=["GET"])
def home():
    return render_template("index.html")

# POST - Criar coleção
@app.route("/api/nova/colecao", methods=["POST"])
def post_playlists():
    new_data = {
        "name" : request.form["name"],
    }

    submitted = Playlists(**new_data)
    db.session.add(submitted)
    db.session.commit()
    return "Salvo com Sucesso"

# Remover coleção
@app.route("/api/remover/colecao", methods=["GET"])
def romeve_playlists():

    result = Playlists.query.all()

    return render_template("remove_playlists.html",
                           list=result)

# POST - Remover coleção por id 
@app.route("/api/remover", methods=["POST"])
def post_remove():

    id = int(request.form["remove_id"])
    
    user = Playlists.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return "OK"

 # GET - Listar coleção  
@app.route("/api/listar/colecao", methods=["GET"])
def submitted_list():
    result = Playlists.query.all()
    return jsonify(all_playlists_schema.dump(result))


 # Selecionar Coleção 
@app.route("/api/selecionar/colecao", methods=["GET"])
def new_book():
   
    result = Playlists.query.all()

    return render_template("insert_playlists.html",
                           list=result)

 # POST - Adicionar Livro
@app.route("/api/adicionar/livro", methods=["POST"])
def post_add_book():

    print("id_playlist:", int(request.form["id_playlist"]))
    print("name_playlist", request.form["name_playlist"])

    id_playlist = int(request.form["id_playlist"])
    name_playlist = request.form["name_playlist"]
    result = BookServiceHandler().get()
    
    return render_template("add_playlist.html",
                           list=result, 
                           id_playlist = id_playlist,
                           name_playlist = name_playlist)

 # POST - Adicionar Livro
@app.route("/api/adicionar/livro/colecao", methods=["POST"])
def post_book():   
    
    print("id_playlist:", int(request.form["id_playlist"]))
    print("name_playlist:", request.form["name_playlist"]) 
    print("name_book:", request.form["name_book"])
    print("id_book:", int(request.form["id_book"])) 

    new_data = {
        "name_playlist": request.form["name_playlist"],
        "id_playlist": int(request.form["id_playlist"]),
        "name_book": request.form["name_book"],
        "id_book": int(request.form["id_book"]),
    }

    submitted = Playlists_Book(**new_data)
    db.session.add(submitted)
    db.session.commit()
    return "Salvo com Sucesso"

 # GET - Listar livros adicionados em coleção
@app.route("/api/colecao/livros/adicionados", methods=["GET"])
def list_book_playlist():
    result = Playlists_Book.query.all()
    return jsonify(all_playlists_book_schema.dump(result))

if __name__ == "__main__":
    if not os.path.exists(database_file):
        db.create_all()
    app.run(host="0.0.0.0", port=11231, debug=True)