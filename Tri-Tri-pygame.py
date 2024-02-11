# import the pygame module 
import pygame
import random
 
# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((850, 850)) 
# Fill the background colour to the screen 
screen.fill(background_colour)
for r in range(17):
    for c in range(17):
        pygame.draw.rect(screen, (r*10, c*10, c*10), pygame.Rect(r * 51, c*51, 51, 51))
# Update the display using flip 
pygame.display.flip() 
# Variable to keep our game loop running 
running = True
# game loop 
while running: 
# for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

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
            if square[r][c] != 0: #checks if current value in square has a value
                numbers[i] = [] #creates the row in hashmap
                position = (r, c) #where the value is on the grid
                area = square[r][c] #the area of the triangle to be made
                base = factor_tree(area*2) #finds all the possible integer bases for the right angle triangle refer to area of triangle formula --> A = (B*H)/2 
                rotation = 0 #current rotation status in degrees
                numbers[i] += [position, area, base, rotation] #adds the position, area, base, rotation to the hashmap row created prior
                i += 1 #increments the index of hashmap

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
    return H

hashmap(grid)