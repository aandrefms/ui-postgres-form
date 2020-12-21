from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from config_localdb import ConfigForm
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
editar_pag = None
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
            self.ui = UiForm2page()
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


class UiForm2page(object):
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
        Form.resize(760, 680)
        Form.setMinimumSize(QtCore.QSize(760, 680))
        Form.setMaximumSize(QtCore.QSize(760, 680))
        
        self.label = QtWidgets.QLabel("Formulário", Form)
        self.label.setGeometry(QtCore.QRect(290, 30, 172, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        
        
        self.back_btn = QtWidgets.QPushButton(Form)
        self.back_btn.setGeometry(QtCore.QRect(20, 20, 83, 50))
        self.back_btn.setStyleSheet("background-color:#ffffff;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 15px;\n"
                                    "padding: 4px;;")
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imgs/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(55, 55))
        self.back_btn.setObjectName("back_btn")

        self.label = QtWidgets.QLabel("Nome", Form)
        self.label.setGeometry(QtCore.QRect(70, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nome_input = QtWidgets.QLineEdit(Form)
        self.nome_input.setGeometry(QtCore.QRect(70, 120, 611, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.nome_input.setFont(font)
        self.nome_input.setStyleSheet("border-radius:6 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;\n"
                                      "\n"
                                      "")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.nome_input.setFont(font)

        self.endereco = QtWidgets.QLabel('Endereço', Form)
        self.endereco.setGeometry(QtCore.QRect(70, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.endereco.setFont(font)
        self.endereco.setObjectName("label_2")
        self.end_input = QtWidgets.QLineEdit(Form)
        self.end_input.setGeometry(QtCore.QRect(70, 250, 611, 61))
        self.end_input.setStyleSheet("border-radius:7 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.end_input.setFont(font)
        self.end_input.setObjectName("lineEdit_2")

        self.cpflabel = QtWidgets.QLabel("CPF", Form)
        self.cpflabel.setGeometry(QtCore.QRect(70, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.cpflabel.setFont(font)
        self.cpflabel.setObjectName("label_3")
        self.cpf_input = QtWidgets.QLineEdit(Form)
        self.cpf_input.setGeometry(QtCore.QRect(70, 370, 291, 61))
        self.cpf_input.setStyleSheet("border-radius:7 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.cpf_input.setFont(font)
        self.cpf_input.setObjectName("lineEdit_3")

        self.situacaolabel = QtWidgets.QLabel("Situação", Form)
        self.situacaolabel.setGeometry(QtCore.QRect(70, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.situacaolabel.setFont(font)
        self.situacaolabel.setObjectName("label_4")
        self.situacao_comboBox = QtWidgets.QComboBox(Form)
        self.situacao_comboBox.setGeometry(QtCore.QRect(70, 500, 291, 60))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.situacao_comboBox.setFont(font)
        self.situacao_comboBox.setStyleSheet("border-radius:6 px;\n"
                                             "background-color: #e4eaeb;\n"
                                             "padding: 8px;")

        self.situacao_comboBox.setObjectName("situacao_comboBox")
        self.situacao_comboBox.addItem("")
        self.situacao_comboBox.addItem("true")
        self.situacao_comboBox.addItem("false")

        self.sexo_comboBox = QtWidgets.QComboBox(Form)
        self.sexo_comboBox.setGeometry(QtCore.QRect(390, 370, 291, 60))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.sexo_comboBox.setFont(font)
        self.sexo_comboBox.setStyleSheet("border-radius:6 px;\n"
                                         "background-color: #e4eaeb;\n"
                                         "padding: 8px;")
        self.sexo_comboBox.setObjectName("sexo_comboBox")
        self.sexo_comboBox.addItem("")
        self.sexo_comboBox.addItem("Male")
        self.sexo_comboBox.addItem("Female")
        
        self.sexolabel = QtWidgets.QLabel("Sexo", Form)
        self.sexolabel.setGeometry(QtCore.QRect(390, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.sexolabel.setFont(font)
        self.sexolabel.setObjectName("label_6")

        self.mat_input = QtWidgets.QLineEdit(Form)
        self.mat_input.setGeometry(QtCore.QRect(390, 500, 291, 61))
        self.mat_input.setStyleSheet("border-radius:7 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.mat_input.setFont(font)
        self.mat_input.setObjectName("lineEdit_4")
        self.matlabel = QtWidgets.QLabel("Matricula", Form)
        self.matlabel.setGeometry(QtCore.QRect(390, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.matlabel.setFont(font)
        self.matlabel.setObjectName("label_5")

        self.procurar_btn = QtWidgets.QPushButton("Procurar", Form)
        self.procurar_btn.setGeometry(QtCore.QRect(510, 590, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.procurar_btn.setFont(font)
        self.procurar_btn.setStyleSheet("background-color:#0cddf5;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 15px;\n"
                                        "padding: 4px;;")
        self.procurar_btn.setObjectName("procurar_btn")

        self.procurar_btn.clicked.connect(self.procurar)
        self.back_btn.clicked.connect(self.goBack)
    
    def procurar(self, control=0):
        global config_variable
        global results
        global dados
        '''global num_control
        num_control = None'''
        dados = [self.mat_input.text(), self.nome_input.text(), self.end_input.text(),
                 self.situacao_comboBox.currentText(), self.cpf_input.text(), self.sexo_comboBox.currentText()]
        
        results = ConfigForm().get_results(nome=self.nome_input.text(), matri=self.mat_input.text(),
                                           endereco=self.end_input.text(), situacao=self.situacao_comboBox.currentText(),
                                           cpf=self.cpf_input.text(), sexo=self.sexo_comboBox.currentText(),
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
            elif move == "b":
                num_control -= 1
                if num_control < 0:
                    num_control = 0
            '''elif move == "r":
                if num_control == None:
                    num_control = 0
                else:
                    pass'''
        except:
            if move == 'n':
                num_control = 1
            if move == "b" or move == "r":
                num_control = 0

        '''num_control != None and'''
        if move != 'csv':
            results = ConfigForm().get_results(nome=dados[1], matri=dados[0],
                                               time=dados[2], situacao=dados[3],
                                               cpf=dados[4], sexo=dados[5],
                                               config=config_variable, control_offset=num_control)
            
        elif move == 'csv':
            print(dados)
            ConfigForm().create_csv(nome=dados[1],
                                    endereco=dados[2], situacao=dados[3],
                                    cpf=dados[4], sexo=dados[5],
                                    config=config_variable)
        
        if move != 'csv':
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_MostrarResultados()
            self.ui.setupUi(self.Form)
            segunda_pag = self.Form
            self.Form.show()
    
    def goBack(self):
        global procurar_pag
        global segunda_pag
        
        self.Form = QtWidgets.QWidget()
        self.ui = UiForm2page()
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
        self.width = 1200
        self.height = 640
        self.Form.setWindowTitle(self.Form.title)
        Form.setStyleSheet("background-color:#ffffff")
        
        #calling function to show results
        self.createTable()
        #set max and min size
        Form.setMinimumSize(QtCore.QSize(self.width+25, 702))
        Form.setMaximumSize(QtCore.QSize(self.width+25, 702))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget, alignment=QtCore.Qt.AlignTop)
        
        self.group = QGroupBox()
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.addWidget(self.csv_btn, 0, 0)
        self.gridLayout.addWidget(self.back_btn, 0, 1)
        self.gridLayout.addWidget(self.next_btn, 0, 2)
        self.group.setLayout(self.gridLayout)
        
        self.layout.addWidget(self.group)
        self.Form.setLayout(self.layout)
    
    def createTable(self):
        global results
        global segunda_pag
        self.tableWidget = QTableWidget()
        
        # Row count
        self.tableWidget.setRowCount(15)
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        # hide row count
        self.tableWidget.verticalHeader().hide()
        # Column count
        words = ['', 'ID', 'Nome', 'Cpf', 'Sexo', 'Endereço', 'Situacao']
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(words)
        self.setTableWidth()

        # font
        fnt = self.tableWidget.font()
        fnt.setPointSize(13)
        fnt.setFamily("Georgia")
        self.tableWidget.horizontalHeader().setFont(fnt)
        fnt = self.tableWidget.font()
        fnt.setPointSize(10)
        fnt.setFamily("Georgia")
        self.tableWidget.setFont(fnt)
        
        header = self.tableWidget.horizontalHeader()
        # Adjusting header spaces
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.controle_page_row()
        
        # NEXT AND BACK BUTTONS
        def control_btn(move):
            if move != 'csv':
                segunda_pag.close()
            Ui_FormProcurar().show_results_page(move=move)
        
        #Creating
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
                                    "padding: 4px;")
        self.next_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imgs/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn.setIcon(icon)
        self.next_btn.setIconSize(QtCore.QSize(40, 40))
        self.next_btn.setObjectName("next_btn")
        self.next_btn.clicked.connect(lambda: control_btn('n'))
        
        self.csv_btn = QtWidgets.QPushButton(self.Form)
        self.csv_btn.setStyleSheet("background-color:#ffffff;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 15px;\n"
                                    "padding: 4px;")
        self.csv_btn.setText('Gerar CSV')
        self.csv_btn.clicked.connect(lambda: control_btn('csv'))
        
        self.back_btn.setFixedWidth(70)
        self.next_btn.setFixedWidth(70)
    
    # Impressão
    def print_widget(self):
        # Create printer
        printer = QtPrintSupport.QPrinter()
        # Create painter
        painter = QtGui.QPainter()
        # Start painter
        painter.begin(printer)
        # Grab a widget you want to print
        screen = self.tableWidget.grab()
        # Draw grabbed pixmap
        painter.drawPixmap(10, 10, screen)
        # End painting
        painter.end()
    
    
    # control width size
    def setTableWidth(self):
        width = self.tableWidget.verticalHeader().width()
        width += self.tableWidget.horizontalHeader().length()
        if self.tableWidget.verticalScrollBar().isVisible():
            width += self.tableWidget.verticalScrollBar().width()
        width += self.tableWidget.frameWidth() * 2
        self.width = width
        self.tableWidget.setFixedWidth(width)
    
    # NEXT AND BACK BUTTONS
    def control_btn(move):
        segunda_pag.close()
        Ui_FormProcurar().show_results_page(move=move)
    
    def controle_page_row(self):
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
            btn2.setIconSize(QtCore.QSize(20, 20))
            btn2.setMinimumHeight(8)
            btn2.setMaximumWidth(25)
            btn2.clicked.connect(lambda throw_away=0, i=i: self.delete_item(i))
            self.btn2 = btn2
            
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
            # adding to cell
            self.tableWidget.setCellWidget(self.i_control, 0, layout)

            # adding rows
            self.tableWidget.setItem(self.i_control, 1, QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(self.i_control, 2, QTableWidgetItem(i[1]))
            self.tableWidget.setItem(self.i_control, 3, QTableWidgetItem(i[2]))
            self.tableWidget.setItem(self.i_control, 4, QTableWidgetItem(i[3]))
            self.tableWidget.setItem(self.i_control, 5, QTableWidgetItem(i[4]))
            self.tableWidget.setItem(self.i_control, 6, QTableWidgetItem(i[5]))
            
            self.i_control += 1
            
    # DELETE FUNCTION
    @staticmethod
    def delete_item(info):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Voce tem certeza que deseja deletar este item?")
        msgBox.setWindowTitle("Deletar item")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        bttn = msgBox.exec_()
        if bttn == 1024:
            try:
                ConfigForm().delete(info[2], config_variable)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('Item deletado!')
                msg.setWindowTitle("Aviso")
                msg.exec_()
                segunda_pag.close()
                Ui_FormProcurar().show_results_page(move="r")
            except:
                pass
        else:
            pass
        
    
    def edit_page(self, some):
        global edit_pag
        global editar_pag
        edit_pag = some
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_EditPage()
        self.ui.setupUi(self.Form)
        editar_pag = self.Form
        self.Form.show()


class Ui_Cadastro(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setStyleSheet("background-color:#ffffff")
        Form.setWindowTitle('Formulário')
        Form.resize(760, 680)
        Form.setMinimumSize(QtCore.QSize(760, 680))
        Form.setMaximumSize(QtCore.QSize(760, 680))
    
        self.label = QtWidgets.QLabel("Formulário", Form)
        self.label.setGeometry(QtCore.QRect(290, 30, 172, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
    
        self.back_btn = QtWidgets.QPushButton(Form)
        self.back_btn.setGeometry(QtCore.QRect(20, 20, 83, 50))
        self.back_btn.setStyleSheet("background-color:#ffffff;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 15px;\n"
                                    "padding: 4px;;")
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imgs/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(55, 55))
        self.back_btn.setObjectName("back_btn")
    
        self.label = QtWidgets.QLabel("Nome", Form)
        self.label.setGeometry(QtCore.QRect(70, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nome_input = QtWidgets.QLineEdit(Form)
        self.nome_input.setGeometry(QtCore.QRect(70, 120, 611, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.nome_input.setFont(font)
        self.nome_input.setStyleSheet("border-radius:6 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;\n"
                                      "\n"
                                      "")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.nome_input.setFont(font)
    
        self.endereco = QtWidgets.QLabel('Endereço', Form)
        self.endereco.setGeometry(QtCore.QRect(70, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.endereco.setFont(font)
        self.endereco.setObjectName("label_2")
        self.end_input = QtWidgets.QLineEdit(Form)
        self.end_input.setGeometry(QtCore.QRect(70, 250, 611, 61))
        self.end_input.setStyleSheet("border-radius:7 px;\n"
                                     "background-color: #e4eaeb;\n"
                                     "padding: 4px;")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.end_input.setFont(font)
        self.end_input.setObjectName("lineEdit_2")
    
        self.cpflabel = QtWidgets.QLabel("CPF", Form)
        self.cpflabel.setGeometry(QtCore.QRect(70, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.cpflabel.setFont(font)
        self.cpflabel.setObjectName("label_3")
        self.cpf_input = QtWidgets.QLineEdit(Form)
        self.cpf_input.setGeometry(QtCore.QRect(70, 370, 291, 61))
        self.cpf_input.setStyleSheet("border-radius:7 px;\n"
                                     "background-color: #e4eaeb;\n"
                                     "padding: 4px;")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.cpf_input.setFont(font)
        self.cpf_input.setObjectName("lineEdit_3")
    
        self.situacaolabel = QtWidgets.QLabel("Situação", Form)
        self.situacaolabel.setGeometry(QtCore.QRect(70, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.situacaolabel.setFont(font)
        self.situacaolabel.setObjectName("label_4")
        self.situacao_comboBox = QtWidgets.QComboBox(Form)
        self.situacao_comboBox.setGeometry(QtCore.QRect(70, 500, 291, 60))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.situacao_comboBox.setFont(font)
        self.situacao_comboBox.setStyleSheet("border-radius:6 px;\n"
                                             "background-color: #e4eaeb;\n"
                                             "padding: 8px;")
    
        self.situacao_comboBox.setObjectName("situacao_comboBox")
        self.situacao_comboBox.addItem("true")
        self.situacao_comboBox.addItem("false")
    
        self.sexo_comboBox = QtWidgets.QComboBox(Form)
        self.sexo_comboBox.setGeometry(QtCore.QRect(390, 370, 291, 60))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.sexo_comboBox.setFont(font)
        self.sexo_comboBox.setStyleSheet("border-radius:6 px;\n"
                                         "background-color: #e4eaeb;\n"
                                         "padding: 8px;")
        self.sexo_comboBox.setObjectName("sexo_comboBox")
        self.sexo_comboBox.addItem("Male")
        self.sexo_comboBox.addItem("Female")
    
        self.sexolabel = QtWidgets.QLabel("Sexo", Form)
        self.sexolabel.setGeometry(QtCore.QRect(390, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.sexolabel.setFont(font)
        self.sexolabel.setObjectName("label_6")
    
        self.mat_input = QtWidgets.QLineEdit(Form)
        self.mat_input.setGeometry(QtCore.QRect(390, 500, 291, 61))
        self.mat_input.setStyleSheet("border-radius:7 px;\n"
                                     "background-color: #e4eaeb;\n"
                                     "padding: 4px;")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.mat_input.setFont(font)
        self.mat_input.setObjectName("lineEdit_4")
        self.matlabel = QtWidgets.QLabel("Matricula", Form)
        self.matlabel.setGeometry(QtCore.QRect(390, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.matlabel.setFont(font)
        self.matlabel.setObjectName("label_5")
    
        self.cadastrar_btn = QtWidgets.QPushButton("Cadastrar", Form)
        self.cadastrar_btn.setGeometry(QtCore.QRect(510, 590, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.cadastrar_btn.setFont(font)
        self.cadastrar_btn.setStyleSheet("background-color:#0cddf5;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 15px;\n"
                                            "padding: 4px;"
                                         )
        self.cadastrar_btn.setObjectName("procurar_btn")
    
        self.cadastrar_btn.clicked.connect(self.cadastrar)
        self.back_btn.clicked.connect(self.goBack)
    
    # Back btn function
    def goBack(self):
        global inserir_pag
        global segunda_pag
        
        self.Form = QtWidgets.QWidget()
        self.ui = UiForm2page()
        self.ui.setupUi(self.Form)
        segunda_pag = self.Form
        inserir_pag.close()
        self.Form.show()
    
    def cadastrar(self):
        global config_variable
        
        results = ConfigForm().inserir(c_matclien=self.mat_input.text(),
                                       c_nomclien=self.nome_input.text(),
                                       c_cpfclien=self.cpf_input.text(),
                                       c_endclien=self.end_input.text(),
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
        Form.resize(760, 680)
        Form.setMinimumSize(QtCore.QSize(760, 680))
        Form.setMaximumSize(QtCore.QSize(760, 680))

        self.label = QtWidgets.QLabel("Formulário", Form)
        self.label.setGeometry(QtCore.QRect(290, 30, 172, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel("Nome", Form)
        self.label.setGeometry(QtCore.QRect(70, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nome_input = QtWidgets.QLineEdit(Form)
        self.nome_input.setGeometry(QtCore.QRect(70, 120, 611, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.nome_input.setFont(font)
        self.nome_input.setStyleSheet("border-radius:6 px;\n"
                                      "background-color: #e4eaeb;\n"
                                      "padding: 4px;\n"
                                      "\n"
                                      "")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.nome_input.setFont(font)
        self.nome_input.setText(edit_pag[1])

        self.endereco = QtWidgets.QLabel('Endereço', Form)
        self.endereco.setGeometry(QtCore.QRect(70, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.endereco.setFont(font)
        self.endereco.setObjectName("label_2")
        self.end_input = QtWidgets.QLineEdit(Form)
        self.end_input.setGeometry(QtCore.QRect(70, 250, 611, 61))
        self.end_input.setStyleSheet("border-radius:7 px;\n"
                                     "background-color: #e4eaeb;\n"
                                     "padding: 4px;")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.end_input.setFont(font)
        self.end_input.setObjectName("lineEdit_2")
        self.end_input.setText(edit_pag[4])

        self.cpflabel = QtWidgets.QLabel("CPF", Form)
        self.cpflabel.setGeometry(QtCore.QRect(70, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.cpflabel.setFont(font)
        self.cpflabel.setObjectName("label_3")
        self.cpf_input = QtWidgets.QLineEdit(Form)
        self.cpf_input.setGeometry(QtCore.QRect(70, 370, 291, 61))
        self.cpf_input.setStyleSheet("border-radius:7 px;\n"
                                     "background-color: #e4eaeb;\n"
                                     "padding: 4px;")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.cpf_input.setFont(font)
        self.cpf_input.setObjectName("lineEdit_3")
        self.cpf_input.setText(edit_pag[2])

        self.situacaolabel = QtWidgets.QLabel("Situação", Form)
        self.situacaolabel.setGeometry(QtCore.QRect(70, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.situacaolabel.setFont(font)
        self.situacaolabel.setObjectName("label_4")
        self.situacao_comboBox = QtWidgets.QComboBox(Form)
        self.situacao_comboBox.setGeometry(QtCore.QRect(70, 500, 291, 60))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.situacao_comboBox.setFont(font)
        self.situacao_comboBox.setStyleSheet("border-radius:6 px;\n"
                                             "background-color: #e4eaeb;\n"
                                             "padding: 8px;")
        self.situacao_comboBox.setObjectName("situacao_comboBox")
        self.situacao_comboBox.addItem('true')
        self.situacao_comboBox.addItem('false')
        index = self.situacao_comboBox.findText(edit_pag[5], QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.situacao_comboBox.setCurrentIndex(index)

        self.sexo_comboBox = QtWidgets.QComboBox(Form)
        self.sexo_comboBox.setGeometry(QtCore.QRect(390, 370, 291, 60))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.sexo_comboBox.setFont(font)
        self.sexo_comboBox.setStyleSheet("border-radius:6 px;\n"
                                         "background-color: #e4eaeb;\n"
                                         "padding: 8px;")
        self.sexo_comboBox.setObjectName("sexo_comboBox")
        self.sexo_comboBox.addItem('Male')
        self.sexo_comboBox.addItem('Female')
        index = self.sexo_comboBox.findText(edit_pag[3], QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.sexo_comboBox.setCurrentIndex(index)

        self.sexolabel = QtWidgets.QLabel("Sexo", Form)
        self.sexolabel.setGeometry(QtCore.QRect(390, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.sexolabel.setFont(font)
        self.sexolabel.setObjectName("label_6")

        self.mat_input = QtWidgets.QLineEdit(Form)
        self.mat_input.setGeometry(QtCore.QRect(390, 500, 291, 61))
        self.mat_input.setStyleSheet("border-radius:7 px;\n"
                                     "background-color: #e4eaeb;\n"
                                     "padding: 4px;")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.mat_input.setFont(font)
        self.mat_input.setObjectName("lineEdit_4")
        self.mat_input.setText(str(edit_pag[0]))
        self.matlabel = QtWidgets.QLabel("Matricula", Form)
        self.matlabel.setGeometry(QtCore.QRect(390, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.matlabel.setFont(font)
        self.matlabel.setObjectName("label_5")

        self.editar_btn = QtWidgets.QPushButton("Editar", Form)
        self.editar_btn.setGeometry(QtCore.QRect(510, 590, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.editar_btn.setFont(font)
        self.editar_btn.setStyleSheet("background-color:#0cddf5;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 15px;\n"
                                         "padding: 4px;;")
        self.editar_btn.setObjectName("procurar_btn")

        self.editar_btn.clicked.connect(self.goEditar)
    
    def goEditar(self):
        global config_variable
        global edit_pag
        unique = edit_pag[0]
        try:
            editado = ConfigForm().editar(c_nomclien=self.nome_input.text(), c_matclien=self.mat_input.text(),
                                          endereco=self.end_input.text(), c_sitclien=self.situacao_comboBox.currentText(),
                                          c_cpfclien=self.cpf_input.text(), c_sexclien=self.sexo_comboBox.currentText(),
                                          config=config_variable, unique=unique)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Item editado!')
            msg.setWindowTitle("Aviso")
            msg.exec_()
            editar_pag.close()
            segunda_pag.close()
            Ui_FormProcurar().show_results_page(move="r")
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Não foi possivel editar o item')
            msg.setWindowTitle("Erro!")
            msg.exec_()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
