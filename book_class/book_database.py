from config import db, ma

# Criando tabelas 
class Book(db.Model):
    __tablename__ = "create_book_table"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(256), nullable=False)
    isbn = db.Column(db.String(256), nullable=False)
    autor = db.Column(db.String(256), nullable=False)
    genero = db.Column(db.String(256), nullable=False)

# Tratando Exibição dos json
class BookSchema(ma.SQLAlchemyAutoSchema):
    submitted = ma.Nested(Book, many=True)
    class Meta:
      model = Book

#Salvando no Banco 
class InsertBook():
    @staticmethod
    def insert_book(titulo, isbn, autor, genero) -> bool:
    
        if titulo==None or isbn==None or autor==None or genero == None: 
            return False

        new_data = {
            "titulo": titulo,
            "isbn": isbn,
            "autor": autor,
            "genero": genero,
        }
        print(new_data)

        submitted = Book(**new_data)
        db.session.add(submitted)
        db.session.commit()
        return True

 
class RemoveBook():

    @staticmethod
    def remove_book(id) -> bool:
        if id==None:
            return False
        

        id = Playlists.query.get(id)
        db.session.delete(id)
        db.session.commit()
        return True