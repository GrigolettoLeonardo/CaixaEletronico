
import os

notas = [
    {"qtd": 0, "valor": 100},
    {"qtd": 0, "valor": 50},
    {"qtd": 0, "valor": 20},
    {"qtd": 0, "valor": 10},
    {"qtd": 0, "valor": 5},
    {"qtd": 0, "valor": 2}
]

def pegandoValores():

    while(1):

        
        try:
            valor_saque = int(input('Informe o valor que deseja sacar:\n'))
            if valor_saque <= 1:
                print('Só possuimos notas a partir de R$2,00\n')
                continue
            else:
                break
        except:
            print('Informe um valor inteiro!')    

    return valor_saque
    
def calculo(valor):

    posicao_nota = 0
    qtd_nota = 0

    while(valor>1 and posicao_nota<len(notas)):

        if valor < notas[posicao_nota]["valor"]:
            posicao_nota = posicao_nota + 1
        elif valor >= notas[posicao_nota]["valor"]:
            qtd_nota = valor // notas[posicao_nota]["valor"]
            valor = valor - (qtd_nota*notas[posicao_nota]["valor"])
            notas[posicao_nota]["qtd"] = qtd_nota

    if valor > 0:
        print(f'Não foi possível sacar R${valor} pois não temos notas desse valor!')

def exibir_notas():

    for valores in notas:
        if valores['qtd'] > 0:
            print(f'{valores['qtd']} de R${valores['valor']}')


def main():
    saque = pegandoValores()
    calculo(saque)
    exibir_notas()

if __name__ == '__main__':
    main()