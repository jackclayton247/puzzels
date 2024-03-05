import math

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 2, 0, 0, 0],#
        [0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0],#
        [4, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],#
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],#
        [0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 10, 0, 0, 0],#
        [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#
        [0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3],#
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#
        [0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0],#
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#
        [4, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0],#
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0],#
        [0, 0, 0, 9, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0],#
        [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#
        [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 6],#
        [0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0],#
        [0, 0, 0, 2, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def hashmap(square):
    numbers = {} #hashmap-numbers = |index:position|area|base|rotation|
    i = 0 #index for hashmap
    for r in range(len(square[0])): #iterates through rows in square
        for c in range(len(square[0])): #iterates through colums in square
            if square[c][r] != 0: #checks if current value in square has a value
                numbers[i] = [] #creates the row in hashmap
                position = (r, c) #where the value is on the grid
                area = square[c][r] #the area of the triangle to be made
                base = factor_tree(area*2) #finds all the possible integer bases for the right angle triangle refer to area of triangle formula --> A = (B*H)/2 
                rotation = 0 #current rotation status in degrees
                numbers[i] += [position, area, base, rotation] #adds the position, area, base, rotation to the hashmap row created prior
                i += 1 #increments the index of hashmap
    return numbers

def factor_tree(number):
    factors = [] #creates list to hold factors
    for x in range(1,number+1, 1): #iterates through all integers from 1 to number
        if x in (1, number): #excludes factors of 1 and itself
            pass 
        elif number % x == 0: #checks if number is divisible cleanly by current x
            factors.append(x) #adds x value to factors list
    return factors

def height(B, A): #B = base, A = area
    H = (2*A)/B #rearanged formular for area of triangle
    return int(H)

def graidient(B, H, rot): #change in y over change in x 
    if rot == 0 or rot == 180:
        M = (H/B) #adjusts for the fact that the Base input and height input are moduli
    if rot == 90 or rot == 270:
        M = (B/H) #adjusts for the fact that the Base input and height input are moduli
    return M

def roots(pos, B, rot, grad,H):#range of coors 0 --> 16 (x,y)
    lengths = [] #creates list to hold num of consecutive whole squares per layer of triangle
    roots = []
    chunk = 1/grad #reciprocal of gradient
    i = 1 #creates counter variable
    while B-(i*chunk) > 0: #while there are whole squares in layer
        x = math.floor(B-(i*chunk)) 
        if x != 0:                  #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            lengths.append(x) #adds length to list
        i += 1 #increments counter
    for y in range(len(lengths)): #iterates through all the y coords
        for x in range(lengths[y]): #iterates through all the x coords on current layer
            if rot == 0:
                if 0 <= pos[0]-x <= 16 and 0 <= pos[1]+y <= 16: #keeps roots within index limit
                    if 0 <= pos[0]-x+B <= 16 and  0 <= pos[1]+y-H <=16:
                        roots.append([pos[0]-x, pos[1]+y]) #adds to list
            elif rot == 1:
                if 0 <= pos[0]-y <= 16 and 0 <= pos[1]-x <= 16: #keeps roots within index limit
                    if 0 <= pos[0]-y+H <= 16 and  0 <= pos[1]-x+B <=16:
                        roots.append([pos[0]-y, pos[1]-x]) #adds to list
            elif rot == 2:
                if 0 <= pos[0]+x <= 16 and 0 <= pos[1]-y <= 16: #keeps roots within index limit
                    if 0 <= pos[0]+x-B <= 16 and  0 <= pos[1]-y+H <=16:
                        roots.append([pos[0]+x, pos[1]-y]) #adds to list
            elif rot == 3:
                if 0 <= pos[0]+y <= 16 and 0 <= pos[1]+x <= 16: #keeps roots within index limit
                    if 0 <= pos[0]+y-H <= 16 and  0 <= pos[1]+x-B <=16:
                        roots.append([pos[0]+y, pos[1]+x]) #adds to list
    return roots
        
def occupied(pos, B, H, rot, grad):
    pass












def main(hash):
    for one in range(29):
        print(hash[one][1],hash[one][0], "<<<<<<<<<<<<<")
        for two in range(len(hash[one][2])):
            Pos = hash[one][0]
            A = hash[one][1]
            B = hash[one][2][two]
            Rot = hash[one][3]
            H = height(B, A)
            grad = graidient(B, H, Rot)
            x = roots(Pos, B, Rot, grad, H) #pos, B, rot, grad
            print(B,x)
            print("----------")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

main(hashmap(grid))




