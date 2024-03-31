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

coords = [[1, 8], [1, 4], [1, 2], [2, 6], [2, 0], [3, 4], [4, 7], [4, 1], [5, 4], [6, 8], [6, 2], [7, 6], [7, 4], [7, 0]]

#base 4 counting system to keep track of each hooks rotation
def base_10_to_4(denary):
    base_four = ""
    while denary != 0:
        base_four += str(denary%4) #concanates remainder of division
        denary //= 4 #creates subsequent value
    while len(base_four) < 8:
        base_four = "0" + base_four #adds zeros until there are 8 bits
    return base_four

def constrict(rotation, current_grid):  #deletes row and columb (removes an l-shape) based on rotation
    if rotation == "0":
        current_grid[0][0] += 1
        current_grid[1][0] += 1
    elif rotation == "1":
        current_grid[0][0] += 1
        current_grid[1][1] -= 1
    elif rotation == "2":
        current_grid[0][1] -= 1
        current_grid[1][1] -= 1
    else:
        current_grid[0][1] -= 1
        current_grid[1][0] += 1
    return current_grid

def get_base(rotation, current_grid): #finds the coordinate of the corner of the "hook"
    if rotation == "0":
        base = [current_grid[0][0],current_grid[1][0]]
    elif rotation == "1":
        base = [current_grid[0][0],current_grid[1][1]]
    elif rotation == "2":
        base = [current_grid[0][1],current_grid[1][1]]
    elif rotation == "3":
        base = [current_grid[0][1],current_grid[1][0]]
    return base

def get_every_square(base, rotation, length): #finds the coordinate of every square in the hook
    every_square = []
    if rotation == "0":
        for x in range(0, length, 1):
            if x == 0:
                pass
            else:
                every_square.append([base[0]+x, base[1]])
        for y in range(length):
            every_square.append([base[0], base[1]+y])
    elif rotation == "1":
        for x in range(length):
            if x == 0:
                pass
            else:
                every_square.append([base[0]+x, base[1]])
        for y in range(length):
            every_square.append([base[0], base[1]-y])
    elif rotation == "2":
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
def convert_to_list_list(List):
    copy = list(set(List[:]))
    new = []
    doubles = []
    for i in range(len(List)):
        focus = List[i]
        List[i] = "poo"
        if focus in List:
            doubles.append(focus)
    for item in copy:
        if item in doubles:
            new.append([item, 2])
        else:
            new.append([item, 1])
    return new
            

def check(every_square, value, poo):#
    spaces = every_square[:]
    for item in coords:
        try:
            spaces.remove(item)
        except:
            pass
    print(len(spaces), value)
    if len(spaces) >= value:
        clashing_values = []
        for i in range(14): #finds all the values that could have a number in the hook
            affected_values = numbers[i][5][:]
            for item in affected_values:
                if item in every_square: #not working
                    clashing_values.append(i)
        clashing_values = convert_to_list_list(clashing_values)
        #print(clashing_values)
        #convert clashing numbers into lists 
        for number in clashing_values:
            save = []
            partitions = numbers[number[0]][4][:]
            #print(partitions)
            for x in range (len(partitions)):
                partition = partitions[x][:]
                #can fit
                #print(numbers[number][0], partitions)
                if number[1] == 1:
                    if value in partition:
                        save.append(partition)
                    elif partition[-1] in ["1", "2", "3"]:
                        save.append(partition)
                        temp = numbers[number[0]]
                        temp[4][x][-1] = str(int(temp[4][x][-1])-1)
                        numbers[number[0]] = temp
                elif number[1] == 2:
                    if partition.count(value) == 2:
                        save.append(partition)
                    elif partition.count(value) == 1 and partition[-1] in ["1", "2", "3"]:
                        save.append(partition)
                        temp = numbers[number[0]]
                        temp[4][x][-1] = str(int(temp[4][x][-1])-1)
                        numbers[number[0]] = temp
                    elif partition[-1] in ["2", "3"]:
                        save.append(partition)
                        temp = numbers[number[0]]
                        temp[4][x][-1] = str(int(temp[4][x][-1])-2)
                        numbers[number[0]] = temp
            for i in range(len(save)):
                save[i].pop()
                save[i].append("0")
            remove = end_partitions[number[0]][:]
            #print(numbers[number][0], remove)
            #print("-------------")
            for item in save:
                try:
                    remove.remove(item)
                except:
                    pass #working
            #print(numbers[number][0], remove)
            #print("-------------")
            #print(holder)
            for item in remove:
                end_partitions[number[0]].remove(item)
            #print(number, end_partitions[number])
            #print("---------")
        #print("--------------------------------------------------------------")
        return True
    else:
        return False
                                    
def to_be_or_not_to_be():
    for i in range(14):
        if end_partitions[i] == []:
            return False
    return True


def reset():
    #numbers[i][4] = (partition(numbers[i][0], numbers[i][3], True))
    #end_partitions[i] = partition(numbers[i][0], numbers[i][3], False)
    end_partitions[0] = [[9, 9, '0'], [1, 8, 9, '0'], [2, 7, 9, '0'], [2, 8, 8, '0'], [3, 6, 9, '0'], [3, 7, 8, '0'], [4, 5, 9, '0'], [4, 6, 8, '0'], [4, 7, 7, '0'], [5, 5, 8, '0'], [5, 6, 7, '0']]
    end_partitions[1] = [[5, '0'], [1, 4, '0'], [2, 3, '0'], [1, 2, 2, '0']]
    end_partitions[2] = [[9, '0'], [1, 8, '0'], [2, 7, '0'], [3, 6, '0'], [4, 5, '0'], [1, 2, 6, '0'], [1, 3, 5, '0'], [1, 4, 4, '0'], [2, 2, 5, '0'], [2, 3, 4, '0'], [1, 2, 2, 4, '0'], [1, 2, 3, 3, '0']]
    end_partitions[3] = [[9, '0'], [1, 8, '0'], [2, 7, '0'], [3, 6, '0'], [4, 5, '0'], [1, 2, 6, '0'], [1, 3, 5, '0'], [1, 4, 4, '0'], [2, 2, 5, '0'], [2, 3, 4, '0'], [1, 2, 2, 4, '0'], [1, 2, 3, 3, '0']]
    end_partitions[4] = [[4, 9, 9, '0'], [5, 8, 9, '0'], [6, 7, 9, '0'], [6, 8, 8, '0'], [7, 7, 8, '0']]
    end_partitions[5] = [[2, 9, '0'], [3, 8, '0'], [4, 7, '0'], [5, 6, '0'], [1, 2, 8, '0'], [1, 3, 7, '0'], [1, 4, 6, '0'], [1, 5, 5, '0'], [2, 2, 7, '0'], [2, 3, 6, '0'], [2, 4, 5, '0'], [3, 3, 5, '0'], [3, 4, 4, '0'], [1, 2, 2, 6, '0'], [1, 2, 3, 5, '0'], [1, 2, 4, 4, '0'], [1, 3, 3, 4, '0'], [2, 2, 3, 4, '0']]
    end_partitions[6] = [[3, 9, '0'], [4, 8, '0'], [5, 7, '0'], [6, 6, '0'], [1, 2, 9, '0'], [1, 3, 8, '0'], [1, 4, 7, '0'], [1, 5, 6, '0'], [2, 2, 8, '0'], [2, 3, 7, '0'], [2, 4, 6, '0'], [2, 5, 5, '0'], [3, 3, 6, '0'], [3, 4, 5, '0'], [1, 2, 2, 7, '0'], [1, 2, 3, 6, '0'], [1, 2, 4, 5, '0'], [1, 3, 3, 5, '0'], [1, 3, 4, 4, '0'], [2, 2, 3, 5, '0'], [2, 2, 4, 4, '0'], [2, 3, 3, 4, '0']]
    end_partitions[7] = [[5, 9, '0'], [6, 8, '0'], [7, 7, '0'], [1, 4, 9, '0'], [1, 5, 8, '0'], [1, 6, 7, '0'], [2, 3, 9, '0'], [2, 4, 8, '0'], [2, 5, 7, '0'], [2, 6, 6, '0'], [3, 3, 8, '0'], [3, 4, 7, '0'], [3, 5, 6, '0'], [4, 4, 6, '0'], [4, 5, 5, '1'], [1, 2, 2, 9, '0'], [1, 2, 3, 8, '0'], [1, 2, 4, 7, '0'], [1, 2, 5, 6, '0'], [1, 3, 3, 7, '0'], [1, 3, 4, 6, '0'], [1, 3, 5, 5, '0'], [1, 4, 4, 5, '0'], [2, 2, 3, 7, '0'], [2, 2, 4, 6, '0'], [2, 2, 5, 5, '0'], [2, 3, 3, 6, '0'], [2, 3, 4, 5, '0'], [3, 3, 4, 4, '0']]
    end_partitions[8] = [[4, 9, 9, '0'], [5, 8, 9, '0'], [6, 7, 9, '0'], [6, 8, 8, '0'], [7, 7, 8, '0'], [1, 3, 9, 9, '0'], [1, 4, 8, 9, '0'], [1, 5, 7, 9, '0'], [1, 5, 8, 8, '0'], [1, 6, 6, 9, '0'], [1, 6, 7, 8, '0'], [2, 2, 9, 9, '0'], [2, 3, 8, 9, '0'], [2, 4, 7, 9, '0'], [2, 4, 8, 8, '0'], [2, 5, 6, 9, '0'], [2, 5, 7, 8, '0'], [2, 6, 6, 8, '0'], [2, 6, 7, 7, '0'], [3, 3, 7, 9, '0'], [3, 3, 8, 8, '0'], [3, 4, 6, 9, '0'], [3, 4, 7, 8, '0'], [3, 5, 5, 9, '0'], [3, 5, 6, 8, '0'], [3, 5, 7, 7, '0'], [3, 6, 6, 7, '0'], [4, 4, 5, 9, '0'], [4, 4, 6, 8, '0'], [4, 4, 7, 7, '0'], [4, 5, 5, 8, '0'], [4, 5, 6, 7, '0'], [5, 5, 6, 6, '0']]
    end_partitions[9] = [[7, '0'], [1, 6, '0'], [2, 5, '0'], [3, 4, '0'], [1, 2, 4, '0'], [1, 3, 3, '0'], [2, 2, 3, '0']]
    end_partitions[10] = [[1, 9, 9, '0'], [2, 8, 9, '0'], [3, 7, 9, '0'], [3, 8, 8, '0'], [4, 6, 9, '0'], [4, 7, 8, '0'], [5, 5, 9, '0'], [5, 6, 8, '0'], [5, 7, 7, '0'], [6, 6, 7, '0'], [1, 2, 7, 9, '0'], [1, 2, 8, 8, '0'], [1, 3, 6, 9, '0'], [1, 3, 7, 8, '0'], [1, 4, 5, 9, '0'], [1, 4, 6, 8, '0'], [1, 4, 7, 7, '0'], [1, 5, 5, 8, '0'], [1, 5, 6, 7, '0'], [2, 2, 6, 9, '0'], [2, 2, 7, 8, '0'], [2, 3, 5, 9, '0'], [2, 3, 6, 8, '0'], [2, 3, 7, 7, '0'], [2, 4, 4, 9, '0'], [2, 4, 5, 8, '0'], [2, 4, 6, 7, '0'], [2, 5, 5, 7, '0'], [2, 5, 6, 6, '0'], [3, 3, 4, 9, '0'], [3, 3, 5, 8, '0'], [3, 3, 6, 7, '0'], [3, 4, 4, 8, '0'], [3, 4, 5, 7, '0'], [3, 4, 6, 6, '0'], [3, 5, 5, 6, '0'], [4, 4, 5, 6, '0']]
    end_partitions[11] = [[5, 8, 9, 9, '0'], [6, 7, 9, 9, '0'], [6, 8, 8, 9, '0'], [7, 7, 8, 9, '0']]
    end_partitions[12] = [[4, 9, 9, '0'], [5, 8, 9, '0'], [6, 7, 9, '0'], [6, 8, 8, '0'], [7, 7, 8, '0'], [1, 3, 9, 9, '0'], [1, 4, 8, 9, '0'], [1, 5, 7, 9, '0'], [1, 5, 8, 8, '0'], [1, 6, 6, 9, '0'], [1, 6, 7, 8, '0'], [2, 2, 9, 9, '0'], [2, 3, 8, 9, '0'], [2, 4, 7, 9, '0'], [2, 4, 8, 8, '0'], [2, 5, 6, 9, '0'], [2, 5, 7, 8, '0'], [2, 6, 6, 8, '0'], [2, 6, 7, 7, '0'], [3, 3, 7, 9, '0'], [3, 3, 8, 8, '0'], [3, 4, 6, 9, '0'], [3, 4, 7, 8, '0'], [3, 5, 5, 9, '0'], [3, 5, 6, 8, '0'], [3, 5, 7, 7, '0'], [3, 6, 6, 7, '0'], [4, 4, 5, 9, '0'], [4, 4, 6, 8, '0'], [4, 4, 7, 7, '0'], [4, 5, 5, 8, '0'], [4, 5, 6, 7, '0'], [5, 5, 6, 6, '0']]
    end_partitions[13] = [[6, 9, '0'], [7, 8, '0'], [1, 5, 9, '0'], [1, 6, 8, '0'], [1, 7, 7, '0'], [2, 4, 9, '0'], [2, 5, 8, '0'], [2, 6, 7, '0'], [3, 3, 9, '0'], [3, 4, 8, '0'], [3, 5, 7, '0'], [3, 6, 6, '0'], [4, 4, 7, '0'], [4, 5, 6, '0']]
    ########
    numbers[0][4] = [[9, 9, '1'], [1, 8, 9, '0'], [2, 7, 9, '0'], [2, 8, 8, '0'], [3, 6, 9, '0'], [3, 7, 8, '0'], [4, 5, 9, '0'], [4, 6, 8, '0'], [4, 7, 7, '0'], [5, 5, 8, '0'], [5, 6, 7, '0']]
    numbers[1][4] = [[5, '3'], [1, 4, '2'], [2, 3, '2'], [1, 2, 2, '1']]
    numbers[2][4] = [[9, '3'], [1, 8, '2'], [2, 7, '2'], [3, 6, '2'], [4, 5, '2'], [1, 2, 6, '1'], [1, 3, 5, '1'], [1, 4, 4, '1'], [2, 2, 5, '1'], [2, 3, 4, '1'], [1, 2, 2, 4, '0'], [1, 2, 3, 3, '0']]
    numbers[3][4] = [[9, '3'], [1, 8, '2'], [2, 7, '2'], [3, 6, '2'], [4, 5, '2'], [1, 2, 6, '1'], [1, 3, 5, '1'], [1, 4, 4, '1'], [2, 2, 5, '1'], [2, 3, 4, '1'], [1, 2, 2, 4, '0'], [1, 2, 3, 3, '0']]
    numbers[4][4] = [[4, 9, 9, '0'], [5, 8, 9, '0'], [6, 7, 9, '0'], [6, 8, 8, '0'], [7, 7, 8, '0']]
    numbers[5][4] = [[2, 9, '2'], [3, 8, '2'], [4, 7, '2'], [5, 6, '2'], [1, 2, 8, '1'], [1, 3, 7, '1'], [1, 4, 6, '1'], [1, 5, 5, '1'], [2, 2, 7, '1'], [2, 3, 6, '1'], [2, 4, 5, '1'], [3, 3, 5, '1'], [3, 4, 4, '1'], [1, 2, 2, 6, '0'], [1, 2, 3, 5, '0'], [1, 2, 4, 4, '0'], [1, 3, 3, 4, '0'], [2, 2, 3, 4, '0']]
    numbers[6][4] = [[3, 9, '2'], [4, 8, '2'], [5, 7, '2'], [6, 6, '2'], [1, 2, 9, '1'], [1, 3, 8, '1'], [1, 4, 7, '1'], [1, 5, 6, '1'], [2, 2, 8, '1'], [2, 3, 7, '1'], [2, 4, 6, '1'], [2, 5, 5, '1'], [3, 3, 6, '1'], [3, 4, 5, '1'], [1, 2, 2, 7, '0'], [1, 2, 3, 6, '0'], [1, 2, 4, 5, '0'], [1, 3, 3, 5, '0'], [1, 3, 4, 4, '0'], [2, 2, 3, 5, '0'], [2, 2, 4, 4, '0'], [2, 3, 3, 4, '0']]
    numbers[7][4] = [[5, 9, '2'], [6, 8, '2'], [7, 7, '2'], [1, 4, 9, '1'], [1, 5, 8, '1'], [1, 6, 7, '1'], [2, 3, 9, '1'], [2, 4, 8, '1'], [2, 5, 7, '1'], [2, 6, 6, '1'], [3, 3, 8, '1'], [3, 4, 7, '1'], [3, 5, 6, '1'], [4, 4, 6, '1'], [4, 5, 5, '1'], [1, 2, 2, 9, '0'], [1, 2, 3, 8, '0'], [1, 2, 4, 7, '0'], [1, 2, 5, 6, '0'], [1, 3, 3, 7, '0'], [1, 3, 4, 6, '0'], [1, 3, 5, 5, '0'], [1, 4, 4, 5, '0'], [2, 2, 3, 7, '0'], [2, 2, 4, 6, '0'], [2, 2, 5, 5, '0'], [2, 3, 3, 6, '0'], [2, 3, 4, 5, '0'], [3, 3, 4, 4, '0']]
    numbers[8][4] = [[4, 9, 9, '1'], [5, 8, 9, '1'], [6, 7, 9, '1'], [6, 8, 8, '1'], [7, 7, 8, '1'], [1, 3, 9, 9, '0'], [1, 4, 8, 9, '0'], [1, 5, 7, 9, '0'], [1, 5, 8, 8, '0'], [1, 6, 6, 9, '0'], [1, 6, 7, 8, '0'], [2, 2, 9, 9, '0'], [2, 3, 8, 9, '0'], [2, 4, 7, 9, '0'], [2, 4, 8, 8, '0'], [2, 5, 6, 9, '0'], [2, 5, 7, 8, '0'], [2, 6, 6, 8, '0'], [2, 6, 7, 7, '0'], [3, 3, 7, 9, '0'], [3, 3, 8, 8, '0'], [3, 4, 6, 9, '0'], [3, 4, 7, 8, '0'], [3, 5, 5, 9, '0'], [3, 5, 6, 8, '0'], [3, 5, 7, 7, '0'], [3, 6, 6, 7, '0'], [4, 4, 5, 9, '0'], [4, 4, 6, 8, '0'], [4, 4, 7, 7, '0'], [4, 5, 5, 8, '0'], [4, 5, 6, 7, '0'], [5, 5, 6, 6, '0']]
    numbers[9][4] = [[7, '2'], [1, 6, '1'], [2, 5, '1'], [3, 4, '1'], [1, 2, 4, '0'], [1, 3, 3, '0'], [2, 2, 3, '0']]
    numbers[10][4] = [[1, 9, 9, '1'], [2, 8, 9, '1'], [3, 7, 9, '1'], [3, 8, 8, '1'], [4, 6, 9, '1'], [4, 7, 8, '1'], [5, 5, 9, '1'], [5, 6, 8, '1'], [5, 7, 7, '1'], [6, 6, 7, '1'], [1, 2, 7, 9, '0'], [1, 2, 8, 8, '0'], [1, 3, 6, 9, '0'], [1, 3, 7, 8, '0'], [1, 4, 5, 9, '0'], [1, 4, 6, 8, '0'], [1, 4, 7, 7, '0'], [1, 5, 5, 8, '0'], [1, 5, 6, 7, '0'], [2, 2, 6, 9, '0'], [2, 2, 7, 8, '0'], [2, 3, 5, 9, '0'], [2, 3, 6, 8, '0'], [2, 3, 7, 7, '0'], [2, 4, 4, 9, '0'], [2, 4, 5, 8, '0'], [2, 4, 6, 7, '0'], [2, 5, 5, 7, '0'], [2, 5, 6, 6, '0'], [3, 3, 4, 9, '0'], [3, 3, 5, 8, '0'], [3, 3, 6, 7, '0'], [3, 4, 4, 8, '0'], [3, 4, 5, 7, '0'], [3, 4, 6, 6, '0'], [3, 5, 5, 6, '0'], [4, 4, 5, 6, '0']]
    numbers[11][4] = [[5, 8, 9, 9, '0'], [6, 7, 9, 9, '0'], [6, 8, 8, 9, '0'], [7, 7, 8, 9, '0']]
    numbers[12][4] = [[4, 9, 9, '1'], [5, 8, 9, '1'], [6, 7, 9, '1'], [6, 8, 8, '1'], [7, 7, 8, '1'], [1, 3, 9, 9, '0'], [1, 4, 8, 9, '0'], [1, 5, 7, 9, '0'], [1, 5, 8, 8, '0'], [1, 6, 6, 9, '0'], [1, 6, 7, 8, '0'], [2, 2, 9, 9, '0'], [2, 3, 8, 9, '0'], [2, 4, 7, 9, '0'], [2, 4, 8, 8, '0'], [2, 5, 6, 9, '0'], [2, 5, 7, 8, '0'], [2, 6, 6, 8, '0'], [2, 6, 7, 7, '0'], [3, 3, 7, 9, '0'], [3, 3, 8, 8, '0'], [3, 4, 6, 9, '0'], [3, 4, 7, 8, '0'], [3, 5, 5, 9, '0'], [3, 5, 6, 8, '0'], [3, 5, 7, 7, '0'], [3, 6, 6, 7, '0'], [4, 4, 5, 9, '0'], [4, 4, 6, 8, '0'], [4, 4, 7, 7, '0'], [4, 5, 5, 8, '0'], [4, 5, 6, 7, '0'], [5, 5, 6, 6, '0']]
    numbers[13][4] = [[6, 9, '1'], [7, 8, '1'], [1, 5, 9, '0'], [1, 6, 8, '0'], [1, 7, 7, '0'], [2, 4, 9, '0'], [2, 5, 8, '0'], [2, 6, 7, '0'], [3, 3, 9, '0'], [3, 4, 8, '0'], [3, 5, 7, '0'], [3, 6, 6, '0'], [4, 4, 7, '0'], [4, 5, 6, '0']]

def Break():
    for i in range(14):
        if end_partitions[i] == []:
            return True     
    return False

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

class nine():
    def __init__(self, current_grid):
        self.length = 9 #how wide and tall the hook is
        self.rotation = rotation_values[0]
        self.value = hook_values[0] #from 3 ---> 9
        self.base = get_base(self.rotation, current_grid) #the coords of the corner of the hook
        self.current_grid = constrict(self.rotation, current_grid)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        self.Continue = check(self.every_square, self.value, self.length)
        if not Break() and self.Continue:
            eight(self.current_grid)

class eight():
    def __init__(self, current_grid):
        self.length = 8 #how wide and tall the hook is
        self.rotation = rotation_values[1]
        self.value = hook_values[1] #the number assigned to this hook
        self.base = get_base(self.rotation, current_grid) #the coords of the corner of the hook
        self.current_grid = constrict(self.rotation, current_grid)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        self.Continue = check(self.every_square, self.value, self.length)
        if not Break() and self.Continue:
            seven(self.current_grid)

class seven():
    def __init__(self, current_grid):
        self.length = 7 #how wide and tall the hook is
        self.rotation = rotation_values[2]
        self.value = hook_values[2] #the number assigned to this hook
        self.base = get_base(self.rotation, current_grid) #the coords of the corner of the hook
        self.current_grid = constrict(self.rotation, current_grid)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        self.Continue = check(self.every_square, self.value, self.length)
        if not Break() and self.Continue:
            six(self.current_grid)

class six():
    def __init__(self, current_grid):
        self.length = 6 #how wide and tall the hook is
        self.rotation = rotation_values[3]
        self.value = hook_values[3] #the number assigned to this hook
        self.base = get_base(self.rotation, current_grid) #the coords of the corner of the hook
        self.current_grid = constrict(self.rotation, current_grid)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        self.Continue = check(self.every_square, self.value, self.length)
        if not Break() and self.Continue:
            five(self.current_grid)

class five():
    def __init__(self, current_grid):
        self.length = 5 #how wide and tall the hook is
        self.rotation = rotation_values[4]
        self.value = hook_values[4] #the number assigned to this hook
        self.base = get_base(self.rotation, current_grid) #the coords of the corner of the hook
        self.current_grid = constrict(self.rotation, current_grid)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        self.Continue = check(self.every_square, self.value, self.length)
        if not Break() and self.Continue:
            four(self.current_grid)

class four():
    def __init__(self, current_grid):
        self.length = 4 #how wide and tall the hook is
        self.rotation = rotation_values[5]
        self.value = hook_values[5] #the number assigned to this hook
        self.base = get_base(self.rotation, current_grid) #the coords of the corner of the hook
        self.current_grid = constrict(self.rotation, current_grid)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        self.Continue = check(self.every_square, self.value, self.length)
        if not Break() and self.Continue:
            three(self.current_grid)

class three():
    def __init__(self, current_grid):
        self.length = 3 #how wide and tall the hook is
        self.rotation = rotation_values[6]
        self.value = hook_values[6] #the number assigned to this hook
        self.base = get_base(self.rotation, current_grid) #the coords of the corner of the hook
        self.current_grid = constrict(self.rotation, current_grid)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        self.Continue = check(self.every_square, self.value, self.length)
        if not Break() and self.Continue:
            two(self.current_grid)

class two():
    def __init__(self, current_grid):
        self.length = 2 #how wide and tall the hook is
        self.rotation = rotation_values[7]
        self.value = 2 #the number assigned to this hook
        self.base = get_base(self.rotation, current_grid) #the coords of the corner of the hook
        self.current_grid = constrict(self.rotation, current_grid)
        self.every_square = get_every_square(self.base, self.rotation, self.length)
        self.Continue = check(self.every_square, self.value, self.length)
        if not Break() and self.Continue:
            one(self.current_grid)

class one():
    def __init__(self, current_grid):
        self.rotation = "0"
        self.length = 1 #how wide and tall the hook is
        self.value = 1
        self.base = get_base(self.rotation, current_grid)
        self.every_square = [self.base]
        self.Continue = check(self.every_square, self.value, self.length)
        #for x in range(14):
            #print(end_partitions[x])
        if to_be_or_not_to_be() and self.Continue:
            print(rotation_values, hook_values)
            exit()

for x in range(0, 10001, 1):
#for x in range(10000, 20001, 1):
#for x in range(20000, 30001, 1):
#for x in range(30000, 40001, 1):
#for x in range(40000, 50001, 1):
#for x in range(50000, 60001, 1):
#for x in range(60000, 65537, 1):
    print(x)
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
                                                        reset()
                                                        hook_values = [a, b, c, d, e, f, g]
                                                        base4 = base_10_to_4(x)
                                                        rotation_values = [base4[7], base4[6], base4[5], base4[4], base4[3], base4[2], base4[1], base4[0]]
                                                        nine([[0, 8], [0, 8]])
   

#reset()
#hook_values = [9, 8, 7, 6, 5, 4, 3]
#rotation_values = ['0', '0', '0', '0', '0', '0', '0', '0']
#nine([[0, 8], [0, 8]])