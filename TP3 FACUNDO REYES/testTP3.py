import funcionesTP3


def test():
    registro_vehiculos = []
    creado = False
    opc = 0
    while opc != 10:
        print('\nMenu de opciones:\n')
        print('1. Crear el arreglo de registros')
        print('2. Cargar un registro')
        print('3. Mostrar todos los registros del arreglo ordenados')
        print('4. Buscar si existe en el arreglo un registro por patente')
        print('5. Buscar si existe en el arreglo un registro por código de ticket')
        print('6. Determinar la cantidad de vehículos de cada país que pasaron por las cabinas')
        print('7. Determinar el importe acumulado por pagos de tickets')
        print('8. determinar y mostrar cuál fue cuál fue el tipo de vehículo con mayor monto acumulado')
        print('9. Calcular y mostrar la distancia promedio desde la última cabina recorrida')
        print('10. Salir')

        opc = input('\nIngrese su eleccion: \n')
        opc_validada = funcionesTP3.validar_opc(opc)
        if opc_validada is not None:
            if opc_validada == 1:
                if not creado:
                    funcionesTP3.crear_registro(registro_vehiculos)
                if creado:
                    respuesta = input(
                        'El arreglo ya fue creado, esta seguro que desea borrarlo y crearlo de nuevo? , seleccione "s" '
                        'para Si y "n" para No: ')
                    if respuesta.lower() == "s":
                        funcionesTP3.crear_registro(registro_vehiculos)
                        print('Arreglo cargado desde cero correctamente')
                        continue
                    if respuesta.lower() == "n":
                        print('Usted cancelo la operacion de cargar de nuevo el arreglo.')
                        continue
                    else:
                        print('Opcion Invalida')
                creado = True

            if opc_validada == 2:
                funcionesTP3.cargar_registro(registro_vehiculos)

            if opc_validada == 3:
                funcionesTP3.mostrar_registros_ordenados(registro_vehiculos)

            if opc_validada == 4:
                funcionesTP3.buscar_patente_y_pais(registro_vehiculos)

            if opc_validada == 5:
                funcionesTP3.buscar_y_cambiar_forma_de_pago(registro_vehiculos)

            if opc_validada == 6:
                funcionesTP3.contar_vehiculos_por_pais(registro_vehiculos)

            if opc_validada == 7:
                funcionesTP3.importe_por_vehiculo(registro_vehiculos)

            if opc_validada == 8:
                funcionesTP3.mayor_monto(registro_vehiculos)
                print('')

            if opc_validada == 9:
                print(f'La distancia promedio: {round(funcionesTP3.distancia_promedio(registro_vehiculos), 2)} KM')
                print(
                    f'Vehiculos que superaron la distancia promedio: {funcionesTP3.mayor_promedio(registro_vehiculos, funcionesTP3.distancia_promedio(registro_vehiculos))}')

            if opc_validada == 10:
                break

        else:
            print('Ingreso una opcion invalida')


if __name__ == '__main__':
    test()
