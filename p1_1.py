import cmath as z

a=float(input("enter a : "))
b=float(input("enter b : "))
c=float(input("enter c : "))


d=(b**2)-(4*a*c)

sol1=(-b-z.sqrt(d))/(2*a)
sol2=(-b+z.sqrt(d))/(2*a)

print("The solution are {0} and {1}".format(sol1,sol2))
