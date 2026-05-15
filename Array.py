# import array as arr
from array import *

#Not fixed size , data of same datatype
#it is shrinkable or expandable 


vals = array('i' , [5,9,8,4,2])  #here i is short for integers

# print(vals)
# print(vals.buffer_info())   #(address of array, size)
# print(vals.typecode)
# vals.reverse()  #reverse the array
# print(vals)
# print(vals[0])
# print(vals[3])

# for i in range(len(vals)):
#     print(vals[i])


# for e in vals:
#     print(e)

# newArr = array(vals.typecode , (a*a for a in vals))

# for e in newArr:
#     print(e)

char = array('w' , ['a' , 'e' , 'i' , 'o' ])


#taking user input 

arr = array('i' , [])
n = int(input("Enter the length of the array : "))

for i in range(n):                
    x = int(input("Enter the next value : "))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search : "))


k=0 
for e in arr:
    if e == val:
        print(k)
        break
    k+=1
print(arr.index(val))