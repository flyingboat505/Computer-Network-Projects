from socket import *
serverPort=12001
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The Server is Ready to Listen")
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(2048).decode()
    line = []
    wordLength = sentence.split()  # counts all the words in the sentence
    for i in range(0, len(wordLength)):
        line.append(len(wordLength[i]))
    modsentence = str(line).strip('[]')
    connectionSocket.send(modsentence.encode())
    connectionSocket.close()