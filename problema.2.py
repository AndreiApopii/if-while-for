n=int(input('dati nr: '))
s=0
for m in range(1,n+1):
    x=m
    while (m-1)>0:
        x*=m-1
        m-=1
    s+=x
print('suma=',s)
