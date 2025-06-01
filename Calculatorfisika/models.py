# models.py
from database import db # Mengimpor instance db dari database.py

class Perhitungan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jenis = db.Column(db.String(50), nullable=False)
    hasil = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Perhitungan {self.jenis}: {self.hasil}>"