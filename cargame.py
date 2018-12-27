import pygame
pygame.init()
gray=(119,118,110)
display_width=800
display_height=600
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("car game")
clock=pygame.time.Clock()
carimg=pygame.image.load('car1.jpg')

def car(x,y):
    gamedisplay.blit(carimg,(x,y))

def game_loop():
    x=(display_width*0.45)
    y=(display_height*0.8)
    bumped=false
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                bumped=true


gamedisplay.fill(gray)
car(x,y)
pygame.display.update()
clock.tick(60)
game_loop
pygame.quit()
quit()

