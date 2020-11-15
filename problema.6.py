n=int(input("introduceti numarul: "))
s=1
s2=1
x=0
for i in range(1,n+1):
    s=s*2+i
print("a)cind Mihai a implinit",n,"ani,aprimit",s,"dolari")
while s2<=100:
    x=x+1
    s2=s2*2+x
    print("b)cadoul lui Mihai a fost mai mare de 90$,cand a implinit",x,"ani")