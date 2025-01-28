from src.database.db_mysql import db

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)
    genero_id = db.Column(db.Integer, db.ForeignKey('genero.id'), nullable=False)
    stock = db.relationship('LibroStock', backref='libro', uselist=False, lazy='noload')

    def __repr__(self):
        return f"Libro(id='{self.id}', nombre='{self.nombre}', anio='{self.anio}', autor_id='{self.autor_id}', genero_id='{self.genero_id}')"
