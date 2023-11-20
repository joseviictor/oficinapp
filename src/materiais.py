
from bd import *
# ------------------------------
def db_add_material(v_material, v_custo, v_preço, v_fornecedor, v_telefone, v_email, v_part_number):
    conn, cursor = connector()
    cursor.execute('INSERT INTO MATRIAL (material, custo, preço, fornecedor, telefone, email, part_number) VALUES (?, ?, ?, ?, ?, ?, ?)', (v_material, v_custo, v_preço, v_fornecedor, v_telefone, v_email, v_part_number))
    conn.commit()
    conn.close()
    
# ------------------------------
def db_update_material(v_define_field, v_define_value, v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()
    cursor.execute('UPDATE MATRIAL SET ' + v_define_field + ' = ' + '\'' + v_define_value + '\'' +' WHERE ' + v_condition_field + ' ' + v_condition_operator + '\'' + v_condition_value + '\'')
    conn.commit()
    conn.close()
# ------------------------------
def db_delete_material(v_condition_field, v_condition_operator, v_condition_value):
    conn, cursor = connector()
    cursor.execute('DELETE FROM MATRIAL WHERE ' + v_condition_field + ' ' + v_condition_operator + '\'' + v_condition_value + '\'' )
    conn.commit()
    conn.close()
# ------------------------------
# bloco de textes
if __name__ == "__main__":
    #db_show_material()
    db_add_material('1', '1', '1', '1', '1', '1', '1')
    db_update_material('material', 'madeira', 'id_material', '=', '2')
    #db_delete_material('id_material', '=', '3')
    db_show('MATRIAL')
