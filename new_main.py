from PyQt5 import QtCore, QtGui, QtWidgets
from config_form import ConfigForm
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys

config_variable = None
controle_pag = None
procurar_pag = None
inserir_pag = None


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QtCore.QSize(550, 335))
        self.setMaximumSize(QtCore.QSize(550, 335))
        self.setStyleSheet("background-color:#ffffff")
        self.setWindowTitle('Formulário')

        self.usuario_input = QtWidgets.QLineEdit(self)
        self.usuario_input.setGeometry(QtCore.QRect(110, 90, 330, 55))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)

        #input_user
        self.usuario_input.setFont(font)
        self.usuario_input.setAutoFillBackground(False)
        self.usuario_input.setStyleSheet("border-radius:6 px;\n"
                                         "background-color: #e4eaeb;\n"
                                         "padding: 4px;\n"
                                         "\n"
                                         "")
        self.usuario_input.setPlaceholderText("Usuário *")
        self.usuario_input.setObjectName("usuario_input")

        #titulo
        self.titulo = QtWidgets.QLabel('Iniciar sessão', self)
        self.titulo.setGeometry(QtCore.QRect(190, 40, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color:black")
        self.titulo.setObjectName("titulo")

        #input_senha
        self.senha_input = QtWidgets.QLineEdit(self)
        self.senha_input.setGeometry(QtCore.QRect(110, 160, 330, 55))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.senha_input.setFont(font)
        self.senha_input.setStyleSheet("border-radius:6 px;\n"
                                       "background-color: #e4eaeb;\n"
                                       "padding: 4px;\n"
                                       "\n"
                                       "")
        self.senha_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha_input.setPlaceholderText("Senha *")
        self.senha_input.setObjectName("senha_input")


        self.entrar_btn = QtWidgets.QPushButton("Entrar",self)
        self.entrar_btn.setGeometry(QtCore.QRect(190, 240, 170, 50))
        self.entrar_btn.setFont(font)
        self.entrar_btn.setStyleSheet("background-color:#0cddf5;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 15px;\n"
                                      "padding: 4px;;")
        self.show()
        self.entrar_btn.clicked.connect(self.goForm)

    def goForm(self):
        global config_variable
        global segunda_pag
        try:
            self.config = ConfigForm().get_login(self.usuario_input.text(), self.senha_input.text())
            config_variable = self.config

            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form2page()
            self.ui.setupUi(self.Form)
            segunda_pag = self.Form
            self.close()
            self.Form.show()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Usuário ou senha incorretos   ')
            msg.setWindowTitle("Erro!")
            msg.exec_()


class Ui_Form2page(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 335)
        Form.setMinimumSize(QtCore.QSize(550, 335))
        Form.setMaximumSize(QtCore.QSize(550, 335))
        Form.setStyleSheet("background-color:#ffffff")
        Form.setWindowTitle('Formulário')

        self.procurar_btn = QtWidgets.QPushButton("Procurar", Form)
        self.procurar_btn.setGeometry(QtCore.QRect(155, 70, 240, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.procurar_btn.setFont(font)
        self.procurar_btn.setStyleSheet("background-color:#0cddf5;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 15px;\n"
                                         "padding: 4px;;")
        self.procurar_btn.setObjectName("procurar2_btn")

        self.inserir_btn = QtWidgets.QPushButton("Inserir",Form)
        self.inserir_btn.setGeometry(QtCore.QRect(155, 195, 240, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.inserir_btn.setFont(font)
        self.inserir_btn.setStyleSheet("background-color:#0cddf5;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 15px;\n"
                                       "padding: 4px;;")
        self.inserir_btn.setObjectName("inserir_btn")

        self.procurar_btn.clicked.connect(self.goProcurar)

    def goProcurar(self):
        global procurar_pag
        global segunda_pag

        self.Form1 = QtWidgets.QWidget()
        self.ui1 = Ui_FormProcurar()
        self.ui1.setupUi(self.Form1)
        procurar_pag = self.Form1
        segunda_pag.close()
        self.Form1.show()

class Ui_FormProcurar(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setStyleSheet("background-color:#ffffff")
        Form.setWindowTitle('Formulário')
        Form.resize(644, 800)
        Form.setMinimumSize(QtCore.QSize(644, 800))
        Form.setMaximumSize(QtCore.QSize(644, 800))

        self.label = QtWidgets.QLabel("Formulário", Form)
        self.label.setGeometry(QtCore.QRect(236, 30, 172, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.back_btn = QtWidgets.QPushButton(Form)
        self.back_btn.setGeometry(QtCore.QRect(20, 20, 91, 61))
        self.back_btn.setStyleSheet("background-color:#ffffff;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 15px;\n"
                                    "padding: 4px;;")
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imgs/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(70, 70))
        self.back_btn.setObjectName("back_btn")

        self.nome_input = QtWidgets.QLineEdit(Form)
        self.nome_input.setGeometry(QtCore.QRect(62, 100, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.nome_input.setFont(font)
        self.nome_input.setStyleSheet("border-radius:6 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;\n"
                                      "\n"
                                      "")
        self.nome_input.setPlaceholderText("Nome")


        self.matricula_input = QtWidgets.QLineEdit(Form)
        self.matricula_input.setGeometry(QtCore.QRect(62, 200, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.matricula_input.setFont(font)
        self.matricula_input.setStyleSheet("border-radius:6 px;\n"
                                           "background-color: #e4eaeb;\n"
                                           "padding: 4px;\n"
                                           "\n"
                                           "")
        self.matricula_input.setPlaceholderText("Matrícula")


        self.time_input = QtWidgets.QLineEdit(Form)
        self.time_input.setGeometry(QtCore.QRect(62, 300, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.time_input.setFont(font)
        self.time_input.setStyleSheet("border-radius:6 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;\n"
                                      "\n"
                                      "")
        self.time_input.setPlaceholderText('Time')

        self.situacao_input = QtWidgets.QLineEdit(Form)
        self.situacao_input.setGeometry(QtCore.QRect(62, 400, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.situacao_input.setFont(font)
        self.situacao_input.setStyleSheet("border-radius:6 px;\n"
                                          "background-color: #e4eaeb;\n"
                                          "padding: 4px;\n"
                                          "\n"
                                          "")
        self.situacao_input.setPlaceholderText('Situação')




        self.procurar_btn = QtWidgets.QPushButton("Procurar", Form)
        self.procurar_btn.setGeometry(QtCore.QRect(410, 490, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.procurar_btn.setFont(font)
        self.procurar_btn.setStyleSheet("background-color:#0cddf5;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 15px;\n"
                                        "padding: 4px;;")

        self.text_browser = QtWidgets.QTextBrowser(Form)
        self.text_browser.setGeometry(QtCore.QRect(70, 575, 511, 171))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.text_browser.setFont(font)
        self.text_browser.setStyleSheet("border-radius:6 px;\n"
                                        "background-color: #e4eaeb;\n"
                                        "padding: 4px;\n"
                                        "font-size: 12pt")
        self.text_browser.setObjectName("text_browser")

        self.procurar_btn.clicked.connect(self.procurar)
        self.back_btn.clicked.connect(self.goBack)

    def procurar(self):
        global config_variable
        results = ConfigForm().get_results(nome=self.nome_input.text(), matri=self.matricula_input.text(),
                                           time=self.time_input.text(), situacao=self.situacao_input.text(),
                                           config=config_variable)
        for item in results:
            self.text_browser.append(f'{item[1]}')

    def goBack(self):
        global procurar_pag
        global segunda_pag

        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form2page()
        self.ui.setupUi(self.Form)
        segunda_pag = self.Form
        procurar_pag.close()
        self.Form.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())