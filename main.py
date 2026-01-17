
## Creación de una lista
movimientos = []

## Creación de un diccionario
m1 = {
    'fecha' : '2026-01-15',
    'tipo' : 'ingreso',
    'monto' : 1500.00,
    'categoria' : 'sueldo',
    'descripción' : 'pago mensual'

}

m2 = {
    'fecha': '2026-01-15',
    'tipo' : 'egreso',
    'monto' : 200,
    'categoria' : 'comida',
    'descripción' : 'almuerzo'

}

## Insertar en la lista

movimientos.append(m1)
movimientos.append(m2)

print(movimientos)