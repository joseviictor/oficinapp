
from bd import *
# ------------------------------
def db_add_fatura(v_id_veiculo_fatura, v_dataFatura):
    conn, cursor = connector()
    cursor.execute('INSERT INTO FATURA (id_veiculo_fatura, dataFatura) VALUES (?, ?)', (v_id_veiculo_fatura, v_dataFatura))
    conn.commit()
    conn.close()
    
# ------------------------------
def db_delete_fatura(v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()
    cursor.execute('DELETE FROM FATURA WHERE ' + v_condition_field + ' ' + v_condition_operator + '\'' + v_condition_value + '\'' )
    conn.commit()
    conn.close()
# ------------------------------
# bloco de textes
if __name__ == "__main__":
    #db_show_fatura()
    db_add_fatura('1', '1')
    #db_delete_fatura('id_cliente_fatura', '=', '3')
    db_show('FATURA')
