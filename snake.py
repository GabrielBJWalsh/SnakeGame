import pygame
import time
import random
pygame.init()
count=0
#==================DISPLAY STUFF======================
count=0
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
FPS=15
block_size =10

display_width=1000
display_height=600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('snake')

clock=pygame.time.Clock()
clock=pygame.time.Clock()
font= pygame.font.SysFont(None,25)

#===========================SNAKE==========================================

def snake(block_size,snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])



#=========================MESSAGE============================================
def mesage_to_screen(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text, [display_width/2,display_height/2])






def gameLoop():
#======================CHANGE VARIABLES============================
    pygame.display.update()

    gameExit=False
    gameOver = False

    lead_x=display_width/2
    lead_y=display_height/2

    lead_x_change=0
    lead_y_change=0
    snakeList=[]
    snakeLenth=1


    #applex= round(random.randrange(0,display_width-block_size)/10.0*10.0)
    #appley= round(random.randrange(0,display_height-block_size)/10.0*10.0)
    applex= random.randrange(0,display_width-block_size,10)
    appley= random.randrange(0,display_height-block_size,10)
#========================GAME LOOP=================================

    while not gameExit:

# =======================GAME OVER==================================
        while gameOver== True:
            gameDisplay.fill(white)
            mesage_to_screen("Game over press C to play again or Q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_q:
                        gameExit= True
                        gameOver= False
                    if event.key==pygame.K_c:
                        gameLoop()

# =======================MAIN GAME=================================
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit= True
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    lead_x_change+=block_size
                    lead_y_change=0
                elif event.key==pygame.K_LEFT:
                    lead_x_change-= block_size
                    lead_y_change=0
                elif event.key==pygame.K_DOWN:
                    lead_y_change+=block_size
                    lead_x_change=0
                elif event.key==pygame.K_UP:
                    lead_y_change-= block_size
                    lead_x_change=0
            """if event.type== pygame.KEYUP:
                if event.key== pygame.K_LEFT or event.key==pygame.K_RIGHT:
        
                    lead_x_change=0"""

        if lead_x>=display_width or lead_x<0 or lead_y>= display_height or lead_y<0:
            gameOver=True

        lead_x+= lead_x_change
        lead_y+=lead_y_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,red,[applex,appley,block_size,block_size])


        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList)>snakeLenth:
            del snakeList[0]
        for seg in snakeList[:-1]:
            if seg == snakeHead:
                gameOver=True

        snake(block_size,snakeList)
       # pygame.draw.rect(gameDisplay,green,[lead_x,lead_y,10,10])
        #pygame.draw.rect(gameDisplay,red,[400,300,10,10])
        #gameDisplay.fill(red, rect=[200,200,50,50])
#======================OM NOM NOM=======================================
        pygame.display.update()

        if lead_x==applex and lead_y== appley:
            applex= random.randrange(0,display_width-block_size,10)
            appley= random.randrange(0,display_height-block_size,10)
            snakeLenth+=1

            
            print("om nom nom")

        clock.tick(FPS)

    print(event)

gameLoop()
#mesage_to_screen("you lose",red)
#pygame.display.update()
#time.sleep(2)
pygame.quit()
quit()
