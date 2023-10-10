print("------")
print("Este programa mostra os números de divisão de 1 até o número escolhido")
print("------")
numero = float(input("Digite um número: "))
print("------")

for divisor in range(1, int(numero)):  
    if divisor != 0:
        resp = numero / divisor
        print(resp)
    else:
        print("Não é possível dividir por zero.")