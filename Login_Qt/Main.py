from PyQt6.QtWidgets import QApplication
from Main_Window import MainWindow
import sys

App = QApplication(sys.argv)
janela = MainWindow()
janela.show()

App.exec()
