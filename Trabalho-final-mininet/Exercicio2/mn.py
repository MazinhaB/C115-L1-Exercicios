
#!/usr/bin/python

from __future__ import print_function

import os
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.util import dumpNodeConnections


class NetworkTopo(Topo):
    # Constroi topologia
    def build(self, **_opts):

        # Adiciona switches
        s1 = self.addSwitch('s1', failMode='standalone')
        s2 = self.addSwitch('s2', failMode='standalone')
        s3 = self.addSwitch('s3', failMode='standalone')

        # Adiciona hosts
        h1 = self.addHost('h1', ip='10.0.0.1/8',mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', ip='10.0.0.2/8',mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', ip='10.0.0.3/8',mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', ip='10.0.0.4/8',mac='00:00:00:00:00:04')
        h5 = self.addHost('h5', ip='10.0.0.5/8',mac='00:00:00:00:00:05')

        # Conecta hosts nos switches
        for h, s in [(h1, s1),(h2, s1),(h3, s2),(h4, s3),(h5, s3)]:
            self.addLink(h, s)

        # Conecta switches
        self.addLink(s1, s2)
        self.addLink(s2, s3)


def run():

    topo = NetworkTopo()

    net = Mininet(topo=topo, controller=None)

    net.start()

    CLI( net, script="nodes.sh")

    print('#### Informacoes das portas ####\n')
    dumpNodeConnections(net.hosts)

    h1 = net.get('h1')
    h5 = net.get('h5')

    # Testes de ping com switches standalone
    print('#### Teste de ping H1 para H2 ####\n')
    print(h1.cmd('ping -c1 10.0.0.2'))

    print('#### Teste de ping H1 para H3 ####\n')
    print(h1.cmd('ping -c1 10.0.0.3'))

    print('#### Teste de ping H1 para H5 ####\n')
    print(h1.cmd('ping -c1 10.0.0.5'))

    print('#### Apagando as regras ####\n')

    for switch in ['s1', 's2', 's3']:
        print(h1.cmd('sudo ovs-ofctl del-flows ' + switch))

    # Criando regras MAC

    print('#### Criando as regras MAC ####\n')

    # H1 -> H5

    net['s1'].cmd('sudo ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,actions=output:3')
    net['s2'].cmd('sudo ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,actions=output:3')
    net['s3'].cmd('sudo ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,actions=output:2')

    # H5 -> H1

    net['s3'].cmd('sudo ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,actions=output:3')
    net['s2'].cmd('sudo ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,actions=output:2')
    net['s1'].cmd('sudo ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,actions=output:1')

    # Regra ARP para permitir a resolucao de enderecos

    for switch in ['s1', 's2', 's3']:
        net[switch].cmd('sudo ovs-ofctl add-flow ' + switch + ' dl_type=0x806,nw_proto=1,action=flood')

    print('#### Regras configuradas ####\n')

    for switch in ['s1', 's2', 's3']:
        print('Regras do switch ' + switch)
        print(h1.cmd('sudo ovs-ofctl dump-flows ' + switch))

    # Teste de ping com as regras criadas
 
    print('#### Teste de ping H1 para H5 ####\n')
    print(h1.cmd('ping -c1 10.0.0.5'))

    print('#### Teste de ping H5 para H1 ####\n')
    print(h5.cmd('ping -c1 10.0.0.1'))

    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
