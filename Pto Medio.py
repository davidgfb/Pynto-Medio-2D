from tkinter import Tk, Entry
from numpy import array, isin

n_Filas, ancho, root = 5, 10, Tk()
n_Columnas = n_Filas #rectangular?
malla = n_Columnas * [0]
ns_Filas, ns_Columnas = range(n_Filas), range(n_Columnas)   

#PROBADOR
for n_Fila in ns_Filas:
    fila = n_Filas * [0]
    
    for n_Columna in ns_Columnas:
        celda = Entry(root, width = ancho)
        celda.grid(row = n_Fila, column = n_Columna)
        fila[n_Columna] = celda

    malla[n_Fila] = fila

malla = array(malla[::-1]).transpose()

p_0, p_F = array((0, 0)), array((4, 4))
   
if (p_0 == p_F).all():
    p_0_X, p_0_Y = p_0

    malla[p_0_X][p_0_Y].insert(0, 1)
    
else:
    ptos_Linea, i = [p_0, p_F], 0
    lon_Ptos_Linea = len(ptos_Linea)

    while i < lon_Ptos_Linea:
        p_0, p_F = ptos_Linea[-2::]
        ptoMedio = (p_0 + p_F) // 2

        if not isin(ptoMedio, ptos_Linea).all():
            ptos_Linea.append(ptoMedio)

        lon_Ptos_Linea = len(ptos_Linea)
        i += 1
    
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

