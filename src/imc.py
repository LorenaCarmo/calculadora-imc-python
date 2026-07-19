print("===== Calculadora de IMC =====")

opcao = "1"

while opcao == "1":

    # Entrada de dados do usuário
    nome = input("Digite o seu nome: ")
    peso = float(input("Digite o seu peso atual: "))
    altura = float(input("Digite a sua altura: ").replace(",", "."))

    # Cálculo do IMC
    imc = peso / (altura ** 2)

    # Classificação do IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso."
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade Grau I"
    elif imc < 40:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III"

    # Resultado
    print(f"\n{nome}, o resultado do seu IMC é de: {imc:.2f}")
    print(f"Classificação: {classificacao}")

    # Nova consulta
    opcao = input("\nDeseja realizar uma nova consulta? \nDigite 1 para Sim ou 2 para Não: ")

print("Programa encerrado.")