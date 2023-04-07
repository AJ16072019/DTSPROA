# Impor modul yang dibutuhkan
import math
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QLineEdit, QPushButton, QVBoxLayout

# Membuat kelas VolumeBenda yang merupakan turunan dari kelas QWidget
class VolumeBenda(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aplikasi Hitung Volume Benda')
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon('calculator_icon.png'))
        
        # Menambahkan beberapa widget seperti QLabel dan QLineEdit yang akan digunakan untuk input nilai
        self.widgets = [
            {'label': QLabel('Panjang:', self), 'name': 'le_panjang', 'pos': (20, 120)},
            {'label': QLabel('Lebar:', self), 'name': 'le_lebar', 'pos': (20, 150)},
            {'label': QLabel('Tinggi:', self), 'name': 'le_tinggi', 'pos': (20, 180)},
            {'label': QLabel('Jari-jari:', self), 'name': 'le_jari', 'pos': (20, 120)},
            {'label': QLabel('Tinggi:', self), 'name': 'le_tinggi_tabung', 'pos': (20, 150)},
        ]

        # Menambahkan widget yang telah dibuat ke dalam objek VolumeBenda dan mengatur posisi serta visibility-nya
        for widget in self.widgets:
            widget['label'].move(*widget['pos'])
            setattr(self, widget['name'], QLineEdit(self))
            getattr(self, widget['name']).move(widget['pos'][0] + 100, widget['pos'][1])
            widget['label'].hide()
            getattr(self, widget['name']).hide()

        # Menambahkan beberapa RadioButton yang akan digunakan untuk memilih bentuk benda
        self.rb_balok = QRadioButton('Balok', self)
        self.rb_balok.move(20, 40)
        self.rb_balok.clicked.connect(lambda: self.show_hide(0, 1, 2, hide=[3, 4]))

        self.rb_bola = QRadioButton('Bola', self)
        self.rb_bola.move(20, 60)
        self.rb_bola.clicked.connect(lambda: self.show_hide(3, hide=[0, 1, 2, 4]))

        self.rb_tabung = QRadioButton('Tabung', self)
        self.rb_tabung.move(20, 80)
        self.rb_tabung.clicked.connect(lambda: self.show_hide(3, 4, hide=[0, 1, 2]))

        # Menambahkan button Hitung dan mengatur posisinya
        self.btn_hitung = QPushButton('Hitung', self)
        self.btn_hitung.move(20, 220)
        self.btn_hitung.clicked.connect(self.hitung_volume)

        # Menambahkan label Pilih bentuk benda dan Hasil
        self.lbl_pilih_bentuk = QLabel('Pilih bentuk benda:', self)
        self.lbl_pilih_bentuk.move(20, 20)
        self.lbl_hasil = QLabel('Hasil:', self)
        self.lbl_hasil.move(20, 260)
        self.lbl_hasil.setStyleSheet('font-size: 15pt; font-weight: bold; color: black')

    # Fungsi untuk menampilkan atau menyembunyikan widget-widget tertentu pada interface.
    def show_hide(self, *indices, hide=[]):
        for i, widget in enumerate(self.widgets):
            widget['label'].setVisible(i in indices and i not in hide)
            getattr(self, widget['name']).setVisible(i in indices and i not in hide)

    # Fungsi untuk menghitung volume dari bentuk bangun ruang yang dipilih.
    def hitung_volume(self):
        valid_input = True
        if self.rb_balok.isChecked():
            try:
                panjang, lebar, tinggi = [float(getattr(self, widget['name']).text().replace(',', '.')) for widget in self.widgets[:3]]
                volume = panjang * lebar * tinggi
            except ValueError:
                valid_input = False
        elif self.rb_bola.isChecked():
            try:
                jari_jari = float(self.le_jari.text().replace(',', '.'))
                volume = (4 / 3) * math.pi * jari_jari ** 3
            except ValueError:
                valid_input = False
        elif self.rb_tabung.isChecked():
            try:
                jari_jari, tinggi = [float(getattr(self, widget['name']).text().replace(',', '.')) for widget in self.widgets[3:]]
                volume = math.pi * jari_jari ** 2 * tinggi
            except ValueError:
                valid_input = False
        else:
            volume = 0

        # Untuk mengecheck apakah input yang dimasukkan valid atau tidak.
        if not valid_input:
            self.lbl_hasil.setText('Masukkan angka valid')
            self.lbl_hasil.setFixedWidth(300)
            return

        # Menampilkan hasil volume dengan format angka desimal dua digit dan font ukuran 20pt, tebal, dan warna hitam
        self.lbl_hasil.setText(f'Hasil: {volume:.4f}')
        self.lbl_hasil.adjustSize()

# Script ini untuk mengaktifkan aplikasi ini
if __name__ == '__main__':
    app = QApplication([])
    form = VolumeBenda()
    form.show()
    app.exec_()

