from heuristicanodo import Nodo
import pygame, sys
import random
import copy

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

pygame.init()
dimensiones = [800, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("PROYECTO HEURISTICA")

juego_terminado = False

reloj = pygame.time.Clock()
new_font2 = pygame.font.SysFont('impact', 25)
game_end = new_font2.render("BUSQUEDA HEURISTICA", True, (255,0,0))
inicio = new_font2.render("START", True, (0,0,0))

#PARA MOVER OBJETO
x = 10
y =10
#vel = 10
ancho=125
alto=125
#[0] = POSICION X, [1] =POSICION Y,[2]= COLOR, [3]=TEXTO
matrizInputs=[[dimensiones[0]-240,70,"lightskyblue3",""],[dimensiones[0]-190,70,"lightskyblue3",""],[dimensiones[0]-140,70,"lightskyblue3",""],
            [dimensiones[0]-90,70,"lightskyblue3",""], [dimensiones[0]-240,130,"lightskyblue3",""],[dimensiones[0]-190,130,"lightskyblue3",""],
            [dimensiones[0]-140,130,"lightskyblue3",""],[dimensiones[0]-90,130,"lightskyblue3",""] ,[dimensiones[0]-240,190,"lightskyblue3",""],
            [dimensiones[0]-190,190,"lightskyblue3",""],[dimensiones[0]-140,190,"lightskyblue3",""],[dimensiones[0]-90,190,"lightskyblue3",""] ,
            [dimensiones[0]-240,250,"lightskyblue3",""],[dimensiones[0]-190,250,"lightskyblue3",""],[dimensiones[0]-140,250,"lightskyblue3",""],
            [dimensiones[0]-90,250,"lightskyblue3",""] ]
#MATRIZ DE LA CUADRICULA DE LA MATRIZ
matriz=([ [ [x,y,0,(0,255,0),ancho,alto], [(x+ancho+2),y,2,(255,255,0),ancho,alto], [ (x+(ancho*2)+4),y,1,(255,255,0),ancho,alto ], [(x+(ancho*3)+6),y,4,(255,255,0),ancho,alto] ]
        , [ [x,(y+(alto)+2),6,(255,255,0),ancho,alto] , [(x+ancho+2),(y+(alto)+2),7,(255,255,0),ancho,alto], [(x+(ancho*2)+4),(y+alto+2),3,(255,255,0),ancho,alto], [(x+(ancho*3)+6),(y+alto+2),8,(255,255,0),ancho,alto] ]
        , [ [x,(y+(alto*2)+4),5,(255,255,0),ancho,alto] , [(x+ancho+2),(y+(alto*2)+4),10,(255,255,0),ancho,alto], [(x+(ancho*2)+4),(y+(alto*2)+4),11,(255,255,0),ancho,alto], [(x+(ancho*3)+6),(y+(alto*2)+4),12,(255,255,0),ancho,alto] ]
        , [ [x,(y+(alto*3)+6),9,(255,255,0),ancho,alto] , [(x+ancho+2),(y+(alto*3)+6),13,(255,255,0),ancho,alto], [(x+(ancho*2)+4),(y+(alto*3)+6),14,(255,255,0),ancho,alto], [(x+(ancho*3)+6),(y+(alto*3)+6),15,(255,255,0),ancho,alto] ]  ])
estado_inicial = ( [[1, 0, 2, 4], [6, 7, 3, 8], [5, 10, 11, 12], [9, 13, 14, 15]])
estado_final=([[1, 2, 3,4], [5, 6, 7,8],[9,10, 11, 12],[13,14,15,0]])
posicionEscrita=-1

def busqueda_amplitud(e_inicial,e_final,matrizAtributos):
    exito=False
    textoError=""
    nodos_frontera=[]
    nodos_visitados=[]
    # Creación del primer nodo inicial o un ojbeto de tipo Nodo
    NodoInicial=Nodo(e_inicial)
    nodos_frontera.append(NodoInicial)
    comparaciones=0
    
    while len(nodos_frontera)!=0 and (not exito):
        pygame.time.delay(100) 
        graficarItems(matrizAtributos)
        handleEvents()
        #nodo es el Nodo padre inicialmente y nodos_frontera llegaria a ser una cola porque saca el primero que estuvo en la cola y asi sucesivamente
        nodo=nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        print("Vuelta = ",comparaciones," - ",nodo.obtener_datos())
        if nodo.obtener_datos()==e_final:
            exito=True
            print("cantidad de comparaciones: ",comparaciones)
            return nodo
        else:
            comparaciones+=1            
            aux=nodo.obtener_datos()            
            fila=0
            columna=0
            x=len(aux)
            y= len(aux[0])

            for i in range(x):
                for j in range(y):
                    if aux[i][j]==0:
                        fila=i #2
                        columna=j  #0
                        break
            
            nodos_hijos=[]
            if  (fila + columna)>=2 and fila>0 and columna>0 and fila<3 and columna<3:
                mataux = nodoresultante3X3(copy.deepcopy(aux),fila,columna,0,-1)
                nodo_izquierdo=Nodo(mataux)
                nodo_izquierdo.asignar_coste( costodelnodo(e_final,mataux) )
                mataux =nodoresultante3X3(copy.deepcopy(aux),fila,columna,-1,0)
                nodo_arriba=Nodo(mataux)
                nodo_arriba.asignar_coste( costodelnodo(e_final,mataux) )
                mataux=nodoresultante3X3(copy.deepcopy(aux),fila,columna,0,1)
                nodo_derecho=Nodo(mataux)
                nodo_derecho.asignar_coste( costodelnodo(e_final,mataux) )
                mataux = nodoresultante3X3(copy.deepcopy(aux),fila,columna,1,0)
                nodo_abajo=Nodo(mataux)
                nodo_abajo.asignar_coste( costodelnodo(e_final, mataux) )

                if not nodo_izquierdo.en_lista(nodos_visitados):
                    nodos_hijos.append(nodo_izquierdo) 
                
                if not nodo_arriba.en_lista(nodos_visitados):
                    nodos_hijos.append(nodo_arriba)                
               
                if not nodo_derecho.en_lista(nodos_visitados):
                    nodos_hijos.append(nodo_derecho)                
                
                if not nodo_abajo.en_lista(nodos_visitados):
                    nodos_hijos.append(nodo_abajo)
                
                nodo_elegido=buscar_nodo_elegido(nodos_hijos)
                nodos_frontera.append(nodo_elegido)

                posiciones=encontrar_cero(nodo_elegido.obtener_datos() )
                auxcolor=matrizAtributos[fila][columna][3]
                matrizAtributos[fila][columna][3]=matrizAtributos[posiciones[0]][posiciones[1] ][3]
                matrizAtributos[posiciones[0]][posiciones[1] ][3]=auxcolor
                valor=matrizAtributos[fila][columna][2]
                matrizAtributos[fila][columna][2]=matrizAtributos[posiciones[0]][posiciones[1] ][2]
                matrizAtributos[posiciones[0]][posiciones[1] ][2]=valor

                try:
                    nodo.asignar_hijos([nodo_elegido])
                except:
                    textoError="Sin Nodos, No Solucionado"
                    break
                #nodo.asignar_hijos([nodo_izquierdo,nodo_arriba,nodo_derecho,nodo_abajo])
            elif ((fila+columna)>=1 and  (fila+columna)<=2) or ((fila+columna)>=4 and  (fila+columna)<=5)   :
                #PILLAMOS SI EN UNO DE LOS CENTROS LATERALES ESTA EL CERO                 
                 if fila==1 or fila ==2:                     
                     nodo_arriba=nodoresultante3X3(copy.deepcopy(aux),fila,columna,-1,0)
                     nodo_abajo=nodoresultante3X3(copy.deepcopy(aux),fila,columna,1,0)                    
                     if fila > columna:
                        nodo_centro=nodoresultante3X3(copy.deepcopy(aux),fila,columna,0,1)
                     else:
                        nodo_centro=nodoresultante3X3(copy.deepcopy(aux),fila,columna,0,-1)   
                     
                     nodo_A=Nodo(nodo_arriba)
                     nodo_A.asignar_coste( costodelnodo(e_final,nodo_arriba) )
                     nodo_B=Nodo(nodo_abajo)
                     nodo_B.asignar_coste ( costodelnodo(e_final,nodo_abajo) )
                     nodo_C= Nodo(nodo_centro)
                     nodo_C.asignar_coste( costodelnodo(e_final,nodo_centro) )

                     if not nodo_A.en_lista(nodos_visitados):
                         nodos_hijos.append(nodo_A)
                    
                     if not nodo_B.en_lista(nodos_visitados):
                         nodos_hijos.append(nodo_B)
                     
                     if not nodo_C.en_lista(nodos_visitados):
                         nodos_hijos.append(nodo_C)

                     nodo_elegido=buscar_nodo_elegido(nodos_hijos)
                     nodos_frontera.append(nodo_elegido)

                     try:
                         nodo.asignar_hijos([nodo_elegido])
                     except:
                         textoError="Sin Nodos, No Solucionado"
                         break

                     #nodo.asignar_hijos([nodo_A,nodo_B,nodo_C])
                 else:
                     nodo_izquierda = nodoresultante3X3(copy.deepcopy(aux),fila,columna,0,-1)
                     nodo_derecha = nodoresultante3X3(copy.deepcopy(aux),fila,columna,0,1)
                     if columna>fila:
                        nodo_centro= nodoresultante3X3(copy.deepcopy(aux),fila,columna,1,0)
                     else:
                        nodo_centro= nodoresultante3X3(copy.deepcopy(aux),fila,columna,-1,0)
                    
                     nodo_I=Nodo(nodo_izquierda)
                     nodo_I.asignar_coste( costodelnodo(e_final,nodo_izquierda) )
                     nodo_C=Nodo(nodo_centro)
                     nodo_C.asignar_coste( costodelnodo(e_final,nodo_centro) )
                     nodo_D=Nodo(nodo_derecha)
                     nodo_D.asignar_coste( costodelnodo(e_final,nodo_derecha) )

                     if not nodo_I.en_lista(nodos_visitados):
                        nodos_hijos.append(nodo_I)
                    
                     if not nodo_C.en_lista(nodos_visitados):
                        nodos_hijos.append(nodo_C)
                     
                     if not nodo_D.en_lista(nodos_visitados):
                        nodos_hijos.append(nodo_D)            
                     nodo_elegido=buscar_nodo_elegido(nodos_hijos)
                     nodos_frontera.append(nodo_elegido)

                     try:
                        nodo.asignar_hijos([nodo_elegido])
                     except:
                         textoError="Sin Nodos, No Solucionado"
                         break
                 
                 posiciones=encontrar_cero(nodo_elegido.obtener_datos() )
                 auxcolor=matrizAtributos[fila][columna][3]
                 matrizAtributos[fila][columna][3]=matrizAtributos[posiciones[0]][posiciones[1] ][3]
                 matrizAtributos[posiciones[0]][posiciones[1] ][3]=auxcolor
                 valor=matrizAtributos[fila][columna][2]
                 matrizAtributos[fila][columna][2]=matrizAtributos[posiciones[0]][posiciones[1] ][2]
                 matrizAtributos[posiciones[0]][posiciones[1] ][2]=valor

            else:
                #PILLAMOS SI EN UNA DE LAS ESQUINAS ESTA EL CERO
                if fila<=columna and (fila+columna)<len(aux) :
                    #ESQUINAS  arriba
                    nodo_abajo= nodoresultante3X3(copy.deepcopy(aux),fila,columna,1,0)
                    if columna<=fila:
                         nodo_lado=nodoresultante3X3(copy.deepcopy(aux),fila,columna,0,1)
                    else:
                        nodo_lado = nodoresultante3X3(copy.deepcopy(aux),fila,columna,0,-1)
                    nodo_A = Nodo(nodo_abajo)
                    nodo_A.asignar_coste( costodelnodo(e_final,nodo_abajo) )
                    nodo_L=Nodo(nodo_lado)
                    nodo_L.asignar_coste( costodelnodo(e_final,nodo_lado) )
                    if not nodo_A.en_lista(nodos_visitados):
                        nodos_hijos.append(nodo_A)
                    
                    if not nodo_L.en_lista(nodos_visitados):
                        nodos_hijos.append(nodo_L)
                    #nodo.asignar_hijos([nodo_A,nodo_L])
                    nodo_elegido=buscar_nodo_elegido(nodos_hijos)
                    nodos_frontera.append(nodo_elegido)

                    try:
                        nodo.asignar_hijos([nodo_elegido])
                    except:
                        textoError="Sin Nodos, No Solucionado"
                        break
                else:
                    #esquinas de abajo
                    nodo_arriba=nodoresultante3X3(copy.deepcopy(aux),fila,columna,-1,0)
                    if columna< fila:
                        nodo_abajo= nodoresultante3X3(copy.deepcopy(aux),fila,columna,0,1)
                    else:
                        nodo_abajo=nodoresultante3X3(copy.deepcopy(aux),fila,columna,0,-1)
                    nodo_AA = Nodo(nodo_arriba)
                    nodo_AA.asignar_coste( costodelnodo( e_final,nodo_arriba) )
                    nodo_AAA=Nodo(nodo_abajo)
                    nodo_AAA.asignar_coste( costodelnodo(e_final,nodo_abajo))                    

                    if not nodo_AA.en_lista(nodos_visitados):
                        nodos_hijos.append(nodo_AA)
                    if not nodo_AAA.en_lista(nodos_visitados):
                        nodos_hijos.append(nodo_AAA)
                    #nodo.asignar_hijos([nodo_AA,nodo_AAA])
                    nodo_elegido=buscar_nodo_elegido(nodos_hijos)
                    nodos_frontera.append(nodo_elegido)
                    try:
                        nodo.asignar_hijos([nodo_elegido])
                    except:
                        textoError="Sin Nodos, No Solucionado"
                        break
                
                posiciones=encontrar_cero(nodo_elegido.obtener_datos() )
                auxcolor=matrizAtributos[fila][columna][3]
                matrizAtributos[fila][columna][3]=matrizAtributos[posiciones[0]][posiciones[1] ][3]
                matrizAtributos[posiciones[0]][posiciones[1] ][3]=auxcolor
                valor=matrizAtributos[fila][columna][2]
                matrizAtributos[fila][columna][2]=matrizAtributos[posiciones[0]][posiciones[1] ][2]
                matrizAtributos[posiciones[0]][posiciones[1] ][2]=valor

    #por si ocurre un errorenviamos el mensaje de error
    return textoError       

def nodoresultante3X3(nodo,posicionx,posiciony,sumarorestarX,sumarorestarY):    
    aux = nodo[posicionx][posiciony]
    nodo[posicionx][posiciony]= nodo[posicionx+sumarorestarX][posiciony+sumarorestarY]
    nodo[posicionx+sumarorestarX][posiciony+ sumarorestarY]=0
    return nodo

def costodelnodo(nodooriginal,nodohijo):
    costo=0
    for i in range(len(nodooriginal)):
        for j in range(len(nodooriginal[0])):
            if nodooriginal[i][j]==nodohijo[i][j]:                
                costo+=1       
    return costo

def buscar_nodo_elegido(lista_nodos_hijos):
    coste=0
    nodo_eficiente=[]
    for item in lista_nodos_hijos:
        if(item.obtener_coste()>coste):
            nodo_eficiente=item
            coste=item.obtener_coste()
        elif item.obtener_coste()==coste:
            lista1=encontrar_cero(item.obtener_datos())
            x1=lista1[0]
            y1=lista1[1]
            if  (x1 + y1)>=2 and x1>0 and y1>0 and x1<3 and y1<3:
                 #ACA SI EL NODO ACTUAL CUMPLE CON LAS CONDICIONES DE ESTA EN CENTRO LO ACTUALIZAMOS COMO NODO ACTUAL
                nodo_eficiente=item      
    return nodo_eficiente   

def encontrar_cero(nodo):
    fila=0
    columna=0
    for i in  range(len(nodo)):
        for j in range(len(nodo[0])):
            if nodo[i][j]==0:
                fila=i
                columna=j
                break
    return [fila,columna]

def handleEvents():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def graficarItems(matriz1):
    pantalla.fill(NEGRO) 
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            pygame.draw.rect(pantalla, matriz1[i][j][3], (matriz1[i][j][0], matriz1[i][j][1], matriz1[i][j][4], matriz1[i][j][5] ))            
            letra = new_font2.render( str(matriz1[i][j][2]) , True, (0,0,0) )
            pantalla.blit(letra, (  matriz1[i][j][0] + (matriz1[i][j][4] /2) , matriz1[i][j][1] +(matriz1[i][j][5] /2) )) 

    pygame.draw.rect(pantalla, BLANCO, pygame. Rect(dimensiones[0]-250, 0, 250, dimensiones[1]))
    pantalla.blit(game_end, ( dimensiones[0]-230,10))
    pygame.display.update()  
    reloj.tick(5)
    pygame.display.flip()    

def configurarMatrizAtributos(matriz1,estadoinicial):
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if estadoinicial[i][j]==0:
                matriz1[i][j][2]=estadoinicial[i][j]
                matriz1[i][j][3]=(0,255,0)
            else:
                matriz1[i][j][2]=estadoinicial[i][j]
                matriz1[i][j][3]=(255,255,0)
    return matriz1

def dibujarcuadros(vector):
    for i in range(len(vector)):
        pygame.draw.rect(pantalla, vector[i][2], pygame. Rect(vector[i][0], vector[i][1], 40, 50))
        letra = new_font2.render( str(vector[i][3]) , True, (0,0,0) )
        pantalla.blit( letra, ( vector[i][0]+4, vector[i][1]+4 ))

def verificarToqueCuadro(click,matInputs):
    posicionM=-1
    for i in range(len(matrizInputs)):
        if (matrizInputs[i][0]) <= click[0] <= (matrizInputs[i][0])+40 and (matrizInputs[i][1]) <= click[1] <= (matrizInputs[i][1])+50:
            matrizInputs[i][2]=(0,255,0)
            posicionM=i
        else:
            matrizInputs[i][2]="lightskyblue3"
    return posicionM

def actualizarEstadoInicialUser(estadoInicial,MatrizIngresadoUsuario):
    aux=0
    for i in range(len(estadoInicial)):
        for j in range(len(estadoInicial[0])):
            estadoInicial[i][j]=int(MatrizIngresadoUsuario[aux][3])
            aux+=1
    return estadoInicial

matriz=configurarMatrizAtributos(matriz,estado_inicial)
#[[1, 0, 2, 4], [6, 7, 3, 8], [5, 10, 11, 12], [9, 13, 14, 15]]
#[[1, 2, 0, 4], [6, 7, 3, 8], [5, 10, 11, 12], [9, 13, 14, 15]]

solucion=[]
IniciarBucle=False
graficarItems(matriz)

while juego_terminado is False:
    pygame.time.delay(80)    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #EVENTO
            juego_terminado = True
            pygame.quit()       
        if evento.type == pygame.MOUSEBUTTONDOWN:  #EVENTO comprueba si se hace click en la pantalla
            if (dimensiones[0]-220) <= mouse[0] <= (dimensiones[0]-220)+200 and (dimensiones[1]-100) <= mouse[1] <= (dimensiones[1]-100)+70:
                IniciarBucle=True
                solucion=[]
                estado_inicial= actualizarEstadoInicialUser(estado_inicial,matrizInputs)
                #print("ESTADO ",estado_inicial)
                matriz=configurarMatrizAtributos(matriz,estado_inicial)
                graficarItems(copy.deepcopy(matriz))
            #esta funcion llamara a que input hicimos click
            posicionEscrita=verificarToqueCuadro(mouse,matrizInputs)
        if evento.type==pygame.KEYDOWN: #EVENTO
            #verificamos el teclado
            if posicionEscrita>-1: #verificamos si posicionescrita tiene la posicion del cuadro
                if evento.key == pygame.K_BACKSPACE: #verificamos si esla tecla de borrar
                    matrizInputs[posicionEscrita][3] = matrizInputs[posicionEscrita][3][:-1]#borramos la ultima letra                    
                else:
                    if len(matrizInputs[posicionEscrita][3])<2:#verificamos que lacantidad de letras en la casilla solo sean dos o menos
                        matrizInputs[posicionEscrita][3] += evento.unicode #aca aumentamos la letra que digito en la posicion del cuadro

    mouse = pygame.mouse.get_pos() 
    if solucion!=estado_final and IniciarBucle ==True:        
        solucion=busqueda_amplitud(estado_inicial,estado_final,copy.deepcopy(matriz))
        if(solucion!="Sin Nodos, No Solucionado"):
            solucion=solucion.obtener_datos()                 
        IniciarBucle=False
    elif solucion==estado_final:
        letrerofinal = new_font2.render(" RESUELTO", True, (0,255,0))
        pantalla.blit( letrerofinal, ( dimensiones[0]/3, dimensiones[1]-(dimensiones[1]/8) ))
    elif solucion =="Sin Nodos, No Solucionado":
        letrerofinal = new_font2.render("Sin Nodos, No Solucionado", True, (255,0,0))
        pantalla.blit( letrerofinal, ( dimensiones[0]/3-40, dimensiones[1]-(dimensiones[1]/8) ))
    
    
    #resctangfulko  de menu
    pygame.draw.rect(pantalla, BLANCO, pygame. Rect(dimensiones[0]-250, 0, 250, dimensiones[1]))
    pantalla.blit(game_end, ( dimensiones[0]-230,10))    

    #boton
    if (dimensiones[0]-220) <= mouse[0] <= (dimensiones[0]-220)+200 and (dimensiones[1]-100) <= mouse[1] <= (dimensiones[1]-100)+70:
        pygame.draw.rect(pantalla, (0,255,200), pygame. Rect(dimensiones[0]-220, dimensiones[1]-100, 200, 70))        
    else: 
        pygame.draw.rect(pantalla, (0,255,255), pygame. Rect(dimensiones[0]-220, dimensiones[1]-100, 200, 70))
    
    pantalla.blit(inicio, ( dimensiones[0]-170, dimensiones[1]-90 ))    

    dibujarcuadros(matrizInputs)

    #para actualizar la pantalla y mostrar
    pygame.display.update()  
    pygame.display.flip()
    reloj.tick(5)
    #print(reloj)

