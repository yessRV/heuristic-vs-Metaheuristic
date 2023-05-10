class Nodo():
    padre=None
    hijos=None
    dato=None
    coste=None
    #[0] SERA X, [1] SERA Y, [2] SERA VALOR ,[3] SERA COLOR,[4] SERA ANCHO, [5] sera alto
    matrizPropiedadesNodosIndice=None
    
    # Esta función es el contructor
    def __init__(self,dato,hijos=None,matrizpropiedades=None):
        self.hijos=None
        self.padre=None
        self.dato=dato        
        self.matrizPropiedadesNodosIndice=None
        self.asignar_hijos(hijos)
    
    #asignar x
    def asignar_x_Indice(self,x,fila,columna):
        self.matrizPropiedadesNodosIndice[fila][columna][0]=x
    #obtener x
    def obtener_X_Indice(self,fila,columna):
        return self.matrizPropiedadesNodosIndice[fila][columna][0]

    #asignar y
    def asignar_y_Indice(self,y,fila,columna):
        self.matrizPropiedadesNodosIndice[fila][columna][1]=y
    #obtener y
    def obtener_y_Indice(self,fila,columna):
        return self.matrizPropiedadesNodosIndice[fila][columna][1]

    #obtener color
    def obtener_color_indice(self,fila,columna):
        return self.matrizPropiedadesNodosIndice[fila][columna][3]
    #asignar color
    def asignar_color_indice(self,color,fila,columna):
        self.matrizPropiedadesNodosIndice[fila][columna][3]=color
    #asignar valor ala matriz de nodos
    def  asignar_valor_matriz_indices(self,valor,fila,columna):
        self.matrizPropiedadesNodosIndice[fila][columna][2]=valor
    def obtener_valor_matriz_indices(self,fila,columna):
        return self.matrizPropiedadesNodosIndice[fila][columna][2]

    #obtener ancho
    def obtener_ancho_indice(self,fila,columna):
        return self.matrizPropiedadesNodosIndice[fila][columna][4]
    #asignar ancho
    def asignar_ancho_indice(self,ancho,fila,columna):
        self.matrizPropiedadesNodosIndice[fila][columna][4]=ancho

    #asignar alto
    def asignar_alto_indice(self,alto,fila,columna):
        self.matrizPropiedadesNodosIndice[fila][columna][5]=alto
    #recojer alto
    def obtener_alto_indice(self,fila,columna):
        return self.matrizPropiedadesNodosIndice[fila][columna][5]
    
    #obtener matrizindices
    def obtener_matriz_prop(self):
        return self.matrizPropiedadesNodosIndice
    def asignar_atriz_prop(self,matriz):
        self.matrizPropiedadesNodosIndice=matriz

    # Obtener datos
    def obtener_datos(self):
        return self.dato
    
    # Asignar dato
    def asignar_datos(self,dato):
        self.dato=dato

    def obtener_coste(self):
        return self.coste

    def asignar_coste(self,coste):
        self.coste=coste

    # Asignar hijos
    def asignar_hijos(self,hijos):
        self.hijos=hijos
        if self.hijos!=None:
            for hijito in self.hijos:
                hijito.padre=self
    # Obtener hijos
    def obtener_hijos(self):
        return self.hijos

    # Obtener padre
    def obtener_padre(self):
        return self.padre
    
    # Asignar Padre
    def asignar_padre(self,padre):
        self.padre=padre


    def igual(self,nodo):
        if self.obtener_datos()==nodo.obtener_datos():
            return True
        else:
            return False

    def en_lista(self,lista_nodos):
        en_la_lista=False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista=True
        return en_la_lista
        
    def __str__(self):        
        return str(self.obtener_datos())
        
