"""
3 pair of sum
"""
a=[1,2,3,4,5]
n=12
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
       for k in range(i+2,len(a)):
            if a[i]+a[j]+a[k]==n:
                print(a[i],a[j],a[k])
            