#contraints---------------------------------
grid = 8 # 0 -> 8  so 9 boxes wide and tall
coords = [[18, [1, 8]],[5, [1, 4]],[9, [1, 2]],[9, [2, 6]],[22, [2, 0]],[11, [3, 4]],[12, [4, 7]],[14, [4, 1]],[22, [5, 4]],[7, [6, 8]],[19, [6, 2]],[31, [7, 6]],[22, [7, 4]],[15, [7, 0]]]
absolutes = [[18, [1, 8]], [9, [2, 6]], [22, [2, 0]], [12, [4, 7]], [14, [4, 1]], [7, [6, 8]],[19, [6, 2]],[15, [7, 0]]] #not affected by any other coords
variables = [[5,[1,4]],  [9, [1,2]],  [11,[3,4]],  [22, [5,4]],  [31,[7,6]],  [22,[7,4]]] #affects and is affected by other coords
#to keep track of how many of each number has been used
nines = 9
eights = 8
sevens = 7
sixes = 6
fives = 5
fours = 4
threes = 3
twos = 2
ones = 1
#-------------------------------------------
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


def partition(value, bordering):
    possible = []
    if value <= 9: #1 digit 
        possible.append([value])
    if 3 <= value <= 18: #2 digit
        for x in range(1, 10, 1):
            if 0 < value - x <= 9: 
                possible.append(sorted([x, value-x])) #sorts added list for easier filtering later
    if 5 <= value <= 26: #3 digit
        for x in range(1, 10, 1):
            sum1 = value - x
            if sum1 > 0:
                for y in range(1, 10, 1):
                    if 0 < sum1 - y <= 9:
                        possible.append(sorted([x, y, sum1-y])) #sorts added list for easier filtering later
    if not bordering:
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

def edge(extended):
    temp = []
    for i in range(len(extended)):
        if extended[i][1][1] == 0 or extended[i][1][1] == 8:
            sublist = []
            for x in extended[i][0]:
                if len(x) < 4:
                    sublist.append(extended[i][0])
            temp.append([sublist, extended[i][1]]) #remove sub lists longer than 3
        else:
            temp.append(extended[i])
    for i in temp:
        print(i)
        print("-----")



    
p = filter([5, 6, 7, 8, 9], partition(22, False), False)

for item in p:
    print(item)

'''
    print(partition(absolutes[i][0]))
    print("----------------------")
print(new)
for item in new:
    print(item[0])
    print("------------")
all = []
for a in range(len(new[0][0])):
    for b in range(len(new[1][0])):
        for c in range(len(new[2][0])):
            for d in range(len(new[3][0])):
                for e in range(len(new[4][0])):
                    for f in range(len(new[5][0])):
                        for g in range(len(new[6][0])):
                            for h in range(len(new[7][0])):
                                #all.append([new[0][0], new[0][0], new[0][0], new[0][0], new[0][0], new[0][0], new[0][0], new[0][0]])
                                pass
'''
