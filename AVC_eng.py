from tabulate import tabulate
from datetime import date
import openpyxl
import mysql.connector

#iniciar banco de dados de venda
database_vendas = []

#calculo de comissao
def calcular_comissao(valor):
    taxa_comissao = 0.02
    comissao = valor * taxa_comissao
    return comissao

#gerar nota
def gerar_nota(item, preco, comissao):
    nota = []
    nota.append(["Item", item])
    nota.append(["Preço", preco])
    nota.append(["Comissão", comissao])
    return nota

#programa
print("Sistema de vendas Mosca Branca, seja bem-vindo!!")

while True:
    print("\n[1] Iniciar venda.")
    print("[2] Ver vendas diárias.")
    print("[3] Salvar vendas diárias e sair.")

    escolha = input("\nColoque a opção desejada: ")

    if escolha == "1":
        item = input("Informe o item: ")
        quant = int(input("Informe a quantidade vendida: "))
        preco = float(input("Informe o valor do item: "))
        vendedor = input("Informe o nome do vendedor: ")

        comissao = calcular_comissao(preco)
        nota = gerar_nota(item, preco, comissao)

        database_vendas.append({
            "Item": item,
            "Preço": preco,
            "Quantidade": quant,
            "Comissão": comissao,
            "Vendedor": vendedor
        })

        

        print("\n--- Nota Fiscal ---")
        print(tabulate(nota, tablefmt="grid"))
        print("---------------")

    elif escolha == "2":
        print("\n--- Vendas diárias ---")
        print(tabulate(database_vendas, headers="keys", tablefmt="grid"))
        print("-------------------")

    elif escolha == "3":
        arqnome = f"Vendas_{date.today()}.xlsx"

        wb = openpyxl.Workbook()
        ws = wb.active

        cabecalho = ["Item", "Preço", "Comissão", "Vendedor"]
        ws.append(cabecalho)

        for vendas in database_vendas:
            linha = [vendas["Item"], vendas["Preço"], vendas["Comissão"], vendas["Vendedor"]]
            ws.append(linha)

        wb.save(arqnome)

        print(f"\nVendas diárias salvas com sucesso no nome: {arqnome}")
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Escolha inválida. Tente novamente.")
