from numpy import array

ptos_Linea, pos_Elem = [(0,) * 3, (4,) * 3], 0

while pos_Elem + 1 < len(ptos_Linea):
    p_0, p_F = ptos_Linea[pos_Elem : pos_Elem + 2]
    ptoMedio = tuple((array(p_0) + array(p_F)) // 2)
 
    if ptoMedio in ptos_Linea:
        pos_Elem += 1
            
    else:
        ptos_Linea.insert(pos_Elem + 1, ptoMedio) #list.insert()

print(ptos_Linea)

























'''d3[0][0][0] = 1

print(d3)'''




























'''#x, y, z = [0] * 3

for i in r:
    d3.append((x, y, z))
    x += 1
    
    for i in r:
        d3.append((x, y, z))
        y += 1
        
        for i in r:
            d3.append((x, y, z))
            z += 1

print(d3)'''
            

'''for x in r:
        d3
    for y in r:
        for z in r:
            d3.append((x, y, z))

print(d3)'''
            
