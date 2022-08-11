#primer ejercicio
op = 1
print ("elija una opción 1 para el primer ejercicio  , 2 para el segundo ejercicio y  3 para salir")
op = int(input())
while op <= 2:
    if op == 1:
        plata = 18000
        paga = 10.000
        resultado = plata + paga
        print(resultado)
        print (("el resultado es un: "+ type(resultado).__name__))



        print("ingrese el precio del producto para calcular el IVA")
        producto = int(input())
        iva = (producto * 0.19) 
        total = iva + producto

        print("el iva es: " , iva)
        print("el total a pagar es:" , total)

    #segundo ejercicio
    else:
        print("ingrese el texto que quiere ver en pantalla")
        text= (str(input()))
        print("su texto es: " + text)
        carac = len(text)
        print("el total de caracteres es: ", carac)

        print("ingrese el texto que quiere ver en pantalla")
        t= (str(input()))
        print("ingrese el texto que quiere ver en pantalla")
        e= (str(input()))
        print(t +" "+ e)

        print("ingrese su edad")
        edad= (int(input()))
        print("tu edad es: " , edad)
        print ("elija una opción 1 para el primer ejercicio  y 2 para el segundo ejercicio")
        op = int(input())