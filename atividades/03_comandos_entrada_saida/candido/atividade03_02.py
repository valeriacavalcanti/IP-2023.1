'''
Escreva um programa para obter a descrição e o valor de um
determinado produto. Considerando que será concedido um
desconto de 20%, calcule e exiba:
- Descrição do produto;
- Desconto calculado;
- Valor final desse produto (com precisão de duas casas
decimais após o ponto).
'''
PERC = 20/100
descricao = input("Insira a descrição do produto:\n") 
valor = float(input("Insira o valor do produto:\n"))
desconto = valor * PERC
valor_final = valor - desconto

print(
    f"Descrição do produto:\n {descricao}",
    f"Desconto: R$ {desconto:.2f}",
    f"Valor final: R$ {valor_final:.2f}",
    sep="\n"
    )                                                                    
