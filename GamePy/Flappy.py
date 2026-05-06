import pygame
import random

pygame.init()
    # set up the game window

window_width= 500
window_height= 800
window= pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Flappy Bird")

#Game Variables
gravity=0.25
bird_movement=0
score=0

    #Load images
background_img("mypic1.png")
bird_img=pygame.image.load("bird.png")
pipe_img=pygame.image.load("pipe.png")

      #Create bird object

bird_rect=bird_img.get_rect(center=(100,window_height//2))

      #Create pipe objects
       
pipe_list=[]
SPAWNPIPE=pygame.USEREVENT
pygame,time.set_timer(SPAWNPIPE, 1200)
pipe_heights=[300,400,500]

      #Game loop
running=True 
while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN:
                  if event.key==pygame.K_SPACE:
                    bird_movement=0
                    bird_movement-=6

                if event.type==SPAWNPIPE:
                    random_pipe_pos=random.choice(pipe_heights)
new_pipe= pipe_img.get_rect(midtop=(window_width+100,random_pipe_pos))
pipe_list.append(new_pipe)
      #Update bird movement
bird_movement+=gravity
bird_rect.cenetry+=bird_movement

      #Draw background
window.blit(background_img,(0,0))
      #Draw Bird
window.blit(bird_img,bird_rect)

      #DRAW Pipes
pipe_list=move_pipes(pipe_list)
draw_pipes(pipe_list)

        #Check collision
if check_collision(pipe_list,bird_rect):
              running= False

        #Check if bird is off the screen
if bird_rect.cenetry >=window_height:
             running= False

             pygame.display.update()
pygame.quit()