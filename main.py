# Pygame game template

import pygame
import sys
import random

# Color constants (RBG)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
PURPLE = (157, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (150, 75, 0)

# Game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Window title (caption)
# Update the window title as needed
TITLE = 'Sound Effect'
ICON = pygame.image.load('c:\Icons\download.png')
ICON.set_colorkey(WHITE)
# Frame rate (frames per second)
FPS = 60

TEXT_FONT = 'c:\Font\Tektur-VariableFont_wdth,wght.ttf'
SOUND_EFFECT1 = "c:\Sound effects\oblox-death-sound.ogg"
SOUND_EFFECT2 = 'c:\Sound effects\doom-death-sound-effect.ogg'
SOUND_EFFECT3 = 'c:\Sound effects\eep.ogg'
BGM1 = "c:\Sound effects\omic-cat.ogg"

def init_game():
    pygame.init()
    pygame.font.init
    pygame.mixer.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(ICON)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_text(screen, text, font_size, font_name, color, pos, italic=False, bold=False):
    if font_name:
        font = pygame.font.Font(font_name, font_size)
    else:
        font = pygame.font.Font(None, font_size)

    font.set_bold(bold)
    font.set_italic(italic)

    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (pos))

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here

    oof_sound = pygame.mixer.Sound(SOUND_EFFECT1)
    doom_sound = pygame.mixer.Sound(SOUND_EFFECT2)
    beep_sound = pygame.mixer.Sound(SOUND_EFFECT3)
    bgm_cat = pygame.mixer.Sound(BGM1)



    running = True
    while running:
        running = handle_events()
        screen.fill(GREEN) # Use color from config
        
        key = pygame.key.get_pressed()
        if key[pygame.K_1]:
            pygame.mixer.Sound.play(oof_sound)
        if key[pygame.K_2]:
            pygame.mixer.Sound.play(doom_sound)
        if key[pygame.K_3]:
            pygame.mixer.Sound.play(beep_sound)
        if key[pygame.K_SPACE]:
            pygame.mixer.Sound.play(bgm_cat)
        if key[pygame.K_p]:
            pygame.mixer.Sound.stop(bgm_cat)
        
        




        pygame.display.flip()
        # Limit the frame rate to the specified frames per second
        clock.tick(FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



