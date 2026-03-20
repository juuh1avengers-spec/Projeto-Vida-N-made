import json
import os

ARQUIVO_DADOS = "dados_nomade.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            return json.load(f)
    return {"escala": [], "dividas": [], "equipamentos": [
        {"item": "Powerbank", "valor": 150.0},
        {"item": "Fone de Ouvido", "valor": 200.0},
        {"item": "Rede de Lona", "valor": 120.0}
    ]}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump(dados, f, indent=4)

dados = carregar_dados()

def excluir_item(categoria):
    if not dados[categoria]:
        print(f"\nNenhum item em {categoria} para excluir.")
        return

    print(f"\n--- EXCLUIR DE {categoria.upper()} ---")
    for i, item in enumerate(dados[categoria]):
        nome = item.get('nome') or item.get('item')
        print(f"{i} - {nome}")
    
    try:
        posicao = int(input("\nDigite o número do item que quer apagar: "))
        if 0 <= posicao < len(dados[categoria]):
            removido = dados[categoria].pop(posicao)
            salvar_dados(dados)
            print(f"✅ Removido com sucesso!")
        else:
            print("❌ Número inválido!")
    except ValueError:
        print("❌ Digite um número válido!")

def menu():
    print("\n" + "="*40)
    print("      🇧🇷 DASHBOARD NÔMADE: JULIA 🇧🇷")
    print("="*40)
    print("1. Cadastrar Freela (Entrada)")
    print("2. Cadastrar Dívida/Gasto (Saída)")
    print("3. Ver Escala e Saldo Real")
    print("4. Ver Metas de Equipamentos")
    print("5. Excluir Freela ou Dívida")
    print("6. Sair")
    return input("\nEscolha uma opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        nome = input("Evento/Lugar: ")
        data = input("Data (DD/MM): ")
        valor = float(input("Valor: R$ ").replace(',', '.'))
        local = input("Endereço/Local: ")
        dados["escala"].append({"nome": nome, "data": data, "valor": valor, "local": local})
        salvar_dados(dados)
        print("✅ Freela salvo!")

    elif opcao == "2":
        nome_divida = input("O que precisa pagar? ")
        valor_divida = float(input("Valor: R$ ").replace(',', '.'))
        dados["dividas"].append({"item": nome_divida, "valor": valor_divida})
        salvar_dados(dados)
        print("⚠️ Gasto registrado.")

    elif opcao == "3":
        print("\n--- MINHA ESCALA DETALHADA ---")
        total_ganho = 0
        for ev in dados["escala"]:
            print(f"📅 {ev['data']} | {ev['nome']} | R$ {ev['valor']:.2f}")
            print(f"📍 Local: {ev.get('local', 'Não informado')}\n")
            total_ganho += ev['valor']
        total_dividas = sum(item["valor"] for item in dados["dividas"])
        print(f"💰 Saldo Líquido: R$ {total_ganho - total_dividas:.2f}")

    elif opcao == "4":
        total_ganho = sum(item["valor"] for item in dados["escala"])
        total_dividas = sum(item["valor"] for item in dados["dividas"])
        saldo = total_ganho - total_dividas
        print("\n--- METAS ---")
        for eq in dados["equipamentos"]:
            status = "✅" if saldo >= eq["valor"] else "❌"
            print(f"{status} {eq['item']}: R$ {eq['valor']:.2f}")

    elif opcao == "5":
        cat = input("Excluir de onde? (1 para Freelas, 2 para Dívidas): ")
        excluir_item("escala" if cat == "1" else "dividas")

    elif opcao == "6":
        print("Dados salvos. Bom descanso, Julia! 🏃‍♀️")
        break