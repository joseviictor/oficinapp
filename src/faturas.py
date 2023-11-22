
from bd import connector
# ------------------------------
def db_add_fatura(v_id_veiculo_fatura, v_dataFatura):
    """
    Função para adicionar faturas na base de dados.
    Args:
        v_id_veiculo_fatura (int) : ID do veículo da fatura.
        v_dataFatura (str) : Data da fatura.
    
     Returns:
        None. A função realiza a inserção na base de dados.
    
    """
    
    conn, cursor = connector()
    cursor.execute('INSERT INTO FATURA (id_veiculo_fatura, dataFatura) VALUES (?, ?)', (v_id_veiculo_fatura, v_dataFatura))
    conn.commit()
    conn.close()
