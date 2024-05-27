from pygame import *
from utils import GameSprite, Player, Ball
from variables import *

init()

window = display.set_mode(GAME_DIMENSIONS)
display.set_caption("Пинг понг")
window.fill((255, 255, 255))

bg = transform.scale(image.load('assets/bg.jpeg'), (window.get_width(), window.get_height()))
player = Player(window.get_width() / 6)
player1 = Player(window.get_width() - window.get_width() / 6)
players = [player, player1]
ball = Ball()

#pause menu
menu_bg = transform.scale(image.load('assets/pause_bg.jpg'), (window.get_width() - 20, window.get_height() - 20))
menu_bg.set_alpha(120)

play_button = GameSprite('pause_button_play.jpeg', window.get_width() / 2, window.get_height() / 4, 100, 50)
reset_button = GameSprite('pause_button_reset.png', window.get_width() / 2, play_button.rect.y + play_button.height + 10, 100, 50)
settings_button = GameSprite('pause_button_reset.png', window.get_width() / 2, reset_button.rect.y + reset_button.height + 10, 100, 50)

offset = 50

while updateFramerate:
    for e in event.get():
        if e.type == QUIT: updateFramerate = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            #ААААААААААААААА ОФФСЕТЫ
            if play_button.rect.collidepoint(x + (play_button.width / 2), y + (play_button.height / 2)) and paused:
                paused = False
            if reset_button.rect.collidepoint(x + (reset_button.width / 2), y + (reset_button.height / 2)) and paused:
                ball.direction.counter = 0
                ball.speed = 1
                paused = False
            #if settings_button.rect.collidepoint(x + (settings_button.width / 2), y + (settings_button.height / 2)) and paused:

    counterText = font.SysFont("Arial", 20).render(f"Очки:{ball.direction.counter}", False, (255, 255, 255))
    
    window.blits(((bg, (0, 0)), (counterText, (0, 0))))
    ball.render(window)
    player.render(window)
    player1.render(window)

    keys = key.get_pressed()

    #pause
    if paused:
        window.blit(menu_bg, (10, 10))

        play_button.render(window, True)
        reset_button.render(window, True)
        settings_button.render(window, True)

    if keys[K_SPACE]: paused = not paused
        
    #TODO: make level system
    match level:
        case 2: mult = 1.2
        case 3: mult = 1.4
        case 4: mult = 1.6
        case 5: mult = 1.8

    if not paused:
        ball.direction.update(players)
        if not botplay:
            flipY = ""
            if ball.direction.counter >= 10:
                offset = 50 - window.get_height()
                flipY = "-"
                
            mousePos = eval(f"{flipY}mouse.get_pos()[1] - offset")
            if mouse.get_pos()[1] - player1.rect.height / 3 >= 0:
                player1.rect.y = player.rect.y = mousePos
        else:
            player1.rect.y = player.rect.y = ball.rect.y - player.height / 3

    clock.tick(FPS)
    display.update()