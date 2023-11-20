
from bd import connector
# ------------------------------
def db_add_veiculo(v_marca, v_modelo, v_matricula, v_combustivel, v_ano, v_kms, v_cilindrada, v_cor, v_observacoes):
    conn, cursor = connector()
    cursor.execute('INSERT INTO VEICULO (marca, modelo, matricula, combustivel, ano, kms, cilindrada, cor, observacoes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (v_marca, v_modelo, v_matricula, v_combustivel, v_ano, v_kms, v_cilindrada, v_cor, v_observacoes))
    conn.commit()
    conn.close()
