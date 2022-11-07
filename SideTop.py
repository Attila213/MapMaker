import functions as fun
import pygame
import font
class SideTop:
    def __init__(self,display):
        self.display = display
        self.font = font.Font("assets/font/small_font.png",(180,180,180))
        self.tilesets = fun.image_loader("assets/images/tilesets/")
        self.current_tileset = []
        
        #fill buttons
        self.buttons = []
        self.tiles = []
        for i in range(len(self.tilesets)):
            self.buttons.append({"value":str(self.tilesets[i][0]),"rect":pygame.Rect(0,4+(i*10),self.display.get_width(),10)})

    def listTilesets(self,mouse_pos):
        for i in range(len(self.tilesets)):
            self.font.render(str(self.tilesets[i][0]),self.display,(5,5+(10*i)),None)

    def listClickedvalue(self,mouse_pos):
        for i in range(len(self.tilesets)):
            if self.buttons[i]["rect"].collidepoint(mouse_pos):
                self.current_tileset = self.buttons[i]["value"]

        for i in self.tilesets:
            if i[0] == self.current_tileset:
                tiles = fun.cut_img(i[1])
                return tiles











