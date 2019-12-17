#mostrar edad invalida
edad=-1
edad_invalida=(edad<0 or edad>18)
while(edad_invalida):
    edad=int(input("ingrese edad:"))
    edad_invalida=(edad<0 or edad>18)
#fin_while
print("MENOR DE EDAD")
