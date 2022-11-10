'''Creating a key with values to substitute'''

key=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','','x','c','v','b','n','m']

'''to enter the text that has to be encrypted'''

plaintext=input("Enter Plaintext: ")

'''creating two lists where the text will be appended. One for ciphering and the other for deciphering'''

c=[]
p=[]

for i in range(0,len(plaintext)):

    '''The ord() function returns an integer representing the Unicode character.'''

    c.append(key[ord(plaintext[i])-97])

    '''this will show the unicode'''

    #print(ord(plaintext[i])); to check the ord values, uncomment this

print("Ciphertext (i.e.Encrypted text): ")

'''the list appeneded at c will be printed'''

print(c)

for i in range(0,len(c)):

    for j in range(0,len(key)):

        '''if c and the key will have the same unicode, then it will append the
        value into p after adding it with 97 which will result in our og text'''

        if(c[i]==key[j]):

            '''chr() a unicode character of the corresponding integer argument'''

            p.append(chr(j+97))

print("Plaintext (i.e.Decrypted text): ")

'''the list appeneded at p will be printed'''

print(p)
