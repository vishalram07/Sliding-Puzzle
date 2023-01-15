from importlib.resources import contents
from re import L
from threading import current_thread
from turtle import window_width
import pygame, random
pygame.init()
WINDOW_WIDTH = 649
WINDOW_HEIGHT = 600
screen  = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Puzzle Game') 
#Frames per Second
FPS = 10
#Object of Class Clock
clock = pygame.time.Clock()
#In Pygame color is represented in tuple
#(RED,BLUE,GREEN)Channels
WHITE = (255,255,255)
BLACK = (0,0,0)
RED  = (255,0,0)
CRIMSON = (220,20,60)
ORANGE = (255,127,0)
#Loading Image 
bg_img = pygame.image.load('Background.jpg')
bg_img_rect = bg_img.get_rect()
bg_img_rect.topleft = (0,0)
bg1 = pygame.image.load('pic.jpg')
bg1_rect = bg1.get_rect()
bg1_rect.topleft = (70,300)
bg2 = pygame.image.load('pic2.jpg')
bg2_rect = bg2.get_rect()
bg2_rect.topleft = (250,300)
bg3 = pygame.image.load('pic3.jpg')
bg3_rect = bg3.get_rect()
bg3_rect.topleft = (450,300)
#Texts in Game
font_title = pygame.font.Font('EvilEmpire.ttf',110)
font1_title = pygame.font.Font('EvilEmpire.ttf',70)
contents_title = pygame.font.Font('Hello Avocado.ttf',40)
level_title = pygame.font.Font('Hello Avocado.ttf',25)
level1 = level_title.render('LEVEL 1',True,CRIMSON,WHITE)
level1_rect = level1.get_rect()
level1_rect.topleft = (99,255)
level2 = level_title.render('LEVEL 2',True,CRIMSON,WHITE)
level2_rect = level1.get_rect()
level2_rect.topleft = (99+180,255)
level3 = level_title.render('LEVEL 3',True,CRIMSON,WHITE)
level3_rect = level3.get_rect()
level3_rect.topleft = (99+180+200,255)
game_title = font_title.render('PUZZLE   GAME',True,CRIMSON,WHITE)
game_title_rect = game_title.get_rect()
game_title_rect.center = (WINDOW_WIDTH // 2,WINDOW_HEIGHT // 2  - 130)
game1_title = font1_title.render('PRESS LEVEL NUMBER',True,CRIMSON,WHITE)
game1_title_rect = game1_title.get_rect()
game1_title_rect.center = (WINDOW_WIDTH // 2 + 15,WINDOW_HEIGHT // 2  + 190)
choose_text = contents_title.render('Choose Your difficulty',True,CRIMSON,WHITE)
choose_rect = choose_text.get_rect()
choose_rect.center = (WINDOW_WIDTH // 2,WINDOW_HEIGHT // 2  - 20)
play_again_text = contents_title.render('PLAY AGAIN?',True,BLACK,WHITE)
play_again_text_rect = play_again_text.get_rect()
play_again_text_rect.center = (WINDOW_WIDTH // 2 ,WINDOW_HEIGHT // 2)
easy_text = contents_title.render("Press 'E' - Easy (3x3)", True, ORANGE,BLACK)
easy_rect = easy_text.get_rect()
easy_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 40)
medium_text = contents_title.render("Press 'M' - Medium (4x4)", True, ORANGE,BLACK)
medium_rect = medium_text.get_rect()
medium_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 90)
hard_text = contents_title.render("Press 'H' - Hard (5x5)", True, ORANGE,BLACK)
hard_rect = hard_text.get_rect()
hard_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 140)
continue_text = contents_title.render('PRESS SPACE',True,BLACK,WHITE)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH // 2,WINDOW_HEIGHT // 2 + 50)
#flags
show_start_screen = True
show_start_screen2 = True
img_selected = None
is_game_over = False
def start_game(mode):
    global cells,cell_width,cell_height,show_start_screen,num_cells
    rows = mode
    cols = mode
    num_cells = rows*cols
    cell_width  = WINDOW_WIDTH // rows
    cell_height = WINDOW_HEIGHT // cols
    cells = []
    rand_indicies = list(range(0,num_cells))
    for i in range(num_cells):
        x = (i%rows)*cell_width
        y = (i//cols)*cell_height
        rect = pygame.Rect(x,y,cell_width,cell_height)
        rand_pos = random.choice(rand_indicies)
        rand_indicies.remove(rand_pos)
        cells.append({'rect':rect , 'border':WHITE,'order' : i, 'pos':rand_pos})
    show_start_screen = False
def image_set(level):
    global show_start_screen2,mbg,mbg_rect
    if level == 1:
        mbg = pygame.image.load('mpic.jpg')
        mbg_rect = mbg.get_rect()
        mbg_rect.topleft = (0,0)
    elif level == 2:
        mbg = pygame.image.load('mpic2.jpg')
        mbg_rect = mbg.get_rect()
        mbg_rect.topleft = (0,0)    
    elif level == 3:
        mbg = pygame.image.load('mpic3.jpeg')
        mbg_rect = mbg.get_rect()
        mbg_rect.topleft = (0,0)    
    show_start_screen2 = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run  = False 
        if is_game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                is_game_over = False
                show_start_screen = True 
                show_start_screen2 = True
        if show_start_screen:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                    start_game(3)
                elif keys[pygame.K_m]:
                    start_game(4)
                elif keys[pygame.K_h]:
                    start_game(5)
        if (show_start_screen == False) and (show_start_screen2 == True):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    image_set(1)
                elif keys[pygame.K_2]:
                    image_set(2)
                elif keys[pygame.K_3]:
                    image_set(3)   
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not is_game_over:
            mouse_pos = pygame.mouse.get_pos()
            for cell in cells:
                rect  = cell['rect']

                if rect.collidepoint(mouse_pos):
                    if not img_selected:
                        img_selected = cell
                        cell['border'] = RED
                    else:
                        current_img = cell
                        #Swapping Images
                        if (current_img['order'] != img_selected['order']):
                            temp = img_selected['pos']
                            cells[img_selected['order']]['pos'] = cells[current_img['order']]['pos']
                            cells[current_img['order']]['pos'] = temp
                            cells[img_selected['order']]['border'] = WHITE
                            img_selected = None
                        #Check if puzzle is Solved    
                        is_game_over = True
                        for cell in cells:
                            if cell['order'] != cell['pos']:
                                is_game_over = False
                        if(is_game_over):
                            print("GAME OVER!!")        
    if show_start_screen:
        screen.fill(BLACK)
        screen.blit(bg_img,bg_img_rect)
        screen.blit(game_title,game_title_rect)
        screen.blit(choose_text,choose_rect)
        screen.blit(easy_text,easy_rect)
        screen.blit(medium_text,medium_rect)
        screen.blit(hard_text,hard_rect)
    elif show_start_screen2:
        screen.fill(BLACK)
        screen.blit(bg_img,bg_img_rect)
        screen.blit(game_title,game_title_rect)
        screen.blit(bg1,bg1_rect)
        screen.blit(bg2,bg2_rect)
        screen.blit(bg3,bg3_rect)
        screen.blit(level1,level1_rect)
        screen.blit(level2,level2_rect)
        screen.blit(level3,level3_rect)
        screen.blit(game1_title,game1_title_rect)
    else:
        screen.fill(WHITE)
        #blit is used to portrate contents on to the surface
        if not is_game_over:
            for i,val in enumerate(cells):
                pos = cells[i]['pos']
                img_area = pygame.Rect(cells[pos]['rect'].x,cells[pos]['rect'].y,cell_width,cell_height)
                screen.blit(mbg,cells[i]['rect'],img_area)
                pygame.draw.rect(screen,cells[i]['border'],cells[i]['rect'],1)
        else:
            screen.blit(mbg,mbg_rect)
            screen.blit(play_again_text,play_again_text_rect)
            screen.blit(continue_text,continue_text_rect)
    pygame.display.update()
    #setting fps of program to max of FPS per second        
    clock.tick(FPS)        
pygame.quit()

