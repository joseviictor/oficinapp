
from bd import connector
# ------------------------------
def db_add_veiculo(v_marca, v_modelo, v_matricula, v_combustivel, v_ano, v_kms, v_cilindrada, v_cor, v_observacoes):
    """
    Funcionalidade para adicionar um veiculo na base de dados.
    Args:
    v_marca (str): Marca do carro.
    v_modelo (str): Modelo do carro.
    v_matricula (str): Matricula do carro.
    v_combustivel (str): Combustival que o carro utiliza.
    v_ano (str): Ano de fabrico do carro.
    v_kms (str): quantidade de kilometros que o carro tem.
    v_cilindrada (str): celindrada correspondente ao carro
    v_cor (str): Cor do carro.
    v_observacoes (str): Alguma observação extra do carro.
    """
    conn, cursor = connector()
    cursor.execute('INSERT INTO VEICULO (marca, modelo, matricula, combustivel, ano, kms, cilindrada, cor, observacoes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (v_marca, v_modelo, v_matricula, v_combustivel, v_ano, v_kms, v_cilindrada, v_cor, v_observacoes))
    conn.commit()
    conn.close()
