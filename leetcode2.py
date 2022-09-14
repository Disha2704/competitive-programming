
number=int(input("enter any number??"))

# while number>0:
#     remainder=number%10
#     number=number//10
#     print(remainder,end="")


string_integer=str(number)



if string_integer[0]=="-":
    final_number=string_integer[1:]
    final_number=int(final_number)
    print("-",end="")
    
    while final_number>0:
        remainder1=final_number%10
        final_number=final_number//10
        print(remainder1,end="")
else:
    while number>0:
        remainder=number%10
        number=number//10
        print(remainder,end="")


