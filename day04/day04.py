with open('input.txt') as text:
    count1 = 0
    count2 = 0
    for line in text:
        pair = line.strip().split(',')
        a1, a2 = map(int,pair[0].split('-'))
        b1, b2 = map(int,pair[1].split('-'))

        if (a1 >= b1 and a2 <= b2) or (a1 <= b1 and a2 >= b2):
            count1 += 1
        
        if not (a1 > b2 or a2 < b1):
            count2 += 1 

    print(count1)
    print(count2)



            

        
    #lines = [line.strip('-') for line in text.split()]
    