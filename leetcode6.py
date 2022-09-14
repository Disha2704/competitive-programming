# n=6
"""
you are gien an aray of size N containing each number between ! to "N-1" at least once.There is single integer value that is present in the array twice.your task is to find the duplicate integer value present in the array


"""
a=[8, 7, 2, 5, 4, 7, 1, 3, 6]
repeating_number=[]
for i in a:
    if i not in repeating_number:
        repeating_number.append(i)
    else:
        print(i)
        break