import json

# Carrega os dados de faturamento de um arquivo JSON
with open('faturamento.json') as f:
    dados = json.load(f)

faturamento = dados["faturamento_diario"]

# Filtra os dias com faturamento diferente de 0
faturamento_validos = [valor for valor in faturamento if valor > 0]

# Calcula o menor e o maior valor de faturamento
menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)

# Calcula a média de faturamento
media_mensal = sum(faturamento_validos) / len(faturamento_validos)

# Conta os dias com faturamento superior à média
dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_mensal)

# Exibe os resultados
print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
