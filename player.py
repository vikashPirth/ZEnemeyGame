from gameObject import GameObject

class Player(GameObject):

    def __init__(self, x, y, width, height, image_path, speed) -> None:
        super().__init__(x, y, width, height, image_path)
        
        self.speed = speed

    # Moving the player character on the screen
    def move(self, direction):
        self.y += (direction * self.speed)
        print(self.y)
    
