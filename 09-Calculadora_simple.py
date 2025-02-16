# el menu
# la variable resultado
# verificar si hay un numero ya fue ingresado
# si no se ha ingresado un numero le tenemos que decir al usuario que no ingresado numero
# si ya ingreso numero decirle al usuario que coloque una operacion
# le pida al usuario un numero y una operacion

# sino no ingreso el numero la primera vez pero ya lo hizo le tenemos que pedir que coloque una operacion
# ingresar operacion

# luego le pediremos que ingrese otro numero

# mostrar el resultado

# finalmente le mostraremos el resultado

# ---------------------------------------------------------------------------------------------------------------
#premiere vesion

print("hola soy una calculadora")
print("puedo: SUMAR, RESTAR, MULTIPLICAR, DIVIDIR")
print("para terminar escribe: salir")

resultado = ""


while True:
    if not resultado:
        resultado = input("escribe un numero: ")
        if resultado.lower() == "salir":
            break
        if resultado != 0:
            resultado = int(resultado)

    operacion = input("ingresa una operacion: ")
    if operacion.lower() == "salir":
        break

    numero_2 = input("ingresa un numero: ")
    if numero_2.lower() == "salir":
        break
    numero_2 = int(numero_2)

    if operacion.lower() == "suma":
        resultado = resultado + numero_2
    if operacion.lower() == "resta":
        resultado = resultado - numero_2
    if operacion.lower() == "multiplicacion":
        resultado = resultado * numero_2
    if operacion.lower() == "division":
        resultado = resultado / numero_2

    print(f"tu resultado es {resultado}")

# -----------------------------------------------------------------------------------------------------------------------
#deuxieme version 
print("**********************************************************************************")
print("**********************************************************************************")
print("***************       HOLA SOY UNA CALCULADORA             ************************")
print("*************    PUEDO, SUMAR, RESTAR, MULTIPLICAR y DIVIDIR   ********************")
print("********            puedes escribir 'salir' para SALIR           ******************")
print("***************                                                    ****************")
print("**********************************************************************************")

resultado = ""

while True:
    if not resultado:
        resultado = input("Por Favor Elija Un Numero O Escriba Salir: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    operacion = input("quieres: sumar, restar, multiplicar o dividir: ")
    if operacion.lower() == "salir":
        break

    numero_2 = input("ingresa tu segundo numero: ")
    if numero_2.lower() == "salir":
        break
    numero_2 = int(numero_2)

    if operacion.lower() == "sumar":
        resultado = resultado + numero_2

    if operacion.lower() == "restar":
        resultado = resultado - numero_2

    if operacion.lower() == "multiplicar":
        resultado = resultado * numero_2

    if operacion.lower() == "dividir":
        resultado = resultado / numero_2

    print(f"tu resultado es {resultado}")
