import pygame 
import random 

class Coin:
  def __init__(self):
    x = random.randint(0,800)
    y = random.randint(0,600)
    self.rect = pygame.Rect(x,y,4,4)
    self.isHidden = False 

  def getRect(self):
    return self.rect

def getHidden(self):
  return self.isHidden