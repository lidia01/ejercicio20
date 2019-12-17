#mostrar alumno aprobado
promedio=0.0
promedio_invalido=(promedio<=10.5 or promedio>=200)
while(promedio_invalido):
    promedio=float(input("ingrese promedio:"))
    promedio_invalido=(promedio<=10.5 or promedio>=200)
#fin_while
print("APROBADO")
