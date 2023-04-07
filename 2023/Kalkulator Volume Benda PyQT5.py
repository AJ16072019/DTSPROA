import sys
import math
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QLineEdit, QPushButton, QVBoxLayout


class VolumeBenda(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi Hitung Volume Benda')
        self.setGeometry(100, 100, 400, 300)

        # Set the window icon
        self.setWindowIcon(QIcon('calculator_icon.png'))

        # Widget radio button untuk memilih bentuk benda
        self.lbl_pilih_bentuk = QLabel('Pilih bentuk benda:', self)
        self.lbl_pilih_bentuk.move(20, 20)

        self.rb_balok = QRadioButton('Balok', self)
        self.rb_balok.move(20, 40)
        self.rb_balok.clicked.connect(self.show_balok)

        self.rb_bola = QRadioButton('Bola', self)
        self.rb_bola.move(20, 60)
        self.rb_bola.clicked.connect(self.show_bola)

        self.rb_tabung = QRadioButton('Tabung', self)
        self.rb_tabung.move(20, 80)
        self.rb_tabung.clicked.connect(self.show_tabung)

        # Widget text variable yang dibutuhkan
        self.lbl_panjang = QLabel('Panjang:', self)
        self.lbl_panjang.move(20, 120)
        self.lbl_panjang.hide()

        self.le_panjang = QLineEdit(self)
        self.le_panjang.move(120, 120)
        self.le_panjang.hide()

        self.lbl_lebar = QLabel('Lebar:', self)
        self.lbl_lebar.move(20, 150)
        self.lbl_lebar.hide()

        self.le_lebar = QLineEdit(self)
        self.le_lebar.move(120, 150)
        self.le_lebar.hide()

        self.lbl_tinggi = QLabel('Tinggi:', self)
        self.lbl_tinggi.move(20, 180)
        self.lbl_tinggi.hide()

        self.le_tinggi = QLineEdit(self)
        self.le_tinggi.move(120, 180)
        self.le_tinggi.hide()

        self.lbl_jari = QLabel('Jari-jari:', self)
        self.lbl_jari.move(20, 120)
        self.lbl_jari.hide()

        self.le_jari = QLineEdit(self)
        self.le_jari.move(120, 120)
        self.le_jari.hide()

        self.lbl_tinggi_tabung = QLabel('Tinggi:', self)
        self.lbl_tinggi_tabung.move(20, 150)
        self.lbl_tinggi_tabung.hide()

        self.le_tinggi_tabung = QLineEdit(self)
        self.le_tinggi_tabung.move(120, 150)
        self.le_tinggi_tabung.hide()

        # Widget button untuk menghitung volume
        self.btn_hitung = QPushButton('Hitung', self)
        self.btn_hitung.move(20, 220)
        self.btn_hitung.clicked.connect(self.hitung_volume)

        # Widget label untuk menampilkan hasil
        self.lbl_hasil = QLabel('Hasil:', self)
        self.lbl_hasil.move(20, 260)
        self.lbl_hasil.setStyleSheet('font-size: 20pt; font-weight: bold; color: black')

    def show_balok(self):
        self.lbl_panjang.show()
        self.le_panjang.show()

        self.lbl_lebar.show()
        self.le_lebar.show()

        self.lbl_tinggi.show()
        self.le_tinggi.show()

        self.lbl_jari.hide()
        self.le_jari.hide()

        self.lbl_tinggi_tabung.hide()
        self.le_tinggi_tabung.hide()

    def show_bola(self):
        self.lbl_panjang.hide()
        self.le_panjang.hide()

        self.lbl_lebar.hide()
        self.le_lebar.hide()

        self.lbl_tinggi.hide()
        self.le_tinggi.hide()

        self.lbl_jari.show()
        self.le_jari.show()

        self.lbl_tinggi_tabung.hide()
        self.le_tinggi_tabung.hide()

    def show_tabung(self):
        self.lbl_panjang.hide()
        self.le_panjang.hide()

        self.lbl_lebar.hide()
        self.le_lebar.hide()

        self.lbl_tinggi.hide()
        self.le_tinggi.hide()

        self.lbl_jari.show()
        self.le_jari.show()

        self.lbl_tinggi_tabung.show()
        self.le_tinggi_tabung.show()

    def hitung_volume(self):
        if self.rb_balok.isChecked():
            panjang = float(self.le_panjang.text())
            lebar = float(self.le_lebar.text())
            tinggi = float(self.le_tinggi.text())
            volume = panjang * lebar * tinggi
        elif self.rb_bola.isChecked():
            jari = float(self.le_jari.text())
            volume = (4/3) * math.pi * jari ** 3      
        elif self.rb_tabung.isChecked():
            jari = float(self.le_jari.text())
            tinggi = float(self.le_tinggi_tabung.text())
            volume = math.pi * jari ** 2 * tinggi
        else:
            volume = 0

        # Menampilkan hasil volume dengan format angka desimal dua digit dan font ukuran 20pt, tebal, dan warna hitam
        self.lbl_hasil.setText(f'Hasil: {volume:.4f}')
        self.lbl_hasil.adjustSize()
        self.lbl_hasil.setStyleSheet('font-size: 20pt; font-weight: bold; color: black')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VolumeBenda()
    ex.show()
    sys.exit(app.exec_())
