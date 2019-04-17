# Desafio105.py
"""
Faca um programa que tenha uma função notas() que pode receber varias
notas de alunos e vai retornar um dicionario com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A media da turma
- A situação (opcional)
Adicione também as docstrings da função:
 ->Funcao para analisar notas e situações de varios alunos
 n: uma ou mais notas dos alunos (aceita varias)
 sit: valor opcional, indicado se deve ou não adicionar a situação
 return: dicionario com varias informações sobre a situação da turma
	>>> notas(5.5, 9.5, 10, 6.5)
	{'total': 4, 'maior': 10, 'menor': 5.5, 'media': 7.875}

	>>> notas(5.5, 9.5, 10, 6.5, sit = True)
	{'total': 4, 'maior': 10, 'menor': 5.5, 'media': 7.875, 'situacao': 'BOA'}

	>>> notas(3.5, 2, 6.5, sit = True)
	{'total': 3, 'maior': 6.5, 'menor': 2, 'media': 4.0, 'situacao': 'RUIM'}

"""


def notas(*nt, sit=False):
    dados = {'total': len(nt), 'maior': max(nt), 'menor': min(nt), 'media': sum(nt) / len(nt)}
    if sit:
        if dados['media'] >= 7:
            dados['situacao'] = 'BOA'
        else:
            dados['situacao'] = 'RUIM'
        return dados
    else:
        return dados


resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
