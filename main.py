import sys,pygame,math
import functions as fun
import SideTop as ST
import SideBottom as SB
import Drawing as DW


from pygame.locals import *

pygame.init()


#region displays
WINDOW_SIZE = [1000,700]
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

Dpos = [[0,0],[0,200],[200,0]]
Dsizes =[[200,200],[200,500],[800,700]]
Dscales =[2.1,2,2]

surfaces = []
for i in range(len(Dpos)):
    #display,scaling,rect    
    surfaces.append([pygame.Surface(Dsizes[i]).convert(),pygame.Surface((Dsizes[i][0]/Dscales[i],Dsizes[i][1]/Dscales[i])).convert(),pygame.Rect(Dpos[i][0],Dpos[i][1],Dsizes[i][0],Dsizes[i][1])])

side_top = surfaces[0][1]
side_bottom = surfaces[1][1]
drawing = surfaces[2][1] 
#endregion
mouse_display_pos = any

sidetop = ST.SideTop(surfaces[0][1])
sidebottom = SB.SideBottom(surfaces[1][1])
dw = DW.Drawing(surfaces[2][1])

tile_size = 18
#------------------------------------------------------


while True:
    #region fill displays
    side_top.fill((20, 35, 40))
    side_bottom.fill((20, 35, 40))
    drawing.fill((0,0,0))
    pygame.draw.line(side_top,(100,100,100),(0,side_top.get_height()-1),(side_top.get_width()-1,side_top.get_height()-1))
    #endregion
    
    #mouse positioning-----------------------------------
    mx,my = pygame.mouse.get_pos()
    for i in range(len(surfaces)):
        if surfaces[i][2].collidepoint(mx,my):
            if i == 0:
                mouse_display_pos = "side_top"
            if i == 1:
                mouse_display_pos = "side_bottom"
                my -= 200
            if i == 2:
                mx -= 200
                mouse_display_pos = "drawing"
            mx = int(mx/Dscales[i])
            my = int(my/Dscales[i])
    #-----------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if mouse_display_pos == "side_top":
                    sidebottom.buttons.clear()
                    sidebottom.tiles = sidetop.listClickedvalue([mx,my])
                    sidebottom.setTilesLocation()
                
                if mouse_display_pos == "side_bottom":
                    selected_tile = sidebottom.setClickedValue([mx,my])
                    dw.selected_tile_img = selected_tile["value"]
                    dw.selected_tile_rect = selected_tile["rect"]
                
    #---------------------------------------------------
    if mouse_display_pos =="side_top":
        for i in range(len(sidetop.tilesets)):
            if sidetop.buttons[i]["rect"].collidepoint([mx,my]):
                pygame.draw.rect(sidetop.display,(20,20,20),sidetop.buttons[i]["rect"])
    sidetop.listTilesets([mx,my])
    
    #draw the current selected tile
    if dw.selected_tile_img != None:
        drawing.blit(dw.selected_tile_img,(10,10))
    
    #draw tiles underneath each other    
    sidebottom.drawTiles()
        
    #blit displays---------------------------------------
    for i in range(len(surfaces)):
        screen.blit(surfaces[i][0],Dpos[i])
        surfaces[i][0].blit(pygame.transform.scale(surfaces[i][1],Dsizes[i]),(0,0))
    
   
    pygame.display.update()
    