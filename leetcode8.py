a=[1,2,3,2,3]
b=[2,3,4,3]

for i in a:
    if i in b:
        print(i)
        value=i
        if i==value:
            continue
