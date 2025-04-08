def funcion():
    numero = 15
    acumulador_izquierda = 0
    acumulador_derecha = 0

    inicio = int(numero / 2)

    while inicio < numero:
        for i in range(inicio,numero,1):
            acumulador_derecha += i

        for i in range(0,inicio,1):
            acumulador_izquierda += i

        if acumulador_izquierda == acumulador_derecha:
            print("Sexo")
        else:
            inicio += 1
            acumulador_derecha=0
            acumulador_izquierda=0

setso = funcion()