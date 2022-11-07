import functions as fun
import pygame
import font

class Drawing:
    def __init__(self,display):
        self.display = display
        self.selected_tile_rect = None
        self.selected_tile_img = None
        
        self.scroll = [0,0]
        
        
    