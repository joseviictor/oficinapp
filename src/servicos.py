
from bd import *
# ------------------------------
def db_add_servico(v_servico, v_preco, v_observacao):
    conn, cursor = connector()
    cursor.execute('INSERT INTO MATRIAL (servico, preco, observacao) VALUES (?, ?, ?)', (v_servico, v_preco, v_observacao))
    conn.commit()
    conn.close()
# ------------------------------
# bloco de textes
if __name__ == "__main__":
    #db_show_servico()
    db_add_servico('1', '1', '1', '1', '1', '1', '1')
    db_show('MATRIAL')
