from clientes import db_add_Cliente
from veiculos import db_add_veiculo
from ordens_reparacao import db_add_ordem_reparacoes
from faturas import db_add_fatura
from materiais import db_add_material
from servicos import db_add_servico
from bd import *
from io_terminal import imprime_lista

import csv

def ler_ficheiro_csv(v_tabela):
    with open("resources/" + v_tabela + '.CSV', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=',')
        for linha in leitor_csv:
            linhas = []
            execCode = ''
            codePt1 = '('
            codePt2 = ''

            campos = db_getfields(v_tabela, False)
            codePt1 = ' (' + ', '.join(campos[1: len(campos)]) + ')'

            execCode += 'INSERT INTO ' + v_tabela + codePt1 + ' VALUES (\"'

            codePt2 += '\", \"'.join(linha).replace("\" ", "\"")
            
            execCode += codePt2 + '\")'

            conn, cursor = connector()

            cursor.execute(str(execCode))

            conn.commit()
            conn.close()

if __name__ == '__main__':
    db_drop()
    db_creator()

    ler_ficheiro_csv('CLIENTE')

    ler_ficheiro_csv('VEICULO')

    ler_ficheiro_csv('MATERIAL')

    ler_ficheiro_csv('SERVICO')

    ler_ficheiro_csv('ORDEM_REPARACOES')

    ler_ficheiro_csv('FATURA')

    ligar = True
    if ligar:
        imprime_lista(db_getfields('CLIENTE', False), db_show('CLIENTE', False, False), False)
        imprime_lista(db_getfields('VEICULO', False), db_show('VEICULO', False, False), False)
        imprime_lista(db_getfields('MATERIAL', False), db_show('MATERIAL', False, False), False)
        imprime_lista(db_getfields('SERVICO', False), db_show('SERVICO', False, False), False)
        imprime_lista(db_getfields('ORDEM_REPARACOES', False), db_show('ORDEM_REPARACOES', False, False), False)
        imprime_lista(db_getfields('FATURA', False), db_show('FATURA', False, False), False)

