from collections import OrderedDict


def Generate_Pairs():
    i = 0
    while i != len(plainText_lis):
        if (i == (len(plainText_lis) - (len(plainText_lis) % 2)) and len(plainText_lis) % 2 != 0):
            plainText_lis.append('x')
            break
        if (plainText_lis[i] == plainText_lis[i + 1]):
            plainText_lis.insert(i + 1, 'x')
        i += 2

    Key_Matrix()


def Key_Matrix():
    key_lis_tmp.extend(key_dup)

    var = 0

    while len(key_lis_tmp) != 25:
        value = chr(97 + var)
        if value not in key_lis_tmp:
            if value != 'j':
                key_lis_tmp.append(value)
        var += 1

    for i in range(0, len(key_lis_tmp), 5):
        matrix_pf.append(key_lis_tmp[i:i + 5])

    print("\nMatrix: ")
    for i in matrix_pf:
        print(i, end="\n")

    Playfair_Cypher_Algo()


def Fetch_Inde(valu_fn):
    for index_one_fe, i in enumerate(matrix_pf):
        for index_two_fe, j in enumerate(i):
            if j == valu_fn:
                return (index_one_fe, index_two_fe)


def Playfair_Cypher_Algo():
    for i in range(0, len(plainText_lis) - 1, 2):
        index_one_pf, index_two_pf = Fetch_Inde(plainText_lis[i])
        index_three_pf, index_four_pf = Fetch_Inde(plainText_lis[i + 1])

        if (index_one_pf == index_three_pf):
            index_two_pf = (index_two_pf + 1) % 5
            index_four_pf = (index_four_pf + 1) % 5
            cipherText.extend(matrix_pf[index_one_pf][index_two_pf])
            cipherText.extend(matrix_pf[index_three_pf][index_four_pf])

        elif (index_two_pf == index_four_pf):
            index_one_pf = (index_one_pf + 1) % 5
            index_three_pf = (index_three_pf + 1) % 5
            cipherText.extend(matrix_pf[index_one_pf][index_two_pf])
            cipherText.extend(matrix_pf[index_three_pf][index_four_pf])

        else:
            cipherText.extend(matrix_pf[index_one_pf][index_four_pf])
            cipherText.extend(matrix_pf[index_three_pf][index_two_pf])

    print("\nCipher Text: ", "".join(cipherText))


plainText = input("\nEnter Plain Text: ")
key = input("Enter Key: ")

plainText = plainText.replace(" ", "").lower()
plainText = plainText.replace("j", "i")
key = key.replace(" ", "").lower()
key = key.replace("j", "i")

key_dup = "".join(OrderedDict.fromkeys(key))

plainText_lis = list(plainText)
matrix_pf = []
key_lis_tmp = []
cipherText = []

Generate_Pairs()
Generate_Pairs()