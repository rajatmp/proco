def gcd(a,b):
    while b!=0:
        return a,b=b,a%b
    return a

def find_d(e,phi):
    for k in range(1,1000):
        d=1+k*phi
        if d%e==0:
            return d//e
    return None

p=int(input("enter prime number p: "))
q=int(input("enter prime number q: "))

n=p*q
phi=(p-1)*(q-1)
