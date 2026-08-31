# Definição da função que calcula a média de uma lista de notas
def calcular_media(notas):
    """Retorna a media.
    
    O que é este Docstring? 
    É um texto descritivo delimitado por três aspas duplas. Ele serve para 
    explicar o objetivo da função. No VS Code, se você passar o mouse por 
    cima do nome da função em qualquer parte do código, este texto aparecerá 
    como uma ajuda flutuante (tooltip) para o programador.
    """
    t = sum(notas)          # Soma todos os valores contidos na lista 'notas'
    return t / len(notas)   # Divide a soma total pela quantidade de elementos da lista


# --- EXEMPLO DE USO DO CÓDIGO ---

# Criando uma lista com quatro notas escolares
minhas_notas = [8.5, 7.0, 9.0, 6.5]

# Chamando a função e passando a lista como argumento
media_final = calcular_media(minhas_notas)

# Exibindo o resultado final formatado com duas casas decimais
print(f"A média das notas é: {media_final:.2f}")

# Exibindo o Docstring da função diretamente no terminal
print("\n--- Documentação da Função (Docstring) ---")
print(calcular_media.__doc__)