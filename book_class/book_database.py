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