# import math
#
#
# def gcd(a, h):
#     temp = 0
#     while (1):
#         temp = a % h
#         if (temp == 0):
#             return h
#         a = h
#         h = temp
#
#
# p = 3
# print("The value of p: ", p)
# q = 7
# print("The value of q: ", q)
# n = p * q
# print("The value of n: ", n)
# e = 2
# print("The value of e: ", e)
# # print("public key: [" + e + "," + n +"]")
# phi = (p - 1) * (q - 1)
# print("The value of phi(n): ", phi)
#
# while (e < phi):
#     if (gcd(e, phi) == 1):
#         break
#     else:
#         e = e + 1
# k = 2
# d = (1 + (k * phi)) / e
# msg = 12.0
#
# print("\n")
# print("Message data = ", msg)
#
# # Encryption c = (msg ^ e) % n
# c = pow(msg, e)
# c = math.fmod(c, n)
# print("Encrypted data = ", c)
#
# # Decryption m = (c ^ d) % n
# m = pow(c, d)
# m = math.fmod(m, n)
# print("Decrypted data = ", m)


























import math

def gcd(a,h):
    temp = 0
    while 1:
        temp = a % h
        if(temp == 0):
            return h
        a = h
        h = temp

p = 3
print("The value of p: ", p)
q = 7
print("The value of q: ", q)
n = p*q
print("The value of n: ", n)
e = 2
print("The value of e: ", e)
phi = (p-1) * (q-1)
print("The value of phi: ", phi)
while(e < phi):
    if(gcd(e, phi) == 1):
        break
    else:
        e = e + 1

k = 2
print("The value of k: ", k)
d = (1 + (k * phi)) / e
print("The value of d: ", d)
msg = 12.00
print("The value of message: ", msg)

#encryption
c = pow(msg, e)
c = math.fmod(c, n)

print("The encrypted message is: ", c)

#decryption
m = pow(c, d)
m = math.fmod(m, n)

print("The decryption is: ", m)

