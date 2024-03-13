bandas=[]

#Contruyendo la interfaz

print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100
while(opcion!=5):
    print ("1. Registrar Banda")
    print ("2. Buscar Banda")
    print ("3. Mostrar Banda")
    print ("4. Modificar Banda")
    print ("5. Salir")

    opcion = int(input("Digite una opción: "))
#Creando los datos del diccionario
    if opcion==1:
        banda={}
        banda["id_banda"]=int(input("Digite el ID de la banda: "))
        banda["nombre_banda"]=input("Ingrese el nombre de la banda: ")
        banda["genero_banda"]=input("Ingrese el genero de la banda: ")
        banda["clasificacion_banda"]=input("Clasificación: ")
        banda["tiempo_banda"]=int(input("Tiempo: "))
        banda["valor_banda"]=int(input("Ingrese el valor de la banda: "))
#Agregando un diccionario a una lista
        bandas.append(banda)
    elif opcion==2:
        
        banda_buscada = input("Ingresa el nombre de la banda: ")
        for banda_auxiliar in bandas:
            if banda_auxiliar["nombre_banda"] == banda_buscada:
                #Mostrar los datos de la banda_auxiliar
                print(f"id: {banda_auxiliar[id]} -- nombre: {banda_auxiliar["Nombre"]}")
            else:
                print("Siga buscando")

    elif opcion==3:
        print(bandas)
    elif opcion==4:
        pass
    else:
        pass
