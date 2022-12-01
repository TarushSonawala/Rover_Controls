
import sys

import socket

import pygame
from pygame.locals import *
import sys

s = socket.socket()

print("Socket successfully created")

port = 80

s.bind(("192.168.46.35", 27339))
print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")
c, addr = s.accept()
print('Got connection from', addr)


def dataPacket(data, data1, data2, data3, data4, data5):
    sendData("m" + "s" + data + "f" + data1 +
             "n" + data2 + data3 + data4 + data5)


def sendData(me):

    while True:

        c.send(me.encode())
        return


pygame.init()
display = pygame.display.set_mode((300, 300))

while (1):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("Key A has been pressed")
                sendData(me='a')

                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print("Key A has been released")
                sendData(me='ar')

                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                print("Key B has been pressed")
                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_b:
                print("Key B has been released")
                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print("Key S has been pressed")
                sendData(me='s')

                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                print("Key S has been released")
                sendData(me='sr')

                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print("Key D has been pressed")
                sendData(me='d')

                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                print("Key D has been released")
                sendData(me='dr')

                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("Key W has been pressed")
                sendData(me='w')
                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                print("Key W has been released")
                sendData(me='wr')

                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                print("Key Z has been pressed")
                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                print("Key Z has been released")
                # dataPacket(data='rl',data1='0',data2='0',data3='0',data4='0',data5='0')