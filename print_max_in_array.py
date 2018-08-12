a=[]
n=int(input("enter a range"))
for i in range(1,n+1):
  x=int(input("enter element"))
  a.append(x)
max=a[0]
for i in range(1,len(a)):
    if(a[i]>max):
      max=a[i]

print(max)
