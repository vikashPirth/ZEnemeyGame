import pygame

class Game:

    def __init__(self) -> None:
        self.width = 800
        self.height = 800
        self.white_color = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        background_image = pygame.image.load('assets/background.png')
        treasure_image =  pygame.image.load('assets/treasure.png')

        self.background = pygame.transform.scale(background_image, (self.width, self.height))
        self.treasure = pygame.transform.scale(treasure_image, (50, 50))


    def draw_objects(self,):
        self.game_window.fill(self.white_color)
        self.game_window.blit(self.background, (0,0))
        self.game_window.blit(self.treasure, (375,50))
    
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