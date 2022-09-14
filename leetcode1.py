"""
234
product=2*3*4 =24
sum=2+3+4=9
answer=product-sum
"""



number=int(input("enter a number?"))
m=1
s=0
while number!=0:
    d=number%10
    m=m*d
    s=s+d
    number=number//10

print("diffrence between product of a digit and sum of digit is {}".format(m-s))
