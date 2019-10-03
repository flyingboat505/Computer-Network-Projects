from socket import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind( ('',serverPort)    )
print("Server is ready to receive")

while True:
    #print("running")
    message,clientAddress=serverSocket.recvfrom(2048)
    sentence=message.decode()
    line = []
    wordLength = sentence.split()  # counts all the words in the sentence
    for i in range(0, len(wordLength)):
        line.append(len(wordLength[i]))
    sentence=str(line).strip('[]')

    serverSocket.sendto(sentence.encode(),clientAddress)
