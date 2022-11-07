import functions as fun
import pygame
import font

class SideBottom:
    def __init__(self,display):
        self.display = display
        self.buttons = []
        self.tiles = []

    def setTilesLocation(self):
        last_pos = any
        for i in range(len(self.tiles)):
            if i == 0:
                last_pos = pygame.Rect(5,5+(i*20),self.tiles[i].get_width(),self.tiles[i].get_height())
                self.buttons.append({"value":self.tiles[i],"rect":last_pos})
                
            else:
                last_pos = pygame.Rect(5,last_pos.bottom+4,self.tiles[i].get_width(),self.tiles[i].get_height())
                self.buttons.append({"value":self.tiles[i],"rect":last_pos})
    
    def drawTiles(self):
        for i in self.buttons:
            self.display.blit(i["value"],(i["rect"].x,i["rect"].y))

    def setClickedValue(self,mouse_pos):
        value = any
        for i in self.buttons:
            if i["rect"].collidepoint(mouse_pos):
                value = i
                
        return value

    