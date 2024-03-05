
def dupe(possible):
    temp = []
    for item in possible: 
        temp.append(item) 
        for i in range(1, 10, 1):
            if i == 1:
                if item.count(1) > 1: #removes lists with more than a single 1
                    temp.remove(item)
            else:
                if item.count(i) > 2:  #removes lists with more than 2 of a single number
                    temp.remove(item)
    return temp


def partition(value):
    possible = []
    if value <= 9: #1 digit 
        possible.append([value])
    if 3 <= value <= 18: #2 digit
        for x in range(1, 9, 1):
            if 0 < value - x <= 9:
                possible.append(sorted([x, value-x])) #sorts added list for easier filtering later
    if 5 <= value <= 26: #3 digit
        for x in range(1, 10, 1):
            sum1 = value - x
            if sum1 > 0:
                for y in range(1, 10, 1):
                    if 0 < sum1 - y <= 9:
                        possible.append(sorted([x, y, sum1-y])) #sorts added list for easier filtering later
    if 8 <= value <= 34: #4 digits
        for x in range(1, 10, 1):
            sum1 = value - x
            if sum1 > 0:
                for y in range(1, 10, 1):
                    sum2 = sum1 - y
                    if sum2 > 0:
                        for z in range(1, 10, 1):
                            if 0 < (sum2 - z) <= 9:
                                possible.append(sorted([x, y, z, sum2-z])) #sorts added list for easier filtering later
    temp = []
    for item in possible: #filters duplicates
        if item not in temp:
            temp.append(item)
    possible = temp
    return dupe(possible)

def filter(values, list_, should):
    if should:
        temp = []
        remove = False
        for item in list_:
            for x in values:
                if x in item:
                    remove = True 
            if remove:
                temp.append(item)
                remove = False
        return temp
    else:
        return list_
    
p = filter([5, 6, 7, 8, 9], partition(int(input("what number would you like to partition?"))), False)

for item in p:
    print(item)
