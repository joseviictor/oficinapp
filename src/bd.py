
import sqlite3
from io_terminal import imprime_lista, pause
# ------------------------------------------------------------
def connector():
    conn = sqlite3.connect('resources/OFICINA.db')
    cursor = conn.cursor()
    return conn, cursor
# ------------------------------
def db_creator():
    conn, cursor = connector()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS CLIENTE (id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, nif INTEGER, cc TEXT, dob DATE, morada TEXT, telefone TEXT, email TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS FATURA (id_cliente_fatura INTEGER PRIMARY KEY AUTOINCREMENT, id_veiculo_fatura INTEGER, dataFatura DATE)')
    cursor.execute('CREATE TABLE IF NOT  EXISTS MATRIAL (id_material INTEGER PRIMARY KEY AUTOINCREMENT, material TEXT, custo FLOAT, preço FLOAT, fornecedor TEXT, telefone TEXT, email TEXT, part_number TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS ORDEM_REPARACOES (id_or INTEGER PRIMARY KEY AUTOINCREMENT, id_cliente_or INTEGER, id_veiculo_or INTEGER, data_or DATE, serviços TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS SERVICO (id_servico INTEGER PRIMARY KEY AUTOINCREMENT, servico TEXT, preco FLOAT, observacao TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS VEICULO (id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT, marca TEXT, modelo TEXT, matricula TEXT, combustivel TEXT, ano INTEGER, kms INTEGER, cilindrada INTEGER, cor TEXT, observacoes TEXT)')
    
    conn.commit()
    conn.close()
# ------------------------------
def db_drop():
    conn, cursor = connector()
    cursor.execute(f'DROP TABLE IF EXISTS CLIENTE;')
    cursor.execute(f'DROP TABLE IF EXISTS FATURA;')
    cursor.execute(f'DROP TABLE IF EXISTS MATRIAL;')
    cursor.execute(f'DROP TABLE IF EXISTS ORDEM_REPARACOES;')
    cursor.execute(f'DROP TABLE IF EXISTS SERVICO;')
    cursor.execute(f'DROP TABLE IF EXISTS VEICULO;')
    conn.commit()
    conn.close()
# ------------------------------------------------------------
def db_clearTable(v_table_name):
    conn, cursor = connector()
    cursor.execute('DELETE FROM ' + v_table_name)
    conn.commit()
    conn.close()

# ------------------------------------------------------------
def db_getfields(v_nome_tabela, mostra_pergunta=True):
    conn, cursor = connector()
    cursor.execute(f"PRAGMA table_info({v_nome_tabela});")
    nomes_colunas = [coluna[1] for coluna in cursor.fetchall()]
    conn.close()
    if mostra_pergunta:
        for nome, i in zip(nomes_colunas, range(len(nomes_colunas))):
            print('[' + str(i) + '] - ' + nome)
        
        return nomes_colunas[int(input('ESCOLHA A COLUNA: '))]
    else:
        return nomes_colunas
# ------------------------------------------------------------
def db_show(v_tableName, return_value=True):
    conn, cursor = connector()
    cursor.execute('SELECT * FROM ' + v_tableName)
    dados = cursor.fetchall()
    conn.close()
    
    if return_value:
        for linha in dados:
            print(linha)
        pause()
    else:
        return dados

    
# ------------------------------
def db_update(v_tableName, v_define_field, v_define_value, v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()
    cursor.execute('UPDATE ' + v_tableName + ' SET ' + v_define_field + ' = ' + '\'' + v_define_value + '\'' +' WHERE ' + v_condition_field + ' ' + v_condition_operator + '\'' + v_condition_value + '\'')
    conn.commit()
    conn.close()
# ------------------------------
def db_delete(v_tableName, v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()
    cursor.execute('DELETE FROM ' + v_tableName + ' WHERE ' + v_condition_field + ' ' + v_condition_operator + '\'' + v_condition_value + '\'' )
    conn.commit()
    conn.close()
