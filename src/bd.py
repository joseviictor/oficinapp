import sqlite3

def connector():
    conn = sqlite3.connect('../resources/OFICINA.db')
    cursor = conn.cursor()
    return conn, cursor

def db_creator():
    conn, cursor = connector()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS CLIENTE (id_cliente INTEGER PRIMARY KEY, nome TEXT, nif INTEGER, cc TEXT, dob DATE, morada TEXT, telefone TEXT, email TEXT)')

    cursor.execute('CREATE TABLE IF NOT EXISTS FATURA (id_cliente_fatura INTEGER, id_veiculo_fatura INTEGER, dataFatura DATE)')

    cursor.execute('CREATE TABLE IF NOT  EXISTS MATRIAL (id_material INTEGER PRIMARY KEY, material TEXT, custo FLOAT, preço FLOAT, fornecedor TEXT, telefone TEXT, email TEXT, part_number TEXT)')

    cursor.execute('CREATE TABLE IF NOT EXISTS ORDEM_REPARACOES (id_or INTEGER PRIMARY KEY, id_cliente_or INTEGER, id_veiculo_or INTEGER, data_or DATE, serviços TEXT)')

    cursor.execute('CREATE TABLE IF NOT EXISTS SERVICO (id_servico INTEGER PRIMARY KEY, servico TEXT, preco FLOAT, observacao TEXT)')

    cursor.execute('CREATE TABLE IF NOT EXISTS VEICULO (id_veiculo INTEGER PRIMARY KEY, marca TEXT, modelo TEXT, matricula TEXT, combustivel TEXT, ano INTEGER, kms INTEGER, cilindrada INTEGER, cor TEXT, observacoes TEXT)')
    
    conn.commit()
    conn.close()



db_creator()

          
