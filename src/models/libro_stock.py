from src.database.db_mysql import db

class LibroStock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer, nullable=False)
    prestados = db.Column(db.Integer, default=0)
    libro_id = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    
    def prestar_libro(self) -> bool:
        prestado = False
        
        if self.prestados < self.total:
            self.prestados += 1
            prestado = True
            db.session.commit()
        
        return prestado
    
    def regresar_libro(self):
        if self.prestados > 0:
            self.prestados -= 1
            db.session.commit()
        else:
            raise ValueError("No hay libros prestados para regresar.")
    
    def __repr__(self):
        return f"LibroStock(id='{self.id}', total='{self.total}', prestados='{self.prestados}', libro_id='{self.libro_id}')"
    
