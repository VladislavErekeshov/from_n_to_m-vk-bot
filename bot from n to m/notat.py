d = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15,
    'G':16,
    'H':17,
    'I':18,
    'J':19,
    'K':20,
    'L':21,
    'M':22,
    'N':23,
    'O':24,
    'P':25,
    'Q':26,
    'R':27,
    'S':28,
    'T':29,
    'U':30,
    'V':31,
    'W':32,
    'X':33,
    'Y':34,
    'Z':35
}


def from_n_to_10(a, b):
    a = a.upper()
    a = [a[x:x+1] for x in range(0, len(a), 1)]
    l = []
    ind = []
    ans = 0
    for i in a:
        n = d.get(i)
        l.append(n)

    for el in range(0, len(l)):
        ind.append(el)
    ind.reverse()

    for i in l:
        s = ind[0]
        ans = ans + i * b ** s 
        ind.remove(s)
    return ans

def from_10_to_n(a, c):
    o = list(d.keys())
    l = []
    while a > 0:
        i = a % c
        a = a // c
        h = o[i]
        l.append(h)
    l.reverse()
    l = [str(i) for i in l]
    l = ''.join(l)
    return l

def if_a_bigger_b(a, b):
    a = a.upper()
    a = [a[x:x+1] for x in range(0, len(a), 1)]
    l = []
    for i in a:
        n = d.get(i)
        l.append(n)
    for i in l:
        if i > b - 1:
            a = 1
            break
        else:
            a = 0
    return a

def abcerror(a, arr1):
    lg = 0
    for i in arr1:
        for l in a:
            if i == l:
                lg = lg + 1
    if lg < len(a):
        return 1
    else:
        return 0

def bc(b):
    if b < 2:
        return 1
    else:
        return 0