'''
Faça um programa em Python que abra e reproduza o áudio de arquivo MP3.
'''

import pygame
pygame.init() #INICIANDO O PYGAME
pygame.mixer.music.load('../funk.mp3')
pygame.mixer.music.play()
pygame.event.wait()
