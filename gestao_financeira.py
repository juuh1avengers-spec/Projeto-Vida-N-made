# --- MEU DASHBOARD NÔMADE ---

print("--- 💰 GESTÃO FINANCEIRA DA JULIA 💰 ---")

# 1. ENTRADAS (TRAMPOS DE BARTENDER)
# Vamos somar quanto você já tem ou vai receber
ganho_hoje = float(input("Quanto você recebeu no freela de hoje? R$ "))
local_trampo = input("Onde foi o trampo? ")

# 2. DÍVIDAS E GASTOS FIXOS (SP)
dividas_mes = float(input("Qual o total de dívidas para pagar este mês? R$ "))

# 3. EQUIPAMENTOS ESSENCIAIS (META DE COMPRA)
# Preços estimados "no precinho" em SP
powerbank = 150.00
fone_ouvido = 200.00
rede_lona = 120.00
total_equipamentos = powerbank + fone_ouvido + rede_lona

# --- CÁLCULOS ---
saldo_atual = ganho_hoje - dividas_mes
quanto_falta_equipos = total_equipamentos - saldo_atual

# --- RESULTADO NO TERMINAL ---
print("\n" + "="*30)
print(f"Resumo do dia no {local_trampo}:")
print(f"Saldo após pagar dívidas: R$ {saldo_atual:.2f}")

if saldo_atual >= total_equipamentos:
    print("✅ Boa! Você já pode comprar o kit essencial!")
else:
    print(f"❌ Ainda faltam R$ {quanto_falta_equipos:.2f} para o kit (Powerbank, Fone, Rede).")
print("="*30)
