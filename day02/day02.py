with open('input.txt') as line:
    l = [x.strip('\n') for x in line]

    result1 = {'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z':9, 'C X':7, 'C Y':2, 'C Z':6}    
    points1 = 0
    for x in l:
        points = points + result1[x]
    
    print(points)

    result2 = {'A X':3, 'A Y':4, 'A Z':8, 'B X':1, 'B Y':5, 'B Z':9, 'C X':2, 'C Y':6, 'C Z':7} 
    points2 = 0 
    for x in l:
        points2 = points2 + result2[x]
    
    print(points2)