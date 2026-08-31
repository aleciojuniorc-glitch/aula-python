# retorno antecipado
def dividir(a, b):
   if b == 0:
     return None   
   return a / b      # sai antes

# devolver varios valores
def dividir2(a, b):
   return a // b, a % b

m = dividir(10, 5)
print(m)
q, r = dividir2(7, 2)  # 3 e 1