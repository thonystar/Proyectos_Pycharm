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

        while True:

            if len(movimientos) == 0:
                print('No existes movimientos registrados')
                input("Presiona enter para continuar")
                continue

            mes = input("Indique el mes de resumen (YYYY-MM): ").strip()

            if not (len(mes) == 7 and mes[4] == "-") :
                print('Indique un valor de mes valido. Ejemplo: 2026-01')
                continue

            total_ingresos = 0
            total_egresos = 0
            encontrados = 0

            egresos_por_categ = {}

            for i in movimientos:

                if i["fecha"].startswith(mes):
                    encontrados += 1
                    if i["tipo"] == 'ingreso':
                        total_ingresos += i["monto"]
                    elif i["tipo"] == 'egreso':
                        cat = i["categoria"]
                        total_egresos += i["monto"]
                        egresos_por_categ[cat] = egresos_por_categ.get(cat, 0) + i["monto"]
                    else:
                        print("Tipo incorrecto")
            balance = total_ingresos - total_egresos

            print("\n Resumen del mes:", mes)
            if encontrados == 0:
                print("No hay movimientos registrados para este mes")
            else:
                print(f'Total de ingresos: {total_ingresos:.2f}')
                print(f'Total de egresos: {total_egresos:.2f}')
                print(f'Balance: {balance:.2f}')

                print("\n Egresos por categorias: ")
                for cat, total in sorted(egresos_por_categ.items(), key= lambda x: x[1], reverse= True):
                    print(f' - {cat}: {total:.2f}')


            input("Presiona enter para continuar")
            break



    elif opcion == "4":
        print("Saliendo del menú")
        break
    else:
        print(f'La opción {opcion} es invalida')
        input("Presione enter para continuar")


