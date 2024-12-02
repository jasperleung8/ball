import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("ball")

blue = (0,0,255)
red = (255,0,0)
green = (0,255,255)
white = (255,255,255)
black = (0,0,0)

screen.fill(white)
pygame.display.update()

class circle():

    def __init__(self,colour,position,size,width=0):
        self.colour = colour
        self.position = position
        self.size = size
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen,self.colour,self.position,self.size,self.width)

    def grow(self,x):
        self.size += x 
        pygame.draw.circle(self.screen,self.colour,self.position,self.size,self.width)

position = (300,300)
radius = 50
widht = 2

pygame.draw.circle(screen,black,position,radius,widht)
pygame.display.update()

bluecircle = circle(blue,position,radius+60)
redcircle = circle(red,position,radius+40)
greencircle = circle(green,position,radius,20)

while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            bluecircle.draw()
            redcircle.draw()
            greencircle.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            bluecircle.grow(2)
            redcircle.grow(2)
            greencircle.grow(2)
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION):
            position = pygame.mouse.get_pos()
            blackcircle = circle(black,position,5)
            blackcircle.draw()
            pygame.display.update()

        elif event.type == pygame.QUIT:
            pygame.quit()        

