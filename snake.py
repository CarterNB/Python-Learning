import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,255,0)
yellow=(255,255,102)

gameOver = False
gameClose = False

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("SNAKE")

clock = pygame.time.Clock()

snake_speed = 30
snake_block = 10

font = pygame.font.SysFont("bahnschrift",25)
scoreFont=pygame.font.SysFont("bahnschrift",25)

def score(score):
    value = scoreFont.render("Your Score: "+str(score),True,red)
    dis.blit(value,[dis_width-300, 0])

def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])

def message(msg, colour):
    note = font.render(msg, True, colour)
    dis.blit(note, [0, 0])


def gameLoop():
    gameOver = False
    gameClose = False
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1C = 0
    y1C = 0

    snake_list=[]
    length=1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
    while not gameOver:
        while gameClose:
            dis.fill(white)
            message("YOU LOST! PRESS Q TO QUIT OR C TO PLAY AGAIN.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1C = -snake_block
                    y1C = 0
                elif event.key == pygame.K_RIGHT:
                    x1C = snake_block
                    y1C = 0
                elif event.key == pygame.K_UP:
                    x1C = 0
                    y1C = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1C = 0
                    y1C = snake_block
        if x1 >= dis_width or x1 <= 0 or y1 >= dis_height or y1 <= 0:
            gameClose = True

        x1 += x1C
        y1 += y1C
        dis.fill(white)
        pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block])
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list)>length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_Head:
                gameClose=True
        snake(snake_block,snake_list)
        score(length-1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("YUM")
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            length+=1

        clock.tick(snake_speed)

    pygame.display.update()
    time.sleep(1)
    pygame.quit()


gameLoop()
