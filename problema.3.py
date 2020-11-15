import math
m=int(input("introduceti m : "))
n=int(input("introduceti n :"))
if((m>n)or(m==n)):
    print("nu corespunde conditiei")
else:
    l=round(math.log(n,m))
    if(m**l==n):
        print(n,"este o putere a lui",m)
    else:
        print(n,"nu e o putere a lui",m)