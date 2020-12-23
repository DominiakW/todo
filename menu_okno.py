#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QComboBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

class WindowSprezarka(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def wstecz(self):
        self.w = Menu()
        self.w.show()
        self.hide()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.w = Menu()
            self.w.show()
            self.hide()

    def interfejs(self):

        # etykiety
        etykietaNazwaSprężarki = QLabel("Nazwa sprężarki:", self)
        etykietaWydajnosc = QLabel("Wydajność układu - Qcomp+AD [l/min]:", self)
        etykietaPmax = QLabel("Ciśnienie maksymalne - pmax [bar]:", self)
        etykietaPmin = QLabel("Ciśnienie minimalne - pmin [bar]:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykietaNazwaSprężarki, 0, 0)
        ukladT.addWidget(etykietaWydajnosc, 1, 0)
        ukladT.addWidget(etykietaPmax, 2, 0)
        ukladT.addWidget(etykietaPmin, 3, 0)

        # 1-liniowe pola edycyjne
        self.nazwaSprężarkiEdt = QLineEdit()
        self.wydajnoscEdt = QLineEdit()
        self.pmaxEdt = QLineEdit()
        self.pminEdt = QLineEdit()

        ukladT.addWidget(self.nazwaSprężarkiEdt, 0, 1)
        ukladT.addWidget(self.wydajnoscEdt, 1, 1)
        ukladT.addWidget(self.pmaxEdt, 2, 1)
        ukladT.addWidget(self.pminEdt, 3, 1)

        # przyciski
        zapiszBtn = QPushButton("&Zapisz", self)
        wsteczBtn = QPushButton("&Wstecz", self)
        wsteczBtn.resize(wsteczBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(zapiszBtn)

        ukladT.addLayout(ukladH, 4, 0, 1, 3)
        ukladT.addWidget(wsteczBtn, 5, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        wsteczBtn.clicked.connect(self.wstecz)
        zapiszBtn.clicked.connect(self.wstecz)

        self.nazwaSprężarkiEdt.setFocus()
        self.setGeometry(800, 400, 400, 300)
        self.setWindowIcon(QIcon('lukasiewicz.png'))
        self.setWindowTitle("Nowa sprężarka")
        self.show()

class WindowTrasa(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def wstecz(self):
        self.w = Menu()
        self.w.show()
        self.hide()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.w = Menu()
            self.w.show()
            self.hide()

    def interfejs(self):

        # etykiety
        etykietaNazwaTrasy = QLabel("Nazwa trasy:", self)
        etykietaPredkosc = QLabel("Średnia prędkość - V [km/h]:", self)
        etykietaLiczbaStacji = QLabel("Liczba stacji (bez 1.) - ns:", self)
        etykietaCzasPodrozy = QLabel("Całkowity czas podróży - T [min]:", self)
        etykietaCzasPostoju = QLabel("Średni czas postoju - tstat [s]:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykietaNazwaTrasy, 0, 0)
        ukladT.addWidget(etykietaPredkosc, 1, 0)
        ukladT.addWidget(etykietaLiczbaStacji, 2, 0)
        ukladT.addWidget(etykietaCzasPodrozy, 3, 0)
        ukladT.addWidget(etykietaCzasPostoju, 4, 0)

        # 1-liniowe pola edycyjne
        self.nazwaTrasyEdt = QLineEdit()
        self.predkoscEdt = QLineEdit()
        self.liczbaStacjiEdt = QLineEdit()
        self.czasPodrozyEdt = QLineEdit()
        self.czasPostojuEdt = QLineEdit()

        ukladT.addWidget(self.nazwaTrasyEdt, 0, 1)
        ukladT.addWidget(self.predkoscEdt, 1, 1)
        ukladT.addWidget(self.liczbaStacjiEdt, 2, 1)
        ukladT.addWidget(self.czasPodrozyEdt, 3, 1)
        ukladT.addWidget(self.czasPostojuEdt, 4, 1)

        # przyciski
        zapiszBtn = QPushButton("&Zapisz", self)
        wsteczBtn = QPushButton("&Wstecz", self)
        wsteczBtn.resize(wsteczBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(zapiszBtn)

        ukladT.addLayout(ukladH, 5, 0, 1, 3)
        ukladT.addWidget(wsteczBtn, 6, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        wsteczBtn.clicked.connect(self.wstecz)
        zapiszBtn.clicked.connect(self.wstecz)

        self.nazwaTrasyEdt.setFocus()
        self.setGeometry(800, 400, 400, 300)
        self.setWindowIcon(QIcon('lukasiewicz.png'))
        self.setWindowTitle("Nowa trasa")
        self.show()

class WindowCzlon(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def wstecz(self):
        self.w = Menu()
        self.w.show()
        self.hide()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.w = Menu()
            self.w.show()
            self.hide()

    def interfejs(self):

        # etykiety
        etykietaNazwaSprężarki = QLabel("Nazwa sprężarki:", self)
        etykietaWydajnosc = QLabel("Wydajność układu - Qcomp+AD [l/min]:", self)
        etykietaPmax = QLabel("Ciśnienie maksymalne - pmax [bar]:", self)
        etykietaPmin = QLabel("Ciśnienie minimalne - pmin [bar]:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykietaNazwaSprężarki, 0, 0)
        ukladT.addWidget(etykietaWydajnosc, 1, 0)
        ukladT.addWidget(etykietaPmax, 2, 0)
        ukladT.addWidget(etykietaPmin, 3, 0)

        # 1-liniowe pola edycyjne
        self.nazwaSprężarkiEdt = QLineEdit()
        self.wydajnoscEdt = QLineEdit()
        self.pmaxEdt = QLineEdit()
        self.pminEdt = QLineEdit()

        ukladT.addWidget(self.nazwaSprężarkiEdt, 0, 1)
        ukladT.addWidget(self.wydajnoscEdt, 1, 1)
        ukladT.addWidget(self.pmaxEdt, 2, 1)
        ukladT.addWidget(self.pminEdt, 3, 1)

        # przyciski
        zapiszBtn = QPushButton("&Zapisz", self)
        wsteczBtn = QPushButton("&Wstecz", self)
        wsteczBtn.resize(wsteczBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(zapiszBtn)

        ukladT.addLayout(ukladH, 4, 0, 1, 3)
        ukladT.addWidget(wsteczBtn, 5, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        wsteczBtn.clicked.connect(self.wstecz)
        zapiszBtn.clicked.connect(self.wstecz)

        self.nazwaSprężarkiEdt.setFocus()
        self.setGeometry(300, 100, 1400, 800)
        self.setWindowIcon(QIcon('lukasiewicz.png'))
        self.setWindowTitle("Nowa sprężarka")
        self.show()

class WindowBadanie(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def wstecz(self):
        self.w = Menu()
        self.w.show()
        self.hide()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.w = Menu()
            self.w.show()
            self.hide()

    def interfejs(self):

        # etykiety
        etykietaNazwaBadania = QLabel("Nazwa badania:", self)
        etykietaTrasa = QLabel("Trasa: ", self)
        etykietaIlosc = QLabel("Ilosc: ", self)
        etykietaCzlon = QLabel("Człon:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykietaNazwaBadania, 0, 0)
        ukladT.addWidget(etykietaTrasa, 1, 0)
        ukladT.addWidget(etykietaIlosc, 2, 2)
        ukladT.addWidget(etykietaCzlon, 2, 0)

        # 1-liniowe pola edycyjne
        self.nazwaBadaniaEdt = QLineEdit()
        self.trasaEdt = QComboBox(self)
        for v in ('E51', 'E59', 'E69'):
            self.trasaEdt.addItem(v)
        self.czlonEdt = QComboBox(self)
        for v in ('227', '228'):
            self.czlonEdt.addItem(v)
        self.iloscEdt = QLineEdit()

        ukladT.addWidget(self.nazwaBadaniaEdt, 0, 1)
        ukladT.addWidget(self.trasaEdt, 1, 1)
        ukladT.addWidget(self.iloscEdt, 2, 3)
        ukladT.addWidget(self.czlonEdt, 2, 1)

        # przyciski
        uruchomBtn = QPushButton("&Uruchom badanie", self)
        wsteczBtn = QPushButton("&Wstecz", self)
        wsteczBtn.resize(wsteczBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(uruchomBtn)

        ukladT.addLayout(ukladH, 3, 0, 1, 4)
        ukladT.addWidget(wsteczBtn, 4, 0, 1, 4)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        wsteczBtn.clicked.connect(self.wstecz)
        uruchomBtn.clicked.connect(self.wstecz)

        self.nazwaBadaniaEdt.setFocus()
        self.setGeometry(800, 400, 400, 300)
        self.setWindowIcon(QIcon('lukasiewicz.png'))
        self.setWindowTitle("Nowa sprężarka")
        self.show()

class Menu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def koniec(self):
        self.close()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def interfejs(self):
        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        # przyciski
        dodajSprezarkeBtn = QPushButton("Dodaj spręzarkę", self)
        dodajTraseBtn = QPushButton("Dodaj trasę", self)
        dodajCzlonBtn = QPushButton("Dodaj człon", self)
        noweBadanieBtn = QPushButton("Nowe badanie", self)
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajSprezarkeBtn)
        ukladH.addWidget(dodajTraseBtn)
        ukladH.addWidget(dodajCzlonBtn)
        ukladH.addWidget(noweBadanieBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        koniecBtn.clicked.connect(self.koniec)
        dodajSprezarkeBtn.clicked.connect(self.dodajSprezarke)
        dodajTraseBtn.clicked.connect(self.dodajTrase)
        dodajCzlonBtn.clicked.connect(self.dodajCzlon)
        noweBadanieBtn.clicked.connect(self.dodajBadanie)

        self.setGeometry(800, 400, 200, 200)
        self.setWindowIcon(QIcon('lukasiewicz.PNG'))
        self.setWindowTitle("Menu")
        self.show()

    def dodajSprezarke(self):
        self.w = WindowSprezarka()
        self.w.show()
        self.hide()

    def dodajTrase(self):
        self.w = WindowTrasa()
        self.w.show()
        self.hide()

    def dodajCzlon(self):
        self.w = WindowCzlon()
        self.w.show()
        self.hide()

    def dodajBadanie(self):
        self.w = WindowBadanie()
        self.w.show()
        self.hide()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Menu()
    sys.exit(app.exec_())