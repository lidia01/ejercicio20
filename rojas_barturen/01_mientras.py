#mostrar clave incorrecta mientras la clave sea 0727*atv
clave=""
clave_incorrecta=(clave!="0727*atv")
while((clave_incorrecta)):
    clave=input("ingrese clave:")
    clave_incorrecta=(clave!="0727*atv")
#fin_while
print("BIENBENIDO")
