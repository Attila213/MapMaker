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
        


    def drawTileHover(self,mouse_pos):
        
        # Hogy kéne úgy helyeztetni a rectet hogy mindig az egérhez igazodjon de mindig 18-al osztható legyen + ami a scroll-ból marad
              
        self.tile_x = ((mouse_pos[0]//self.tile_size)*self.tile_size)-(self.scroll[0]%18)
        self.tile_y = ((mouse_pos[1]//self.tile_size)*self.tile_size)-(self.scroll[1]%18)
        
        
        
        
        
       
           
        self.selected_tile_rect = pygame.Rect(self.tile_x,self.tile_y,self.tile_size,self.tile_size)

        pygame.draw.rect(self.display,(255,0,0),self.selected_tile_rect)
        
        placeholder_img = self.selected_tile_img.copy()
        placeholder_img.set_alpha(100)
        self.display.blit(placeholder_img,(self.tile_x+self.offset[str(self.offset_index)]["x"],self.tile_y+self.offset[str(self.offset_index)]["y"]))
        
    
        
        
    