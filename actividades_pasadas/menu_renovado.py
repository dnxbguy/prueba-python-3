def registrar_trabajador():
    nombre = input("Ingrese el nombre del trabajador: ")
    if not nombre:
        print("Nombre no puede estar vacío.")
        return

    cargo = input("Ingrese el cargo del trabajador: ")
    if not cargo:
        print("Cargo no puede estar vacío.")
        return

    try:
        sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))
    except ValueError:
        print("Sueldo bruto debe ser un número.")
        return

    # Calcular descuentos y líquido a pagar
    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    liquido = sueldo_bruto - desc_salud - desc_afp

    trabajador = {
        "nombre": nombre,
        "cargo": cargo,
        "sueldo_bruto": round(sueldo_bruto, 2),
        "desc_salud": round(desc_salud, 2),
        "desc_afp": round(desc_afp, 2),
        "liquido": round(liquido, 2)
    }

    trabajadores.append(trabajador)
    print("Trabajador registrado correctamente.")
    print(trabajador)

def listar_trabajadores():
    try:
        trabajador = trabajadores[0]  # Intentamos acceder al primer elemento de la lista
        for trabajador in trabajadores:
            print(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['desc_salud']}, Desc. AFP: {trabajador['desc_afp']}, Líquido: {trabajador['liquido']}")
    except IndexError:
        print("No hay trabajadores registrados.")

def imprimir_planilla():
    try:
        trabajador = trabajadores[0]  # Intentamos acceder al primer elemento de la lista
        opcion = input("Desea imprimir la planilla de todos los trabajadores (1) o por cargo (2)? ")

        if opcion == '1':
            with open('planilla_sueldos.txt', 'w', encoding='utf-8') as archivo:
                archivo.write('Nombre,Cargo,Sueldo Bruto,Desc. Salud,Desc. AFP,Líquido a Pagar\n')
                for trabajador in trabajadores:
                    archivo.write(f"{trabajador['nombre']},{trabajador['cargo']},{trabajador['sueldo_bruto']},{trabajador['desc_salud']},{trabajador['desc_afp']},{trabajador['liquido']}\n")
            print("Planilla de sueldos guardada en 'planilla_sueldos.txt'")
        elif opcion == '2':
            cargos = {trabajador['cargo'] for trabajador in trabajadores}
            print("Cargos disponibles:", ", ".join(cargos))
            cargo = input("Ingrese el cargo: ")
            if cargo not in cargos:
                print("Cargo no encontrado.")
                return
            with open(f'planilla_sueldos_{cargo}.txt', 'w', encoding='utf-8') as archivo:
                archivo.write('Nombre,Cargo,Sueldo Bruto,Desc. Salud,Desc. AFP,Líquido a Pagar\n')
                for trabajador in trabajadores:
                    if trabajador['cargo'] == cargo:
                        archivo.write(f"{trabajador['nombre']},{trabajador['cargo']},{trabajador['sueldo_bruto']},{trabajador['desc_salud']},{trabajador['desc_afp']},{trabajador['liquido']}\n")
            print(f"Planilla de sueldos para {cargo} guardada en 'planilla_sueldos_{cargo}.txt'")
        else:
            print("Opción inválida.")
    except IndexError:
        print("No hay trabajadores registrados.")

def menu():
    with open('mi_archivo.txt', 'w', encoding='utf-8') as archivo:
        archivo.write('Estamos nombrando a los trabajadores con su cargo sueldo descuento y liquido\n')
        archivo.write('por favor colabora con nosotros\n')

    while True:
        print("\nMenu Principal")
        print("[1] Registrar trabajador")
        print("[2] Listar trabajadores")
        print("[3] Imprimir planilla de sueldos")
        print("[0] Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_trabajador()
        elif opcion == '2':
            listar_trabajadores()
        elif opcion == '3':
            imprimir_planilla()
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")

if __name__ == "__main__":
    trabajadores = []
    menu()