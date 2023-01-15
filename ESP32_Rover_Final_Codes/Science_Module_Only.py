import sys

import socket

import pygame
from pygame.locals import *
import sys

s = socket.socket()

print("Socket successfully created")


# s.bind(('10.0.0.7', port))
# print("socket binded to %s" % (port))
# s.listen(5)
# print("socket is listening")
# c, addr = s.accept()
# print('Got connection from', addr)
server = "10.0.0.8"
port = 5005
addr = (server, port)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client.connect(addr)
me = '0'


class TextPrint:

    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 30)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (192, 192, 192))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 20

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 20


def sendData(me):

    while True:

        a = me.encode()
        client.sendto(a,(addr))
        return


def dataPacket(data, data1, data2, data3, data4, data5):
    sendData("m" + "s" + data + "f" + data1 +
             "n" + data2 + data3 + data4 + data5)

# def sendData(me):

#     while True:

#         c.send(me.encode())
#         return

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("SM Controls")

# Used to manage how fast the screen updates.
#clock = pygame.time.Clock()
# Get ready to print.
text_print = TextPrint()
pygame.event.pump()

while (1):
    screen.fill((0, 0, 0))
    text_print.reset()
    text_print.tprint(screen, f"1 - Pour All Chemical")
    # text_print.indent()
    text_print.tprint(screen, f"2 - Water Heater")
    # text_print.indent()
    text_print.tprint(screen, f"3 - Stepper Rotate")
    # text_print.indent()
    text_print.tprint(screen, f"4 - Stepper Direction Toggle")
    # text_print.indent()
    text_print.tprint(screen, f"5 - Auger Down With Rotation")
    # text_print.indent()
    text_print.tprint(screen, f"6 - Auger UP")
    # text_print.indent()
    text_print.tprint(screen, f"7 - Auger Rotation For Deposition")
    # text_print.indent()
    text_print.tprint(screen, f"8 - Sensor Suite Up")
    # text_print.indent()
    text_print.tprint(screen, f"9 - Sensor Suite Down")
    # text_print.indent()
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Limit to 30 frames per second.
    pygame.key.get_focused()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("Key 1 has been pressed")
                me='1'
            elif event.key == pygame.K_2:
                print("Key 2 has been pressed")
                me='2'
            elif event.key == pygame.K_3:
                print("Key 3 has been pressed")
                me='3'
            elif event.key == pygame.K_4:
                print("Key 4 has been pressed")
                me='4'
            elif event.key == pygame.K_5:
                print("Key 5 has been pressed")
                me='5'
            elif event.key == pygame.K_6:
                print("Key 6 has been pressed")
                me='6'
            elif event.key == pygame.K_7:
                print("Key 7 has been pressed")
                me='7'
            elif event.key == pygame.K_8:
                print("Key 8 has been pressed")
                me='8'
            elif event.key == pygame.K_9:
                print("Key 9 has been pressed")
                me='9'
            else:
                me='0'
                
        elif event.type == pygame.KEYUP:
            me='0'
        
        sendData(me)
        print(me)
    sendData(me)
    print(me)
