import numpy as np
def readArq():
    arquivo = open('matriz.txt','r')
    matriz = []
    while True:
        line = arquivo.readline()
        if len(line) == 0: #fim do arquivo
            break
        aux = line.split(" ")
        vector = []
        for i in aux:
            vector.append(int(i))
        matriz.append(vector)
    arquivo.close()
    return matriz

A = readArq()
print(np.matrix(A))
