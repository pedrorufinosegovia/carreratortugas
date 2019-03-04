import sys

import pygame

class Game():

   corredores = []

   def __init__(self):

       self.__screen = pygame.display.set_mode((640, 480))
       pygame.display.set_caption("Carrera de bichos")
       self.background = pygame.image.load("background.png")
       
       self.runner = pygame.image.load("smallball.png")
        
   def competir(self):
       x = 0
       hayganador = False
       while not hayganador:
           # comprobacion de los eventos
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()

           # Refrescar / renderizar la pantalla
           self.__screen.blit(self.background, (0,0))
           self.__screen.blit(self.runner, (x, 200))
           pygame.display.flip()
           
           x += 3
           if x >= 630:
                hayganador = True
        
       pygame.quit()
       sys.exit()


if __name__ == "__main__":
   pygame.init()
   game = Game()
   game.competir()
