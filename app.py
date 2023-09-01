def ejercicio1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for item in reversed(numbers):
        print(item)
    volver_al_menu()

def ejercicio2():
    tupla1 = (4, 5, 6)
    tupla2 = (8, 9, 10)
    suma = tuple(t1 + t2 for t1, t2 in zip(tupla1, tupla2))
    print(suma)
    volver_al_menu()

def ejercicio3():
    conjuntoAex = {1, 2, 3, 4, 5}
    newconj = {item**2 for item in conjuntoAex}
    print(newconj)
    volver_al_menu()

def ejercicio4():
    nombre = input('¿Como te llamas? ')
    edad = input('¿Cuantos años tienes? ')
    print(f"Hola {nombre}, tu edad es {edad}")
    volver_al_menu()

def ejercicio5():
    nota1 = float(input('Ingresar nota 1: '))
    nota2 = float(input('Ingresar nota 2: '))
    nota3 = float(input('Ingresar nota 3: '))
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"El promedio de las notas es: {promedio}")
    volver_al_menu()

def volver_al_menu():
    respuesta = input("¿Deseas volver al menú principal? (1 para sí, 2 para no): ")
    if respuesta == '1':
        menu_principal()
    elif respuesta == '2':
        print("Menu de ejercicios finalizado")
        exit()
    else:
        print("Respuesta no valida, seleccione 1 para volver al menú o 2 para salir del programa.")

def menu_principal():
    print("\nMenu de ejercicios")
    print("Seleccione una opcion: (1-5)")
    print("1. ejercicio 1")
    print("2. ejercicio 2")
    print("3. ejercicio 3")
    print("4. ejercicio 4")
    print("5. ejercicio 5")

    opcion = int(input("Ingrese el numero deseado: "))

    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()
    elif opcion == 4:
        ejercicio4()
    elif opcion == 5:
        ejercicio5()
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú (1-5).")

menu_principal()


