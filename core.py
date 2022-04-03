from random import randint
from secrets import choice

# lista con letras del abecedario

abc : list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']


# crear matriz con espacios 'vacíos'

row : int = 20
column : int = 20
matrix : list = [[0 for j in range(0,column)] for i in range(0,row)]

# extraer lista de palabras de .txt y crear una lista con ellas

f = open('word_list.txt','r',encoding='utf-8')
word_list = [word.replace('\n','') for word in f.readlines()]

# tomar palabra de lista

word = choice(word_list)

# decidir coordenadas iniciales
i = randint(0,row - 1)
j = randint(0,column - 1)

print (i,j)

# función para introducir nueva palabra
def direction( theta:str , i:int , j:int , word:str = 'test'):
    for letter in word.upper():
        
        if ( (row > i and i >= 0) and (column > j and j >= 0) ) and (matrix [i][j] == 0 or matrix[i][j] == letter):
            matrix[i][j] = letter
        else:
            raise(RuntimeError)
        
        if matrix [i][j] == 0 or matrix[i][j] == letter:
            matrix[i][j] = letter

        if theta == 'NE':
            i -= 1
            j += 1

        elif theta == 'E':
            j += 1

        elif theta == 'SE':
            i += 1
            j += 1

        elif theta == 'S':
            i += 1

        elif theta == 'SO':
            i += 1
            j -= 1

        elif theta == 'O':
            j -= 1
    
        elif theta == 'NO':
            i -= 1
            j -= 1

        elif theta == 'N':
            i -= 1

# verificar espación disponibles


# Temporal
direction('N',i,j,word)

# rellenar espacios vacíos con letras aleatorias

for i in range(20):
    for j in range(20):
        if matrix[i][j] == 0:
            matrix[i][j] = choice(abc)

for i in matrix:
    print(i)