
from bd import connector
# ------------------------------
def db_add_material(v_material, v_custo, v_preço, v_fornecedor, v_telefone, v_email, v_part_number):
    """ 
    Inserir um novo material na base de dados
    
    Args:
        v_material (str): Nome do material a inserir.
        v_custo (float): Custo do material em reais.
        v_preço (float): Preço do material em reais.
        v_fornecedor (str): Fornecedor do material.
        v_telefone (str): Telefone do fornecedor.
        v_email (str): Email do fornecedor.
        v_part_number (str): Part number do material.
    """
    
    conn, cursor = connector()
    cursor.execute('INSERT INTO MATRIAL (material, custo, preço, fornecedor, telefone, email, part_number) VALUES (?, ?, ?, ?, ?, ?, ?)', (v_material, v_custo, v_preço, v_fornecedor, v_telefone, v_email, v_part_number))
    conn.commit()
    conn.close()
