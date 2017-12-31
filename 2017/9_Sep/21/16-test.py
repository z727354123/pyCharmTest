def fuzhi(length=4):
    xxx = [[0]*length]*length
    matrix = [[0]*length]*length
    v = [1, 2, 3, 4, 5, 6, 5646]
    print(xxx)
    print(matrix)
    print('------------before')
    matrix[1][0:] = v
    v.append(123)
    print(matrix)


def pprint(l):
    for i in l:
        print(i)

sm = fuzhi(5)