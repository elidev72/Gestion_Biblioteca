from src.database.db_mysql import db

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)
    genero_id = db.Column(db.Integer, db.ForeignKey('genero.id'), nullable=False)
