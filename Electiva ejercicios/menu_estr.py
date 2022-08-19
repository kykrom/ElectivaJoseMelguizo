from html.entities import name2codepoint


op = 1
print ("elija una opción 1 para calcular un factorial  , 2 para hacer una multiplicación a base de sumas,  3 para hacer una division a base de restas, 4 para hacer fibonacci y 5 para salir")
op = (int(input()))
while op <= 4:
    if op == 1:
        print("ingrese el numero que quiere encontrarle el factorial")
        num=(int(input()))
        if num < 0:
            print("no existe factorial de numeros negativos")
        elif num == 0:
            print("el factorial de 0 es 1")
        else:
            c = num
            fact = 1
            while (num > 1 ):
                fact *= num
                num -= 1
                
        print("el factorial de", c,"es" ,fact) 
    if op ==2:
        print("ingrese el numero que quiere multiplicar a base de sumas")
        n=(int(input()))
        print("ingrese cuantas veces lo quiere multiplicar")
        c=(int(input()))
        num=0
        con=1
        while con <= c:
         num = n+num
         con +=con
        print("el numero es:",num)
    if op ==3:
        print("ingrese el numero que quiere dividir a base de restas")
        n=(int(input()))
        print("ingrese el numero con el que lo quiere dividir")
        c=(int(input()))
        num=n
        con=0
        while num > 0:
         con += 1
         num = num-c
         
        print("el numero es:",con)
    if op ==4:
        print("ingrese el valor del numero")
        n=(int(input()))
        c=0; b=1; sum=0; cont=1
        print("la secuencia de fibonacci es la siguiente")
        while cont<=n:
            print(sum)
            cont +=1
            c=b
            b=sum
            sum=c+b


        print ("elija una opción 1 para calcular un factorial  , 2 para hacer una multiplicación a base de sumas,  3 para hacer una division a base de restas, 4 para hacer fibonacci y 5 para salir")
        op = int(input())