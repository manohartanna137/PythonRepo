def disjoint(s,x,y):
    happiness = 0
    for i in s:
        if i in x:
            happiness += 1
        if i in y:
            happiness -= 1

    print("Happiness:", happiness)
    return happiness