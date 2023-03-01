faturamento_estado = {"SP":67836.43,
"RJ":36678.66,
"MG":29229.88,
"ES": 27165.48,
"Outros":19849.53}


total = 0
for f in faturamento_estado:
    total += faturamento_estado[f]

print("% do faturamento do total mensal da distribuidora")
for f in faturamento_estado:
    print(f"{f} -> {faturamento_estado[f]/total}%")


