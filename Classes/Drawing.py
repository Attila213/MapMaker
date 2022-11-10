import assets.editors.functions as fun
import pygame,json
import assets.editors.font as font



class Drawing:
    def __init__(self,display,tilesize):
        self.display = display
        self.selected_tile_rect = None
        self.selected_tile_img = None
        self.tile_size = tilesize
        
        self.scroll = [0,0]
        
        self.offset = None
        self.offset_name = None
        self.offset_index = None
        
        self.tile_x = None
        self.tile_y = None
        
        # arr = fun.loadJson("../assets/images/offsets/grass")


    def drawTileHover(self,mouse_pos):
        
        self.tile_x = (mouse_pos[0]//self.tile_size)*self.tile_size
        self.tile_y = (mouse_pos[1]//self.tile_size)*self.tile_size
        
        pygame.draw.rect(self.display,(255,0,0),pygame.Rect(self.tile_x,self.tile_y,self.tile_size,self.tile_size))
        self.display.blit(self.selected_tile_img,(self.tile_x+self.offset[str(self.offset_index)]["x"],self.tile_y+self.offset[str(self.offset_index)]["y"]))
        
    
        
        
    