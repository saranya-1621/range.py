a=int(input())
k=0
if a<=1000:
 for i in range(2,a):
  if(a%i==0):
   k=k+1
 if(k<=0):
  print("yes")
else:
  print("no")
 
