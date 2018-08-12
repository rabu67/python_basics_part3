x=int(input("enter the size of the array"))
arr=[]
for i in range(0,x):
  y=input("enter the array elements")
  arr.append(y)

for i in range(0,x):
  print(arr[i],arr.index(arr[i]))
  #print(arr.index(2))
