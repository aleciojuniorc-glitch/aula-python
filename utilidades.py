# Funções utilitárias diversas

def converter_temperatura(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32


def validar_senha(senha):
    """
    Valida senha simples:
    - mínimo 6 caracteres
    """
    return len(senha) >= 6


def caixa(*precos):
    """Soma valores recebidos de forma variável."""
    return sum(precos)


def ficha_aluno(**dados):
    """Retorna uma ficha formatada de aluno."""
    return f"Aluno: {dados.get('nome')} | Nota: {dados.get('nota')}"


def lista_segura(lista_original, item):
    """
    Adiciona item sem alterar a lista original (cópia defensiva).
    """
    nova_lista = lista_original.copy()
    nova_lista.append(item)
    return nova_lista


# 🇵🇹 Versão Portugal (pseudocódigo)
"""
função lista_segura(lista, item):
    copiar lista
    adicionar item
    retornar nova lista
"""