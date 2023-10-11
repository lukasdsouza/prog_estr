#programação estruturada 11/10

#listas - definições

letra1 = "a"
letra2 = "b"
#-----------------------------------------
letras = ["a", "f", "x"]
print(letras)

lista = [1, 2, 3, 4, 5, True, "abc", (1,2,3)] #Não é uma boa prática

#acesso
print(letras)
print(letras[3])
print(letras[7]) #IndexError
print(letras[-1]) #pega poultimo elemento da lista
print(letras[-8]) #IndexError


#matrizes
matriz = [
    [10, 15]
    [-2, 5]
    [4, 3.5]
]
print(matriz[1][0]) # -2
print(matriz[2][1]) # -2

#slicing
print("-" * 40)
print(letras[1:4]) #inclui o elemento 1 até o elemento 4, exclusive
print(letras[:4]) #inclui do inicio da lista até o elemento 4, exclusive
print(letras[2:]) # inclui o elemento 2 até o final da lista
print(letras[:]) #exibe a lista inteira
print(letras [2::2]) #inclui do elemento 2 até o final de 2 em 2 elementos
print(letras[::-1]) #inverte a lista

#operações de pertencimento
print("a" in letras)  #true
print("a" not in letras) #false

if "e" in letras:
    print("'e' está em letras.")

#iterações
print("-" *40)
for letras in letras:
    print(letras)

for indice, letras in enumerate(letras):
    print(indice, "-", letras)

#é possivel, mas não faz sentido usar.
for _, letra in enumerate(letras):
    print(letras)

#operações aritméticas
print("-" * 40)
print(len(letras)) #length(comprimento)
letras.append("c") #insere o elemento no final da linha
print(letras)
print(letras.count("a")) #conta quantos elementos "a" existem na lista
if len(letras) > 0:
    print(letras.pop()) #remove o ultimo elemento da losta e retorna esse elemento
print(letras)
print(letras.pop(4))
prit(letras)
ig "g" in letras:
    letras.remove("g")
print(letras)

print("-" * 40)
letras_ord = sorted(letras)
print(letras_ord)
print(letras)

print("-" * 40)
print(letras)
letras.sort()
print(letras)

#compreensão de listas / list comprehension
print("-" * 40)
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

#Não Pythonico
quadrados = [numero ** 2 for numero in numeros]
print(quadrados)

quad_impares = [numero ** 2 for  numero in numeros if numero % 2 == 1]
print(quad_impares)

matriz + [
    [10,15],
    [-2, 5],
    [4, 3, 5]
] # -> [10, 15, -2, 5, 4, 3.5]
lista = [num for elem in matriz for num in elem]
print(lista)

# Dados Mutáveis vs Imutáveis / Passagem por referência
# list              int
# set               str
# class             float
# ....              bool
# xxxx              tuple


#tuplas
t = (1, 2, 3, 4)
print(t[2])
print(t[1:3])
for n in t:
    print(n)

    # t.append(5)-> AtributeError
    # t.pop()

def subsequentes(x):
    return x + 1, x + 2

print(subsequentes(5))
x1, x2 = subsequentes(10)
print(x1)
print(x2)

#Estruturas de dados
"""
- conjuntos
    - Únicos
    - Mutáveis
    - Não ordenados
    - Não indexados
- Dicionários
    - Únicos
    - Mutáveis
    - Não ordenados
    - indexados

"""
conj = {1, 3, 4, 1, 8, 10, 2, 3, 4, 5}
print(conj)
#print(conj[2]) -> TypeError
conj.add(15)
print(conj)
conj.add(10)
print(conj)

conj.remove(5)
print(conj)

print(3 in conj)
for n in conj:
    print(n)

print("-" * 40)
conj = {1, 3, 4, 1, 8, 10, 2, 3, 4, 5}
conj = list(set(conj))
print(conj)

