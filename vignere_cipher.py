'''Firstly, a key is generated with the help of a keyword if the length of
the message is not equal to the keyword.'''
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    '''The join() method takes all items in an iterable and joins them into one string.'''
    return ("".join(key))

'''encryption() to encrypt the message which takes two arguments one is the message that needs to be encrypted and
the second argument is the key that returns the encrypted text.'''
def encryption(string, key):
    encrypt_text = []
    for i in range(len(string)):
        '''In the encryption function the
        message and key are added modulo 26'''
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    return ("".join(encrypt_text))

'''decryption function to decrypt the encrypted message. That takes two
arguments one is the encrypted text and the second one is the key that used for encryption.'''
def decryption(encrypt_text, key):
    orig_text = []
    for i in range(len(encrypt_text)):
        '''In the decryption function encryption text
        and key are subtracted, then added 26 modulo 26.'''
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))


if __name__ == "__main__":
    string = input("Enter the message: ")
    keyword = input("Enter the keyword: ")
    key = generateKey(string, keyword)
    encrypt_text = encryption(string, key)
    print("Encrypted message:", encrypt_text)
    print("Decrypted message:", decryption(encrypt_text, key))

