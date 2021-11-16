import random
puntos_ju1=0
puntos_ju2=0

puntos1=[15,30,40,"deus","advance","win"]
puntos2=[15,30,40,"deus","advance","win"]
con=True
cont=0
cont_ju=1
while con==True:
    if(cont_ju>2):
        cont_ju=1
    print("si es par 1 y si es impar 0\nAdivine el numero jugador numero "+ str(cont_ju)+ ":")
    num1=int(input())
    ran=random.randint(1,10)
    if(cont_ju==1):
        if (ran % 2 == 0):
            if (num1 == 0):
                puntos_ju1 = puntos1[cont]
                cont = cont + 1

        else:
            if (num1 == 1):
                puntos_ju1 = puntos1[cont]
                cont = cont + 1


    else:
        if (ran % 2 == 0):
            if (num1 == 1):
                puntos_ju2 = puntos2[cont]
                cont = cont + 1


        else:
            if (num1 == 0):
                puntos_ju2 = puntos2[cont]
                cont = cont + 1
    cont_ju=cont_ju+1
    print("jugador uno puntos: "+str(puntos_ju1)+" y jugador dos puntos: "+str(puntos_ju2))





