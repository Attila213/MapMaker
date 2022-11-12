import sys,pygame,math
import assets.editors.functions as fun
import Classes.SideTop as ST
import Classes.SideBottom as SB
import Classes.Drawing as DW
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

def scrollRect(left,top,width,height):
    return pygame.Rect(left+dw.scroll[0],top+dw.scroll[1],width,height)

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

map = []

tile_size = 18
scroll_speed =1

hold_left = False
hold_right = False


sidetop = ST.SideTop(surfaces[0][1])
sidebottom = SB.SideBottom(surfaces[1][1])
dw = DW.Drawing(surfaces[2][1],tile_size)

frame = 0
while True:
    frame += 1

    #region fill displays
    side_top.fill((20, 35, 40))
    side_bottom.fill((20, 35, 40))
    drawing.fill((0,0,0))
    pygame.draw.line(side_top,(100,100,100),(0,side_top.get_height()-1),(side_top.get_width()-1,side_top.get_height()-1))
    #endregion

    #region mouse positioning
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
            my = (my/Dscales[i])
    #endregion
    
    #region events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                hold_left = True
            if event.button == 3:
                hold_right = True                                 
                                    
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                hold_left = False
                if mouse_display_pos == "side_top":
                    sidebottom.buttons.clear()
                    tiles = sidetop.listClickedvalue([mx,my])
                    sidebottom.tiles = tiles["tiles"]
                    dw.offset_name = tiles["name"]
                    sidebottom.setTilesLocation()

                if mouse_display_pos == "side_bottom" and sidebottom.setClickedValue([mx,my]) != any:
                    selected_tile = sidebottom.setClickedValue([mx,my])
                    dw.selected_tile_img = selected_tile["value"]
                    dw.selected_tile_rect = selected_tile["rect"]
                    dw.offset_index = selected_tile["index"]
                    dw.offset = fun.loadJson("assets/images/offsets/"+dw.offset_name)
            if event.button == 3:
                hold_right = False
    #scrolling
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        dw.scroll[1]+=scroll_speed            
        for i in map:
            i["rect"].y += scroll_speed
            i["img_pos"][1] += scroll_speed
    if keys[K_s]:
        dw.scroll[1]-=scroll_speed
        for i in map:
            i["rect"].y -= scroll_speed
            i["img_pos"][1] -= scroll_speed         
    if keys[K_a]:
        dw.scroll[0]+=scroll_speed
        for i in map:
            i["rect"].x += scroll_speed 
            i["img_pos"][0] += scroll_speed          
    if keys[K_d]:
        dw.scroll[0]-=scroll_speed
        for i in map:
            i["rect"].x -= scroll_speed
            i["img_pos"][0] -= scroll_speed
    
    #endregion
    
    if mouse_display_pos=="drawing":
        #draw the marker
        if dw.selected_tile_img != None:
            dw.drawTileHover([mx,my])
            
        
        #check if the tile exists in the array
        found = False
        founded_tile = None
        for i in map:
            # if i["rect"] == dw.selected_tile_rect and i["layer"] == dw.layer:
            if i["rect"] == dw.selected_tile_rect and i["layer"] == dw.layer:
                found = True
                founded_tile = i
        
        #if the left click is being held
        if hold_left:
            #if it does then append
            if not found:
                map.append(
                    {"rect":dw.selected_tile_rect,
                     "img_pos":dw.currentTilePos(),
                     "img":dw.selected_tile_img,
                     "layer":dw.layer
                    })

        if hold_right and found:
            map.remove(founded_tile)
            
            
    if mouse_display_pos =="side_top":
        for i in range(len(sidetop.tilesets)):
            if sidetop.buttons[i]["rect"].collidepoint([mx,my]):
                pygame.draw.rect(sidetop.display,(20,20,20),sidetop.buttons[i]["rect"])
    
    #draw the current selected tile
    if dw.selected_tile_img != None :
        drawing.blit(dw.selected_tile_img,(10,10))

    sidetop.listTilesets([mx,my]) 
    sidebottom.drawTiles()
    dw.drawMap(map)
    
    #region draw displays
    for i in range(len(surfaces)):
        screen.blit(surfaces[i][0],Dpos[i])
        surfaces[i][0].blit(pygame.transform.scale(surfaces[i][1],Dsizes[i]),(0,0))
    #endregion
    clock.tick(300)
    pygame.display.update()
