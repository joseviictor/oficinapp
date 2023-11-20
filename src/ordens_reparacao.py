from bd import *
# ------------------------------
def db_add_ordem_reparacoes(v_id_cliente_or, v_id_veiculo_or, v_data_or, v_serviços):
    conn, cursor = connector()
    cursor.execute('INSERT INTO ORDEM_REPARACOES (id_cliente_or, id_veiculo_or, data_or, serviços) VALUES (?, ?, ?, ?)', (v_id_cliente_or, v_id_veiculo_or, v_data_or, v_serviços))
    conn.commit()
    conn.close()
    
# ------------------------------
def db_delete_ordem_reparacoes(v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()
    cursor.execute('DELETE FROM ORDEM_REPARACOES WHERE ' + v_condition_field + ' ' + v_condition_operator + '\'' + v_condition_value + '\'' )
    conn.commit()
    conn.close()
# ------------------------------
# bloco de textes
if __name__ == "__main__":
    #db_show_ordem_reparacoes()
    db_add_ordem_reparacoes('1', '1', '1', '1')
    #db_delete_ordem_reparacoes('id_or', '=', '3')
    db_show('ORDEM_REPARACOES')
