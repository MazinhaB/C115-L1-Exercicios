from socket import *

serverName = 'localhost'
serverPort = 3000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

name = input('Digite seu nome: ')

#a mensagem deve estar em bytes antes de ser enviada ao buffer de transmissao
clientSocket.send(name.encode())

for i in range(3):
    question = clientSocket.recv(1024).decode()
    print(f"Questão {i+1}) {question}\n")
    answer = input("Resposta: ")
    clientSocket.send(answer.encode())

# #recebe a resposta do servidor
finalOutput = clientSocket.recv(1024).decode()
print(finalOutput)

#fecha a conexao
clientSocket.close()