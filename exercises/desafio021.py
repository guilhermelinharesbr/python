"""Faça um programa em Python que abra e 
reproduza o áudio de um arquivo MP3."""

#Primeira forma
"""Dependendo da máquina é preciso instalar o pygame via pip. 
pip install pygame.
O pygame tem funcionalidade para carregar, sons, imagens, vídeos.
Obs: Estou trabalhando 3.14.4 em uma máquina Windows 11, porém
a biblioteca pygame não tem compatibilidade ainda com essa versão do python,
por isso foi preciso instalar a versão 3.12.10 do Python."""
import pygame
import time

#Iniciando o pygame:
pygame.init()

arquivo = r'C:\Users\guilherme.linhares\Documents\GitHub\python\exercises\desafio021.mp3'

pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)  # volume máximo (0.0 a 1.0)
print("▶ Tocando áudio...")

# Mantém o programa vivo enquanto o áudio toca
while pygame.mixer.music.get_busy():
    time.sleep(0.5)

print("✅ Áudio finalizado!")
