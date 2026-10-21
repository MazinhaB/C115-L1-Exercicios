# Trabalho Mininet — Topologia Linear com 6 Switches

## 1. Objetivo

Este projeto tem como objetivo criar e testar uma topologia de rede linear utilizando o Mininet, conforme as instruções do trabalho da disciplina.

As atividades realizadas foram:

- Criar uma topologia linear com 6 switches.
- Configurar endereços MAC padronizados.
- Definir a largura de banda dos links em 25 Mbps.
- Inspecionar nós, conexões, interfaces, endereços MAC, endereços IP e portas dos switches.
- Testar a conectividade entre os hosts utilizando `ping`.
- Configurar um servidor TCP em `h1`, na porta `5555`.
- Executar um teste de desempenho com `iperf`, utilizando `h2` como cliente, com relatórios a cada segundo durante 15 segundos.

## 2. Topologia utilizada

A topologia criada é linear, composta por seis switches Open vSwitch e seis hosts, com um host conectado a cada switch.

```text
s1 ------ s2 ------ s3 ------ s4 ------ s5 ------ s6
 |         |         |         |         |        |
 h1        h2        h3        h4        h5       h6
```

### Configuração

- **Topologia:** linear, com 6 switches e 6 hosts.
- **Endereçamento MAC:** padronizado pelo Mininet.
- **Endereçamento IP:** `10.0.0.1` a `10.0.0.6`.
- **Largura de banda configurada:** 25 Mbps.
- **Controlador:** controlador padrão do Mininet.

## 3. Criação da topologia

### Comando utilizado

```bash
sudo mn --topo=linear,6 --mac --link=tc,bw=25
```

### Print

- `Criando-topologia` — criação da topologia.

## 4. Inspeção dos nós e das conexões

### Comando `nodes`

```text
nodes
```

Lista os dispositivos existentes na topologia, incluindo hosts, switches e controlador.

**Print:** `nodes-net-dump`.

### Comando `net`

```text
net
```

Exibe as conexões entre os dispositivos, identificando as interfaces utilizadas pelos hosts e switches.

Esse comando foi utilizado para verificar a organização da topologia linear e identificar as interfaces conectadas entre os switches.

**Print:** `nodes-net-dump`.

### Comando `dump`

```text
dump
```

Exibe informações detalhadas dos dispositivos, incluindo interfaces, endereços IP dos hosts e informações dos switches e controlador.

Foi utilizado para conferir o endereçamento IP atribuído pelo Mininet.

**Print:** `nodes-net-dump`.

## 5. Inspeção das interfaces, dos endereços MAC e dos IPs

Para consultar as interfaces de rede e seus endereços, foi utilizado o comando `ifconfig -a` em cada host.

### Comandos utilizados

```text
h1 ifconfig -a
h2 ifconfig -a
h3 ifconfig -a
h4 ifconfig -a
h5 ifconfig -a
h6 ifconfig -a
```

Os comandos foram utilizados para verificar:

- Nome da interface de rede de cada host.
- Endereço MAC da interface.
- Endereço IP configurado.
- Estado da interface.
- Estatísticas de transmissão e recepção de pacotes.

### Endereçamento observado

| Host | Interface | Endereço MAC | Endereço IP |
|---|---|---|---|
| h1 | `h1-eth0` | `00:00:00:00:00:01` | `10.0.0.1` |
| h2 | `h2-eth0` | `00:00:00:00:00:02` | `10.0.0.2` |
| h3 | `h3-eth0` | `00:00:00:00:00:03` | `10.0.0.3` |
| h4 | `h4-eth0` | `00:00:00:00:00:04` | `10.0.0.4` |
| h5 | `h5-eth0` | `00:00:00:00:00:05` | `10.0.0.5` |
| h6 | `h6-eth0` | `00:00:00:00:00:06` | `10.0.0.6` |

### Prints

- `ifconfig-h1-h2` — interfaces, endereços MAC e IPs de h1 e h2.
- `ifconfig-h3-h4` — interfaces, endereços MAC e IPs de h3 e h4.
- `ifconfig-h5-h6` — interfaces, endereços MAC e IPs de h5 e h6.

## 6. Inspeção das portas dos switches

Para verificar as portas e as interfaces de cada switch, foi utilizado o comando `ovs-ofctl show`.

### Comandos utilizados

```text
sh ovs-ofctl show s1
sh ovs-ofctl show s2
sh ovs-ofctl show s3
sh ovs-ofctl show s4
sh ovs-ofctl show s5
sh ovs-ofctl show s6
```

Os comandos permitiram verificar as interfaces conectadas a cada switch e identificar as portas utilizadas para conectar hosts e switches vizinhos.

### Prints

- `portas-switch1` — portas e interfaces de s1.
- `portas-switch2` — portas e interfaces de s2.
- `portas-switch3` — portas e interfaces de s3.
- `portas-switch4` — portas e interfaces de s4.
- `portas-switch5` — portas e interfaces de s5.
- `portas-switch6` — portas e interfaces de s6.

## 7. Testes de conectividade com ping

### Teste geral

```text
pingall
```

Esse comando realiza testes de conectividade entre todos os hosts da topologia, permitindo verificar se os dispositivos conseguem se comunicar.

**Resultado observado:** 0% de perda de pacotes, com 30 de 30 pacotes recebidos.

**Print:** `pingall`.

### Testes individuais

Foram realizados testes entre pares de hosts em diferentes posições da topologia.

```text
h1 ping -c 4 h2
h1 ping -c 4 h6
h3 ping -c 4 h5
```

Os pares foram escolhidos para testar a comunicação entre hosts próximos, hosts em extremidades opostas e hosts em posições intermediárias.

**Resultado observado:** os três testes foram concluídos com quatro pacotes recebidos e nenhuma perda.

**Print:** `pings-individuais`.

## 8. Teste de desempenho com iperf

O `iperf` foi utilizado para medir a taxa de transferência entre dois hosts por meio de uma conexão TCP.

Nesta atividade, `h1` foi configurado como servidor e `h2` como cliente, utilizando a porta TCP `5555`.

### 8.1. Abertura dos terminais dos hosts

```text
xterm h1 h2
```

Esse comando abre terminais separados para h1 e h2, permitindo executar os comandos do servidor e do cliente de forma independente.

### 8.2. Configuração do servidor TCP em h1

```bash
iperf -s -p 5555 -i 1
```

### 8.3. Configuração do cliente TCP em h2

```bash
iperf -c 10.0.0.1 -p 5555 -i 1 -t 15
```

### 8.4. Resultado do teste

Durante o teste, o `iperf` apresentou relatórios periódicos com a quantidade de dados transferidos e a taxa de transferência observada em cada intervalo.

**Print:** `servidor-cliente`.

## 9. Resumo dos comandos executados

| Comando | Finalidade | Print |
|---|---|---|
| `sudo mn --topo=linear,6 --mac --link=tc,bw=25` | Criar a topologia linear com seis switches e links de 25 Mbps | `Criando-topologia` |
| `nodes` | Listar os dispositivos da topologia | `nodes-net-dump` |
| `net` | Inspecionar as conexões e interfaces | `nodes-net-dump` |
| `dump` | Consultar informações detalhadas dos dispositivos e IPs | `nodes-net-dump` |
| `h1 ifconfig -a` até `h6 ifconfig -a` | Consultar interfaces, MACs, IPs e estatísticas dos hosts | `ifconfig-h1-h2`, `ifconfig-h3-h4`, `ifconfig-h5-h6` |
| `sh ovs-ofctl show s1` até `s6` | Consultar portas e interfaces dos switches | `portas-switch1` até `portas-switch6` |
| `pingall` | Testar conectividade entre todos os hosts | `pingall` |
| `h1 ping -c 4 h2` | Testar conectividade entre h1 e h2 | `pings-individuais` |
| `h1 ping -c 4 h6` | Testar conectividade entre hosts nas extremidades | `pings-individuais` |
| `h3 ping -c 4 h5` | Testar conectividade entre hosts intermediários | `pings-individuais` |
| `xterm h1 h2` | Abrir terminais separados para os hosts | `servidor-cliente` |
| `iperf -s -p 5555 -i 1` | Iniciar o servidor TCP em h1 | `servidor-cliente` |
| `iperf -c 10.0.0.1 -p 5555 -i 1 -t 15` | Executar o teste TCP a partir de h2 durante 15 segundos | `servidor-cliente` |
