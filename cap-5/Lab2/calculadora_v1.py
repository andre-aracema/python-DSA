# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

def main():
    print("\n******************* Calculadora em Python *******************\n")
    sms = """

    1. soma.
    2. subtração.
    3. multiplicação.
    4. divisão.

    """
    print(sms)
    
    try:
        escolha = input("Selecione a número da operação desejada: ")

        if int(escolha) > 4:
            print("Operação não encontrada. Tente novamente.")
            main()

        x = float(input("Digete o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        
        escolhas = {
            '1': soma,
            '2': sub,
            '3': mul,
            '4': div
        }
        
        operacao = escolhas.get(escolha)
        print(operacao(x, y))
        exit()

    except ValueError:
        print("\nValor errado. Por favor, tente novamente\n")
        main()
        
        
# funções das operações:

def soma(x, y):
    return f"A soma de {x} + {y} = {x + y}\n"

def sub(x, y):
    return f"A subtração de {x} - {y} = {x - y}\n"

def mul(x, y):
    return f"A multiplicação de {x} * {y} = {x * y}\n"

def div(x, y):
    try:
        return f"A divisão de {x} / {y} = {x / y}\n"
    
    except ZeroDivisionError:
        print("\nDivisão por zero. Por favor, tente novamente\n")
        main()


if __name__ == "__main__":
    main()
    
