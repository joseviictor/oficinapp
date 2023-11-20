
from bd import *
# ------------------------------
def db_add_fatura(v_id_veiculo_fatura, v_dataFatura):
    conn, cursor = connector()
    cursor.execute('INSERT INTO FATURA (id_veiculo_fatura, dataFatura) VALUES (?, ?)', (v_id_veiculo_fatura, v_dataFatura))
    conn.commit()
    conn.close()
    
# ------------------------------
# bloco de textes
if __name__ == "__main__":
    #db_show_fatura()
    db_add_fatura('1', '1')
    db_show('FATURA')
