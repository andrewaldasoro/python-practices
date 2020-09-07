bandera = True


def pedirNumero ():
    while True:
        try:
            x = int(input(""))
            return x
        except ValueError:  # habra error si los numeros son enteros
            print("Los numeros deben de ser enteros")


def unidades (num):
        if num == 1:
                return 'uno'
        if num == 2:
                return 'dos'
        if num == 3:
                return 'tres'
        if num == 4:
                return 'cuatro'
        if num == 5:
                return 'cinco'
        if num == 6:
                return 'seis'
        if num == 7:
                return 'siete'
        if num == 8:
                return 'ocho'
        if num == 9:
                return 'nueve'

def decenas (num):
        if num > 9 and num < 20:
                if num == 10:
                        return 'diez'
                elif num == 11:
                        return'once'
                elif num == 12:
                        return'doce'
                elif num == 13:
                        return'trece'
                elif num == 14:
                        return'catorce'
                elif num == 15:
                        return'quince'
                elif num == 16:
                        return'dieciseis'
                elif num == 17:
                        return'diecisiete'
                elif num == 18:
                        return'dieciocho'
                elif num == 19:
                        return'diecinueve'
def otros (num):
        if num > 19 and num < 30:
                if num == 20:
                        return 'veinte'
                else:
                        return 'veinti'
        if num > 29 and num < 40 :
                if num == 30:
                        return 'treinta'
                else:
                        return 'treinta y'
        if num > 29 and num < 50 :
                if num == 40:
                        return 'cuarenta'
                else:
                        return 'cuarenta y'
        if num > 29 and num < 60 :
                if num == 50:
                        return 'cincuenta'
                else:
                        return 'cincuenta y'
        if num > 29 and num < 70 :
                if num == 60:
                        return 'sesenta'
                else:
                        return 'sesenta y'
        if num > 29 and num < 80 :
                if num == 70:
                        return 'setenta'
                else:
                        return 'setenta y'
        if num > 29 and num < 90 :
                if num ==80:
                        return 'ochenta'
                else:
                        return 'ochenta y'
        if num > 29 and num < 100 :
                if num == 90:
                        return 'noventa'
                else:
                        return 'noventa y'

def centenas (num):
        if num > 99 and num<200:
                if num == 100:
                        return 'cien'
                else:
                        return 'ciento'
        if num > 199 and num < 300:
                return 'docientos'
        if num > 299 and num < 400:
                return 'trecientos'
        if num > 399 and num < 500:
                return 'cuatrocientos'
        if num > 499 and num < 600:
                return 'quinientos'
        if num > 599 and num < 700:
                return 'seiscientos'
        if num > 699 and num < 800:
                return 'setecientos'
        if num > 799 and num < 900:
                return 'ochocientos'
        if num > 899 and num < 1000:
                return 'novecientos'

def dividirCifras(num):
    cifras = []
    if num >= 1 and num < 1000:
        cifras.append(num)

    elif num > 999 and num < 1000000:
        temp = num // 1000
        cifras.append(temp)
        temp1 = temp * 1000
        temp2 = num - temp1
        cifras.append(temp2)

    elif num > 999999 and num < 1000000000:
        temp = num // 1000000000
        cifras.append(temp)
        temp1 = temp * 1000000
        temp2 = num - temp1
        temp3 = temp2 // 1000
        cifras.append(temp3)
        temp4 = temp3 * 1000
        temp5 = temp4 - temp1
        cifras.append(temp5)

    else:
        print("Numero fuera de rango")

    return cifras

def convertir(num):
    numTx = ""
    casoN = 0
    if num > 99:
        numTx = numTx + centenas(num)
        temp = num // 100
        num = temp * 100
        if (num % 100 == 0):
            casoN = 1
    if num > 9 and casoN == 0:
        if (num > 9 and num < 16):
            casoN = 1
        numTx = numTx + decenas(num)
        temp = num // 10
        num = num - temp * 10

    if casoN == 0 and num != 0:
        numTx - numTx + unidades(num)

    return numTx

def numeroTexto(cifras):
    tamaño = len(cifras)

    if tamaño == 1 and cifras[0] == 0:
        return "cero"

    if tamaño == 1:
        return convertir(cifras[0])

    if tamaño == 2:
        if cifras[0] == 1:
            return " mil " + convertir(cifras[1])
        else:
            return convertir(cifras[0]) + " mil " + convertir(cifras[1])

    if tamaño == 3:
        if cifras[0] == 1 and cifras[1] == 0:
            return "un millon " + convertir(cifras[2])
        elif cifras[0] == 1 and cifras[1] == 1:
            return "un millon mil " + convertir(cifras[2])
        elif cifras[0] != 1 and cifra[1] == 0:
            return convertir(cifras[0]) + " millones " + divertir(cifras[2])
        else:
            return convertir(cifras[0]) + " millones " + convertir(cifras[1]) + " mil " + convertir(cifras[2])

def prograNumTx():
    print("Ingresa el numero: ")
    num = pedirNumero()
    print(numeroTexto(dividirCifras(num)))
    print("")


def pedirOpcion ():
        while True:
                try:
                        opcion = int (input ('Por favor ingrese una opción: '))
                        return opcion
                except ValueError:
                        print ('Su opcion no es valida\n')

while bandera == True:
        print ('\tPrograma que muestra la notacion desarrollada de un número entero\n')
        print ('Opciones\n1.- Número en texto\n2.- Salir \n')
        opcion = pedirOpcion()

        if opcion == 1:
                prograNumTx ()

        elif opcion == 2:
                bandera = False

        else:
                print ("Su opción no es valida\n")
