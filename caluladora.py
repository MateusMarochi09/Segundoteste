##Primeira alteração no código
def soma(a,b):
    return a + b

## Segunda alteração no código
def subtracao(a,b):
    return a - b

## Terceira alteração no código
print("Escolha a operação:")
print("1. Soma")
print("2. Subtração")

opcao = input("Opção: ")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if opcao == "1":
    print("Resultado:", soma(a, b))
elif opcao == "2":
    print("Resultado:", subtracao(a, b))
else:
    print("Opção inválida")