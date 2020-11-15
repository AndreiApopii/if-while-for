n=int(input("introduceti numarul :"))
s1x=0
s1y=0
s2x=0
s2y=0
s2=0
s1=0
s2i=0
for i in range(1,n+1):
    s1x+=i**3
for i in range(1,n+1):
    s2+=i
s2x=s2**2
if s1x>s2x:
    print("x)S1>S2")
elif s1x<s2x:
    print("x)S1<S2")
else:
    print("x)S1=S2")
for i in range(1,n+1):
    s1+=i**2
s1y=s1*3
for i in range(1,n+1):
    s2i+=i
s2y=s2i+n**3+n**2
if s1y>s2y:
    print("y)S1>S2")
elif s1y<s2y:
    print("y)S1<S2")
else:
    print("y)S1=S2")