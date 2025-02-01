from src.database.db_mysql import db

class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    entregado = db.Column(db.Boolean, default=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    libro_id = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    bibliotecario_id = db.Column(db.Integer, db.ForeignKey('bibliotecario.id'), nullable=False)
    
    def __repr__(self):
        return f"Prestamo(id='{self.id}', fecha_inicio='{self.fecha_inicio}', fecha_fin='{self.fecha_fin}', entregado='{self.entregado}', cliente_id='{self.cliente_id}', libro_id='{self.libro_id}', bibliotecario_id='{self.bibliotecario_id}')"
    