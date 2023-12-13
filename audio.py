import os
import pygame


class Audio:

    oceanSound = "./Audio/ocean sound"

    def __init__(self) -> None:
        pygame.mixer.init(buffer=10000)
        pygame.mixer.music.set_volume(100)
        print (os.getcwd()) 

    def play_sound(self):
        playing = pygame.mixer.get_busy()
        if not playing:
            sound = pygame.mixer.Sound(self.oceanSound)
            sound.play()
    
    def __del__(self):
        pygame.mixer.quit()