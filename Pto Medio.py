from tkinter import Tk, Entry
from numpy import array

n_Filas, ancho, root, obstaculos, r, ptos_Linea, pos_Elem = 5,\
            10, Tk(), [], range(1, 4), [(0,) * 2, (4,) * 2], 0
p_0, p_F = ptos_Linea
n_Columnas = n_Filas #rectangular?
malla, ns_Filas = n_Columnas * [0], range(n_Filas)              
ns_Columnas = ns_Filas
 
#PROBADOR
for n_Fila in ns_Filas:
    fila = n_Filas * [0]
    
    for n_Columna in ns_Columnas:
        celda = Entry(root, width = ancho)
        celda.grid(row = n_Fila, column = n_Columna)
        fila[n_Columna] = celda

    malla[n_Fila] = fila

malla = array(malla[::-1]).transpose()

'''for n_Fila in r:
    for n_Columna in r:
        obstaculos.append((n_Fila, n_Columna))
        malla[n_Fila][n_Columna].insert(0, 0)'''

while pos_Elem + 1 < len(ptos_Linea):
    p_0, p_F = ptos_Linea[pos_Elem : pos_Elem + 2]
    ptoMedio = tuple((array(p_0) + array(p_F)) // 2)

    if ptoMedio in obstaculos:
        pos_Elem = len(ptos_Linea)
        ptos_Linea[-1] = ptoMedio #no tiene xq ser el 1º comprueba
                                  #si hay mas subinterss
        
    else:
        if ptoMedio in ptos_Linea:
            pos_Elem += 1
            
        else:
            ptos_Linea.insert(pos_Elem + 1, ptoMedio) #list.insert()

for pto_Linea in ptos_Linea:
    pto_Linea_X, pto_Linea_Y = pto_Linea
    
    malla[pto_Linea_X][pto_Linea_Y].insert(0, 1) #tkinter.Entry.insert()











        
        

'''for n_Columna in ns_Columnas:
    for n_Fila in ns_Filas:   
        malla[n_Fila][n_Columna].insert(0, array((n_Fila, n_Columna)))'''

'''ps = array((0, 0)), array((0, 0))
p_0, p_F = ps                              
dibuja_Ptos_Medios_Calculados(ps)'''

'''for n_Fila in ns_Filas:
    for n_Columna in ns_Columnas:
        malla[n_Fila][n_Columna].insert(0, 1)
        print(array((n_Fila, n_Columna)))
    print()'''

