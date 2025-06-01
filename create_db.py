# create_db.py
from run import create_app # Mengimpor fungsi create_app
from database import db # Mengimpor instance db
from models import Perhitungan # Mengimpor model yang baru dibuat

app = create_app() # Membuat instance aplikasi

with app.app_context():
    db.create_all() # Membuat semua tabel yang terdaftar di db.Model
    print("Database tables created!")