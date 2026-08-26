from socket import *
import json
import random

serverPort = 3000
serverSocket = socket(AF_INET, SOCK_STREAM)

#atribui a porta ao socket criado
serverSocket.bind(('', serverPort))

with open("questions.json", "r", encoding="utf-8") as file:
	questions = json.load(file)


serverSocket.listen(1)
print("Servidor disponível para conexão...")
while True:
    numberRightAnswers = 0
    finalResult = ""
    questionNumber = 1

    connectionSocket, addr = serverSocket.accept()
    print("Cliente conectado: ", addr)

    quiz = random.sample(questions, 3)
    clientName = connectionSocket.recv(1024).decode()
    for q in quiz:
        message = q["question"] + "\n"
        for op, statement in q["options"].items():
            message += f"{op}) {statement}\n"
        rightAnswer = q["answer"]

        connectionSocket.send(message.encode())
        answer = connectionSocket.recv(1024).decode().strip().upper()
        if answer == rightAnswer:
             numberRightAnswers += 1
        finalResult += f"Q{questionNumber} (resposta: {answer} | correta: {rightAnswer})\n"
        questionNumber += 1

    message = f"Nome do Cliente: {clientName}\nTotal de acertos: {numberRightAnswers}/3\n{finalResult}"
    connectionSocket.send(message.encode())


    connectionSocket.close()