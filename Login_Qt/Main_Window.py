from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


File_Qt = "Menu.ui"


class MainWindow(QMainWindow):
    Email = "adm"
    Senha = "123"

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi(File_Qt, self)

        self.submit.clicked.connect(self.login)

    def login(self):
        InputEmail = self.InputEmail.text()
        InputPassword = self.InputPassword.text()

        if InputEmail == "" or InputPassword == "":
            self.alert.setText("Preencha Todos Os Campos")
        else:
            if InputEmail == self.Email:
                if InputPassword == self.Senha:
                    self.alert.setText("Login Realizado Com Sucesso")
                    self.InputEmail.clear()
                    self.InputPassword.clear()
                else:
                    self.alert.setText("Senha Inválida")
            else:
                self.alert.setText("E-mail Inválido!")
