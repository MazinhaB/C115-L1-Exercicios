# Exercício 1 — Topologia Árvore

## 1. Objetivo

Criar e configurar uma topologia de rede em árvore utilizando Mininet, com profundidade 3 e ramificação 5, realizando a inspeção dos dispositivos e testes de conectividade e desempenho.

## 2. Características da topologia

A topologia possui a seguinte configuração:

| Característica | Valor |
|---|---|
| Tipo de topologia | Árvore |
| Profundidade | 3 |
| Ramificação | 5 |
| Total de switches | 31 |
| Total de hosts | 125 |
| Largura de banda inicial | 30 Mbps |
| Endereçamento IP | Sequencial |
| Endereçamento MAC | Padronizado |

Os hosts utilizam endereços IP sequenciais, começando em `10.0.0.1`, e endereços MAC padronizados, começando em `00:00:00:00:00:01`.

## 3. Implementação e inspeção

A topologia foi criada utilizando os comandos padrão do Mininet, considerando a estrutura em árvore e os parâmetros definidos no enunciado.

Foram realizadas inspeções para identificar:
- Interfaces de rede dos hosts e switches.
- Endereços MAC.
- Endereços IP.
- Portas e conexões entre os dispositivos.

As informações obtidas foram utilizadas para elaborar a representação ilustrativa da topologia.

## 4. Testes de conectividade

Foram realizados testes de conectividade entre os diferentes nós utilizando o comando `ping`.

Também foi utilizado o comando `tcpdump` para observar a chegada dos pacotes nos nós durante os testes.

## 5. Testes de desempenho com iperf

Foi configurado um servidor TCP no Host 1, utilizando a porta `5555`, e um cliente no Host 2.

Os testes foram realizados durante 20 segundos, considerando duas configurações de largura de banda:

| Teste | Largura de banda | Duração |
|---|---:|---:|
| 1 | 30 Mbps | 20 segundos |
| 2 | 40 Mbps | 20 segundos |

Para cada configuração, a topologia foi reconstruída conforme solicitado no enunciado.

## 6. Imagens

Os registros e capturas de tela dos procedimentos estão organizados nesta pasta.

Entre as imagens estão:
- Criação da topologia.
- Inspeção dos nós e conexões.
- Inspeção das interfaces e endereços.
- Testes de conectividade.
- Capturas de pacotes com `tcpdump`.
- Resultados dos testes `iperf` com 30 Mbps e 40 Mbps.
- Representação ilustrativa da topologia.