import pygame
from gameObject import GameObject
from player import Player

class Game:

    def __init__(self) -> None:
        self.width = 800
        self.height = 800
        self.white_color = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.background = GameObject(0, 0, self.width, self.height,'assets/background.png')
        self.treasure = GameObject(375, 50, 50, 50,'assets/treasure.png')

        self.player = Player(375, 700, 50, 50, 'assets/player.png', 10)
    

    def draw_objects(self,):
        self.game_window.fill(self.white_color)
        self.game_window.blit(self.background.image, (self.background.x,self.background.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x,self.treasure.y))
    
    
    def run_game_loop(self):
        while True:
            # handle events 
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
            
            self.draw_objects()

            pygame.display.update()

            self.clock.tick(60)