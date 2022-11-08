import sys,math,json
import pygame
import functions as fun
from pygame.locals import *

tileset = input("Choose a tileset: ")
pygame.init()

WINDOW_SIZE = [500,500]
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface(screen.get_size()).convert()
scale = 10

path = "assets/images/tilesets/"+tileset+".png"
images = pygame.image.load(path).convert()
tiles = fun.cut_img(images)


img_pos = [10,10]
counter = 0

offset = {}

rect = pygame.Rect(10,10,18,18)
while True:
    display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                img_pos[1] += 1
            if event.key == pygame.K_UP:
                img_pos[1] -= 1
            if event.key == pygame.K_RIGHT:
                img_pos[0] += 1
            if event.key == pygame.K_LEFT:
                img_pos[0] -= 1
            if event.key == pygame.K_RETURN:
                
                x_offset =img_pos[0]-rect.x
                y_offset = img_pos[1]-rect.y
                
                if x_offset != 0 or y_offset != 0:
                    offset[str(counter)] = {"x":x_offset,"y":y_offset}
                img_pos = [10,10]
                
                if counter == len(tiles)-1:
                    fun.writeJson("assets/images/offsets/"+tileset,offset)
                    sys.exit()
                else: 
                    counter += 1
    
    pygame.draw.rect(display,(255,0,0),rect)
    display.blit(tiles[counter].convert(),img_pos)
    
    
    screen.blit(pygame.transform.scale(display,(screen.get_width()*scale,screen.get_height()*scale)),(0,0))
    
    pygame.display.update()

