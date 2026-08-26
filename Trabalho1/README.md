
# Mini Kahoot

Mini Kahoot desenvolvido em Python utilizando comunicação cliente-servidor através de sockets TCP.

O projeto consiste em um quiz executado pelo terminal, no qual o cliente se conecta ao servidor, informa seu nome, responde a três questões sorteadas de um banco de perguntas e, 
ao final, recebe sua pontuação e o resultado de cada questão.

### `server.py`

Responsável por:

- criar e configurar o socket TCP do servidor;
- carregar o banco de questões;
- aguardar conexões de clientes;
- sortear três questões do banco de dados para cada partida;
- receber o nome do usuário;
- enviar as questões ao cliente;
- receber as respostas e verificar se estão corretas;
- calcular a pontuação;
- enviar o resultado final ao cliente.

### `client.py`

Responsável por:

- conectar-se ao servidor;
- solicitar o nome do usuário;
- receber e exibir as questões;
- solicitar as respostas do usuário;
- enviar as respostas ao servidor;
- receber e exibir o resultado final.

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/MazinhaB/C115-L1-Exercicios.git
```

Entre na pasta do projeto:

```bash
cd C115-L1-Exercicios\Trabalho1
```

### 2. Inicie o servidor

Abra um terminal na pasta *Trabalho1* e execute:

```bash
python server.py
```
O servidor deverá iniciar com a mensagem:

```text
Servidor disponível para conexão...
```

### 3. Inicie o cliente

Abra **outro** terminal na mesma pasta e execute:

```bash
python client.py
```

### 4. Siga as instruções do terminal do cliente

Informe o nome de usuário e responda as questões sorteadas, escolhendo uma opção entre A, B, C ou D.