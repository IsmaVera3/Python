import numpy as np

a = np.array([[2, 2, 2],[2, 2, 2],[2, 2, 2]])

b = np.array([[2, 2, 2],[2, 2, 2],[2, 2, 2]])


resultado = np.dot(a, b)
print(resultado)


m1= [[4,4,4],[4,4,4],[4,4,4]]
m2 = [[4,4,4],[4,4,4],[4,4,4]]
res = [[0,0,0],[0,0,0],[0,0,0]]

def multiplicacion(m1,m2,res):
    for i in range(len(m1)):
        for e in range(len(m2)):
            res[i][e] = m1[i][e] * m2[e][e]
            
    return res

print(multiplicacion(m1,m2,res))