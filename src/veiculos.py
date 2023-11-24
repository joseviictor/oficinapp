
from bd import connector
# ------------------------------
def db_add_veiculo(v_marca, v_modelo, v_matricula, v_combustivel, v_ano, v_kms, v_cilindrada, v_cor, v_observacoes):
    """
   
    Funcionalidade para adicionar um veículo na base de dados.

    Args:
        v_marca (str): Marca do veículo.
        v_modelo (str): Modelo do veículo.
        v_matricula (str): Matrícula do veículo.
        v_combustivel (str): Tipo de combustível que o veículo utiliza.
        v_ano (str): Ano de fabrico do veículo.
        v_kms (str): Quantidade de quilômetros que o veículo percorreu.
        v_cilindrada (str): Cilindrada correspondente ao veículo.
        v_cor (str): Cor do veículo.
        v_observacoes (str): Observações adicionais sobre o veículo.
        
        
    """
    conn, cursor = connector()
    cursor.execute('INSERT INTO VEICULO (marca, modelo, matricula, combustivel, ano, kms, cilindrada, cor, observacoes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (v_marca, v_modelo, v_matricula, v_combustivel, v_ano, v_kms, v_cilindrada, v_cor, v_observacoes))
    conn.commit()
    conn.close()
