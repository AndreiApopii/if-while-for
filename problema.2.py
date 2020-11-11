n=int(input('dati nr: '))
s=0
for y in range(1,n+1):
    x=y
    while (y-1)>0:
        x*=y-1
        y-=1
    s+=x
print('suma=',s)