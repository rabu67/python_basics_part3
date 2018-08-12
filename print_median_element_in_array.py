def findmid(arr):
    middle=(len(arr)/2)
    
    if middle%2!=0:
        return arr[(int(middle-0.5))]
    else:
        return arr[int(middle-1)]

a=[]
n=int(input("enter a range"))
for i in range(0,n):
  x=int(input("enter element"))
  a.append(x)
middle=findmid(a)
if(n%2!=0):
    middle=middle-1
    print(middle)
else:
    print(middle)
