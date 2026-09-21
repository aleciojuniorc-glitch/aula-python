# Importando o módulo com o alias solicitado
import estatistica as est

# Dados de exemplo
dados = [10, 20, 20, 30, 40, 50]

# Utilizando as funções através do alias 'est'
resultado_media = est.media(dados)
resultado_mediana = est.mediana(dados)
resultado_moda = est.moda(dados)

print(f"Média: {resultado_media}")
print(f"Mediana: {resultado_mediana}")
print(f"Moda: {resultado_moda}")