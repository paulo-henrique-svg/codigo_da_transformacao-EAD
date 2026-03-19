# ==============================
# CALCULADORA COM FUNÇÕES
# ==============================

historico_detalhado = []

# ------------------------------
# Função para converter número
# ------------------------------
def converter_numero(valor):
    return float(valor) if '.' in valor else int(valor)


# ------------------------------
# Função de cálculo básico
# ------------------------------
def calcular():
    v1 = input("Primeiro número: ")
    v2 = input("Segundo número: ")

    n1 = converter_numero(v1)
    n2 = converter_numero(v2)

    print("Operações: [1]+ [2]- [3]* [4]/")
    op = input("Operação: ")

    if op == '1':
        simbolo = '+'
        resultado = n1 + n2
    elif op == '2':
        simbolo = '-'
        resultado = n1 - n2
    elif op == '3':
        simbolo = '*'
        resultado = n1 * n2
    elif op == '4':
        simbolo = '/'
        resultado = n1 / n2 if n2 != 0 else "Indeterminado"
    else:
        print("Operação inválida!")
        return

    registro = f"Cálculo: {n1} {simbolo} {n2} | Resultado: {resultado} | Tipo: {type(resultado).__name__}"
    
    print(f"\n>> {registro}")
    historico_detalhado.append(registro)


# ------------------------------
# Função de porcentagem
# ------------------------------
def calcular_porcentagem():
    v_porcent = float(input("Valor da porcentagem: "))
    v_total = float(input("Valor base: "))

    print("1. Apenas a parte (X% de Y)")
    print("2. Acréscimo")
    print("3. Desconto")

    tipo = input("Opção: ")

    parte = (v_porcent / 100) * v_total

    if tipo == '1':
        resultado = parte
        mensagem = f"{v_porcent}% de {v_total} é {resultado}"
    elif tipo == '2':
        resultado = v_total + parte
        mensagem = f"{v_total} com acréscimo de {v_porcent}% = {resultado}"
    elif tipo == '3':
        resultado = v_total - parte
        mensagem = f"{v_total} com desconto de {v_porcent}% = {resultado}"
    else:
        print("Opção inválida!")
        return

    print(f"\n>> {mensagem}")
    historico_detalhado.append(mensagem)


# ------------------------------
# Função para mostrar histórico
# ------------------------------
def mostrar_historico():
    print("\n--- HISTÓRICO DE OPERAÇÕES ---")

    if not historico_detalhado:
        print("Nenhum cálculo realizado.")
    else:
        for i, item in enumerate(historico_detalhado, 1):
            print(f"{i}. {item}")


# ------------------------------
# Função do menu principal
# ------------------------------
def menu():
    while True:
        print("\n==============================")
        print("      Calculadora - Python")
        print("==============================")
        print("1. Calcular (Inteiro/Decimal)")
        print("2. Porcentagem")
        print("3. Ver Histórico")
        print("0. Sair")

        escolha = input("\nOpção: ")

        if escolha == '1':
            calcular()
        elif escolha == '2':
            calcular_porcentagem()
        elif escolha == '3':
            mostrar_historico()
        elif escolha == '0':
            print("Encerrando... Até à próxima!")
            break
        else:
            print("Opção inválida!")


# ------------------------------
# Executar programa
# ------------------------------
menu()