n=int(input("how many numbers="))
n1,n2=0,1
count=0
if n<=0:
    print("please enter a positive number:")
elif n==1:
    print("fibonacci sequence upto",n,":")
    print(n1)
else:
    print("fibonacci sequence:")
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
