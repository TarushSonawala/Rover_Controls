import sys

import socket

import pygame
from pygame.locals import *
import sys

s = socket.socket()

print("Socket successfully created")

port = 5005

s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")
c, addr = s.accept()
print('Got connection from', addr)


def dataPacket(data, data1, data2, data3, data4, data5):
    sendData("m" + "s" + data + "f" + data1 +"n" + data2 + data3 + data4 + data5)


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
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_0:
        #         print("Key 0 has been pressed")
        #         sendData(me='0')
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_0:
        #         print("Key 0 has been released")
        #         sendData(me='0')

                # dataPacket(data='2', data1='0', data2='0',
                #            data3='0', data4='0', data5='0')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("Key 1 has been pressed")
                sendData(me='1')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                print("Key 1 has been released")
                sendData(me='0')

                # dataPacket(data='rl', data1='2', data2='0',
                #            data3='0', data4='0', data5='0')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                print("Key 2 has been pressed")
                sendData(me='2')

                # dataPacket(data='rl', data1='0', data2='0',
                #            data3='0', data4='0', data5='0')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_2:
                print("Key 2 has been released")
                sendData(me='0')

                # dataPacket(data='rl', data1='0', data2='0',
                #            data3='0', data4='0', data5='0')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                print("Key 3 has been pressed")
                sendData(me='3')

                # dataPacket(data='rl', data1='0', data2='0',
                #            data3='0', data4='0', data5='0')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_3:
                print("Key 3 has been released")
                sendData(me='0')

        #         dataPacket(data='rl', data1='0', data2='0',
        #                    data3='0', data4='0', data5='0')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
                print("Key 4 has been pressed")
                sendData(me='4')

                # dataPacket(data='rl', data1='0', data2='0',
                #            data3='0', data4='0', data5='0')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_4:
                print("Key 4 has been released")
                sendData(me='0')
                
        #         dataPacket(data='rl', data1='0', data2='0',
        #                    data3='0', data4='0', data5='0')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_5:
                print("Key 5 has been pressed")
                sendData(me='5')
                
                # dataPacket(data='rl', data1='0', data2='0',
                #            data3='0', data4='0', data5='0')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_5:
                print("Key 5 has been released")
                sendData(me='0')
                
                # dataPacket(data='rl', data1='0', data2='0',
                #            data3='0', data4='0', data5='0')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_6:
                print("Key 6 has been pressed")
                sendData(me='6')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_6:
                print("Key 6 has been released")
                sendData(me='0')  
                              
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_7:
                print("Key 7 has been pressed")
                sendData(me='7')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_7:
                print("Key 7 has been released")
                sendData(me='0') 
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_8:
                print("Key 8 has been pressed")
                sendData(me='8')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_8:
                print("Key 8 has been released")
                sendData(me='0') 
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_9:
                print("Key 9 has been pressed")
                sendData(me='9')     
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_9:
                print("Key 9 has been released")
                sendData(me='0')                                  
