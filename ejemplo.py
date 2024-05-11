saldo = 100000
continuar = True

while continuar:
    menu = int(input('''
    ===============================================
    Cajero Automático
    ===============================================
    1.- Ingresar dinero.
    2.- Retirar dinero.
    3.- Mostrar saldo.
    4.- Salir
    Seleccione la opción que desea: '''))

    # DEPOSITAR
    if menu == 1:
        x = int(input("\nCuánto dinero desea ingresar: $"))
        saldo += x
        print(f"Su saldo queda en ${saldo}.")

    # RETIRAR
    elif menu == 2:
        x = int(input("\nCuánto dinero desea retirar: $"))
        if x % 5000 == 0:
            if x == 0:
                print("No puede retirar $0.")
            elif x > saldo or x < 0:
                print(f"Ingrese un retiro válido, su saldo es de ${saldo}.")
            elif x <= saldo or x > 0:
                saldo -= x
                print(f"Usted ha retirado: ${x}.")
                print(f"Su saldo queda en ${saldo}.")
        else:
            print("Este cajero solo entrega billetes múltiplos de 5.")

    # SALDO
    elif menu == 3:
        print(f"\nSu saldo es de: ${saldo}.")

    # SALIR
    elif menu == 4:
        print("\nGracias por usar este cajero.")
        continuar = False

    # OTROS
    else:
        print("\nOpción no encontrada.")

    # Preguntar si desea volver al menú
    if menu != 4:
        resp = input('¿Desea volver al menú? (Y/N): ')
        if resp.lower() != 'y':
            continuar = False