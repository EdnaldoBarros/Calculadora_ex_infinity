def subtrair(numero1, numero2):
    return numero1 - numero2

def dividir(numero1, numero2):
    return numero1 / numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def somar(numero1, numero2):
    return numero1 + numero2

print('''
Calculadora:
[1] - Subtrair
[2] - Dividir
[3] - Multiplicar
[4] - Somar
''')

opcao = int(input('Digite uma opção: '))

numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))

if opcao == 1:
    resultado = subtrair(numero1, numero2)
    print(f'{numero1} - {numero2} = {resultado}')
elif opcao == 2:
    if numero2 == 0:
        print("Erro: divisão por zero!")
    else:
        resultado = dividir(numero1, numero2)
        print(f'{numero1} / {numero2} = {resultado}')
elif opcao == 3:
    resultado = multiplicar(numero1, numero2)
    print(f'{numero1} * {numero2} = {resultado}')
elif opcao == 4:
    resultado = somar(numero1, numero2)
    print(f'{numero1} + {numero2} = {resultado}')
else:
    print("Opção inválida!")


