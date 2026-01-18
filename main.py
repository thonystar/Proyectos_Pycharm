## Librerias a utilizar

from datetime import datetime


## Creación de una lista
movimientos = []

## Creación de un diccionario
m1 = {
    'fecha' : '2026-01-15',
    'tipo' : 'ingreso',
    'monto' : 1500.00,
    'categoria' : 'Sueldo',
    'descripcion' : 'pago mensual'

}

m2 = {
    'fecha': '2026-01-15',
    'tipo' : 'egreso',
    'monto' : 200,
    'categoria' : 'Comida',
    'descripcion' : 'almuerzo'

}

## Insertar en la lista

movimientos.append(m1)
movimientos.append(m2)

##print(movimientos)


##print("Cantidad de movimientos:", len(movimientos))

##print(movimientos[0])
##print(movimientos[1])

# Acceder por medio del indice a los elementos de las listas
## movimientos[0]['fecha'] = '2026-01-16'

# print(movimientos[0])




while True:
    print("\n=== MENÚ ===")
    print("1.- Agregar Movimiento")
    print("2.- Listar Movimientos")
    print("3.- Resumen mensual")
    print("4.- Salir")

    opcion = input("Elige una opción: ").strip() ## Elimina los espacios en blanco

    ## Debuggear
    #print("DEBUG opción: ", repr(opcion))

    if opcion == "1":
        while True:
            tipo_input = input("Indique el tipo de movimiento Ingreso(I) o Egreso (E): ").strip().upper()
            if tipo_input in ("E", "EGRESO"):
                tipo = "egreso"
                break
            elif tipo_input in ("I", "INGRESO"):
                tipo = 'ingreso'
                break
            else:
                print("Tipo invalido. Use I o E")

        while True:
            monto_input = input("Introduce un monto: ").strip().replace(",", ".")
            ## para que no escriban letras en vez de números usamos el try except
            try:
                monto = round(float(monto_input),2)
                if monto <= 0:
                    print(f'Monto invalido: {monto_input}. Debe ser mayor a cero.')
                else:
                    break
            except ValueError:
                print("Indique un valor valido. Ejemplo 40.50")


        while True:
            input_fecha = input("Indique la fecha del movimiento (YYYY-mm-dd): ").strip()

            if input_fecha == "":
                fecha = datetime.today().date().isoformat() ## con isoformat convierte el date en formato str
                break
            try:
                datetime.strptime(input_fecha, '%Y-%m-%d')
                fecha = input_fecha
                break
            except ValueError:
                print("Fecha invalida. Ejemplo 2026-01-15")

        while True:
            input_categoria = input("Indique la categoría a la que corresponde: ").strip()

            if input_categoria == "":

                print("La categoría no puede estar vacía, indicar una categoría")

            else:
                categoria = input_categoria.capitalize()
                break

        input_descripcion = input("Indique una descripción para su movimiento: ").strip()

        if input_descripcion == "":
            descripcion = "(Sin descripción)"
        else:
            descripcion = input_descripcion

        nuevo = {
            "fecha" : fecha,
            "tipo" : tipo,
            "monto" : monto,
            "categoria" : categoria,
            "descripcion" : descripcion
        }

        movimientos.append(nuevo)

        print("Movimiento Agregado")
        print(f'Tienes {len(movimientos)} movimientos')

        input("Presiona enter para continuar")





    elif opcion == "2":
        if len(movimientos) == 0:
            print("No hay movimientos registrados")
        else:
            for i in movimientos:
                ### creación de la variable signo
                signo = "+" if i['tipo'] == "ingreso" else '-'
                ## imprime los valores
                print(f'{i["fecha"]} | {i["tipo"]} | {signo}{i["monto"]:.2f} | {i["categoria"]} | {i["descripcion"]}')
        input("Presiona enter para continuar")

    elif opcion == "3":
        mes = input("Indique el mes de resumen (YYYY-MM): ").strip()

        total_ingresos = 0
        total_egresos = 0

        for i in movimientos:

            if i["fecha"].startswith(mes):
                if i["tipo"] == 'ingreso':
                    total_ingresos += i["monto"]
                else:
                    total_egresos += i["monto"]
        print(total_egresos)
        print(total_ingresos)

        input("Presiona enter para continuar")
    elif opcion == "4":
        print("Saliendo del menú")
        break
    else:
        print(f'La opción {opcion} es invalida')
        input("Presione enter para continuar")


