from sqlalchemy import MetaData, Table, Column, Integer, String, Sequence, create_engine, select, and_, insert, func
from psycopg2 import *

import pandas as pd

import csv

'''engine = create_engine(f'postgresql://andre:manchester00@35.198.41.232/postgres')
metadata = MetaData(bind=None)
table = Table('clientes_aabb', metadata, autoload=True, autoload_with=engine)
stmt = select([table])
nome = 'Henka'
if nome != '':
    stmt = stmt.where(table.c.first_name.contains(nome))
connection = engine.connect()
query = connection.execute(stmt).fetchall()
for i in query:
    print(i)
connection.close()'''

'''
for i in result.fetchall():
        print(i[3])
'''


class ConfigForm():
    def __init__(self):
        pass
    
    def get_login(self, usuario, senha, nome=False):
        engine = create_engine(f'postgresql://{usuario}:{senha}@localhost/aabb')
        conn = engine.connect()
        self.config = [usuario, senha]
        return self.config
    
    def get_results(self, nome='', matri='', endereco='', situacao='', sexo='', cpf='',
                    config=False, time='', control_offset=0):
        self.config = config
        
        engine = create_engine(f'postgresql://{self.config[0]}:{self.config[1]}@localhost/aabb')
        metadata = MetaData(bind=None)
        table = Table('clientes_aabb', metadata, autoload=True, autoload_with=engine)
        stmt = select([table])
        
        if situacao != '':
            stmt = stmt.where(table.c.situacao == situacao)
        if cpf != '':
            stmt = stmt.where(table.c.cpf == cpf)
        if sexo != '':
            stmt = stmt.where(table.c.gender == sexo)
        if endereco != "":
            stmt = stmt.where(table.c.address == endereco)
        if matri != '':
            stmt = stmt.where(table.c.id == matri)
        if nome != '':
            stmt = stmt.where(table.c.first_name.contains(nome))
        
        stmt = stmt.limit(15).order_by(table.c.id.asc())
        stmt = stmt.offset(control_offset * 15)
        connection = engine.connect()
        query = connection.execute(stmt).fetchall()
        connection.close()
        
        lista_controle = []
        lista = []
        for row in query:
            lista_controle.append(row[0])
            lista_controle.append(row[1] + " " + row[2])
            lista_controle.append(row[5])
            lista_controle.append(row[3])
            lista_controle.append(row[4])
            lista_controle.append(row[6])
            lista_controle.append(row[0])
            lista.append(lista_controle)
            lista_controle = []
        
        return lista
    
    def inserir(self, c_matclien, c_nomclien, c_cpfclien, c_sexclien, c_endclien=''
                , c_sitclien='', config=False):
        self.config = config
        
        engine = create_engine(f'postgresql://{self.config[0]}:{self.config[1]}@localhost/aabb')
        metadata = MetaData(bind=None)
        table = Table('clientes_aabb', metadata, autoload=True, autoload_with=engine)
        connection = engine.connect()
        
        stmt = select([func.max(table.c.id)])
        seq = connection.execute(stmt)
        seq = seq.fetchall()[0][0]
        
        stmt = insert(table).values(id=seq + 1, first_name=c_nomclien, last_name='Silva',
                                    gender=c_sexclien, cpf=c_cpfclien,
                                    situacao=c_sitclien, address=c_endclien)
        
        connection = engine.connect()
        connection.execute(stmt)
        connection.close()
    
    def editar(self, c_matclien, c_nomclien, c_cpfclien, c_sexclien, endereco, unique
               , c_sitclien='', config=False):
        
        self.config = config
        engine = create_engine(f'postgresql://{self.config[0]}:{self.config[1]}@localhost/aabb')
        metadata = MetaData(bind=None)
        table = Table('clientes_aabb', metadata, autoload=True, autoload_with=engine)
        
        stmt = table.update().where(table.c.id == unique).values(first_name=c_nomclien, cpf=c_cpfclien,
                                                                 gender=c_sexclien, situacao=c_sitclien,
                                                                 address=endereco)
        
        connection = engine.connect()
        connection.execute(stmt)
        connection.close()
    
    def delete(self, item, config):
        self.config = config
        engine = create_engine(f'postgresql://{self.config[0]}:{self.config[1]}@localhost/aabb')
        metadata = MetaData(bind=None)
        table = Table('clientes_aabb', metadata, autoload=True, autoload_with=engine)
        
        delete = table.delete().where(table.c.cpf == item)
        connection = engine.connect()
        connection.execute(delete)
        connection.close()
    
    def create_output(self, nome='', situacao='', cpf='', sexo='', endereco='', config=False, move=False):
        self.config = config
        
        engine = create_engine(f'postgresql://{self.config[0]}:{self.config[1]}@localhost/aabb')
        metadata = MetaData(bind=None)
        table = Table('clientes_aabb', metadata, autoload=True, autoload_with=engine)
        stmt = select([table])

        if situacao != '':
            stmt = stmt.where(table.c.situacao == situacao)
        if cpf != '':
            stmt = stmt.where(table.c.cpf == cpf)
        if sexo != '':
            stmt = stmt.where(table.c.gender == sexo)
        if endereco != "":
            stmt = stmt.where(table.c.address == endereco)
        if nome != '':
            stmt = stmt.where(table.c.first_name.contains(nome))

        connection = engine.connect()
        results = connection.execute(stmt)

        if move == 'csv':
            with open('data.csv', 'w') as f:
                outcsv = csv.writer(f)
                outcsv.writerow(results.keys())
                outcsv.writerows(results)

        else:
            columns = results.keys()
            data = results
            df = pd.DataFrame(list(data), columns=columns)
    
            writer = pd.ExcelWriter('foo.xlsx')
            df.to_excel(writer, sheet_name='bar')
            writer.save()
