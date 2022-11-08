import sys,math
import pygame
from pygame.locals import *
pygame.init()

def check_around(x,y,arr):
    for i in range(y-2,y+2):
        for j in range(x-2,x+2):
            if img.get_at((j,i)) != (0 ,0 ,0 , 255) and [j,i] not in arr:
                arr.append([j,i])
                check_around(j,i,arr)
    return arr

def blit_generated(surf,arr):
    for i in range(len(arr)):
        if i == 0:
            pos = [1,1]
        else:
            pos[1] = (arr[i-1][2][1]+pos[1]+2)
            
        surf.set_at((pos[0]-1,pos[1]-1),(255,0,255))
        surf.set_at((pos[0]-1+arr[i][2][0]+1,pos[1]-1),(0,255,255))
        surf.set_at((0,pos[1]-1+arr[i][2][1]+1),(0,255,255))

        surf.set_colorkey((0,0,0))
        surf.blit(arr[i][0],pos)
        
        surf.set_colorkey((0,0,0))
        surf.blit(images[i][0],pos)
#-----------------------------------------------------------------------------------------------
SCALE = 3
screen = pygame.display.set_mode((500, 500),0,32)
img = pygame.image.load("test.png").convert()

WINDOW_SIZE = [img.get_width()*SCALE, img.get_height()*SCALE]
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface((img.get_width(), img.get_height()))

img_rect = any
pixels = []
rects = []
images = []
spritesheet_mode = False


while True:
    display.fill((0,0,0))
    
    mx,my = pygame.mouse.get_pos()
    mx = math.floor(mx/SCALE)
    my = math.floor(my/SCALE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            #generációs módba váltás
            if event.key == K_g:
                pixels.clear()
                spritesheet_mode = True
                
                height = 0
                width = 0
                for i in range(len(images)):
                    height += (images[i][2][1]+2)
                    
                    if images[i][2][0] > width:
                        width = images[i][2][0]+3
                screen = pygame.display.set_mode((width*SCALE,height*SCALE),0,32)
            if event.key == K_s:
                screen = pygame.display.set_mode((width,height),0,32)
                display = pygame.Surface((width,height))

                blit_generated(display,images)


                
                screen.blit(pygame.transform.scale(display,(width,height)),(0,0))
                
                pygame.image.save(display,"save.png")
                sys.exit()
            if event.key == K_r:
                rects.clear()
                images.clear()
                pixels.clear()     
       
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pixels.clear()
            if img.get_at((mx,my)) != (0 ,0 ,0 , 255):
                arr = check_around(mx,my,pixels)
            
    
    if not spritesheet_mode:
        display.blit(img,(0,0))
        
        print(len(pixels))
        
        if len(pixels) > 0:

            min = [100,100]
            max = [0,0]
            
            for i in pixels:
                if i[0] < min[0]:
                    min[0] = i[0]            
                if i[1] < min[1]:
                    min[1] = i[1]                    
                if i[0] > max[0]:
                    max[0] = i[0]
                if i[1] > max[1]:
                    max[1] = i[1]

    
            handle_surf = display.copy()
            clip_rect = pygame.Rect(min[0],min[1],max[0]-min[0]+1,max[1]-min[1]+1)
            rects.append(clip_rect)
            handle_surf.set_clip(clip_rect)
            image = display.subsurface(handle_surf.get_clip())
            image = image.copy()
            
            for i in rects:
                pygame.draw.rect(display,(255,0,255),i,1)


            
            arr = [image,min,[max[0]-min[0],max[1]-min[1]]]
            
            if len(images) > 0:
                if arr[1] != images[len(images)-1][1] and arr[2] != images[len(images)-1][2]:
                    images.append(arr)
            else:
                images.append(arr)
    else:
        blit_generated(display,images)

    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
