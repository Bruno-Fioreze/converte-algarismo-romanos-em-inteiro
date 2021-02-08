valores_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

valor_total = 0
caractere_digitado = list(input("digite o algarismo romano : ").upper())
indice = 0

for caractere in caractere_digitado:
    try:
        proximo_caractere = caractere_digitado[indice + 1]
    except Exception as e:
        proximo_caractere = caractere_digitado[indice]

    if valores_dict.get(caractere) < valores_dict.get(proximo_caractere):
        valor_total -= valores_dict.get(caractere)
    else:
        valor_total += valores_dict.get(caractere)
    indice = indice + 1

print(f"{join(caractere_digitado)} = {valor_total} ")
