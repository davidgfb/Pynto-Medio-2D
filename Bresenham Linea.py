from tkinter import Tk, Entry
from numpy import array

malla, n_Filas, n_Columnas, ancho, root = [], 5, 5, 10, Tk()
ns_Filas, ns_Columnas = range(n_Filas), range(n_Columnas)

def ptos_Medios_Calculados(ps):
    p_0, p_F = ps
    
    if (p_0 == p_F).all():
        p_0_X, p_0_Y = p_0

        malla[p_0_X][p_0_Y].insert(0, 1)
        
        return p_0

    p_M = (p_F - p_0) // 2
    ptos_Linea = [p_0, p_F, p_M]
    print(p_M)

for n_Fila in ns_Filas:
    fila = []
    
    for n_Columna in ns_Columnas:
        celda = Entry(root, width = ancho)
        celda.grid(row = n_Fila, column = n_Columna)
        #celda.insert(0, (n_Fila, n_Columna))
        fila.append(celda)
        #fila.append(lambda f = n : (n_Fila, n_Columna))

    malla.append(fila)

malla = array(malla[::-1]).transpose()

#PROBADOR
'''for n_Fila in ns_Filas:
    for n_Columna in ns_Columnas:
        malla[n_Fila][n_Columna].insert(0, (n_Fila, n_Columna))'''

'''ps = array((0, 0)), array((5, 5))
p_0, p_F = ps
ptos_Medios_Calculados(ps)'''

'''ps = array((0, 0)), array((0, 0))
p_0, p_F = ps                              
print(ptos_Medios_Calculados(ps), 'debe ser', p_0)'''

'''for n_Fila in ns_Filas:
    for n_Columna in ns_Columnas:
        malla[n_Fila][n_Columna].insert(0, 1)
        print(malla[n_Fila][n_Columna]) 
    print()'''

