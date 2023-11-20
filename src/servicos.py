
from bd import *
# ------------------------------
def db_add_servico(v_servico, v_preco, v_observacao):
    conn, cursor = connector()
    cursor.execute('INSERT INTO MATRIAL (servico, preco, observacao) VALUES (?, ?, ?)', (v_servico, v_preco, v_observacao))
    conn.commit()
    conn.close()
    
# ------------------------------
def db_update_servico(v_define_field, v_define_value, v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()
    cursor.execute('UPDATE MATRIAL SET ' + v_define_field + ' = ' + '\'' + v_define_value + '\'' +' WHERE ' + v_condition_field + ' ' + v_condition_operator + '\'' + v_condition_value + '\'')
    conn.commit()
    conn.close()
# ------------------------------
def db_delete_servico(v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()
    cursor.execute('DELETE FROM MATRIAL WHERE ' + v_condition_field + ' ' + v_condition_operator + '\'' + v_condition_value + '\'' )
    conn.commit()
    conn.close()
# ------------------------------
# bloco de textes
if __name__ == "__main__":
    #db_show_servico()
    db_add_servico('1', '1', '1', '1', '1', '1', '1')
    db_update_servico('material', 'madeira', 'id_servico', '=', '2')
    #db_delete_servico('id_servico', '=', '3')
    db_show('MATRIAL')
