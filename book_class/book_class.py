import os.path
from config import app, db, database_file, project_dir
from flask import jsonify, render_template, request
from dateutil import parser

import sys
sys.path.insert(1, f"{project_dir}/../book_class/")
from book_system import BookSystem
from book_database import Book, BookSchema

list_book = BookSchema(many = True)

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

     print("remove_id", remove_id)
     book_system = BookSystem()
     book_system.remove_book(remove_id)
    
     return "Salvo"

# Remover coleção
@app.route("/api/selecione/livro", methods=["POST"])
def redirectEdit():
    result = Book.query.all()

    return render_template("select_book.html",
                           list=result)

# POST - Edit Livro por id 
@app.route("/api/editar/livro", methods=["POST"])
def post_edit():
     edit_id = int(request.form.get('edit_id'))

     print("edit_id", edit_id)    
     book = Book.query.get(edit_id)
     print("titulo", book.titulo)  

     return render_template("edit_book.html", id=book.id, titulo=book.titulo, isbn=book.isbn, autor=book.autor)


@app.route("/api/salvar/edicao", methods=["POST"])
def salvar_edit():
    id = request.form.get('id')
    titulo = request.form.get('titulo')
    isbn = request.form.get('isbn')
    autor = request.form.get('autor')
    genero = request.form.get('genero')

    print("id", id)
    print("titulo", titulo)
    print("isbn", isbn)
    print("autor", autor)
    print("genero", genero)

    book_system = BookSystem()
    book_system = book_system.update_book(
        id,
        titulo,
        isbn,
        autor,
        genero
    )


    return "Salvo"

# Listar Livros
@app.route("/api/lista/livros", methods=["POST"])
def redirectList():
    classes = Book.query.all()
    return jsonify(list_book.dump(classes))

if __name__ == "__main__":
    if not os.path.exists(database_file):
        db.create_all()
    app.run(host="0.0.0.0", port=12300, debug=True)