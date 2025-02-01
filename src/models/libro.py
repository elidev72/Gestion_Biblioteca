from src.database.db_mysql import db

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    stock = db.relationship('LibroStock', backref='libro', uselist=False, lazy='noload')

    def __repr__(self):
        return f"Libro(id='{self.id}', nombre='{self.nombre}', anio='{self.anio}', autor='{self.autor}', genero='{self.genero}')"
