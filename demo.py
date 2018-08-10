print("starting")
n=str(input("enter a string :"))
a=""
s=len(n)
while s>0:
    a=a+n[s-1]
    s=s-1
print(a)
print("end")