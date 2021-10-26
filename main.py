import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import sqlite3

class MainMenuScreen(QMainWindow):
    def __init__(self):
        super(MainMenuScreen, self).__init__()
        loadUi('projekt.ui', self)

        self.kategoria_box.addItem("Końcówki do przewodów")
        self.kategoria_box.addItem("Narzędzia")
        self.kategoria_box.addItem("Przewody")
        self.kategoria_box.addItem("Inne")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Baza danych OBR")
    mainapp = MainMenuScreen()
    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
    mainapp.setWindowFlags(flags)

    mainapp.show()

    sys.exit(app.exec())