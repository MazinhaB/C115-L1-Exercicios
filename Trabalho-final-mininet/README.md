# Trabalho Final — Mininet

Repositório com a implementação e documentação dos 2 exercícios do trabalho final de Mininet da disciplina **C115 — Conceitos e Tecnologias para Dispositivos Conectados**.

O trabalho contempla a criação de topologias de rede utilizando Mininet e Python, configuração de switches e hosts, inspeção de interfaces e endereços, testes de conectividade e análise do tráfego de rede.

## Exercícios

### [Exercício 1 — Topologia Árvore](./Exercicio1/README.md)

Implementação de uma topologia em árvore com profundidade 3 e ramificação 5, contendo 31 switches e 125 hosts.

Principais atividades:
- Criação da topologia com MACs padronizados e largura de banda de 30 Mbps.
- Inspeção de interfaces, endereços MAC, IPs e portas.
- Testes de conectividade com `ping`.
- Captura de pacotes com `tcpdump`.
- Configuração de servidor e cliente TCP e testes com `iperf`, utilizando larguras de banda de 30 e 40 Mbps.

### [Exercício 2 — Topologia Personalizada](./Exercicio2/README.md)

Implementação de uma topologia personalizada com três switches interligados e cinco hosts.

Principais atividades:
- Criação da topologia por meio de código em Python.
- Inspeção de interfaces, endereços MAC, IPs e portas.
- Testes de conectividade com switches em modo standalone.
- Remoção de regras anteriores e configuração de regras OpenFlow baseadas em endereços MAC.
- Testes de comunicação entre hosts conectados a switches diferentes.


Cada exercício possui um README próprio, com a descrição da implementação, procedimentos realizados e evidências dos resultados.