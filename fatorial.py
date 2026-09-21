def fatorial(n):
  # Caso base: se n for 0 ou 1, o fatorial é 1
  if n == 0 or n == 1:
    return 1

  # Chamada recursiva: o número multiplicado pelo fatorial do anterior
  return n * fatorial(n - 1)


# Exemplo de uso:
print(fatorial(6))  # Resultado: 120 (5 * 4 * 3 * 2 * 1)