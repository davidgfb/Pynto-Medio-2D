from tkinter import Tk, Entry
from numpy import array, isin

malla, n_Filas, n_Columnas, ancho, root = [], 5, 5, 10, Tk()
ns_Filas, ns_Columnas = range(n_Filas), range(n_Columnas)   

#PROBADOR
for n_Fila in ns_Filas:
    fila = []
    
    for n_Columna in ns_Columnas:
        celda = Entry(root, width = ancho)
        celda.grid(row = n_Fila, column = n_Columna)
        fila.append(celda)

    malla.append(fila)

malla = array(malla[::-1]).transpose()

ps = array((0, 0)), array((4, 4))
p_0, p_F = ps
   
if (p_0 == p_F).all():
    p_0_X, p_0_Y = p_0

    malla[p_0_X][p_0_Y].insert(0, 1)
    
else:
    ptos_Linea = [p_0, p_F]
    i = 0
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

