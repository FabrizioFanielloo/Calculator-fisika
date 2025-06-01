# controllers/kalkulator_controller.py
from flask import Blueprint, render_template, request, flash
from database import db
from models import Perhitungan # Pastikan ini diimpor

kalkulator_bp = Blueprint('kalkulator', __name__)

@kalkulator_bp.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    if request.method == 'POST':
        jenis_perhitungan = request.form.get('jenis')

        try:
            if jenis_perhitungan == 'ep':
                massa = float(request.form.get('massa_ep'))
                gravitasi = float(request.form.get('gravitasi_ep'))
                tinggi = float(request.form.get('tinggi_ep'))
                hasil = massa * gravitasi * tinggi
                jenis_nama = "Energi Potensial"
            elif jenis_perhitungan == 'ek':
                massa = float(request.form.get('massa_ek'))
                kecepatan = float(request.form.get('kecepatan_ek'))
                hasil = 0.5 * massa * (kecepatan ** 2)
                jenis_nama = "Energi Kinetik"
            elif jenis_perhitungan == 'usaha':
                gaya = float(request.form.get('gaya_usaha'))
                jarak = float(request.form.get('jarak_usaha'))
                hasil = gaya * jarak
                jenis_nama = "Usaha"
            else:
                flash("Jenis perhitungan tidak valid.", "error")
                return render_template('index.html', hasil=None)

            # Simpan hasil ke database
            new_perhitungan = Perhitungan(jenis=jenis_perhitungan, hasil=hasil)
            db.session.add(new_perhitungan)
            db.session.commit()
            flash(f"{jenis_nama} berhasil dihitung dan disimpan!", "success")

        except (ValueError, TypeError) as e:
            flash(f"Input tidak valid: {e}. Pastikan semua kolom terisi dengan angka.", "error")
            hasil = None
        except Exception as e:
            flash(f"Terjadi kesalahan: {e}", "error")
            hasil = None

    return render_template('index.html', hasil=hasil)