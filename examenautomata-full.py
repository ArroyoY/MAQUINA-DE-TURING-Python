""" 
    Universidad Interamericana de Panamá
        Automata y Lenguajes Formales
            Yorlenis Arroyo 
              8-986-1893
     Prof:ING. Master Salomón Londoño
             Examen final
"""


import os

opcion=True

while opcion:
    os.system("clear")
    print ("""
    ---MAQUINA DE TURING---
	
    1.Palabras Palindromas
    2.Palabras Bifronte
    3.Números Binarios
    4.Salir/Cancelar
	""")
    opcion=input("¿Que desea evaluar? : ") 

    if opcion == "1" :
        print("\n---Palabras Palindromas---")
        texto = input(str("Ingrese la palabra: "))
        if texto == (texto)[::-1]:
            print("\nEs palindroma")
            enter = input("\n[Enter] para continuar >>")
            
        else:
            print("\nNo es palindroma")
            enter = input("\n[Enter] para continuar >>")
	
    if opcion=="2":
        print("\n---Palabras Bifronte---")
        palabras = [
  "acitron","nortica", "rabos","sobar", 
   "amor","roma","notar","raton"
  ]
        nombre = input("Ingrese una palabra: ")
        if nombre in palabras:
            print("\nEs una palabra bifronte")
            enter = input("\n[Enter] para continuar >>")
        else:
            print("\nNo es una palabra bifronte")
            enter = input("\n[Enter] para continuar >>")

    elif opcion=="3":
        print("\n---Números Binarios---")
        try:
            numero= input("Ingrese el binario: ")
            numero = int(numero, 2) 
            numero  +=  1
            siguiente = format(numero, "b")
            print("\nEl Binario siguiente es: ",siguiente)
        except:
            numero= 0
            print("\nError: ingresa un numero binario")
       
        enter = input("\n[Enter] para continuar >>") 

    elif opcion=="4":
        print("\n Adiós") 
        enter = input("\n[Enter] para continuar >>")
        break