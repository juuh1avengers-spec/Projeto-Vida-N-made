# --- SISTEMA DE GESTÃO: ESCALA DE BARTENDER & METAS ---

# Lista que vai guardar todos os nossos eventos (nossa planilha virtual)
escala_trabalho = []
compras_pendentes = [
    {"item": "Powerbank", "valor": 150.0},
    {"item": "Fone de Ouvido", "valor": 200.0},
    {"item": "Rede de Lona", "valor": 120.0}
]

def menu():
    print("\n" + "="*40)
    print("      🌟 DASHBOARD DA JULIA 🌟")
    print("="*40)
    print("1. Cadastrar Novo Evento")
    print("2. Ver Minha Escala e Total a Receber")
    print("3. Ver Lista de Compras (Equipamentos)")
    print("4. Sair")
    return input("\nEscolha uma opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        print("\n--- CADASTRAR EVENTO ---")
        nome = input("Nome do Evento/Lugar: ")
        data = input("Data (DD/MM): ")
        valor = float(input("Valor combinado: R$ "))
        endereco = input("Endereço/Local: ")
        
        # Criando a "linha da planilha" e adicionando na lista
        evento = {"nome": nome, "data": data, "valor": valor, "local": endereco}
        escala_trabalho.append(evento)
        print("✅ Evento salvo na escala!")

    elif opcao == "2":
        print("\n--- MINHA ESCALA DETALHADA ---")
        total_acumulado = 0
        for ev in escala_trabalho:
            print(f"📅 {ev['data']} | {ev['nome']} | R$ {ev['valor']:.2f}")
            print(f"📍 Local: {ev['local']}\n")
            total_acumulado += ev['valor']
        
        print("-" * 20)
        print(f"💰 TOTAL ACUMULADO A RECEBER: R$ {total_acumulado:.2f}")

    elif opcao == "3":
        print("\n--- EQUIPAMENTOS PARA A VIAGEM ---")
        total_compra = 0
        for item in compras_pendentes:
            print(f"🛒 {item['item']}: R$ {item['valor']:.2f}")
            total_compra += item['valor']
        print(f"\n💸 Total necessário para o kit: R$ {total_compra:.2f}")

    elif opcao == "4":
        print("Até mais, Julia! Partiu correr ou estudar? 🏃‍♀️💻")
        break
    else:
        print("Opção inválida, tenta de novo!")
