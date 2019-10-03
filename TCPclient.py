from socket import *
import sys

f = open("testcases.txt", 'r')
sentence = f.readline()

serverName = 'DESKTOP-LRH3NGC'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)


while (sentence != ""): #until the end of the file
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, 12001))
    clientSocket.send(sentence.encode())
    modMessage=clientSocket.recv(2048)
    print(modMessage.decode())
    sentence = f.readline()
    clientSocket.close()

f.close()