# run.py
from flask import Flask
from database import db
from controllers.kalkulator_controller import kalkulator_bp
from models import Perhitungan # Diperlukan untuk memastikan model dimuat dan terdaftar dengan SQLAlchemy
import os # Impor modul os untuk membuat secret key yang baik

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- TAMBAHKAN BARIS INI ---
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'super_secret_key_yang_sangat_sulit_ditebak_dan_panjang_sekali_untuk_produksi'
    # --------------------------

    db.init_app(app)
    app.register_blueprint(kalkulator_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)