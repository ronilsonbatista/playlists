from config import app, db, ma
from flask import jsonify, render_template, request

class Book(db.Model):
    __tablename__ = "book"
    book_id = db.Column(db.Integer(),
                   primary_key=True)
    name = db.Column(db.String(256), nullable=False, unique=True)


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        fields = ["name", "book_id"]

all_classes_schema = BookSchema(many = True)

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
    return "Savo"

# Remover coleção
@app.route("/api/remover/livro", methods=["POST"])
def redirectRemove():
    return render_template("remove_playlists.html")

@app.route("/api/lista/livros", methods=["POST"])
def redirectList():
    classes = Book.query.all()
    schema = all_classes_schema.dump(classes)
    return jsonify(schema)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12300, debug=True)
