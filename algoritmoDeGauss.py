#!/usr/bin/python
# -*- coding: utf-8 -*-
#Algoritmo: Gauss
#Complexidade: O(n^3) + O(n^2) = O(n^3)
"""
Seja A = (aij)m x n
 1 - seja P1 != 0 o pivo 1, L1.
	seja C1 o indice da coluna em que P1 esta
	OBJETIVO: Eliminar os termos abaixo de P1,
			  através de operações:
			  Li -> Li - aic1/p1 * L1, para todo i = 2, ... , m
 2 - continuar o processo até obter uma matriz escalonada
"""
import numpy as np
def findPivo(A):

	if A[0][0] == 0:
		print(A[0][0])
		swap(A,0,len(A)-1)
	for i in range(len(A) - 1):
		for j in range(i+1,len(A)):
			aic1 = A[j][i] #aic1
			if aic1 == 0:
				for k in range(i, len(A)):
					if A[k][i] != 0:
						swap(A,i,k)
						n1 = A[j][i]
			pivo = A[i][i] #p1 != 0 pivo da linha 1, L1
			if pivo == 0:
				continue
			div = aic1/pivo
			A[j] = sumVector(multVector(A[i], -div),A[j]) # li -> li - aic1/p1 * l1
	return A

def multVector(v,x):
	newV = []
	for i in range(len(v)): #para todo termo da linha
		newV += [v[i] * x]
	return newV

def sumVector(v1,v2):
	newV = []
	for i in range(len(v1)): #para todo termo da linha
		newV += [v1[i] + v2[i]]
	return newV

def swap(A, i, j):
	newI = []
	newJ = []
	for index in range(len(A) +1):
		newI += [A[j][index]] #trocando as linhas
		newJ += [A[i][index]] #Li <-> lj
	A[i] = newI
	A[j] = newJ

def printMatrix(A):
	print(np.matrix(A))

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

def main():
	A = readArq()
	printMatrix(A)
	print("\n")
	printMatrix(findPivo(A))

main()
