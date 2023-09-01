def ejercicio1():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
    for item in reversed(numbers):
        print(item)
    
def ejercicio2():
    tupla1=(4,5,6)
    tupla2=(8,9,10)
    suma=()
    for i in range(len(tupla1)):
     suma+=(tupla1[i]+tupla2[i],)    
        
    print(suma)
   
def ejercicio3():
    conjuntoAex={1,2,3,4,5}
    newconj=set()
    for item in conjuntoAex:
     newconj.add(item**2)

    print(newconj)
   

def ejercicio4():
    nombre=input('¿como te llamas?')
    edad=input('¿cuantos años tienes')

    print("Hola "+nombre+" tu edad es "+edad)
def ejercicio5():
    nota1=float(input('ingresar nota 1 '))
    nota2=float(input('ingresar nota 2 '))
    nota3=float(input('ingresar nota 3 '))

    print(((nota1+nota2+nota3)/3))
    

print("Menu de ejercicios")
print("Seleccione una opcion: (1-5)")
print("1. ejercicio 1")
print("2. ejercicio 2")
print("3. ejercicio 3")
print("4. ejercicio 4")
print("5. ejercicio 5")

opcion= int(input("Ingrese el numero deseado: "))

if opcion==1:
    ejercicio1()
elif opcion==2:
    ejercicio2()
elif opcion==3:
    ejercicio3()
elif opcion==4:
    ejercicio4()
elif opcion==5:
    ejercicio5()

##ejercicio 1: almacenar una lista de numeros del 1 al 12 y los muestre por pantalla en orden inverso
##ejercicio 2: crear una sumatoria de dos listas
##ejercicio 3: creacion de un nuevo conjunto basado en el primer conjunto, cuyo valores sean al cuadrado
##ejercicio 4: pedir un nombre y una edad y traiga un mensaje de hola persona y la edad
##ejercicio 5:promedio de notas

