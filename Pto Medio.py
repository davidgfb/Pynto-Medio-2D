from tkinter import Tk, Entry
from numpy import array

n_Filas, ancho, root = 5, 10, Tk()
n_Columnas = n_Filas #rectangular?
malla, ns_Filas, ns_Columnas = n_Columnas * [0], range(n_Filas),\
                               range(n_Columnas)  

#PROBADOR
for n_Fila in ns_Filas:
    fila = n_Filas * [0]
    
    for n_Columna in ns_Columnas:
        celda = Entry(root, width = ancho)
        celda.grid(row = n_Fila, column = n_Columna)
        fila[n_Columna] = celda

    malla[n_Fila] = fila

malla = array(malla[::-1]).transpose()
p_0, p_F = (0, 0), (4, 4) 
   
if p_0 == p_F:
    p_0_X, p_0_Y = p_0

    malla[p_0_X][p_0_Y].insert(0, 1)
    
else:
    ptos_Linea, pos_Elem = [p_0, p_F], 0

    while pos_Elem + 1 < len(ptos_Linea):
        p_0, p_F = ptos_Linea[pos_Elem : pos_Elem + 2]
        ptoMedio = tuple((array(p_0) + array(p_F)) // 2)

        if ptoMedio in ptos_Linea:
            pos_Elem += 1
            
        else:
            ptos_Linea.insert(pos_Elem + 1, ptoMedio)
  
    for pto_Linea in ptos_Linea:
        pto_Linea_X, pto_Linea_Y = pto_Linea
        
        malla[pto_Linea_X][pto_Linea_Y].insert(0, 1)














'''for n_Fila in ns_Filas:
    for n_Columna in ns_Columnas:
        malla[n_Fila][n_Columna].insert(0, array((n_Fila, n_Columna)))'''

'''ps = array((0, 0)), array((0, 0))
p_0, p_F = ps                              
dibuja_Ptos_Medios_Calculados(ps)'''

'''for n_Fila in ns_Filas:
    for n_Columna in ns_Columnas:
        malla[n_Fila][n_Columna].insert(0, 1)
        print(array((n_Fila, n_Columna)))
    print()'''

