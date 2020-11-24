#safwan hasan
import pygame
import random
import sys

WIDTH = 800
HEIGHT = 800
FPS = 30

#initial values for maze
x = 0
y = 0
w = 20
visit = []
stack = []

def drawRect(x,y): #draws a white rectange to carve a maze 
    pygame.draw.rect(screen, white, (x+1,y+1,20,20),0)
    pygame.display.update()
    
def grid(): #creates a grid based on input of n
    n = int(input("Enter n: "))
    line_space = 800/n

    counter = 0
    while(counter<800):
        pygame.draw.line(screen,black,(counter,0),(counter,800),2) #horiz lines
        pygame.draw.line(screen,black,(0,counter),(800,counter),2)#vertical lines
        counter = counter+line_space
        pygame.display.update()

#direction of maze carve
        
def down(x,y): #carves a maze upward
    pygame.draw.rect(screen,white,(x+1, y-w+1, 20, 40),0)
    pygame.display.update()

def up(x,y):
    pygame.draw.rect(screen,white,(x+1, y+1, 20, 40),0)
    pygame.display.update()

def left(x,y):
    pygame.draw.rect(screen,white,(x-w+1, y+1, 40, 20),0)
    pygame.display.update()

def right(x,y):
    pygame.draw.rect(screen,white,(x+1, y+1, 40, 20),0)
    pygame.display.update()


def backTrack(x,y):
    pygame.draw.rect(screen,white,(x+1, y+1, 20, 20),0)
    pygame.display.update()
    
def Maze(x,y):
    drawRect(x,y) #initial spot
    stack.append((x,y)) #places coordinates in stack and visit
    visit.append((x,y))
    while (len(stack)>0):
        cell = []
        if (x + w, y) not in visit: #if right hasn't been visited
            cell.append("right")
        if (x-w, y) not in visit:
            cell.append("left")
        if (x , y + w) not in visit:
            cell.append("up")
        if (x, y - w) not in visit:
            cell.append("down")
        if (len(cell)>0):
            cell_choice = (random.choice(cell)) #selects random direction
        
            if cell_choice == "left":
                left(x,y)
                x = x-w
                visit.append((x,y))
                stack.append((x,y))
            elif cell_choice == "right":
                right(x,y)
                x = x+w
                visit.append((x,y))
                stack.append((x,y))
            elif cell_choice == "up":
                left(x,y)
                y = y+w
                visit.append((x,y))
                stack.append((x,y))
            elif cell_choice == "down":
                left(x,y)
                y = y-w
                visit.append((x,y))
                stack.append((x,y))
        else:
            x,y = stack.pop() #choose last coordinate from stack and delete 
            drawRect(x,y)
            backTrack(x,y)
            
# initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()
white = [255, 255, 255]
black = [0,0,0]
screen.fill(white)
pygame.display.update()
grid()
Maze(random.randint(0,800),random.randint(0,800)) #starts at a random location
pygame.display.update()
running = True
while running:
# keep running at the at the right speed
    clock.tick(FPS)


# process input (events)
    for event in pygame.event.get():
# check for closing the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
