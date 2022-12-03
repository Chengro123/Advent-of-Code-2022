def same(s,n=None,m=None):
    if n == None and m == None:
        a = set(s[0:len(s)//2])
        b = set(s[len(s)//2:])
        c = a.intersection(b)
    else:
        a = set(s)
        b = set(n)
        c = set(m).intersection(b).intersection(a)
    return next(iter(c))


with open('input.txt') as line:
    l = [x.strip('\n') for x in line]
    sum1 = 0
    for x in l:
        common = same(x)
        if common.islower():
            sum1 += ord(common) - 96
        elif common.isupper():
            sum1 += ord(common) - 38
    print(sum1)

    sum2 = 0
    for i in range(len(l)//3): 
        y = l[i*3:i*3+3]
        common = same(*y)
        if common.islower():
            sum2 += ord(common) - 96
        elif common.isupper():
            sum2 += ord(common) - 38
    print(sum2)






