length=int(input())
length-=2
x=int(input())
y=input()
temp=1
for i in range(length-1):
    temp=temp*(x-1)
temp=temp*(x-2)
temp=temp+1
print(temp)