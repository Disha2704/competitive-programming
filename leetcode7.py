"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

"""




a=[1]
repeating_number=[]
for i in a:
    if i not in repeating_number:
        repeating_number.append(i)
    else:
        print(i)
        