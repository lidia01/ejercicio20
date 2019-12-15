#01
edad=12
edad_invalido=(edad<18 or edad>200)
while(edad_invalido):
    edad=int(input("ingrese edad:"))
    edad_invalido=(edad<18 or edad>200)
#fin_while
print("edad invalida:",edad)
