#mostrar precio invalido del arroz
precio=0.0
precio_invalido=(precio<2.00 or precio>10)
while(precio_invalido):
    precio=float(input("ingrese precio:"))
    precio_invalido=(precio<2.00 or precio>10)
#fin_while
print("conforme con el precio")
