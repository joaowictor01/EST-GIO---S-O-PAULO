def inverter_string(s):
    # Cria uma lista para armazenar a string invertida
    invertida = []
    
    # Itera sobre a string original do final para o início
    for i in range(len(s) - 1, -1, -1):
        invertida.append(s[i])
    
    # Converte a lista de volta para uma string
    return ''.join(invertida)

# Entrada do usuário
entrada = input("Informe a string para inverter: ")

# Inverte a string
resultado = inverter_string(entrada)

# Exibe o resultado
print(f"String invertida: {resultado}")