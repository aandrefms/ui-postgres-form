from PyQt5 import QtCore, QtGui, QtWidgets
from config import ConfigForm
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys

config_variable = None
controle_pag = None
procurar_pag = None
inserir_pag = None
segunda_pag = None
dados = None
results = None
edit_pag = None
num_control = 0


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

        # input_user
        self.usuario_input.setFont(font)
        self.usuario_input.setAutoFillBackground(False)
        self.usuario_input.setStyleSheet("border-radius:6 px;\n"
                                         "background-color: #e4eaeb;\n"
                                         "padding: 4px;\n"
                                         "\n"
                                         "")
        self.usuario_input.setPlaceholderText("Usuário *")
        self.usuario_input.setObjectName("usuario_input")

        # titulo
        self.titulo = QtWidgets.QLabel('Iniciar sessão', self)
        self.titulo.setGeometry(QtCore.QRect(190, 40, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color:black")
        self.titulo.setObjectName("titulo")

        # input_senha
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
        
        self.entrar_btn = QtWidgets.QPushButton("Entrar", self)
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
                                        "padding: 4px;")
        self.procurar_btn.setObjectName("procurar2_btn")
        
        self.inserir_btn = QtWidgets.QPushButton("Inserir", Form)
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
        self.inserir_btn.clicked.connect(self.goInserir)
    
    def goProcurar(self):
        global procurar_pag
        global segunda_pag
        
        self.Form1 = QtWidgets.QWidget()
        self.ui1 = Ui_FormProcurar()
        self.ui1.setupUi(self.Form1)
        procurar_pag = self.Form1
        segunda_pag.close()
        self.Form1.show()
    
    def goInserir(self):
        global inserir_pag
        global segunda_pag
        
        self.Form2 = QtWidgets.QWidget()
        self.ui2 = Ui_Cadastro()
        self.ui2.setupUi(self.Form2)
        inserir_pag = self.Form2
        segunda_pag.close()
        self.Form2.show()


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
        
        self.cpf_input = QtWidgets.QLineEdit(Form)
        self.cpf_input.setGeometry(QtCore.QRect(62, 300, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.cpf_input.setFont(font)
        self.cpf_input.setStyleSheet("border-radius:6 px;\n"
                                     "background-color: #e4eaeb;\n"
                                     "padding: 4px;\n"
                                     "\n"
                                     "")
        self.cpf_input.setPlaceholderText("CPF")
        
        self.sexo_input = QtWidgets.QLineEdit(Form)
        self.sexo_input.setGeometry(QtCore.QRect(62, 400, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.sexo_input.setFont(font)
        self.sexo_input.setStyleSheet("border-radius:6 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;\n"
                                      "\n"
                                      "")
        self.sexo_input.setPlaceholderText("Sexo")
        
        self.situacao_input = QtWidgets.QLineEdit(Form)
        self.situacao_input.setGeometry(QtCore.QRect(62, 500, 520, 65))
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
        
        self.time_input = QtWidgets.QLineEdit(Form)
        self.time_input.setGeometry(QtCore.QRect(62, 600, 520, 65))
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
        
        self.procurar_btn = QtWidgets.QPushButton("Procurar", Form)
        self.procurar_btn.setGeometry(QtCore.QRect(410, 690, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.procurar_btn.setFont(font)
        self.procurar_btn.setStyleSheet("background-color:#0cddf5;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 15px;\n"
                                        "padding: 4px;;")
        
        self.procurar_btn.clicked.connect(self.procurar)
        self.back_btn.clicked.connect(self.goBack)
    
    def procurar(self, control=0):
        global config_variable
        global results
        global dados
        global num_control
        num_control = None
        dados = [self.nome_input.text(), self.matricula_input.text(), self.time_input.text(),
                 self.situacao_input.text(), self.cpf_input.text(), self.sexo_input.text()]
        
        results = ConfigForm().get_results(nome=self.nome_input.text(), matri=self.matricula_input.text(),
                                           time=self.time_input.text(), situacao=self.situacao_input.text(),
                                           cpf=self.cpf_input.text(), sexo=self.sexo_input.text(),
                                           config=config_variable, control_offset=control)
        
        self.show_results_page()
    
    def show_results_page(self, move=None):
        global results
        global num_control
        global segunda_pag
        global config_variable
        try:
            if move == 'n':
                num_control += 1
            if move == "b":
                num_control -= 1
                if num_control < 0:
                    num_control = 0
        except:
            num_control = 1
        
        if num_control != None:
            results = ConfigForm().get_results(nome=dados[0], matri=dados[1],
                                               time=dados[2], situacao=dados[3],
                                               cpf=dados[4], sexo=dados[5],
                                               config=config_variable, control_offset=num_control)
        
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_MostrarResultados()
        self.ui.setupUi(self.Form)
        segunda_pag = self.Form
        self.Form.show()
    
    def goBack(self):
        global procurar_pag
        global segunda_pag
        
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form2page()
        self.ui.setupUi(self.Form)
        segunda_pag = self.Form
        procurar_pag.close()
        self.Form.show()


class Ui_MostrarResultados(object):
    def setupUi(self, Form):
        self.Form = Form
        self.Form.title = 'PyQt5 - QTableWidget'
        self.left = 300
        self.top = 300
        self.width =1200
        self.height = 640
    
        self.Form.setWindowTitle(self.Form.title)
        #self.Form.setFixedHeight(750)

        self.createTable()
    
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget, alignment=QtCore.Qt.AlignTop)
        

        self.group = QGroupBox()
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.addWidget(self.back_btn, 0, 1)
        self.gridLayout.addWidget(self.next_btn, 0, 2)
        self.group.setLayout(self.gridLayout)
        
        self.layout.addWidget(self.group)
        self.Form.setLayout(self.layout)
        
        # Create table

    def createTable(self):
        global results
        global segunda_pag
        self.tableWidget = QTableWidget()

        # Row count
        self.tableWidget.setRowCount(15)
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        #hide row count
        self.tableWidget.verticalHeader().hide()
        # Column count
        words = ['','ID', 'Nome', 'Cpf', 'Sexo',  'Endereço', 'Situacao']
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(words)
        self.setTableWidth()
        
        #font
        fnt = self.tableWidget.font()
        fnt.setPointSize(13)
        fnt.setFamily("Georgia")
        self.tableWidget.horizontalHeader().setFont(fnt)
        fnt = self.tableWidget.font()
        fnt.setPointSize(10)
        fnt.setFamily("Georgia")
        self.tableWidget.setFont(fnt)
        
        header = self.tableWidget.horizontalHeader()
        
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.controle_page()

        # NEXT AND BACK BUTTONS
        def control_btn(move):
            segunda_pag.close()
            Ui_FormProcurar().show_results_page(move=move)
        
        self.back_btn = QtWidgets.QPushButton(self.Form)
        self.back_btn.setStyleSheet("background-color:#ffffff;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 15px;\n"
                                    "padding: 4px;;")
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imgs/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(40, 40))
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(lambda: control_btn('b'))
        
        self.next_btn = QtWidgets.QPushButton(self.Form)
        self.next_btn.setStyleSheet("background-color:#ffffff;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 15px;\n"
                                    "padding: 4px;;")
        self.next_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imgs/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn.setIcon(icon)
        self.next_btn.setIconSize(QtCore.QSize(40, 40))
        self.next_btn.setObjectName("next_btn")
        self.next_btn.clicked.connect(lambda: control_btn('n'))
        
        self.back_btn.setFixedWidth(70)
        self.next_btn.setFixedWidth(70)


    #control page size
    def setTableWidth(self):
        width = self.tableWidget.verticalHeader().width()
        width += self.tableWidget.horizontalHeader().length()
        if self.tableWidget.verticalScrollBar().isVisible():
            width += self.tableWidget.verticalScrollBar().width()
        width += self.tableWidget.frameWidth() * 2
        self.tableWidget.setFixedWidth(width)

    # NEXT AND BACK BUTTONS
    def control_btn(move):
        segunda_pag.close()
        Ui_FormProcurar().show_results_page(move=move)
        
    def controle_page(self):
        global results
        self.i_control = 0
        for i in results:
            btn1 = QtWidgets.QPushButton(self.Form)
            btn1.setIcon(QtGui.QIcon("./imgs/draw.png"))
            btn1.setIconSize(QtCore.QSize(20, 20))
            btn1.setMinimumHeight(8)
            btn1.setMaximumWidth(25)
            btn1.clicked.connect(lambda throw_away=0, i=i: self.edit_page(i))

            btn2 = QtWidgets.QPushButton(self.Form)
            btn2.setIcon(QtGui.QIcon("./imgs/delete.png"))
            btn2.setIconSize(QtCore.QSize(25, 25))
            btn2.setMinimumHeight(8)
            btn2.setMaximumWidth(25)
            btn2.clicked.connect(lambda throw_away=0, i=i: self.delete_item(i))

            # add your buttons
            self.gridLayout = QtWidgets.QGridLayout()

            # adjust spacings to your needs
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setSpacing(0)
            # add your buttons
            self.gridLayout.addWidget(btn1, 0, 1)
            self.gridLayout.addWidget(btn2, 0, 0)
            # adding to layout
            layout = QtWidgets.QWidget()
            layout.setLayout(self.gridLayout)
            #adding to cell
            self.tableWidget.setCellWidget(self.i_control, 0, layout)

            #adding rows
            self.tableWidget.setItem(self.i_control, 1, QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(self.i_control, 2, QTableWidgetItem(i[1]))
            self.tableWidget.setItem(self.i_control, 3, QTableWidgetItem(i[2]))
            self.tableWidget.setItem(self.i_control, 4, QTableWidgetItem(i[3]))
            self.tableWidget.setItem(self.i_control, 5, QTableWidgetItem(i[4]))
            self.tableWidget.setItem(self.i_control, 6, QTableWidgetItem(i[5]))
            
            self.i_control += 1
            
    def delete_item(self, info):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Voce tem certeza que deseja deletar este item?")
        msgBox.setWindowTitle("Deletar item")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        bttn = msgBox.exec_()
        if bttn:
            ConfigForm().delete(info[2], config_variable)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Item deletado!')
            msg.setWindowTitle("Aviso")
            msg.exec_()

        else:
            pass

    def edit_page(self, some):
        global edit_pag
        edit_pag = some
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_EditPage()
        self.ui.setupUi(self.Form)
        segunda_pag = self.Form
        self.Form.show()


class Ui_Cadastro(object):
    def setupUi(self, Cadastro):
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(644, 800)
        Cadastro.setMinimumSize(QtCore.QSize(644, 800))
        Cadastro.setMaximumSize(QtCore.QSize(644, 800))
        Cadastro.setStyleSheet("background-color:#ffffff")
        Cadastro.setWindowTitle('Formulário')
        
        self.nome_input = QtWidgets.QLineEdit(Cadastro)
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
        
        self.cpf_input = QtWidgets.QLineEdit(Cadastro)
        self.cpf_input.setGeometry(QtCore.QRect(62, 200, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.cpf_input.setFont(font)
        self.cpf_input.setStyleSheet("border-radius:6 px;\n"
                                     "background-color: #e4eaeb;\n"
                                     "padding: 4px;\n"
                                     "\n"
                                     "")
        self.cpf_input.setText("")
        self.cpf_input.setPlaceholderText("CPF (Apenas números)")
        
        self.endereco_input = QtWidgets.QLineEdit(Cadastro)
        self.endereco_input.setGeometry(QtCore.QRect(62, 300, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.endereco_input.setFont(font)
        self.endereco_input.setStyleSheet("border-radius:6 px;\n"
                                          "background-color: #e4eaeb;\n"
                                          "padding: 4px;\n"
                                          "\n"
                                          "")
        self.endereco_input.setText("")
        self.endereco_input.setPlaceholderText("Endereço")
        
        self.mat_input = QtWidgets.QLineEdit(Cadastro)
        self.mat_input.setGeometry(QtCore.QRect(60, 400, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.mat_input.setFont(font)
        self.mat_input.setStyleSheet("border-radius:6 px;\n"
                                     "background-color: #e4eaeb;\n"
                                     "padding: 4px;\n"
                                     "\n"
                                     "")
        self.mat_input.setPlaceholderText("Matrícula")
        
        self.label = QtWidgets.QLabel("Formulário", Cadastro)
        self.label.setGeometry(QtCore.QRect(236, 30, 172, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.time_input = QtWidgets.QLineEdit(Cadastro)
        self.time_input.setGeometry(QtCore.QRect(60, 500, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.time_input.setFont(font)
        self.time_input.setStyleSheet("border-radius:6 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;\n"
                                      "\n"
                                      "")
        self.time_input.setPlaceholderText("Time")
        
        self.sexo_comboBox = QtWidgets.QComboBox(Cadastro)
        self.sexo_comboBox.setGeometry(QtCore.QRect(62, 600, 230, 60))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.sexo_comboBox.setFont(font)
        self.sexo_comboBox.setStyleSheet("border-radius:6 px;\n"
                                         "background-color: #e4eaeb;\n"
                                         "padding: 8px;")
        self.sexo_comboBox.setObjectName("sexo_comboBox")
        self.sexo_comboBox.addItem("Masculino")
        self.sexo_comboBox.addItem("Feminino")
        
        self.situacao_comboBox = QtWidgets.QComboBox(Cadastro)
        self.situacao_comboBox.setGeometry(QtCore.QRect(350, 600, 230, 60))
        self.situacao_comboBox.setFont(font)
        self.situacao_comboBox.setStyleSheet("border-radius:6 px;\n"
                                             "background-color: #e4eaeb;\n"
                                             "padding: 8px;")
        self.situacao_comboBox.setObjectName("situacao_comboBox")
        self.situacao_comboBox.addItem("Ativo")
        self.situacao_comboBox.addItem("Inativo")
        
        self.cadastrar_btn = QtWidgets.QPushButton("Cadastrar", Cadastro)
        self.cadastrar_btn.setGeometry(QtCore.QRect(410, 700, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.cadastrar_btn.setFont(font)
        self.cadastrar_btn.setStyleSheet("background-color:#0cddf5;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 15px;\n"
                                         "padding: 4px;;")
        self.cadastrar_btn.setObjectName("cadastrar_btn")
        
        self.back_btn = QtWidgets.QPushButton(Cadastro)
        self.back_btn.setGeometry(QtCore.QRect(20, 20, 91, 61))
        self.back_btn.setStyleSheet("background-color:#ffffff;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 15px;\n"
                                    "padding: 4px;;")
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(70, 70))
        self.back_btn.setObjectName("back_btn")
        
        self.back_btn.clicked.connect(self.goBack)
        self.cadastrar_btn.clicked.connect(self.cadastrar)
    
    def goBack(self):
        global inserir_pag
        global segunda_pag
        
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form2page()
        self.ui.setupUi(self.Form)
        segunda_pag = self.Form
        inserir_pag.close()
        self.Form.show()
    
    def cadastrar(self):
        global config_variable
        
        results = ConfigForm().inserir(c_matclien=self.mat_input.text(),
                                       c_nomclien=self.nome_input.text(),
                                       c_cpfclien=self.cpf_input.text(),
                                       c_endclien=self.endereco_input.text(),
                                       c_timclien=self.time_input.text(),
                                       c_sexclien=self.sexo_comboBox.currentText(),
                                       c_sitclien=self.situacao_comboBox.currentText(),
                                       config=config_variable)


class Ui_EditPage(object):
    def setupUi(self, Form):
        global edit_pag
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
        self.nome_input.setText(edit_pag[1])
        
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
        self.matricula_input.setText(str(edit_pag[0]))
        
        self.cpf_input = QtWidgets.QLineEdit(Form)
        self.cpf_input.setGeometry(QtCore.QRect(62, 300, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.cpf_input.setFont(font)
        self.cpf_input.setStyleSheet("border-radius:6 px;\n"
                                     "background-color: #e4eaeb;\n"
                                     "padding: 4px;\n"
                                     "\n"
                                     "")
        self.cpf_input.setText(edit_pag[2])
        
        self.sexo_input = QtWidgets.QLineEdit(Form)
        self.sexo_input.setGeometry(QtCore.QRect(62, 400, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.sexo_input.setFont(font)
        self.sexo_input.setStyleSheet("border-radius:6 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;\n"
                                      "\n"
                                      "")
        self.sexo_input.setText(edit_pag[3])
        
        self.situacao_input = QtWidgets.QLineEdit(Form)
        self.situacao_input.setGeometry(QtCore.QRect(62, 500, 520, 65))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.situacao_input.setFont(font)
        self.situacao_input.setStyleSheet("border-radius:6 px;\n"
                                          "background-color: #e4eaeb;\n"
                                          "padding: 4px;\n"
                                          "\n"
                                          "")
        self.situacao_input.setText(edit_pag[5])
        
        self.time_input = QtWidgets.QLineEdit(Form)
        self.time_input.setGeometry(QtCore.QRect(62, 600, 520, 65))
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
        
        self.editar_btn = QtWidgets.QPushButton("Editar", Form)
        self.editar_btn.setGeometry(QtCore.QRect(410, 690, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.editar_btn.setFont(font)
        self.editar_btn.setStyleSheet("background-color:#0cddf5;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 15px;\n"
                                      "padding: 4px;;")
        
        self.editar_btn.clicked.connect(self.goEditar)
    
    def goEditar(self):
        global config_variable
        global edit_pag
        unique = edit_pag[0]
        editado = ConfigForm().editar(c_nomclien=self.nome_input.text(), c_matclien=self.matricula_input.text(),
                                      c_timclien=self.time_input.text(), c_sitclien=self.situacao_input.text(),
                                      c_cpfclien=self.cpf_input.text(), c_sexclien=self.sexo_input.text(),
                                      config=config_variable, unique=unique)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())