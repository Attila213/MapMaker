import pygame,sys,os,random,json

# make a col*row size table and return an array full of rects
def map_generation(startpos,size,col,row):
    map = []
    x= startpos[0]
    y= startpos[1]
    
    for i in range(col):
        arr = []
        for j in range(row):
            r = pygame.Rect(x+ i*(size),y+j*(size),size,size)
            arr.append(r)
        map.append(arr)
    return map

#screen pygame image load(img)
def cut_img(img):
    arr = []
    start_pos = []
    width = 0
    height = 0
    counter = 0

    for i in range(img.get_height()):   
        for j in range(img.get_width()):
            if img.get_at((j,i)) == (255 ,0 , 255, 255):
                start_pos = [j+1,i+1]
            if img.get_at((j,i)) == (0 ,255 , 255, 255):
                counter+=1
                
                if counter == 1:
                    width = j-start_pos[0]
                if counter == 2:
                    height = i-start_pos[1]
                    
                    handle_surf = img.copy()
                    
                    clip_rect = pygame.Rect(start_pos[0],start_pos[1],width,height)
                    handle_surf.set_clip(clip_rect)
                    image = img.subsurface(handle_surf.get_clip())
                    image = image.copy()
                    image.set_colorkey((0,0,0))
                    arr.append(image)
                    
                    start_pos = []
                    width = 0
                    height = 0
                    counter = 0
    return arr

def image_loader(path):
    imgs = []
    for i in os.listdir(path):
        imgs = []
        path = path
        for i in os.listdir(path):
            imgs.append([i.split(".")[0],pygame.image.load(path+i).convert_alpha()]) 
    return imgs

def loadJson(filename,value={}):
    arr = any
    try:
        with open(filename+".json","r") as f:
            try:
                arr=json.load(f)
            except:
                arr = value
    except:
        arr = {}
    return arr

def writeJson(filename,arr):
    with open(filename+".json", 'w') as outfile:
        json.dump(arr, outfile)

def swap(a,b):
    temp = a
    a = b
    b = temp