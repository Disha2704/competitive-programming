
number=int(input("enter a number"))
lst=[] #empty list
while number>0:
    remainder=number%2
    number=number//2
    # print(remainder)
    lst.append(remainder)

binary= ''.join(str(lst).split(','))
compliment=lst[::-1] #reverse list

print("binary of {}".format(binary))
print("compliment of is ",end="")
for i in compliment:
    if i==0:
        print("1",end="")
    else:
        print("0",end="")