n=int(input())
s,p=0,1
while(n!=0):
    rem=n%10
    s=s+rem
    p=p*rem
    n=n//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")