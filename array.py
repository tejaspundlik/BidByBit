def countArray(n, k, x):
    length=n
#length of array
    length-=2
 # k is number of total possible values
    temp=1
    for i in range(length-1):
        temp=temp*(k-1)
    temp=temp*(k-2)
    temp=temp+1
    return temp
print(countArray(4,30,2))