from numba import jit


numbers = {}
numbers[0] = [[18],[1, 8],[True], [True], [], [[0, 8],[1, 7],[2, 8]]] #value, coord, absolute?,bordering?, list, affected squares, possible partitions
numbers[1] = [[5],[1, 4],[False], [False], [], [[0, 4],[1, 3],[1, 5],[2, 4]]]
numbers[2] = [[9],[1, 2],[False], [False], [], [[0, 2],[1, 1],[1, 3],[2, 2]]]
numbers[3] = [[9],[2, 6],[True], [False], [], [[1, 6],[2, 5],[2, 7],[3, 6]]]
numbers[4] = [[22],[2, 0],[True], [True], [], [[1, 0],[2, 1],[3, 0]]]
numbers[5] = [[11],[3, 4],[False], [False], [], [[2, 4],[3, 5],[3, 3],[4, 4]]]
numbers[6] = [[12],[4, 7],[True], [False], [], [[3, 7],[4, 8],[4, 6],[5, 7]]]
numbers[7] = [[14],[4, 1],[True], [False], [], [[3, 1],[4, 2],[4, 0],[5, 1]]]
numbers[8] = [[22],[5, 4],[False], [False], [], [[4, 4],[5, 5],[5, 3],[6, 4]]]
numbers[9] = [[7],[6, 8],[True], [True], [], [[5, 8],[6, 7],[7, 8]]]
numbers[10] = [[19],[6, 2],[True], [False], [], [[5, 2],[6, 3],[6, 1],[7, 2]]]
numbers[11] = [[31],[7, 6],[False], [False], [], [[6, 6],[7, 7],[7, 5],[8, 6]]]
numbers[12] = [[22],[7, 4],[False], [False], [], [[6, 4],[7, 3],[7, 5],[8, 4]]]
numbers[13] = [[15],[7, 0],[True], [True], [], [[6, 0],[7, 1],[8, 0]]]

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

def partition(value, bordering, freebies):
    value = value[0]
    bordering = bordering[0]
    possible = []
    if value <= 9: #1 digit 
        if freebies and bordering:
            possible.append([value, "2"])
        elif freebies:
            possible.append([value, "3"])
        else:
            possible.append([value, "0"])
    if 3 <= value <= 18: #2 digit
        for x in range(1, 10, 1):
            if 0 < value - x <= 9:
                if freebies and bordering:
                    possible.append(sorted([x, value-x]) + ["1"]) #sorts added list for easier filtering later
                elif freebies:
                    possible.append(sorted([x, value-x]) + ["2"])
                else:
                    possible.append(sorted([x, value-x]) + ["0"])
    if 5 <= value <= 26: #3 digit
        for x in range(1, 10, 1):
            sum1 = value - x
            if sum1 > 0:
                for y in range(1, 10, 1):
                    if 0 < sum1 - y <= 9:
                        if freebies and bordering:
                            possible.append(sorted([x, y, sum1-y]) + ["0"]) #sorts added list for easier filtering later
                        elif freebies:
                            possible.append(sorted([x, y, sum1-y]) + ["1"])
                        else:
                            possible.append(sorted([x, y, sum1-y]) + ["0"])
    if bordering == False:
        if 8 <= value <= 34: #4 digits
            for x in range(1, 10, 1):
                sum1 = value - x
                if sum1 > 0:
                    for y in range(1, 10, 1):
                        sum2 = sum1 - y
                        if sum2 > 0:
                            for z in range(1, 10, 1):
                                if 0 < (sum2 - z) <= 9:
                                    possible.append(sorted([x, y, z, sum2-z]) + ["0"]) #sorts added list for easier filtering later
    temp = []
    for item in possible: #filters duplicates
        if item not in temp:
            temp.append(item)
    possible = temp
    return dupe(possible)

for i in range(14):
    numbers[i][4] = (partition(numbers[i][0], numbers[i][3], True))



#plan
#i have decide to place hooks from the outskirts so that there are only four possibilities of rotation
#place hooks from the outside in having the rotation based on the base four counter 0 = no rotation, 1 = one rotation, 2 = two rotations, 3 = three rotations
#somehow check the proposed solution
#if the proposed solution passes the verification then break
#else increment counter and restart



#base 4 counting system to keep track of each hooks rotation
def base_10_to_4(denary):
    base_four = ""
    while denary != 0:
        base_four += str(denary%4) #concanates remainder of division
        denary //= 4 #creates subsequent value
    while len(base_four) < 8:
        base_four = "0" + base_four #adds zeros until there are 8 bits
    return base_four

current_grid = [[0, 8], [0, 8]]  #[[x-axis][y-axis]]

def constrict(rotation):  #deletes row and columb (removes an l-shape) based on rotation
    if rotation == 0:
        current_grid[0][0] += 1
        current_grid[1][0] += 1
    if rotation == 1:
        current_grid[0][0] += 1
        current_grid[1][1] -= 1
    if rotation == 2:
        current_grid[0][1] -= 1
        current_grid[1][1] -= 1
    if rotation == 3:
        current_grid[0][1] -= 1
        current_grid[1][0] += 1

def get_base(rotation): #finds the coordinate of the corner of the "hook"
    if rotation == "0":
        base = [current_grid[0][0],current_grid[1][0]]
    if rotation == "1":
        base = [current_grid[0][0],current_grid[1][1]]
    if rotation == "2":
        base = [current_grid[0][1],current_grid[1][1]]
    if rotation == "3":
        base = [current_grid[0][1],current_grid[1][0]]
    return base

def get_every_square(base, rotation, length): #finds the coordinate of every square in the hook
    every_square = []
    if rotation == 0:
        for x in range(length):
            if x == 0:
                pass
            else:
                every_square.append([base[0]+x, base[1]])
        for y in range(length):
            every_square.append([base[0], base[1]+y])
    elif rotation == 1:
        for x in range(length):
            if x == 0:
                pass
            else:
                every_square.append([base[0]+x, base[1]])
        for y in range(length):
            every_square.append([base[0], base[1]-y])
    elif rotation == 2:
        for x in range(length):
            if x == 0:
                pass
            else:
                every_square.append([base[0]-x, base[1]])
        for y in range(length):
            every_square.append([base[0], base[1]-y])
    else:
        for x in range(length):
            if x == 0:
                pass
            else:
                every_square.append([base[0]-x, base[1]])
        for y in range(length):
            every_square.append([base[0], base[1]+y])
    return every_square

def check(every_square, value, hook_num): #
    for a in range(14):
        #print(end_partitions[a])
        temp = []
        done = False
        conjugate = []
        for affected_square in numbers[a][5]:
            if affected_square in every_square and done == False:
                done = True
                #print(numbers[a][0])
                for b in range(len(numbers[a][4])):
                    #print(numbers[a][4][b], b)
                    partition = numbers[a][4][b]
                    #print(partition)
                    #if partition == [7, 8, '0']:
                        #print("poo")
                    if value in partition:
                        temp.append(partition)
                    elif partition[-1] in ["1", "2", "3"]:
                        numbers[a][4][b][-1] = str(int(numbers[a][4][b][-1]) - 1)
                        temp.append(partition)
                            

        #find conjugate of temp                     
        for i in range(len(temp)):
            temp[i].pop()
            temp[i].append("0")
            #pass
        if temp != []:
            #print(temp)
            conjugate = end_partitions[a]      
            for item in temp:
                try:
                    conjugate.remove(item)
                except:
                    pass
        holder = end_partitions[a]
        for item in conjugate:
            try:
                holder.remove(item)
            except:
                pass
        end_partitions[a] = holder

        
            #print(numbers[a][0],a, conjugate)            
        #remove from end_partitions
                                    
def to_be_or_not_to_be():
    for i in range(13):
        if end_partitions[i] == []:
            return False
    return True

def reset():
    for i in range(14):
        numbers[i][4] = (partition(numbers[i][0], numbers[i][3], True))
        end_partitions[i] = partition(numbers[i][0], numbers[i][3], False)





end_partitions = {}
end_partitions[0] = []
end_partitions[1] = []
end_partitions[2] = []
end_partitions[3] = []
end_partitions[4] = []
end_partitions[5] = []
end_partitions[6] = []
end_partitions[7] = []
end_partitions[8] = []
end_partitions[9] = []
end_partitions[10] = []
end_partitions[11] = []
end_partitions[12] = []
end_partitions[13] = []

for i in range(14):
    end_partitions[i] = partition(numbers[i][0], numbers[i][3], False)



class nine():
    def __init__(self) -> None:
        pass
    def poo(self):
        self.length = 9 #how wide and tall the hook is
        self.rotation = rotation_values[0]
        self.value = hook_values[0] #from 3 ---> 9
        self.base = get_base(self.rotation) #the coords of the corner of the hook
        constrict(self.rotation)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        check(self.every_square, self.value, self.length)
        eight()

class eight():
    def __init__(self) -> None:
        self.length = 8 #how wide and tall the hook is
        self.rotation = rotation_values[1]
        self.value = hook_values[1] #the number assigned to this hook
        self.base = get_base(self.rotation) #the coords of the corner of the hook
        constrict(self.rotation)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        check(self.every_square, self.value, self.length)
        seven()

class seven():
    def __init__(self) -> None:
        self.length = 7 #how wide and tall the hook is
        self.rotation = rotation_values[2]
        self.value = hook_values[2] #the number assigned to this hook
        self.base = get_base(self.rotation) #the coords of the corner of the hook
        constrict(self.rotation)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        check(self.every_square, self.value, self.length)
        six()

class six():
    def __init__(self) -> None:
        self.length = 6 #how wide and tall the hook is
        self.rotation = rotation_values[3]
        self.value = hook_values[3] #the number assigned to this hook
        self.base = get_base(self.rotation) #the coords of the corner of the hook
        constrict(self.rotation)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        check(self.every_square, self.value, self.length)
        five()

class five():
    def __init__(self) -> None:
        self.length = 5 #how wide and tall the hook is
        self.rotation = rotation_values[4]
        self.value = hook_values[4] #the number assigned to this hook
        self.base = get_base(self.rotation) #the coords of the corner of the hook
        constrict(self.rotation)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        check(self.every_square, self.value, self.length)
        four()

class four():
    def __init__(self) -> None:
        self.length = 4 #how wide and tall the hook is
        self.rotation = rotation_values[5]
        self.value = hook_values[5] #the number assigned to this hook
        self.base = get_base(self.rotation) #the coords of the corner of the hook
        constrict(self.rotation)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        check(self.every_square, self.value, self.length)
        three()

class three():
    def __init__(self) -> None:
        self.length = 3 #how wide and tall the hook is
        self.rotation = rotation_values[6]
        self.value = hook_values[6] #the number assigned to this hook
        self.base = get_base(self.rotation) #the coords of the corner of the hook
        constrict(self.rotation)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        check(self.every_square, self.value, self.length)
        two()

class two():
    def __init__(self) -> None:
        self.length = 2 #how wide and tall the hook is
        self.rotation = rotation_values[7]
        self.value = 2 #the number assigned to this hook
        self.base = get_base(self.rotation) #the coords of the corner of the hook
        constrict(self.rotation)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        check(self.every_square, self.value, self.length)
        one()

class one():
    def __init__(self) -> None:
        self.rotation = "0"
        self.length = 1 #how wide and tall the hook is
        self.value = 1
        self.base = get_base(self.rotation)
        self.every_square = self.base
        check(self.every_square, self.value, self.length)
        if to_be_or_not_to_be():
            print(rotation_values, hook_values)
        reset()

for x in range(65536): #rearange list for each order (!)
    for a in range(3, 10, 1):
        for b in range(3, 10, 1):
            if a not in [b]:
                for c in range(3, 10, 1):
                    if c not in [a, b]:
                        for d in range(3, 10, 1):
                            if d not in [a, b, c]:
                                for e in range(3, 10, 1):
                                    if e not in [a, b, c, d]:
                                        for f in range(3, 10, 1):
                                            if f not in [a, b, c, d, e]:
                                                for g in range(3, 10, 1):
                                                    if g not in [a, b, c, d, e, f]:
                                                        hook_values = [a, b, c, d, e, f, g]
                                                        base4 = base_10_to_4(x)
                                                        rotation_values = [base4[7], base4[6], base4[5], base4[4], base4[3], base4[2], base4[1], base4[0]]
                                                        n = nine()
                                                        n.poo()
    print(x)
                                                        

#print(partition([9], [False]))