def ap(n,a,d):
  sum=(n/2)*(2*a+(n-1)*d)
  return sum

n=int(input("n:"))
a=int(input("a:"))
d=int(input("d:"))
print(ap(n,a,d))
