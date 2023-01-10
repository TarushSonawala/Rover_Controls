import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8000	
s.connect(('192.168.21.35', port))
while True:
    print("Waiting For Response")
    server_msg=s.recv(1024)
    print("Message from Server: ", server_msg.decode())
    # client_msg=input("Send Message to Server:")
    # s.send(client_msg.encode())
