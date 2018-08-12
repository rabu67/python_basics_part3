a=[]
n=int(input("enter a range"))
for i in range(1,n+1):
  x=int(input("enter element"))
  a.append(x)
a.sort()
for i in range(0,n):
  print(a[i],end=' ')
