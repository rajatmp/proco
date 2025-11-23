def power(base,exp,mod):
    return(base**exp)%mod
p=int(input("enter prime number p:"))
q=int(input("enter primitive root q:"))
if q>=p:
    print("q must be less than p")
    exit()
x=int(input("enter the private key for userA:"))
if x>=p:
    print("x must be less than p")
    exit()
A=power(q,x,p)

y=int(input("enter the private key for userB:"))
if y>=p:
    print("y must be less than p")
    exit()
B=power(q,y,p)

print("--------so now we have------------")
print("user A ---PRIVATE KEY x:",x,"PUBLIC KEY A:",A)
print("user B ---PRIVATE KEY y:",y,"PUBLIC KEY B:",B)

k1=power(B,x,p)
k2=power(A,y,p)
print(k1)
print(k2)

if k1==k2:
    print("secret key generation successfull")
else:
    print("secret key generation failed")
