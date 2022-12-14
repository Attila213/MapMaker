import assets.editors.functions as fun
import pygame,json
import assets.editors.font as font
class Drawing:
    def __init__(self,display,tilesize):
        self.display = display
        self.selected_tile_rect = None
        self.selected_tile_img = None
        self.tile_size = tilesize
        self.layer = 0
        self.scroll = [0,0]
        
        self.offset = None
        self.offset_name = None
        self.offset_index = None
        
        self.tile_x = None
        self.tile_y = None

    def currentTilePos(self):
        #Check if this index in the offset
        exists = False
        for key in self.offset:
            if key == str(self.offset_index):
                exists= True
        
        #draw tile img with the offset           
        if self.offset !={} and exists:
            return [self.selected_tile_rect.x+self.offset[str(self.offset_index)]["x"],self.selected_tile_rect.y+self.offset[str(self.offset_index)]["y"]]
        else:
            return [self.selected_tile_rect.x,self.selected_tile_rect.y]
    
    def drawTileHover(self,mouse_pos):
        
        #mousepos % tile_size(18) == 0  TRUE 
        self.tile_x = ((mouse_pos[0]//self.tile_size)*self.tile_size)+self.scroll[0]%self.tile_size
        self.tile_y = ((mouse_pos[1]//self.tile_size)*self.tile_size)+self.scroll[1]%self.tile_size
        
         
        self.selected_tile_rect = pygame.Rect(self.tile_x,self.tile_y,self.tile_size,self.tile_size)
        
        marker_x = pygame.Rect(mouse_pos[0],0,1,self.display.get_height())
        marker_y = pygame.Rect(0,mouse_pos[1],self.display.get_width(),1)

        #mouse x config
        if not self.selected_tile_rect.colliderect(marker_x):
            self.selected_tile_rect.x -= self.tile_size
            
        #mouse y config
        if not self.selected_tile_rect.colliderect(marker_y):
            self.selected_tile_rect.y -= self.tile_size
                
        placeholder_img = self.selected_tile_img.copy()
        placeholder_img.set_alpha(100)
        
        
        self.display.blit(placeholder_img,self.currentTilePos())

    def drawMap(self,map):
        for i in map:
            #we draw it if it can be seen bc we can improve the processing speed
            if (i["img_pos"][0] > 0 and i["img_pos"][0] < self.display.get_width()-self.tile_size) and (i["img_pos"][1] > 0 and i["img_pos"][1] < self.display.get_height()-self.tile_size):
                self.display.blit(i["img"],(i["img_pos"][0],i["img_pos"][1]))
        
        
        
    
