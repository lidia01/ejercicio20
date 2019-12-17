#mostrar numero valido
numero=-1
numero_invalido=(numero<0 or numero>=200)
while(numero_invalido):
   numero=float(input("ingrese numero:"))
   numero_invalido=(numero<0 or numero>=200)
#fin_while
print("número valido")

