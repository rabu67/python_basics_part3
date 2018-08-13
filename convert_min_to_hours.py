def hours(min):
  h=int(min*(1/60))
  return h
def minutes(min):
  m=(min*(1/60))-res1
  return int(m*60)


min=int(input("enter minutes"))
if(min<60):
  print("0",min)
else:
  res1=hours(min)
  res2=minutes(min)
  print(res1,res2)
