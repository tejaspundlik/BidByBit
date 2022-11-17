str=input()
str=str.split(" ")
if(str[-1]==" "):
    str.pop()
length=int(str[0])
length-=2
x=int(str[1])
temp=1
for i in range(length-1):
    temp=temp*(x-1)
temp=temp*(x-2)
temp=temp+1
print(temp)