import os.path
from config import app, db, database_file, project_dir
from flask import jsonify, render_template, request
from dateutil import parser

import sys
sys.path.insert(1, f"{project_dir}/../services/")
from ServiceMapping import BookServiceHandler

sys.path.insert(1, f"{project_dir}/../create_playlists/")
from playlists_build_database import Playlists, PlaylistsSchema, Playlists_Book, PlaylistsBookSchema, Submitted
from playlist_system import  PlaylistSystem

all_playlists_schema = PlaylistsSchema(many = True)
all_playlists_book_schema = PlaylistsBookSchema(many = True)

# Criar coleção
@app.route("/api/criar/colecao", methods=["GET"])
def home():
    return render_template("index.html")

# POST - Criar coleção
@app.route("/api/nova/colecao", methods=["POST"])
def post_playlists():
    name = request.form.get('name')

    data = PlaylistSystem()
    new_data = data.insert_playlist(name)

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
@app.route("/api/remover", methods=["POST"]) # Fazer Redireciomaneto automatico 
def post_remove():

    remove_id = int(request.form.get('remove_id'))
    
    id = Playlists.query.get(remove_id)
    db.session.delete(id)
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

    id_playlist = int(request.form.get('id_playlist'))
    name_playlist = request.form.get('name_playlist')
    result = BookServiceHandler().get()

    print("id_playlist:",  id_playlist)
    print("name_playlist", name_playlist)
    
    return render_template("add_playlist.html",
                           list=result, 
                           id_playlist = id_playlist,
                           name_playlist = name_playlist)

 # POST - Adicionar Livro
@app.route("/api/adicionar/livro/colecao", methods=["POST"])
def post_book():   
    
    id_playlist = int(request.form.get('id_playlist'))
    name_playlist = request.form.get('name_playlist')
    id_book = int(request.form.get('id_book'))
    name_book = request.form.get('name_book')

    data = PlaylistSystem()
    new_data = data.insert_book_to_playlist(
        name_playlist,
        id_playlist,
        name_book,
        id_book,  
    )

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