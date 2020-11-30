import datetime
import mysql.connector
import tkinter as tk



class ConfigForm():
    def __init__(self):
        pass

    def get_login(self, usuario, senha, nome=False):
        self.usuario = usuario
        self.senha = senha
        self.config = {
            'user': self.usuario,
            'password': self.senha,
            'host': '127.0.0.2',
            'database': 'mydb',
            'auth_plugin': 'mysql_native_password'
        }
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor()
        return self.config


    def get_results(self, nome=False, matri=False, time=False, situacao=False, config=False):

        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()
        query = (f'SELECT * FROM clientes WHERE c_nomclien = "{nome}" ORDER BY "Name"')


        self.cursor.execute(query)
        lista = []
        for row in self.cursor:
            lista.append(row)
        self.cursor.close()
        self.cnx.close()
        return lista