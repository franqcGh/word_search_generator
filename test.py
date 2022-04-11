# Importing neccesary libraries and modules

from random import randint
from secrets import choice
from core import direction

# Creating list of alphabet letters, to randomly fill in the empty spaces

abc : list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Creating matrix filled in with zeros, the number of columns and rows have to be entered

row : int = int( input( 'Enter the number of rows:\n>>> ' ) )
column : int = int( input( 'Enter the number of columns\n>>> ' ) )

matrix : list = [[0 for j in range(0,column)] for i in range(0,row)]

# Getting list of words from a .txt file

f = open('word_list.txt','r',encoding='utf-8')
word_list = [word.replace('\n','') for word in f.readlines()]
f.close()

###

for word in word_list:

    # Deciding initial position

    i = randint(0,row - 1)
    j = randint(0,column - 1)

    # Writing word
    theta = 1

    while theta < 9:
        
        try:
            direction( 1 , i , j ,word , row , column , matrix)
            break
        except RuntimeError:
            theta += 1

for i in matrix:
    print(i)