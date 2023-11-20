import sqlite3
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
def db_getfields(v_nome_tabela):
    conn, cursor = connector()
    cursor.execute(f"PRAGMA table_info({v_nome_tabela});")
    nomes_colunas = [coluna[1] for coluna in cursor.fetchall()]
    conn.close()
    for nome, i in zip(nomes_colunas, range(len(nomes_colunas))):
        print('[' + str(i) + '] - ' + nome)
    
    return nomes_colunas[int(input('INSIRA A SUA OPÇÃO: '))]
# ------------------------------
def db_show(v_tableName):
    conn, cursor = connector()
    cursor.execute('SELECT * FROM ' + v_tableName)
    dados = cursor.fetchall()
    for linha in dados:
        print(linha)
    conn.close()
