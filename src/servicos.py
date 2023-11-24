
from bd import connector
# ------------------------------
def db_add_servico(v_servico, v_preco, v_observacao):
    """
    Inserir um novo servico na base de dados
    
    Args:
        v_servico (str): Nome do servico a ser inserido.
        v_preco (float): Preço do servico a ser inserido.
        v_observacao (str): Observação do servico a ser inserido.
    
        
    """
    
    conn, cursor = connector()
    cursor.execute('INSERT INTO MATRIAL (servico, preco, observacao) VALUES (?, ?, ?)', (v_servico, v_preco, v_observacao))
    conn.commit()
    conn.close()
