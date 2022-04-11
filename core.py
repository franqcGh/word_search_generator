import asyncio

def game():
    from random import randint
    from secrets import choice

    # lista con letras del abecedario

    abc : list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']


    # crear matriz con espacios 'vacíos'

    row : int = 20
    column : int = 20
    matrix : list = [['-' for j in range(0,column)] for i in range(0,row)]

    # extraer lista de palabras de .txt y crear una lista con ellas

    f = open('word_list.txt','r',encoding='utf-8')
    word_list = [word.replace('\n','') for word in f.readlines()]
    f.close()

    # # tomar palabra de lista

    # word = choice(word_list)

    # # decidir coordenadas iniciales
    # i = randint(0,row - 1)
    # j = randint(0,column - 1)

    # print (i,j)

    # función para introducir nueva palabra
    def direction( theta:int , i:int , j:int , word:str):
        for letter in word.upper():
            
            if ( (row > i and i >= 0) and (column > j and j >= 0) ) and (matrix [i][j] == '-' or matrix[i][j] == letter):
                matrix[i][j] = letter
            else:
                raise(RuntimeError)
            
            if matrix [i][j] == '-' or matrix[i][j] == letter:
                matrix[i][j] = letter

            if theta == 1:
                i -= 1
                j += 1

            elif theta == 2:
                j += 1

            elif theta == 3:
                i += 1
                j += 1

            elif theta == 4:
                i += 1

            elif theta == 5:
                i += 1
                j -= 1

            elif theta == 6:
                j -= 1
        
            elif theta == 7:
                i -= 1
                j -= 1

            elif theta == 8:
                i -= 1

    # matar loop

    time = 1

    # Temporal
    for word in word_list:

        # Deciding initial position

        i = randint(0,row - 1)
        j = randint(0,column - 1)

        # Writing word
        theta = 1

        while theta < 9:
            time +=1
            if time > 300:
                raise ValueError

            try:
                direction( theta , i , j ,word)
                break
            except RuntimeError:
                theta += 1
            if theta == 9:
                theta = 1
                i = randint(0,row - 1)
                j = randint(0,column - 1)

    # rellenar espacios vacíos con letras aleatorias
    # for i in matrix:
    #     print(i)

    # print('\n')

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == '-':
                matrix[i][j] = choice(abc)

    for i in matrix:
        print(i)

while True:
    try:
        game()
        break
    except ValueError:
        pass