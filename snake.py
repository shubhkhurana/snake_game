import pygame
import random
from pygame.constants import KEYDOWN
pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
screen_width =1200
screen_height = 500
font = pygame.font.SysFont(None ,55)

gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("sanpon_ki_nagri")
pygame.display.update()
def text_score(text,color,x,y):
        screen_text = font.render(text,True,color)
        gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow,color,snk_list,snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gameWindow, color ,[
                        x, y, snake_size, snake_size])

def gameloop():
    snake_x = 45
    snake_y = 55
    snake_size = 10
    exit_game = False
    game_over = False
    fps = 60
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, 1200/2)
    food_y = random.randint(20, 500/2)
    clock = pygame.time.Clock()
    score = 0
    init_velocity = 3
    
    snk_list = []
    snk_length = 1
   

   

    # game loop
    while not exit_game:
 
        if game_over:
            gameWindow.fill(white)
            text_score("gameover! Press enter to continue",red,300,200)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
        


            snake_x += velocity_x
            snake_y += velocity_y


            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score +=1
                # print("score:",score*10)
                food_x = random.randint(20, 1200/2)
                food_y = random.randint(20, 500/2)
                snk_length +=5

            gameWindow.fill(white)
            text_score("score:"+str(score*10),red,5,5)
            pygame.draw.rect(gameWindow ,red,[food_x, food_y, snake_size,snake_size])
        
            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over =True
                print("gameover")
            plot_snake(gameWindow,black,snk_list,snake_size) 
        
       



        pygame.display.update()
        clock.tick(fps)
    
    pygame.quit()
    quit()

gameloop()
