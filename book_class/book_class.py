import os.path
from config import app, db, database_file, project_dir
from flask import jsonify, render_template, request
from dateutil import parser

import sys
sys.path.insert(1, f"{project_dir}/../book_class/")
from book_system import BookSystem
from book_database import Book, BookSchema


@app.route("/api/home")
def home():
    return render_template("home.html")

#Adicionar Livros 
@app.route("/api/adicionar/livro")
def redirectAdd():
    return render_template("add_book.html")

@app.route("/api/salvar/livro", methods=["POST"])
def salvar_livro():
    titulo = request.form.get('titulo')
    isbn = request.form.get('isbn')
    autor = request.form.get('autor')
    genero = request.form.get('genero')

    print("titulo", titulo)
    print("isbn", isbn)
    print("autor", autor)
    print("genero", genero)

    book_system = BookSystem()
    book_system = book_system.insert_book(
       titulo,
        isbn,
        autor,
        genero
    )

    if book_system==True:
        return "Salvo"
    if book_system==False:
        return "Errorr"

# Remover coleção
@app.route("/api/remover/livro", methods=["POST"])
def redirectRemove():
    result = Book.query.all()

    return render_template("remove_book.html",
                           list=result)

# POST - Remover Livro por id 
@app.route("/api/remover", methods=["POST"])
def post_remove():
     remove_id = int(request.form.get('remove_id'))
     id = request.form.get('id-r')

     print("remove_id", remove_id)
     print("id", id)
     book_system = BookSystem()
     book_system.remove_book(remove_id)
    
     return "Salvo"

# Listar Livros
@app.route("/api/lista/livros", methods=["POST"])
def redirectList():
    classes = Book.query.all()
    list_book = BookSchema(many = True)
    return jsonify(list_book.dump(classes))

if __name__ == "__main__":
    if not os.path.exists(database_file):
        db.create_all()
    app.run(host="0.0.0.0", port=12300, debug=True)