from src.database.db_mysql import db

class Genero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(250))
    libros = db.relationship('Libro', backref='genero', lazy='dynamic')
    
    def __repr__(self):
        return f"Genero(id='{self.id}', nombre='{self.nombre}', descripcion='{self.descripcion}')"
