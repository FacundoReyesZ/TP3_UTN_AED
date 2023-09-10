class Vehiculo:
    def __init__(self, identificador, patente, tipo_vehiculo, forma_de_pago, pais_cabina, distancia):
        self.identificador = identificador
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_de_pago = forma_de_pago
        self.pais_cabina = pais_cabina
        self.distancia = distancia

    def __str__(self):
        return 'Codigo: ' + str(self.identificador) \
            + ' | Patente: ' + self.patente \
            + ' | Vehiculo tipo: ' + str(self.tipo_vehiculo) \
            + ' | Forma de pago: ' + str(self.forma_de_pago) \
            + ' | Pais de cabina: ' + str(self.pais_cabina) \
            + ' | Distancia: ' + str(self.distancia)


def print_registro(registro_vehiculos):
    for vehiculo in registro_vehiculos:
        print(vehiculo)


def validar_opc(opcion):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    if opcion in numeros:
        opcion = int(opcion)
        return opcion
    else:
        return None


def validar_n_caracteres(n, msm):
    flag = True
    x = str(input(msm))
    while flag:
        if len(x) == n:
            flag = False
        else:
            x = str(input("ERROR... Porfavor " + msm))
    return x


def validar_entre(lim_izq, lim_der, msm):
    flag = True
    x = int(input(msm))
    while flag:
        if lim_izq <= x <= lim_der:
            flag = False
        else:
            x = int(input("ERROR... " + msm))
    return x


def patente_arg(pat):
    if len(pat) < 7:
        return False

    if pat[:2].isalpha() and pat[2:5].isdigit() and pat[5:].isalpha():
        return True
    return False


def patente_brz(pat):
    if len(pat) < 7:
        return False

    if pat[:3].isalpha() and pat[3].isdigit() and pat[4].isalpha() and pat[5:].isdigit():
        return True
    return False


def patente_bol(pat):
    if len(pat) < 7:
        return False

    if pat[:2].isalpha() and pat[2:].isdigit():
        return True
    return False


def patente_par(pat):
    if len(pat) < 7:
        return False

    if pat[:4].isalpha() and pat[4:].isdigit():
        return True
    return False


def patente_uru(pat):
    if len(pat) < 7:
        return False

    if pat[:3].isalpha() and pat[3:].isdigit():
        return True
    return False


def patente_chi(pat):
    if pat[0].isspace():
        pat = pat[1:]
        if len(pat) < 6:
            return False

        if pat[:4].isalpha() and pat[4:].isdigit():
            return True
        return False


def buscar_idioma(fecha):
    fecha = fecha.upper()
    if "PT" in fecha:
        return "Portugués"
    elif "ES" in fecha:
        return "Español"
    else:
        return "NO SE ENCONTRO IDIOMA"


def crear_registro(arr):
    archivo = open("peajes-tp3.txt", "r")
    fecha = archivo.readline()
    idioma = buscar_idioma(fecha)

    def crear_objeto_vehiculo(vehic):
        identificador = vehic[:10]
        patente = vehic[10:17]
        tipo_vehiculo = int(vehic[17])
        forma_de_pago = int(vehic[18])
        pais_cabina = int(vehic[19])
        distancia = int(vehic[20:])

        return Vehiculo(identificador, patente, tipo_vehiculo, forma_de_pago, pais_cabina, distancia)

    datos_vehiculos = [linea.rstrip() for linea in archivo.readlines()]
    # Creando los objetos de vehículo
    for datos in datos_vehiculos:
        vehiculo = crear_objeto_vehiculo(datos)
        arr.append(vehiculo)

    print(f'\nArreglo creado correctamente\n')


def cargar_registro(arr):
    if not arr:
        crear_registro(arr)

    # Solicitamos los datos del registro
    identificador = validar_n_caracteres(n=10, msm="Ingrese codigo (numero entero de 10 caracteres):")
    patente = validar_n_caracteres(7, "Ingrese patente (combinacion letras y numeros de 7 caracteres):")
    tipo_vehiculo = validar_entre(0, 2, "Ingrese tipo vehiculo (0: motocicleta, 1: automóvil, 2: camión):")
    forma_de_pago = validar_entre(1, 2, "Indique la forma de pago (1: manual, 2 telepeaje):")
    pais_cabina = validar_entre(0, 4,
                                "Ingrese pais cabina (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay):")
    distancia = validar_n_caracteres(3, "Ingrese distancia (numero entero de 3 caracteres):")

    # Creamos el objeto de vehículo
    vehiculo = Vehiculo(identificador, patente, tipo_vehiculo, forma_de_pago, pais_cabina, distancia)

    # Agregamos el registro al arreglo
    arr.append(vehiculo)
    print("Registro cargado correctamente")


def mostrar_registros_ordenados(arr):
    # Ordenamos los registros por código de ticket
    arr.sort(key=lambda vehiculo: vehiculo.identificador)

    # Recorremos los registros ordenados
    for vehic in arr:

        # Obtenemos el nombre del país al que pertenece la patente
        if patente_chi(vehic.patente):
            pais = "Chile"
        elif patente_arg(vehic.patente):
            pais = "Argentina"
        elif patente_bol(vehic.patente):
            pais = "Bolivia"
        elif patente_brz(vehic.patente):
            pais = "Brasil"
        elif patente_par(vehic.patente):
            pais = "Paraguay"
        elif patente_uru(vehic.patente):
            pais = "Uruguay"
        else:
            pais = "Otro"

        # Imprimimos el registro
        print(f'Identificador: {vehic.identificador}  |  Patente: {vehic.patente}  |  País: {pais}')


def buscar_patente_y_pais(arr):
    patente = input("Ingrese la patente: ")
    pais_c = int(
        input("Ingrese el país de la cabina (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): "))

    # (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay)

    for registro in arr:
        if registro.patente == patente and registro.pais_cabina == pais_c:
            print(registro)
            break
        else:
            print(f'No se encontró ningún registro con la patente {patente} y la cabina del pais {pais_c}')
            break


def buscar_y_cambiar_forma_de_pago(arr):
    identificador = input("Ingrese el código de ticket: ")
    encontrado = False

    for registro in arr:
        if registro.identificador == identificador:
            # Cambiamos el valor de la forma de pago
            if registro.forma_de_pago == 1:
                registro.forma_de_pago = 2
            else:
                registro.forma_de_pago = 1

            # Imprimimos el registro modificado
            print(registro)
            encontrado = True
            break
    if not encontrado:
        print(f'No se encontró ningún registro con el codigo identificador:  {identificador}')


def contar_vehiculos_por_pais(arr):
    PAISES = ("Argentina", "Bolivia", "Brasil", "Chile", "Paraguay", "Uruguay", "Otro")

    contadores = [0] * len(PAISES)

    for registro in arr:
        indice_pais = obtener_indice_pais(registro.patente)
        contadores[indice_pais] += 1

    print("Cantidad de vehículos por país:")
    for pais, cantidad in enumerate(contadores):
        print(f'{PAISES[pais]}: {cantidad}')


def obtener_indice_pais(patente):
    if patente_arg(patente):
        return 0
    elif patente_bol(patente):
        return 1
    elif patente_brz(patente):
        return 2
    elif patente_chi(patente):
        return 3
    elif patente_par(patente):
        return 4
    elif patente_uru(patente):
        return 5
    else:
        return 6


def importe_por_vehiculo(arr):
    TIPOS_VEHICULO = ['Moto', 'Automovil', 'Camión']
    contadores = [0] * len(TIPOS_VEHICULO)
    for registro in arr:
        contadores[registro.tipo_vehiculo] += importe(registro)

    print("Monto por tipo de vehiculo:")
    for tipo, cantidad in enumerate(contadores):
        print(f'{TIPOS_VEHICULO[tipo]}: ${cantidad}')


def importe(reg):
    importe_base = 300

    if reg.pais_cabina == 1:
        importe_base = 200
    elif reg.pais_cabina == 2:
        importe_base = 400

    if reg.tipo_vehiculo == 0:
        importe_basico = importe_base * 0.5
    elif reg.tipo_vehiculo == 2:
        importe_basico = importe_base * 1.6
    else:
        importe_basico = importe_base

    if reg.forma_de_pago == 2:
        importe_final = importe_basico * 0.9
    else:
        importe_final = importe_basico

    return importe_final


def mayor_monto(arr):
    TIPOS_VEHICULO = ['Moto', 'Automovil', 'Camión']
    contadores = [0] * len(TIPOS_VEHICULO)
    imp_total = 0
    for registro in arr:
        contadores[registro.tipo_vehiculo] += importe(registro)

    mayor_acumulado = max(contadores)
    indice = contadores.index(mayor_acumulado)

    for cont in contadores:
        imp_total += cont

    porcentaje = (mayor_acumulado / imp_total) * 100

    print(f'vehiculo con mayor monto acumulado es: {TIPOS_VEHICULO[indice]} con: ${mayor_acumulado} \n')
    print(f'El porcentaje que representa el {TIPOS_VEHICULO[indice]} es: %{round(porcentaje, 2)}')


def distancia_promedio(arr):
    accu = average = 0
    for registro in arr:
        accu += registro.distancia
    if len(arr) > 0:
        average = accu / len(arr)

    return average


def mayor_promedio(arr, valor):
    contador = 0
    for registro in arr:
        if registro.distancia > valor:
            contador += 1

    return contador
