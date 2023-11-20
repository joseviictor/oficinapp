
from bd import connector
# ------------------------------
def db_add_servico(v_servico, v_preco, v_observacao):
    conn, cursor = connector()
    cursor.execute('INSERT INTO MATRIAL (servico, preco, observacao) VALUES (?, ?, ?)', (v_servico, v_preco, v_observacao))
    conn.commit()
    conn.close()
