
from io_terminal import imprime_lista
from bd import *
# ------------------------------
def db_add_veiculo(v_marca, v_modelo, v_matricula, v_combustivel, v_ano, v_kms, v_cilindrada, v_cor, v_observacoes):
    conn, cursor = connector()
    cursor.execute('INSERT INTO VEICULO (marca, modelo, matricula, combustivel, ano, kms, cilindrada, cor, observacoes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (v_marca, v_modelo, v_matricula, v_combustivel, v_ano, v_kms, v_cilindrada, v_cor, v_observacoes))
    conn.commit()
    conn.close()
# ------------------------------
# bloco de textes
if __name__ == "__main__":
    #db_add_veiculo('reout', 'clio', '19-20-pq', 'gasolina', '2000', '160000', '1600', 'cizento', 'nao tem')
    db_show('VEICULO')
