#04
edad=0
edad_invalido=(edad<18 or edad>33 and edad<42 or edad>65)
while(edad_invalido):
    edad=int(input("ingrese edad"))
    edad_invalido=(edad<18 or edad>33 and edad<42 or edad>65)
#fin_while
print("edad invalido")
