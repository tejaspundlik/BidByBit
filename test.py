target=int(input())
lenofnum=int(input())
questionarr=input()
questionarr=questionarr.split(" ")
for i in range(lenofnum):
    questionarr[i]=int(questionarr[i])
if(lenofnum!=len(questionarr)):
    questionarr.pop()
arr=[]

def decToBinary(number,LEN):
    arr=[]
    for i in range(0,LEN):
        arr.append(number%2)
        number=number//2

    arr.reverse()
    return arr

answer=0
for k in range(0,pow(2,len(questionarr))-1):
 Sum=0
 arr=decToBinary(k,lenofnum)
 for i in range(0,len(questionarr)):
    if(arr[i]==0):
        Sum=Sum+questionarr[i]
    else:
        Sum=Sum-questionarr[i]
 if(Sum==target):
    answer+=1
print(answer)