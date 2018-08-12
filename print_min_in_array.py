a=[]
n=int(input("enter a range"))
for i in range(1,n+1):
  x=int(input("enter element"))
  a.append(x)
min=a[0]
for i in range(1,len(a)):
    if(a[i]<min):
      min=a[i]

print(min)
