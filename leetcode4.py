
import array as arr
import numpy as np
"""
given array of size 2M+1.
M number should b repeated twice
any 1 number should not be repeated
example=[3,7,2,2,7,3,4]
output=4

"""

M=int(input("enter value of M"))

print("size of your array is {}".format(2*M+1))
print("enter elements of array")
a=[]
for i in range(2*M+1):
    element=int(input())
    a.append(element)

a=np.array(a)
"""
logic
xor:
same number xor=0
0 xor any number=any number
example=[3,7,2,2,7,3,4]



"""
answer=0
for i in range(len(a)):
    answer=answer ^ a[i]

print("the value which is not repeated is {}".format(answer))