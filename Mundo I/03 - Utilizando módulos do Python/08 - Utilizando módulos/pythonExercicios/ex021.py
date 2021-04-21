# DESAFIO 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init() #Inicializa
pygame.mixer.music.load('ex021.mp3') #Seleciona o arquivo
pygame.mixer.music.play() #Toca a música
pygame.event.wait() #Aguarda o evento encerrar