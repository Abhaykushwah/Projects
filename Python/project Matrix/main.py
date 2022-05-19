#importing modules
from lib2to3.pgen2.grammar import opmap
from numpy import *
import random
import numpy

# taking input from user
user_in = input("Enter your msg : ")
user_in_lst = user_in.split()

#printing original list
print("The original msg : " + str(user_in_lst))

# converting string list to ASCII values
# using loop & ord()
op_matrix = []
for i in user_in_lst:
    op_matrix.extend(ord(num) for num in i)

# printing result
print("The ASCII value of msg : " + str(op_matrix))
a = array(op_matrix)
a = a.reshape(2,len(user_in)//2)

# if (len(user_in)%2 == 0):
#     a = a.reshape(2,len(user_in)//2)
# elif(len(user_in)%2 != 0):
#     #a= a.append(0)
#     print("odd")
print(a)

### Transpose of a Matrix

'''
zero_mat = zeros(len(user_in))
transpose_mat = zero_mat.reshape(2,len(user_in)//2)

# iterate through rows
for i in range(len(a)):
    # iterate through coloms
    for j in range(len(a[0])):
        transpose_mat[j][i] = a[i][j]
for t in transpose_mat:
    print(t)

//2nd way
print()
result = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
for t in result:
    print(t)

'''

print()
# key gentration
key = numpy.random.randint(1,5, size=(len(user_in)//2,2))
print(key)
strkey = str(key)
with open('filekey.txt','w') as filekey:
    filekey.write(strkey)


result = [[0,0,],[0,0,]]
# zero_mat = zeros(len(user_in)*len(user_in))
# result = zero_mat.reshape(len(user_in)//2,len(user_in)//2)

print(result)

for i in range(len(a)):
 
    # iterating by column by B
    for j in range(len(key[0])):
 
        # iterating by rows of B
        for k in range(len(key)):
            result[i][j] += a[i][k] * key[k][j]
 
for r in result:
    print(r)

# reading key
with open('filekey.txt','r') as key_mat:
    key_mat = key_mat.read()


# print(key_mat)
key_mat1 = numpy.array(key_mat)
print(key_mat1)
splits = numpy.array_split(key_mat1,2)

# invers_mat = splits.reshape(2,2)
print(splits)
# print(numpy.linalg.inv(key_mat2))
