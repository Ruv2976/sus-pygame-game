from pygame import *
import variables

window_width, window_height = variables.GAME_DIMENSIONS

counter = 0
mult = 1

class GameSprite(sprite.Sprite):
    def __init__(self, skin, x, y, width, height, speed=1) -> None:
        super().__init__()
        self.image = transform.scale(image.load(f'assets/{skin}'), (width, height))
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = Direction(self)

    def render(self, window:Surface, usingOffsets=False): 
        if usingOffsets:
            window.blit(self.image, (self.rect.x - (self.width / 2), self.rect.y - (self.height / 2)))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def __init__(self) -> None: super().__init__('images.jpeg', window_width / 2, window_height / 2, 50, 50, 1)

class Player(GameSprite):
    def __init__(self, x) -> None: super().__init__('rect.png', x, window_height / 2, 30, window_height / 4, 1)

class Direction:
    def __init__(self, obj:GameSprite) -> None:
        self.obj = obj
        self.xOp = "-"
        self.yOp = "+"
        self.counter = 0

    def update(self, targets:list[GameSprite]):
        if self.obj.rect.y >= window_height - 50: self.yOp = "-"
        if self.obj.rect.y <= 0: self.yOp = "+"

        for target in targets:
            if sprite.collide_rect(self.obj, target): 
                """if self.yOp == "-": self.yOp = "+"
                else: self.yOp = "-"

                print(self.yOp)"""

                if self.xOp == "-": self.xOp = "+"
                else: self.xOp = "-"

                self.obj.speed += 0.2 * variables.mult

                self.counter += 1
        
        exec(f"self.obj.rect.x {self.xOp}= 1 * self.obj.speed")
        exec(f"self.obj.rect.y {self.yOp}= 1 * self.obj.speed")