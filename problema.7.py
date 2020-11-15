x=int(input("Introdu numărul x: "))
y=int(input("Introdu numărul y: "))
z=int(input("Introdu numărul z: "))
if ((x+y>z)and(x+z>y)and(y+z>x)):
    if ((x==y)and(x==z)and(y==z)):
        print("Formeaza un triunghi echilateral")
    elif ((x!=y)and(x!=z)and(y!=z)):
        print("Formeaza un triunghi scalen")
    else:
        print("Formeaza un triunghi isoscel")
else:
    print("Nu formeaza un triunghi")