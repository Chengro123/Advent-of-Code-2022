with open('input.txt') as line:
    l = [x[:-1] for x in line]
    s = [0]*100000 
    i = 0  

    for num in l:
        if num == '':
            i += 1 
        else: 
            s[i] += int(num)
    
    print(max(s))
    s.sort()
    print(sum(s[-3:]))
