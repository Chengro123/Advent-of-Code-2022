with open('input.txt') as line:
    matchhistory = [x.strip('\n') for x in line]

    # Part 1
    result1 = {'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z':9, 'C X':7, 'C Y':2, 'C Z':6}    
    points1 = sum([result1[match] for match in matchhistory])
    print(points1)

    # Part 2 
    result2 = {'A X':3, 'A Y':4, 'A Z':8, 'B X':1, 'B Y':5, 'B Z':9, 'C X':2, 'C Y':6, 'C Z':7} 
    points2 = sum([result2[match] for match in matchhistory])
    print(points2)