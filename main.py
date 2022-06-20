import pygame,sys
from pygame.locals import * 
from coin import Coin 

pygame.init()
pygame.font.init() 
FONT = pygame.font.SysFont("Helvetica",30)

size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#define speed variables for the player
speed_x = 0
speed_y = 0

player = pygame.Rect(400,300,11,11)
score = 0 

WHITE = (255,255,255,255)
BLACK = (0,0,0,255)
YELLOW = (255,215,0)
RED = (255,0,0,255)

score = 0
coins = [] 
for i in range(100):
  coins.append(Coin())
#add movement functions
def move_up():
  global speed_y 
  speed_y += -0.1

def move_down():
  global speed_y 
  speed_y += 0.1

def move_left():
  global speed_x 
  speed_x += -0.1

def move_right():
  global speed_x 
  speed_x += 0.1

def movement_loop():
  global speed_x,speed_y 
  player.centerx += speed_x 
  player.centery += speed_y

def collision_loop():
  global coins,player 
  global score
  for coin in coins:
    if player.colliderect(coin.rect) and not coin.isHidden:
      coin.isHidden = True
      score += 1
      print(score)


def render_coin_loop():
  global coins, screen
  for coin in coins:
    if not coin.isHidden: 
      screen.fill(YELLOW,coin.getRect())

def main():
  global speed_x,speed_y
  global FONt, score
  while True:
    clock.tick(60)
    
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      # if event.type == KEYDOWN:
      #   if event.key == K_DOWN:
      #     move_down()
      #   elif event.key == K_UP: 
      #     move_up() 
      #   elif event.key == K_LEFT:
      #     move_left() 
      #   elif event.key == K_RIGHT:
      #     move_right()

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
      move_up()
    if keys[K_DOWN]:
      move_down()
    if keys[K_LEFT]:
      move_left()
    if keys[K_RIGHT]:
      move_right()

    collision_loop()
    movement_loop()
    #fill screen with black
    screen.fill(BLACK)
    
    render_coin_loop()
    
    #render player
    screen.fill(WHITE,player)
    seconds = int(pygame.time.get_ticks()//1000)
    screen.blit(
      FONT.render("TIME: " + str(seconds),True,RED),
      (640,20)
    )
    screen.blit(
      FONT.render("Score: " + str(score),True,RED),
      (20,20)
    )
    pygame.display.flip()

if __name__ == "__main__":
  main()