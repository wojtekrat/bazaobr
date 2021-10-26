import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import sqlite3

class MainMenuScreen(QMainWindow):
    def __init__(self):
        super(MainMenuScreen, self).__init__()
        loadUi('projekt.ui', self)
        
        self.setFixedSize(550, 500)

        self.conn = sqlite3.connect("obr.db")

        self.kategoria_box.addItem("Końcówki do przewodów")
        self.kategoria_box.addItem("Narzędzia")
        self.kategoria_box.addItem("Przewody")
        self.kategoria_box.addItem("Inne")
        


    def dodaj_przedmiot(self):
        id = self.id_edit.text()
        nazwa = self.nazwa_edit.text()
        producent = self.producent_edit()
        kategoria = str(self.kategoria_box())
        ilosc = self.ilosc_box.value()
        cena = self.cena_edit.text()
        zdjecie = self.zdjecie_edit.text()
        link = self.link_edit.text()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Baza danych OBR")
    mainapp = MainMenuScreen()
    flags = QtCore.Qt.WindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    mainapp.setWindowFlags(flags)

    mainapp.show()

    sys.exit(app.exec())