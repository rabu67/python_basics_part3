b=[]
n=int(input("enter a range"))
for i in range(1,n+1):
  x=int(input("enter element"))
  b.append(x)
b.sort()
for i in range(0,n):
  print(b[i],end=' ')
