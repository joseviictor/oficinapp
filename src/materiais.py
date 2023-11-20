
from bd import connector
# ------------------------------
def db_add_material(v_material, v_custo, v_preço, v_fornecedor, v_telefone, v_email, v_part_number):
    conn, cursor = connector()
    cursor.execute('INSERT INTO MATRIAL (material, custo, preço, fornecedor, telefone, email, part_number) VALUES (?, ?, ?, ?, ?, ?, ?)', (v_material, v_custo, v_preço, v_fornecedor, v_telefone, v_email, v_part_number))
    conn.commit()
    conn.close()
