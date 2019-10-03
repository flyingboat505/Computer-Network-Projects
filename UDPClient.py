from socket import *

f = open("testcases.txt",'r')
servername='DESKTOP-LRH3NGC'
serverPort=12000
clientSocket= socket(AF_INET,SOCK_DGRAM)
sentence = f.readline()

while(sentence!=""):
    line = []
    clientSocket.sendto (sentence.encode(), ( servername,serverPort) )
    modMessage,serverAddress=clientSocket.recvfrom(2048)
    print(modMessage.decode())
    sentence = f.readline()

clientSocket.close()

f.close()