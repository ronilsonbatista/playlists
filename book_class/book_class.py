from config import app, db, ma
from flask import jsonify

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

@app.route("/")
def home():
    return "Books" 

@app.route("/api/book", methods=["GET"])
def class_list():
    classes = Book.query.all()
    schema = all_classes_schema.dump(classes)
    return jsonify(schema)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12300, debug=True)
