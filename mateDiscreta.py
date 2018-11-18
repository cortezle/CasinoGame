from random import randrange, choice

#variables
acumDineroGlob=0
cont=0
lista2=[]
lista3=[]
premio=0
bomba=0
cherry=0
vida=3
dinero=0
game=True
cont7=0
contcherry=0
contbomba=0
#funcion, esta devuelve un 'objeto' random
def random():
    lista=['bomba',7,'cherry']
    r=choice(lista)
    return r
 
#digo que tire
while(game):
    
    while(cont<3):
        lista2=[]
        
        for i in range(0,10):
            valor=random()
            lista2.append(valor)
        #al pregugntar si quiere seguir tirando y dice que si, vuelve a entrar al ciclo pero imprime antes de tiempo la lista
        print(lista2)
        #problema con sacar el porcentaje de algo en python:C
        cont7=0
        contcherry=0
        contbomba=0
        for i in range(0,len(lista2)):
            if lista2[i]==7:
                cont7=cont7+1
            elif lista2[i]=="cherry":
                contcherry=contcherry+1
            else:
                contbomba=contbomba+1
        print("La probabilidad que salga cherry es",(contcherry/10)*100,"%")
        print("La probabilidad que salga 7 es",(cont7/10)*100,"%")
        print("La probabilidad que salga bomba es",(contbomba/10)*100,"%")
        print('dinero actual: ',dinero)
        print('vidas: ',vida)    
        tiro=input('presione S para tirar : ')
        
        if tiro=='s' or tiro=='S':
            p=choice(lista2)
            print("Obtuviste: ",p)
            lista3.append(p)
            cont=cont+1
        
        else:
            print('por favot ingrese la palabra S si desea tirar ')
    print(lista3)

    #algoritmo para verificar si gano 1000, perdio -2 vida o +1 de vida
    pre=0
    bom=0
    cher=0
    for i in range(0,len(lista3)):
         if lista3[i]==7:
             pre=pre+1
         elif lista3[i]=='bomba':
             bom=bom+1
         elif lista3[i]=='cherry':
             cher=cher+1
    if pre==3:
        print('GANADOR!!! +1000 dolares')
        print("Vidas restauradas!")
        dinero=dinero+1000
        vida=3
    elif bom==3:
        print('GAMEOVER -2 vida')
        vida=vida-2
    elif cher==3:
        print('+1 vida')
        vida=vida+1
    else:
        vida=vida-1
        print("-1 vida")
        print('Intentalo de nuevo')
    print('dinero actual: ',dinero)
    print('vidas: ',vida)

    if vida<=0:
        print("MORISTE")
        break
    else:
        gameoff=input('presione s para continuar o n para retirarse ')
        if gameoff == 'n':
            game=False
            print('juego terminado')
        else:
            lista3=[]
            cont=0
    

