import pygame

pygame.mixer.init()
pygame.mixer.music.load("test.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()