# Exercício 2 — Topologia Personalizada e Regras OpenFlow

## 1. Objetivo

Criar uma topologia personalizada no Mininet utilizando código Python, realizar a inspeção dos dispositivos e configurar regras de encaminhamento baseadas em endereços MAC para permitir a comunicação entre hosts conectados a switches diferentes.

## 2. Características da topologia

A topologia é composta por três switches interligados em cadeia e cinco hosts:

Os hosts utilizam endereços IP sequenciais e endereços MAC padronizados.

| Host | Endereço IP | Endereço MAC |
|---|---|---|
| H1 | 10.0.0.1 | 00:00:00:00:00:01 |
| H2 | 10.0.0.2 | 00:00:00:00:00:02 |
| H3 | 10.0.0.3 | 00:00:00:00:00:03 |
| H4 | 10.0.0.4 | 00:00:00:00:00:04 |
| H5 | 10.0.0.5 | 00:00:00:00:00:05 |

Os switches foram configurados em modo `standalone`, sem a especificação de um controlador externo.

## 3. Implementação

A topologia foi implementada em Python utilizando a classe `NetworkTopo`, baseada na classe `Topo` do Mininet.

Os arquivos utilizados são:

- `mn.py`: implementação e execução da topologia e dos procedimentos do exercício.
- `topologia.py`: definição da topologia personalizada.
- `nodes.sh`: sequência de comandos utilizada para automatizar parte da inspeção dos nós.

## 4. Inspeção da topologia

Foram utilizados comandos do Mininet para identificar:
- Nós existentes na rede.
- Conexões entre hosts e switches.
- Interfaces de rede.
- Endereços IP e MAC dos hosts.
- Portas utilizadas pelos switches.

As informações obtidas foram utilizadas na elaboração do desenho ilustrativo da topologia.

## 5. Testes de conectividade — switches standalone

Inicialmente, foram realizados testes de conectividade entre hosts antes da configuração das regras OpenFlow.

Os testes permitiram observar o comportamento da comunicação com os switches operando em modo standalone.

## 6. Configuração das regras OpenFlow

Após os testes iniciais, foram removidas as regras anteriores dos switches utilizando `ovs-ofctl del-flows`.

Em seguida, foram configuradas regras de encaminhamento baseadas nos endereços MAC de origem e destino, permitindo a comunicação entre H1 e H5 através dos três switches.

Também foi incluída uma regra relacionada ao tráfego ARP.

As regras configuradas foram inspecionadas utilizando `ovs-ofctl dump-flows`.

## 7. Testes após a configuração

Após a instalação das regras, foram realizados testes de comunicação nos dois sentidos:

- H1 → H5.
- H5 → H1.

Os testes apresentaram comunicação bem-sucedida, com 0% de perda de pacotes nas execuções registradas.

## 8. Imagens

As capturas de tela dos procedimentos estão organizadas nesta pasta, incluindo:

- Código da topologia.
- Criação e inspeção da rede.
- Interfaces e endereços dos hosts.
- Inspeção das interfaces dos switches.
- Representação ilustrativa da topologia.
- Testes iniciais de conectividade.
- Remoção e configuração das regras OpenFlow.
- Inspeção das regras instaladas.
- Testes de ping após a configuração.