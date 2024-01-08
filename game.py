import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy

class Game:

    def __init__(self) -> None:
        self.width = 800
        self.height = 800
        self.white_color = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.background = GameObject(0, 0, self.width, self.height,'assets/background.png')
        self.treasure = GameObject(375, 40, 40, 40,'assets/treasure.png')
        
        self.level = 1.0
        self.reset_map()

    def reset_map(self):
        self.player = Player(375, 700, 40, 40, 'assets/player.png', 5)
        speed = 3 + (self.level * 3)

        if self.level >= 4.0:
            self.enemies =[Enemy(0, 450, 40, 40, 'assets/enemy.png',speed),
                       Enemy(250, 300, 40, 40, 'assets/enemy.png',speed),
                       Enemy(0, 150, 40, 40, 'assets/enemy.png',speed)
            ]
        elif self.level >=2.0:
            self.enemies =[Enemy(0, 450, 40, 40, 'assets/enemy.png',speed),
                       Enemy(0, 150, 40, 40, 'assets/enemy.png',speed)
            ]
        else:
            self.enemies =[Enemy(0, 450, 40, 40, 'assets/enemy.png',speed)]



    def draw_objects(self,):
        self.game_window.fill(self.white_color)
        self.game_window.blit(self.background.image, (self.background.x,self.background.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x,self.treasure.y))
       
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
    

    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies:
            enemy.move(self.width)
    

    def check_if_colideded(self):
        for enemy in self.enemies:
            if self.detect_collission(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collission(self.player, self.treasure):
            self.level+=0.5
            return True
        return False
    
    def detect_collission(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        if object_1.x > (object_2.x + object_2.width):
            return False 
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        return True

    def run_game_loop(self):
        player_direction = 0
        while True:
            # handle events 
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key  == pygame.K_DOWN:
                        player_direction = 0
            

            self.move_objects(player_direction)
            
            self.draw_objects()
            
            pygame.display.update()

            if self.check_if_colideded():
                self.reset_map()

            self.clock.tick(60)