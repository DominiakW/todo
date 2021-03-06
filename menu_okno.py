#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QComboBox, QCheckBox, QMessageBox, QLabel, QGridLayout, QApplication, QWidget
from PyQt5.QtCore import Qt
import os

class WindowSprezarka(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def wstecz(self):
        self.w = Menu()
        self.w.show()
        self.close()

    def zapisz(self):
        lista=[self.wydajnoscEdt.text(), self.pmaxEdt.text(), self.pminEdt.text()]
        plik=open('WIPS\Sprezarki\\'+self.nazwaSprężarkiEdt.text()+".txt", "w")
        for i in (lista):
            plik.write(i+"\n")
        plik.close
        self.w = Menu()
        self.w.show()
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.w = Menu()
            self.w.show()
            self.close()

    def interfejs(self):
        # etykiety
        etykietaNazwaSprężarki = QLabel("Nazwa sprężarki:", self)
        etykietaWydajnosc = QLabel("Wydajność układu [l/min]:", self)
        etykietaPmax = QLabel("Ciśnienie maksymalne [bar]:", self)
        etykietaPmin = QLabel("Ciśnienie minimalne [bar]:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykietaNazwaSprężarki, 0, 0)
        ukladT.addWidget(etykietaWydajnosc, 1, 0)
        ukladT.addWidget(etykietaPmax, 2, 0)
        ukladT.addWidget(etykietaPmin, 3, 0)

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
        zapiszBtn.clicked.connect(self.zapisz)

        self.nazwaSprężarkiEdt.setFocus()
        self.setGeometry(800, 400, 400, 300)
        self.setWindowIcon(QIcon('WIPS\Data\lukasiewicz.png'))
        self.setWindowTitle("Nowa sprężarka")
        self.show()

class WindowTrasa(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def wstecz(self):
        self.w = Menu()
        self.w.show()
        self.close()

    def zapisz(self):
        liczbaStacjiNaGodzine=float(self.liczbaStacjiEdt.text())/(float(self.czasPodrozyEdt.text())/60)
        sredniCzas=float(self.czasPodrozyEdt.text())*60/float(self.liczbaStacjiEdt.text())
        tdyn=sredniCzas-float(self.czasPostojuEdt.text())
        lista=[self.predkoscEdt.text(), self.liczbaStacjiEdt.text(), self.czasPodrozyEdt.text(), str(liczbaStacjiNaGodzine), str(sredniCzas), self.czasPostojuEdt.text(), str(tdyn)]
        plik=open('WIPS\Trasy\\'+self.nazwaTrasyEdt.text()+".txt", "w")
        for i in (lista):
            plik.write(i+"\n")
        plik.close
        self.w = Menu()
        self.w.show()
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.w = Menu()
            self.w.show()
            self.close()

    def interfejs(self):
        # etykiety
        etykietaNazwaTrasy = QLabel("Nazwa trasy:", self)
        etykietaPredkosc = QLabel("Średnia prędkość [km/h]:", self)
        etykietaLiczbaStacji = QLabel("Liczba stacji (bez 1.):", self)
        etykietaCzasPodrozy = QLabel("Całkowity czas podróży [min]:", self)
        etykietaCzasPostoju = QLabel("Średni czas postoju [s]:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykietaNazwaTrasy, 0, 0)
        ukladT.addWidget(etykietaPredkosc, 1, 0)
        ukladT.addWidget(etykietaLiczbaStacji, 2, 0)
        ukladT.addWidget(etykietaCzasPodrozy, 3, 0)
        ukladT.addWidget(etykietaCzasPostoju, 4, 0)

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
        zapiszBtn.clicked.connect(self.zapisz)

        self.nazwaTrasyEdt.setFocus()
        self.setGeometry(800, 400, 400, 300)
        self.setWindowIcon(QIcon('WIPS\Data\lukasiewicz.png'))
        self.setWindowTitle("Nowa trasa")
        self.show()

class WindowCzlon(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def wstecz(self):
        self.w = Menu()
        self.w.show()
        self.close()

    def zapisz(self):
        pOtoczenia=1

        #def Hamulce1
        haumlcePojemnoscRobocza=float(self.hamulcePoleTloka.text())*float(self.hamulceSkokCylindra.text())/100
        hamulcePoborPowietrzaNaPojazd=float(self.hamulceLiczbaCylidnrowEdt.text())*((float(self.hamulceCisnienieCylindra.text())+pOtoczenia)*haumlcePojemnoscRobocza+float(self.hamulceCisnienieCylindra.text())*float(self.hamulceMartwaObjetosc.text()))/pOtoczenia

        #def Hamulce2
        hamulcePolePowierzchniRury=3.142/4*(float(self.hamulceSrednicaZewnetrzna.text())-2*float(self.hamulceSrednicaWewnetrzna.text()))*(float(self.hamulceSrednicaZewnetrzna.text())-2*float(self.hamulceSrednicaWewnetrzna.text()))/10000
        hamulcePoborPowietrzaRury=float(self.hamulceCisnienieCylindra.text())*hamulcePolePowierzchniRury*float(self.hamulceDlugoscOrurowania.text())*10/pOtoczenia

        #def Zawieszenie
        zawieszenieStatPobor=float(self.zawieszenieLiczbaMiechow.text())*(float(self.zawieszenieCisnieniePelny.text())-float(self.zawieszenieCisnieniePusty.text()))*float(self.zawieszenieObjetoscMiecha.text())/pOtoczenia
        zawieszenieDynPobor=float(self.zawieszenieLiczbaZaworow.text())*float(self.zawieszeniePoborPowietrza.text())

        #def Klocek
        klocekPoborCylinder=float(self.klocekLiczbaKlockow.text())*float(self.klocekObjetoscSkokowa.text())*(float(self.klocekMaksCisnienie.text())+pOtoczenia)/pOtoczenia
        klocekPolePowierzchniRury=3.142/4*(float(self.klocekZewnetrznaSrednica.text())-2*float(self.klocekWewnetrznaSrednica.text()))*(float(self.klocekZewnetrznaSrednica.text())-2*float(self.klocekWewnetrznaSrednica.text()))/10000
        klocekPoborRury=klocekPolePowierzchniRury*float(self.klocekeDlugoscOrurowania.text())*10*float(self.klocekMaksCisnienie.text())/pOtoczenia
        klocekPobor=klocekPoborRury+klocekPoborCylinder

        #def Piasecznice
        piasecznicePobor=float(self.piasLiczbaDysz.text())*float(self.piasPobor.text())*float(self.piasCzas.text())/60

        #def Smarownice
        smarownicePobor=float(self.smarLiczbaZaworow.text())*float(self.smarPobor.text())*float(self.smarCzas.text())/60

        #def Syreny
        syrenyPobor=float(self.syrenyLiczba.text())*float(self.syrenyPobor.text())*float(self.syrenyCzas.text())/60

        #def WC
        wcPobor=float(self.wcLiczba.text())*float(self.wcPobor.text())

        #def Wycieki
        wyciekiPoleRury=3.142/4*(float(self.zbiornikiRurySredZew.text())-2*float(self.zbiornikiRurySredWew.text()))*(float(self.zbiornikiRurySredZew.text())-2*float(self.zbiornikiRurySredWew.text()))/10000
        wyciekiObjetoscRur=wyciekiPoleRury*float(self.zbiornikiDlugoscOrurowania.text())*10
        wyciekiObjetosc=float(self.zbiornkiGlowny.text())+wyciekiObjetoscRur

        #def Zbiorniki
        zbiornikTot=(float(self.zbiornkiGlowny.text())+wyciekiObjetoscRur+float(self.zbiornikiZawieszenia.text())+float(self.zbiornikiHamulcy.text())+float(self.zbiornikiPozostale.text()))
        zbiornikiMiechow=float(self.zawieszenieLiczbaMiechow.text())*float(self.zawieszenieLiczbaMiechow.text())

        listaCzlon=[str(hamulcePoborPowietrzaNaPojazd),str(hamulcePoborPowietrzaRury),str(zawieszenieStatPobor),str(zawieszenieDynPobor),
                    str(klocekPobor), str(piasecznicePobor), str(smarownicePobor), str(syrenyPobor), str(wcPobor), str(wyciekiObjetosc),
                    str(zbiornikTot), str(zbiornikiMiechow)]

        plik=open('WIPS\Czlony\\'+self.nazwaCzlonuEdt.text()+".txt", "w")

        for i in (listaCzlon):
            plik.write(i+"\n")
        plik.close

        self.w = Menu()
        self.w.show()
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.w = Menu()
            self.w.show()
            self.close()

    def zerowanieHamulcy(self):
        listaHamulce=[self.hamulceLiczbaCylidnrowEdt, self.hamulceMartwaObjetosc, self.hamulcePoleTloka, self.hamulceCisnienieCylindra,
        self.hamulceCisnienieCylindra,self.hamulceSkokCylindra,self.hamulceSrednicaWewnetrzna,self.hamulceSrednicaZewnetrzna,self.hamulceDlugoscOrurowania]
        for i in (listaHamulce):
            i.setText("0")

    def zerowanieZawieszenia(self):
        listaZawieszenie=[self.zawieszenieObjetoscMiecha,self.zawieszenieLiczbaMiechow,self.zawieszenieCisnieniePusty,self.zawieszenieCisnieniePelny,self.zawieszenieLiczbaZaworow,
         self.zawieszeniePoborPowietrza]
        for i in (listaZawieszenie):
            i.setText("0")

    def zerowanieKlocka(self):
        listaKlocka=[self.klocekObjetoscSkokowa,self.klocekLiczbaKlockow,self.klocekMaksCisnienie,self.klocekWewnetrznaSrednica,
         self.klocekZewnetrznaSrednica,self.klocekeDlugoscOrurowania]
        for i in (listaKlocka):
            i.setText("0")

    def zerowaniePiasecznic(self):
        listaPias=[self.piasLiczbaDysz,self.piasPobor,self.piasCzas]
        for i in (listaPias):
            i.setText("0")

    def zerowanieSmarownic (self):
        listaSmar=[self.smarLiczbaZaworow,self.smarPobor, self.smarCzas]
        for i in (listaSmar):
            i.setText("0")

    def zerowanieSyren (self):
        listaSyren=[self.syrenyLiczba,self.syrenyPobor,self.syrenyCzas]
        for i in (listaSyren):
            i.setText("0")

    def zerowanieWc (self):
        listaWc=[self.wcLiczba,self.wcPobor]
        for i in (listaWc):
            i.setText("0")

    def interfejs(self):
        # etykiety
        etykietaNazwaCzlonu = QLabel("Nazwa członu:", self)

        etykietaHamulceLiczbaCylidnrow = QLabel("Liczba cylindrów [-]:", self)
        etykietaHamulceMartwaObjetosc = QLabel("Martwa objętość cylindra [l]:", self)
        etykietaHamulcePoleTloka = QLabel("Powierzchnia tłoka [dm]:", self)
        etykietaHamulceCisnienieCylindra = QLabel("Ciśnienie cylindra przy hamowaniu [bar]:", self)
        etykietaHamulceSkokCylindra = QLabel("Skok cylindra [mm]:", self)
        etykietaHamulceSrednicaWewnetrzna = QLabel("Średnica wewnętrzna rur: [mm]:", self)
        etykietaHamulceSrednicaZewnetrzna = QLabel("Średnica zewnętrzna rur: [mm]:", self)
        etykietaHamulceDlugoscOrurowania = QLabel("Długość orurowania: [m]:", self)

        etykietaZawieszenieObjetoscMiecha = QLabel("Objętość pojedyńczego miecha [l]:", self)
        etykietaZawieszenieLiczbaMiechow = QLabel("Liczba miechów [-]:", self)
        etykietaZawieszenieCisnieniePusty = QLabel("Ciśnienie przy pustym członie [bar]:", self)
        etykietaZawieszenieCisnieniePelny = QLabel("Ciśnienie przy pełnym członie [bar]:", self)
        etykietaZawieszenieLiczbaZaworow = QLabel("Liczba zaworów [-]:", self)
        etykietaZawieszeniePoborPowietrza = QLabel("Pobór powietrza przez zawory [l/min]:", self)

        etykietaKlocekObjetoscSkokowa = QLabel("Objętość skokowa cylindra [l]:", self)
        etykietaKlocekLiczbaKlockow = QLabel("Liczba klocków czyszczących [-]:", self)
        etykietaKlocekMaksCisnienie = QLabel("Maksymalne ciśnienie w cylidnrze [bar]:", self)
        etykietaKlocekWewnetrznaSrednica = QLabel("Srednica wewnętrzna rur: [mm]:", self)
        etykietaKlocekZewnetrznaSrednica = QLabel("Srednica zewnętrzna rur: [mm]:", self)
        etykietaKlocekeDlugoscOrurowania = QLabel("Długość orurowania: [m]:", self)

        etykietaPiasLiczbaDysz = QLabel("Liczba dysz [-]:", self)
        etykietaPiasPobor = QLabel("Pobór powietrza [l/min]:", self)
        etykietaPiasCzas = QLabel("Czas aplikacji [s]:", self)

        etykietaSmarLiczbaZaworow = QLabel("Liczba zaworów [-]:", self)
        etykietaSmarPobor = QLabel("Pobór powietrza przez zawór [l/min]:", self)
        etykietaSmarCzas = QLabel("Czas aplikacji [s]:", self)

        etykietaSyrenyLiczba = QLabel("Liczba syren [-]:", self)
        etykietaSyrenyPobor = QLabel("Pobór powietrza przez syrenę [l/min]:", self)
        etykietaSyrenyCzas = QLabel("Czas aplikacji [s]:", self)

        etykietaWcLiczba = QLabel("Liczba toalet [-]:", self)
        etykietaWcPobor = QLabel("Pobór powietrza przez toaletę [l/min]:", self)

        etykietaZbiorniki = QLabel("Zbiorniki", self)
        etykietaZbiornikiGłowny = QLabel("Objętość zbiornika głównego [l]:", self)
        etykietaZbiornikiZawieszenia = QLabel("Objętość zbiorników zawieszenia [l]:", self)
        etykietaZbiornikiHamulcy = QLabel("Objętość zbiorników hamulcowych [l]:", self)
        etykietaZbiornikiPozostale = QLabel("Objętość zbiorników pozostałych [l]:", self)
        etykietaZbiornikiRuryDlugosc = QLabel("Długość orurowania zbiornika głównego [m]:", self)
        etykietaZbiornikiRuraWew = QLabel("Średnica wewnętrzna rur [mm]:", self)
        etykietaZbiornikiRuraZew = QLabel("Średnica zewnętrzna rur [mm]:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykietaNazwaCzlonu, 0, 0)

        ukladT.addWidget(etykietaHamulceLiczbaCylidnrow, 2, 0)
        ukladT.addWidget(etykietaHamulceMartwaObjetosc, 3, 0)
        ukladT.addWidget(etykietaHamulcePoleTloka, 4, 0)
        ukladT.addWidget(etykietaHamulceCisnienieCylindra, 5, 0)
        ukladT.addWidget(etykietaHamulceSkokCylindra, 6, 0)
        ukladT.addWidget(etykietaHamulceSrednicaWewnetrzna, 7, 0)
        ukladT.addWidget(etykietaHamulceSrednicaZewnetrzna, 8, 0)
        ukladT.addWidget(etykietaHamulceDlugoscOrurowania, 9, 0)

        ukladT.addWidget(etykietaZawieszenieObjetoscMiecha, 2, 2)
        ukladT.addWidget(etykietaZawieszenieLiczbaMiechow, 3, 2)
        ukladT.addWidget(etykietaZawieszenieCisnieniePusty, 4, 2)
        ukladT.addWidget(etykietaZawieszenieCisnieniePelny, 5, 2)
        ukladT.addWidget(etykietaZawieszenieLiczbaZaworow, 6, 2)
        ukladT.addWidget(etykietaZawieszeniePoborPowietrza, 7, 2)

        ukladT.addWidget(etykietaKlocekObjetoscSkokowa, 2, 4)
        ukladT.addWidget(etykietaKlocekLiczbaKlockow, 3, 4)
        ukladT.addWidget(etykietaKlocekMaksCisnienie, 4, 4)
        ukladT.addWidget(etykietaKlocekWewnetrznaSrednica, 5, 4)
        ukladT.addWidget(etykietaKlocekZewnetrznaSrednica, 6, 4)
        ukladT.addWidget(etykietaKlocekeDlugoscOrurowania, 7, 4)

        ukladT.addWidget(etykietaPiasLiczbaDysz, 11, 0)
        ukladT.addWidget(etykietaPiasPobor, 12, 0)
        ukladT.addWidget(etykietaPiasCzas, 13, 0)

        ukladT.addWidget(etykietaSmarLiczbaZaworow, 11, 2)
        ukladT.addWidget(etykietaSmarPobor, 12, 2)
        ukladT.addWidget(etykietaSmarCzas, 13, 2)

        ukladT.addWidget(etykietaSyrenyLiczba, 11, 4)
        ukladT.addWidget(etykietaSyrenyPobor, 12, 4)
        ukladT.addWidget(etykietaSyrenyCzas, 13, 4)

        ukladT.addWidget(etykietaWcLiczba, 11, 6)
        ukladT.addWidget(etykietaWcPobor, 12, 6)

        ukladT.addWidget(etykietaZbiorniki, 1, 6)
        ukladT.addWidget(etykietaZbiornikiGłowny, 2, 6)
        ukladT.addWidget(etykietaZbiornikiZawieszenia, 3, 6)
        ukladT.addWidget(etykietaZbiornikiHamulcy, 4, 6)
        ukladT.addWidget(etykietaZbiornikiPozostale, 5, 6)
        ukladT.addWidget(etykietaZbiornikiRuryDlugosc, 6, 6)
        ukladT.addWidget(etykietaZbiornikiRuraWew, 7, 6)
        ukladT.addWidget(etykietaZbiornikiRuraZew, 8, 6)

        #checkboxy
        hamulceBtn = QCheckBox("Hamulce", self)
        ukladT.addWidget(hamulceBtn, 1, 0)

        zawieszenieBtn = QCheckBox("Zawieszenie pneumatyczne", self)
        ukladT.addWidget(zawieszenieBtn, 1, 2)

        klocekBtn = QCheckBox("Klocki czyszczące", self)
        ukladT.addWidget(klocekBtn, 1, 4)

        piaseczniceBtn = QCheckBox("Piasecznice", self)
        ukladT.addWidget(piaseczniceBtn, 10, 0)

        smarowniceBtn = QCheckBox("Smarownice obrzeży kół", self)
        ukladT.addWidget(smarowniceBtn, 10, 2)

        syrenyBtn = QCheckBox("Syreny", self)
        ukladT.addWidget(syrenyBtn, 10, 4)

        wcBtn = QCheckBox("WC", self)
        ukladT.addWidget(wcBtn, 10, 6)

        self.nazwaCzlonuEdt = QLineEdit()

        #HAMULCE1
        self.hamulceLiczbaCylidnrowEdt = QLineEdit()
        self.hamulceLiczbaCylidnrowEdt.setReadOnly(hamulceBtn.checkState()!=Qt.Checked)
        hamulceBtn.stateChanged.connect(lambda state: self.hamulceLiczbaCylidnrowEdt.setReadOnly(state!=Qt.Checked))

        self.hamulceMartwaObjetosc = QLineEdit()
        self.hamulceMartwaObjetosc.setReadOnly(hamulceBtn.checkState()!=Qt.Checked)
        hamulceBtn.stateChanged.connect(lambda state: self.hamulceMartwaObjetosc.setReadOnly(state!=Qt.Checked))

        self.hamulcePoleTloka = QLineEdit()
        self.hamulcePoleTloka.setReadOnly(hamulceBtn.checkState()!=Qt.Checked)
        hamulceBtn.stateChanged.connect(lambda state: self.hamulcePoleTloka.setReadOnly(state!=Qt.Checked))

        self.hamulceCisnienieCylindra = QLineEdit()
        self.hamulceCisnienieCylindra.setReadOnly(hamulceBtn.checkState()!=Qt.Checked)
        hamulceBtn.stateChanged.connect(lambda state: self.hamulceCisnienieCylindra.setReadOnly(state!=Qt.Checked))

        self.hamulceSkokCylindra = QLineEdit()
        self.hamulceSkokCylindra.setReadOnly(hamulceBtn.checkState()!=Qt.Checked)
        hamulceBtn.stateChanged.connect(lambda state: self.hamulceSkokCylindra.setReadOnly(state!=Qt.Checked))

        #Hamulce2
        self.hamulceSrednicaWewnetrzna = QLineEdit()
        self.hamulceSrednicaWewnetrzna.setReadOnly(hamulceBtn.checkState()!=Qt.Checked)
        hamulceBtn.stateChanged.connect(lambda state: self.hamulceSrednicaWewnetrzna.setReadOnly(state!=Qt.Checked))

        self.hamulceSrednicaZewnetrzna = QLineEdit()
        self.hamulceSrednicaZewnetrzna.setReadOnly(hamulceBtn.checkState()!=Qt.Checked)
        hamulceBtn.stateChanged.connect(lambda state: self.hamulceSrednicaZewnetrzna.setReadOnly(state!=Qt.Checked))

        self.hamulceDlugoscOrurowania = QLineEdit()
        self.hamulceDlugoscOrurowania.setReadOnly(hamulceBtn.checkState()!=Qt.Checked)
        hamulceBtn.stateChanged.connect(lambda state: self.hamulceDlugoscOrurowania.setReadOnly(state!=Qt.Checked))

        #ZAWIESZENIE
        self.zawieszenieObjetoscMiecha = QLineEdit()
        self.zawieszenieObjetoscMiecha.setReadOnly(zawieszenieBtn.checkState()!=Qt.Checked)
        zawieszenieBtn.stateChanged.connect(lambda state: self.zawieszenieObjetoscMiecha.setReadOnly(state!=Qt.Checked))

        self.zawieszenieLiczbaMiechow = QLineEdit()
        self.zawieszenieLiczbaMiechow.setReadOnly(zawieszenieBtn.checkState()!=Qt.Checked)
        zawieszenieBtn.stateChanged.connect(lambda state: self.zawieszenieLiczbaMiechow.setReadOnly(state!=Qt.Checked))

        self.zawieszenieCisnieniePusty = QLineEdit()
        self.zawieszenieCisnieniePusty.setReadOnly(zawieszenieBtn.checkState()!=Qt.Checked)
        zawieszenieBtn.stateChanged.connect(lambda state: self.zawieszenieCisnieniePusty.setReadOnly(state!=Qt.Checked))

        self.zawieszenieCisnieniePelny = QLineEdit()
        self.zawieszenieCisnieniePelny.setReadOnly(zawieszenieBtn.checkState()!=Qt.Checked)
        zawieszenieBtn.stateChanged.connect(lambda state: self.zawieszenieCisnieniePelny.setReadOnly(state!=Qt.Checked))

        self.zawieszenieLiczbaZaworow = QLineEdit()
        self.zawieszenieLiczbaZaworow.setReadOnly(zawieszenieBtn.checkState()!=Qt.Checked)
        zawieszenieBtn.stateChanged.connect(lambda state: self.zawieszenieLiczbaZaworow.setReadOnly(state!=Qt.Checked))

        self.zawieszeniePoborPowietrza = QLineEdit()
        self.zawieszeniePoborPowietrza.setReadOnly(zawieszenieBtn.checkState()!=Qt.Checked)
        zawieszenieBtn.stateChanged.connect(lambda state: self.zawieszeniePoborPowietrza.setReadOnly(state!=Qt.Checked))

        #KLOCEK
        self.klocekObjetoscSkokowa = QLineEdit()
        self.klocekObjetoscSkokowa.setReadOnly(klocekBtn.checkState()!=Qt.Checked)
        klocekBtn.stateChanged.connect(lambda state: self.klocekObjetoscSkokowa.setReadOnly(state!=Qt.Checked))

        self.klocekLiczbaKlockow = QLineEdit()
        self.klocekLiczbaKlockow.setReadOnly(klocekBtn.checkState()!=Qt.Checked)
        klocekBtn.stateChanged.connect(lambda state: self.klocekLiczbaKlockow.setReadOnly(state!=Qt.Checked))

        self.klocekMaksCisnienie = QLineEdit()
        self.klocekMaksCisnienie.setReadOnly(klocekBtn.checkState()!=Qt.Checked)
        klocekBtn.stateChanged.connect(lambda state: self.klocekMaksCisnienie.setReadOnly(state!=Qt.Checked))

        self.klocekWewnetrznaSrednica = QLineEdit()
        self.klocekWewnetrznaSrednica.setReadOnly(klocekBtn.checkState()!=Qt.Checked)
        klocekBtn.stateChanged.connect(lambda state: self.klocekWewnetrznaSrednica.setReadOnly(state!=Qt.Checked))

        self.klocekZewnetrznaSrednica = QLineEdit()
        self.klocekZewnetrznaSrednica.setReadOnly(klocekBtn.checkState()!=Qt.Checked)
        klocekBtn.stateChanged.connect(lambda state: self.klocekZewnetrznaSrednica.setReadOnly(state!=Qt.Checked))

        self.klocekeDlugoscOrurowania = QLineEdit()
        self.klocekeDlugoscOrurowania.setReadOnly(klocekBtn.checkState()!=Qt.Checked)
        klocekBtn.stateChanged.connect(lambda state: self.klocekeDlugoscOrurowania.setReadOnly(state!=Qt.Checked))

        #PIASECZNICE
        self.piasLiczbaDysz = QLineEdit()
        self.piasLiczbaDysz.setReadOnly(piaseczniceBtn.checkState()!=Qt.Checked)
        piaseczniceBtn.stateChanged.connect(lambda state: self.piasLiczbaDysz.setReadOnly(state!=Qt.Checked))

        self.piasPobor = QLineEdit()
        self.piasPobor.setReadOnly(piaseczniceBtn.checkState()!=Qt.Checked)
        piaseczniceBtn.stateChanged.connect(lambda state: self.piasPobor.setReadOnly(state!=Qt.Checked))

        self.piasCzas = QLineEdit()
        self.piasCzas.setReadOnly(piaseczniceBtn.checkState()!=Qt.Checked)
        piaseczniceBtn.stateChanged.connect(lambda state: self.piasCzas.setReadOnly(state!=Qt.Checked))

        #SMAROWNICE
        self.smarLiczbaZaworow = QLineEdit()
        self.smarLiczbaZaworow.setReadOnly(smarowniceBtn.checkState()!=Qt.Checked)
        smarowniceBtn.stateChanged.connect(lambda state: self.smarLiczbaZaworow.setReadOnly(state!=Qt.Checked))

        self.smarPobor = QLineEdit()
        self.smarPobor.setReadOnly(smarowniceBtn.checkState()!=Qt.Checked)
        smarowniceBtn.stateChanged.connect(lambda state: self.smarPobor.setReadOnly(state!=Qt.Checked))

        self.smarCzas = QLineEdit()
        self.smarCzas.setReadOnly(smarowniceBtn.checkState()!=Qt.Checked)
        smarowniceBtn.stateChanged.connect(lambda state: self.smarCzas.setReadOnly(state!=Qt.Checked))

        #SYRENY
        self.syrenyLiczba = QLineEdit()
        self.syrenyLiczba.setReadOnly(syrenyBtn.checkState()!=Qt.Checked)
        syrenyBtn.stateChanged.connect(lambda state: self.syrenyLiczba.setReadOnly(state!=Qt.Checked))

        self.syrenyPobor = QLineEdit()
        self.syrenyPobor.setReadOnly(syrenyBtn.checkState()!=Qt.Checked)
        syrenyBtn.stateChanged.connect(lambda state: self.syrenyPobor.setReadOnly(state!=Qt.Checked))

        self.syrenyCzas = QLineEdit()
        self.syrenyCzas.setReadOnly(syrenyBtn.checkState()!=Qt.Checked)
        syrenyBtn.stateChanged.connect(lambda state: self.syrenyCzas.setReadOnly(state!=Qt.Checked))

        #WC
        self.wcLiczba = QLineEdit()
        self.wcLiczba.setReadOnly(wcBtn.checkState()!=Qt.Checked)
        wcBtn.stateChanged.connect(lambda state: self.wcLiczba.setReadOnly(state!=Qt.Checked))

        self.wcPobor = QLineEdit()
        self.wcPobor.setReadOnly(wcBtn.checkState()!=Qt.Checked)
        wcBtn.stateChanged.connect(lambda state: self.wcPobor.setReadOnly(state!=Qt.Checked))

        #ZBIORNIKI
        self.zbiornkiGlowny = QLineEdit()
        self.zbiornikiZawieszenia = QLineEdit()
        self.zbiornikiHamulcy = QLineEdit()
        self.zbiornikiPozostale = QLineEdit()
        self.zbiornikiDlugoscOrurowania = QLineEdit()
        self.zbiornikiRurySredWew = QLineEdit()
        self.zbiornikiRurySredZew = QLineEdit()

        hamulceBtn.clicked.connect(self.zerowanieHamulcy)
        zawieszenieBtn.clicked.connect(self.zerowanieZawieszenia)
        klocekBtn.clicked.connect(self.zerowanieKlocka)
        piaseczniceBtn.clicked.connect(self.zerowaniePiasecznic)
        smarowniceBtn.clicked.connect(self.zerowanieSmarownic)
        syrenyBtn.clicked.connect(self.zerowanieSyren)
        wcBtn.clicked.connect(self.zerowanieWc)

        listaZerowanie =[self.hamulceLiczbaCylidnrowEdt, self.hamulceMartwaObjetosc, self.hamulcePoleTloka, self.hamulceCisnienieCylindra,
         self.hamulceCisnienieCylindra,self.hamulceSkokCylindra,self.hamulceSrednicaWewnetrzna,self.hamulceSrednicaZewnetrzna,self.hamulceDlugoscOrurowania,
         self.zawieszenieObjetoscMiecha,self.zawieszenieLiczbaMiechow,self.zawieszenieCisnieniePusty,self.zawieszenieCisnieniePelny,self.zawieszenieLiczbaZaworow,
         self.zawieszeniePoborPowietrza,self.klocekObjetoscSkokowa,self.klocekLiczbaKlockow,self.klocekMaksCisnienie,self.klocekWewnetrznaSrednica,
         self.klocekZewnetrznaSrednica,self.klocekeDlugoscOrurowania,self.piasLiczbaDysz,self.piasPobor,self.piasCzas,self.smarLiczbaZaworow,self.smarPobor,
         self.smarCzas,self.syrenyLiczba,self.syrenyPobor,self.syrenyCzas,self.wcLiczba,self.wcPobor,self.zbiornkiGlowny,self.zbiornikiZawieszenia,
         self.zbiornikiHamulcy,self.zbiornikiPozostale,self.zbiornikiDlugoscOrurowania,self.zbiornikiRurySredZew, self.zbiornikiRurySredWew]

        for i in (listaZerowanie):
             i.setText("0")

        ukladT.addWidget(self.nazwaCzlonuEdt, 0, 1)

        ukladT.addWidget(self.hamulceLiczbaCylidnrowEdt, 2, 1)
        ukladT.addWidget(self.hamulceMartwaObjetosc, 3, 1)
        ukladT.addWidget(self.hamulcePoleTloka, 4, 1)
        ukladT.addWidget(self.hamulceCisnienieCylindra, 5, 1)
        ukladT.addWidget(self.hamulceSkokCylindra, 6, 1)
        ukladT.addWidget(self.hamulceSrednicaWewnetrzna, 7, 1)
        ukladT.addWidget(self.hamulceSrednicaZewnetrzna, 8, 1)
        ukladT.addWidget(self.hamulceDlugoscOrurowania, 9, 1)

        ukladT.addWidget(self.zawieszenieObjetoscMiecha, 2, 3)
        ukladT.addWidget(self.zawieszenieLiczbaMiechow, 3, 3)
        ukladT.addWidget(self.zawieszenieCisnieniePusty, 4, 3)
        ukladT.addWidget(self.zawieszenieCisnieniePelny, 5, 3)
        ukladT.addWidget(self.zawieszenieLiczbaZaworow, 6, 3)
        ukladT.addWidget(self.zawieszeniePoborPowietrza, 7, 3)

        ukladT.addWidget(self.klocekObjetoscSkokowa, 2, 5)
        ukladT.addWidget(self.klocekLiczbaKlockow, 3, 5)
        ukladT.addWidget(self.klocekMaksCisnienie, 4, 5)
        ukladT.addWidget(self.klocekWewnetrznaSrednica, 5, 5)
        ukladT.addWidget(self.klocekZewnetrznaSrednica, 6, 5)
        ukladT.addWidget(self.klocekeDlugoscOrurowania, 7, 5)

        ukladT.addWidget(self.piasLiczbaDysz, 11, 1)
        ukladT.addWidget(self.piasPobor, 12, 1)
        ukladT.addWidget(self.piasCzas, 13, 1)

        ukladT.addWidget(self.smarLiczbaZaworow, 11, 3)
        ukladT.addWidget(self.smarPobor, 12, 3)
        ukladT.addWidget(self.smarCzas, 13, 3)

        ukladT.addWidget(self.syrenyLiczba, 11, 5)
        ukladT.addWidget(self.syrenyPobor, 12, 5)
        ukladT.addWidget(self.syrenyCzas, 13, 5)

        ukladT.addWidget(self.wcLiczba, 11, 7)
        ukladT.addWidget(self.wcPobor, 12, 7)

        ukladT.addWidget(self.zbiornkiGlowny, 2, 7)
        ukladT.addWidget(self.zbiornikiZawieszenia, 3, 7)
        ukladT.addWidget(self.zbiornikiHamulcy, 4, 7)
        ukladT.addWidget(self.zbiornikiPozostale, 5, 7)
        ukladT.addWidget(self.zbiornikiDlugoscOrurowania, 6, 7)
        ukladT.addWidget(self.zbiornikiRurySredWew, 7, 7)
        ukladT.addWidget(self.zbiornikiRurySredZew, 8, 7)

        # przyciski
        zapiszBtn = QPushButton("&Zapisz", self)
        wsteczBtn = QPushButton("&Wstecz", self)
        wsteczBtn.resize(wsteczBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(zapiszBtn)

        ukladT.addLayout(ukladH, 14, 7, 1, 1)
        ukladT.addWidget(wsteczBtn, 14, 0, 1, 1)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        wsteczBtn.clicked.connect(self.wstecz)
        zapiszBtn.clicked.connect(self.zapisz)

        self.nazwaCzlonuEdt.setFocus()
        self.setGeometry(300, 100, 1400, 800)
        self.setWindowIcon(QIcon('WIPS\Data\lukasiewicz.png'))
        self.setWindowTitle("Nowy człon")
        self.show()

class WindowBadanie(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def wstecz(self):
        self.w = Menu()
        self.w.show()
        self.close()

    def uruchom(self):
        badaneListaCzlony=[]
        badanieListaTrasa=[]

        plikCzlon=open('WIPS\Czlony\\'+str(self.czlonEdt.currentText())+'.txt', "r")
        for i in plikCzlon:
            badaneListaCzlony.append(float(i))

        plikTrasa=open('WIPS\Trasy\\'+str(self.trasaEdt.currentText())+'.txt', "r")
        for i in plikTrasa:
            badanieListaTrasa.append(float(i))

        #def Hamulce1
        listaQhamulce=[]
        listaKbr=[1.05, 1.1,1.15] #kBr min,nor,max
        for i in (listaKbr):
            p=badaneListaCzlony[0]*i*float(self.iloscEdt.text())*(badanieListaTrasa[3]/60)
            listaQhamulce.append(p)

        #def Hamulce2
        listaQhamulce2=[]
        for i in (listaKbr):
            p=badaneListaCzlony[1]*i*float(self.iloscEdt.text())*(badanieListaTrasa[3]/60)
            listaQhamulce2.append(p)

        #def Zawieszeniestat
        listaQzawieszenieStat=[]
        listaKas=[0.05,0.08,0.1]
        for i in (listaKas):
            p=badaneListaCzlony[2]*i*float(self.iloscEdt.text())*(badanieListaTrasa[3]/60)
            listaQzawieszenieStat.append(p)

        #def Zawieszeniedyn
        listaQzawieszenieDyn=[]
        listaKdyn=[0.75,1,1.25]
        kdyn=(badanieListaTrasa[6]/badanieListaTrasa[4])
        for i in (listaKdyn):
            p=badaneListaCzlony[3]*i*float(self.iloscEdt.text())*kdyn
            listaQzawieszenieDyn.append(p)

        #def Klocek
        listaQklocek=[]
        listaKsc=[1.05,1.1,1.15]
        for i in (listaKsc):
            p=badaneListaCzlony[4]*i*float(self.iloscEdt.text())*(badanieListaTrasa[3]/60)
            listaQklocek.append(p)

        #def Piasecznice
        listaQPias=[]
        listaKsdn=[0.05,0.1,0.15]
        for i in (listaKsdn):
            p=badaneListaCzlony[5]*i*float(self.iloscEdt.text())*(badanieListaTrasa[3]/60)
            listaQPias.append(p)

        #def Smarownica
        listaQSmar=[]
        listaNwfl=[1.8*badanieListaTrasa[0],2.8*badanieListaTrasa[0],3.8*badanieListaTrasa[0]]
        for i in (listaNwfl):
            p=badaneListaCzlony[6]*i/60*float(self.iloscEdt.text())
            listaQSmar.append(p)

        #def Syreny
        listaQSyreny=[]
        listaKho=[0.05,0.1,0.15]
        for i in (listaKho):
            p=badaneListaCzlony[7]*i*(badanieListaTrasa[3]/60)
            listaQSyreny.append(p)

        #def WC
        listaQwc=[]
        listaKwc=[0.8,1,1.2]
        for i in (listaKwc):
            p=badaneListaCzlony[8]*i
            listaQwc.append(p)

        #def Leak
        listaQwyciek=[]
        listaqwyciek=[0.05,0.1,0.2]
        for i in (listaqwyciek):
            p=badaneListaCzlony[9]*i/3*float(self.iloscEdt.text())
            listaQwyciek.append(p)

        listaQ=[[listaQhamulce],[listaQhamulce2],[listaQzawieszenieStat],[listaQzawieszenieDyn],[listaQklocek],[listaQPias],[listaQSmar],[listaQSyreny],[listaQwc],[listaQwyciek]]

        qlistend=[0,0,0] #min,nor,max

        for j in range (3):
            for i in (listaQ):
                qlistend[j]=qlistend[j]+i[0][j]

        vTotVeh=badaneListaCzlony[10]*float(self.iloscEdt.text())
        vAsVeh=badaneListaCzlony[11]*float(self.iloscEdt.text())
        qlistend.append(vTotVeh)
        qlistend.append(vAsVeh)

        plik=open('WIPS\Badania\\'+self.nazwaBadaniaEdt.text()+".txt", "w")

        for i in (qlistend):
            plik.write(str(i)+"\n")
        plik.close

        qnetmin=round(qlistend[0],2)
        qnetnor=round(qlistend[1],2)
        qnetmax=round(qlistend[2],2)

        msg=QMessageBox()
        msg.setWindowTitle("Wyniki")
        msg.setWindowIcon(QIcon('WIPS\Data\lukasiewicz.png'))
        msg.setText("Zapotrzebowanie EZT na powietrze: ")
        msg.setInformativeText("Qnet_veh MIN = "+str(qnetmin)+" l/min\nQnet_veh NOR = "+str(qnetnor)+" l/min\nQnet_veh MAX = "+str(qnetmax)+" l/min")
        msg.exec();

        self.w = Menu()
        self.w.show()
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.w = Menu()
            self.w.show()
            self.close()

    def interfejs(self):
        # etykiety
        etykietaNazwaBadania = QLabel("Nazwa badania:", self)
        etykietaTrasa = QLabel("Trasa: ", self)
        etykietaIlosc = QLabel("Ilość: ", self)
        etykietaCzlon = QLabel("Człon:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykietaNazwaBadania, 0, 0)
        ukladT.addWidget(etykietaTrasa, 1, 0)
        ukladT.addWidget(etykietaIlosc, 2, 2)
        ukladT.addWidget(etykietaCzlon, 2, 0)

        self.nazwaBadaniaEdt = QLineEdit()

        self.trasaEdt = QComboBox(self)

        listaTras=os.listdir('WIPS\Trasy/')
        for item in (listaTras):
            if item.endswith(".txt"):
                item=item[:-4]
            self.trasaEdt.addItem(item)

        self.czlonEdt = QComboBox(self)

        listaCzlonow=os.listdir('WIPS\Czlony/')
        for item in (listaCzlonow):
            if item.endswith(".txt"):
                item=item[:-4]
            self.czlonEdt.addItem(item)

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
        uruchomBtn.clicked.connect(self.uruchom)

        self.nazwaBadaniaEdt.setFocus()
        self.setGeometry(800, 400, 400, 300)
        self.setWindowIcon(QIcon('WIPS\Data\lukasiewicz.png'))
        self.setWindowTitle("Nowe badanie")
        self.show()

class WindowCykle(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def wstecz(self):
        self.w = Menu()
        self.w.show()
        self.close()

    def uruchom(self):
        cykleLista=[]

        plikBadanie=open('WIPS\Badania\\'+str(self.wynikEdt.currentText())+'.txt', "r")
        for i in plikBadanie:
            cykleLista.append(float(i))

        cykleSprezarka=[]

        plikBadanie=open('WIPS\Sprezarki\\'+str(self.sprezarkaEdt.currentText())+'.txt', "r")
        for i in plikBadanie:
            cykleSprezarka.append(float(i))

        #def Cykle
        listatON=[]
        for i in range (3):
            p=cykleLista[3]*(cykleSprezarka[1]-cykleSprezarka[2])/1/(float(self.sprezarkaIlosc.text())*cykleSprezarka[0]-cykleLista[i])
            listatON.append(p)

        listatOFF=[]
        for i in range (3):
            p=cykleLista[3]*(cykleSprezarka[1]-cykleSprezarka[2])/1/(cykleLista[i])
            listatOFF.append(p)

        listatCycle=[]
        for i in range (3):
            p=listatON[i]+listatOFF[i]
            listatCycle.append(p)

        listatFcomp=[]
        for i in range (3):
            p=60/listatCycle[i]
            listatFcomp.append(p)

        listatDCcomp=[]
        for i in range (3):
            p=100*listatON[i]/(listatON[i]+listatOFF[i])
            listatDCcomp.append(p)

        #def Czas
        tCharge=(cykleLista[3]*(cykleSprezarka[1]-0)+cykleLista[4]*(3.4-0))/1/(float(self.sprezarkaIlosc.text())*cykleSprezarka[0])

        #def zapis
        plik=open('WIPS\Badania\\'+self.wynikEdt.currentText()+"_raport.txt", "w")

        plik.write("Qnet_veh_MIN = "+str(round(cykleLista[0],2))+" l/min\n")
        plik.write("Qnet_veh_NOR = "+str(round(cykleLista[1],2))+" l/min\n")
        plik.write("Qnet_veh_MAX = "+str(round(cykleLista[2],2))+" l/min\n\n")

        plik.write("tON_MIN = "+str(round(listatON[0],2))+" min\n")
        plik.write("tON_NOR = "+str(round(listatON[1],2))+" min\n")
        plik.write("tON_MAX = "+str(round(listatON[2],2))+" min\n\n")

        plik.write("tOFF_MIN = "+str(round(listatOFF[0],2))+" min\n")
        plik.write("tOFF_NOR = "+str(round(listatOFF[1],2))+" min\n")
        plik.write("tOFF_MAX = "+str(round(listatOFF[2],2))+" min\n\n")

        plik.write("tcycle_MIN = "+str(round(listatCycle[0],2))+" min\n")
        plik.write("tcycle_NOR = "+str(round(listatCycle[1],2))+" min\n")
        plik.write("tcycle_MAX = "+str(round(listatCycle[2],2))+" min\n\n")

        plik.write("fcomp_MIN = "+str(round(listatFcomp[0],2))+" 1/h\n")
        plik.write("fcomp_NOR = "+str(round(listatFcomp[1],2))+" 1/h\n")
        plik.write("fcomp_MAX = "+str(round(listatFcomp[2],2))+" 1/h\n\n")

        plik.write("DCcomp_MIN = "+str(round(listatDCcomp[0],2))+"%\n")
        plik.write("DCcomp_NOR = "+str(round(listatDCcomp[1],2))+"%\n")
        plik.write("DCcomp_MAX = "+str(round(listatDCcomp[2],2))+"%\n\n")

        plik.write("tcharge = " +str(round(tCharge,2))+" min")
        plik.close

        self.w = Menu()
        self.w.show()
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.w = Menu()
            self.w.show()
            self.close()

    def interfejs(self):
        # etykiety
        etykietaWynik= QLabel("Nazwa badania: ", self)
        etykietaSprezarka = QLabel("Sprężarka:", self)
        etykietaIlosc = QLabel("Ilość: ", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykietaWynik, 0, 0)
        ukladT.addWidget(etykietaIlosc, 1, 2)
        ukladT.addWidget(etykietaSprezarka, 1, 0)

        self.wynikEdt = QComboBox(self)
        listaWynikow=os.listdir('WIPS\Badania/')
        for item in (listaWynikow):
            if item.endswith(".txt"):
                item=item[:-4]
            self.wynikEdt.addItem(item)

        self.sprezarkaEdt = QComboBox(self)
        listaSprezarek=os.listdir('WIPS\Sprezarki/')
        for item in (listaSprezarek):
            if item.endswith(".txt"):
                item=item[:-4]
            self.sprezarkaEdt.addItem(item)

        self.sprezarkaIlosc=QLineEdit(self)

        ukladT.addWidget(self.wynikEdt, 0, 1)
        ukladT.addWidget(self.sprezarkaEdt, 1, 1)
        ukladT.addWidget(self.sprezarkaIlosc, 1, 3)

        # przyciski
        uruchomBtn = QPushButton("&Uruchom", self)
        wsteczBtn = QPushButton("&Wstecz", self)
        wsteczBtn.resize(wsteczBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(uruchomBtn)

        ukladT.addLayout(ukladH, 3, 0, 1, 4)
        ukladT.addWidget(wsteczBtn, 4, 0, 1, 4)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        wsteczBtn.clicked.connect(self.wstecz)
        uruchomBtn.clicked.connect(self.uruchom)

        self.setGeometry(800, 400, 400, 300)
        self.setWindowIcon(QIcon('WIPS\Data\lukasiewicz.png'))
        self.setWindowTitle("Cykle pracy")
        self.show()

class Menu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()

    def koniec(self):
        self.close()

    def wstecz(self):
        self.w = Menu()
        self.w.show()
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def interfejs(self):
        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()

        # przyciski
        dodajSprezarkeBtn = QPushButton("Dodaj sprężarkę", self)
        dodajTraseBtn = QPushButton("Dodaj trasę", self)
        dodajCzlonBtn = QPushButton("Dodaj człon", self)
        noweBadanieBtn = QPushButton("Badanie zapotrzebowania", self)
        noweCykleBtn = QPushButton("Badanie cykli", self)
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajSprezarkeBtn)
        ukladH.addWidget(dodajTraseBtn)
        ukladH.addWidget(dodajCzlonBtn)
        ukladH.addWidget(noweBadanieBtn)
        ukladH.addWidget(noweCykleBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        koniecBtn.clicked.connect(self.koniec)
        dodajSprezarkeBtn.clicked.connect(self.dodajSprezarke)
        dodajTraseBtn.clicked.connect(self.dodajTrase)
        dodajCzlonBtn.clicked.connect(self.dodajCzlon)
        noweBadanieBtn.clicked.connect(self.dodajBadanie)
        noweCykleBtn.clicked.connect(self.dodajBadanieCykli)

        self.setGeometry(600, 300, 800, 400)
        self.setWindowIcon(QIcon('WIPS\Data\lukasiewicz.png'))
        self.setWindowTitle("Menu")
        self.show()

    def dodajSprezarke(self):
        self.w = WindowSprezarka()
        self.w.show()
        self.close()

    def dodajTrase(self):
        self.w = WindowTrasa()
        self.w.show()
        self.close()

    def dodajCzlon(self):
        self.w = WindowCzlon()
        self.w.show()
        self.close()

    def dodajBadanie(self):
        self.w = WindowBadanie()
        self.w.show()
        self.close()

    def dodajBadanieCykli(self):
        self.w = WindowCykle()
        self.w.show()
        self.close()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Menu()
    sys.exit(app.exec_())