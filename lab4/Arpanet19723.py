#!/usr/bin/python  Arpanet19723.py

"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import Node
from mininet.node import OVSSwitch
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

from functools import partial
from collections import defaultdict, OrderedDict

class GeneratedTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )

        # add nodes, switches first...
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        s7 = self.addSwitch( 's7' )
        s8 = self.addSwitch( 's8' )
        s9 = self.addSwitch( 's9' )
        s10 = self.addSwitch( 's10' )
        s11 = self.addSwitch( 's11' )
        s12 = self.addSwitch( 's12' )
        s13 = self.addSwitch( 's13' )
        s14 = self.addSwitch( 's14' )
        s15 = self.addSwitch( 's15' )
        s16 = self.addSwitch( 's16' )
        s17 = self.addSwitch( 's17' )
        s18 = self.addSwitch( 's18' )
        s19 = self.addSwitch( 's19' )
        s20 = self.addSwitch( 's20' )
        s21 = self.addSwitch( 's21' )
        s22 = self.addSwitch( 's22' )
        s23 = self.addSwitch( 's23' )
        s24 = self.addSwitch( 's24' )
        s25 = self.addSwitch( 's25' )

        # ... and now hosts
        h1 = self.addHost( 'ILLINOIS' )
        h2 = self.addHost( 'MITRE' )
        h3 = self.addHost( 'CARNEGIE' )
        h4 = self.addHost( 'CASE' )
        h5 = self.addHost( 'ETAC' )
        h6 = self.addHost( 'AFGWC' )
        h7 = self.addHost( 'BBN' )
        h8 = self.addHost( 'NBS' )
        h9 = self.addHost( 'Tinker' )
        h10 = self.addHost( 'AMES' )
        h11 = self.addHost( 'RADC' )
        h12 = self.addHost( 'McClellan' )
        h13 = self.addHost( 'RAND' )
        h14 = self.addHost( 'AMES13' )
        h15 = self.addHost( 'SDC' )
        h16 = self.addHost( 'BBN15' )
        h17 = self.addHost( 'HARVARD' )
        h18 = self.addHost( 'SRI' )
        h19 = self.addHost( 'UCSB' )
        h20 = self.addHost( 'UCLA' )
        h21 = self.addHost( 'Stanford' )
        h22 = self.addHost( 'USC' )
        h23 = self.addHost( 'UTAH' )
        h24 = self.addHost( 'Lincoln' )
        h25 = self.addHost( 'MIT' )

        # add edges between switch and corresponding host
        self.addLink( s1 , h1 )
        self.addLink( s2 , h2 )
        self.addLink( s3 , h3 )
        self.addLink( s4 , h4 )
        self.addLink( s5 , h5 )
        self.addLink( s6 , h6 )
        self.addLink( s7 , h7 )
        self.addLink( s8 , h8 )
        self.addLink( s9 , h9 )
        self.addLink( s10 , h10 )
        self.addLink( s11 , h11 )
        self.addLink( s12 , h12 )
        self.addLink( s13 , h13 )
        self.addLink( s14 , h14 )
        self.addLink( s15 , h15 )
        self.addLink( s16 , h16 )
        self.addLink( s17 , h17 )
        self.addLink( s18 , h18 )
        self.addLink( s19 , h19 )
        self.addLink( s20 , h20 )
        self.addLink( s21 , h21 )
        self.addLink( s22 , h22 )
        self.addLink( s23 , h23 )
        self.addLink( s24 , h24 )
        self.addLink( s25 , h25 )

        # add edges between switches
        self.addLink( s1 , s25, bw=10, delay='50ms')
        self.addLink( s1 , s23, bw=10, delay='34ms')
        self.addLink( s2 , s3, bw=10, delay='13ms')
        self.addLink( s2 , s5, bw=10, delay='14ms')
        self.addLink( s3 , s4, bw=10, delay='15ms')
        self.addLink( s4 , s11, bw=10, delay='12ms')
        self.addLink( s4 , s6, bw=10, delay='17ms')
        self.addLink( s5 , s8, bw=10, delay='10ms')
        self.addLink( s7 , s25, bw=10, delay='18ms')
        self.addLink( s7 , s16, bw=10, delay='17ms')
        self.addLink( s8 , s17, bw=10, delay='13ms')
        self.addLink( s9 , s22, bw=10, delay='14ms')
        self.addLink( s9 , s16, bw=10, delay='19ms')
        self.addLink( s10 , s18, bw=10, delay='14ms')
        self.addLink( s10 , s14, bw=10, delay='15ms')
        self.addLink( s11 , s24, bw=10, delay='17ms')
        self.addLink( s12 , s18, bw=10, delay='40ms')
        self.addLink( s12 , s23, bw=10, delay='44ms')
        self.addLink( s13 , s20, bw=10, delay='15ms')
        self.addLink( s13 , s21, bw=10, delay='18ms')
        self.addLink( s13 , s15, bw=10, delay='15ms')
        self.addLink( s14 , s21, bw=10, delay='19ms')
        self.addLink( s15 , s22, bw=10, delay='15ms')
        self.addLink( s16 , s17, bw=10, delay='12ms')
        self.addLink( s18 , s19, bw=10, delay='44ms')
        self.addLink( s19 , s20, bw=10, delay='48ms')
        self.addLink( s22 , s23, bw=10, delay='16ms')
        self.addLink( s24 , s25, bw=10, delay='13ms')

topos = { 'generated': ( lambda: GeneratedTopo() ) }

# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

# the following code produces an executable script working with a remote controller
# and providing ssh access to the the mininet hosts from within the ubuntu vm
controller_ip = ''

def setupNetwork(controller_ip):
    "Create network and run simple performance test"
    # check if remote controller's ip was set
    # else set it to localhost
    topo = GeneratedTopo()
    switch = partial(OVSSwitch, protocols='OpenFlow10')
    if controller_ip == '':
        #controller_ip = '10.0.2.2';
        controller_ip = '127.0.0.1';
    net = Mininet(topo=topo, switch=switch, controller=lambda a: RemoteController( a, ip=controller_ip, port=6633 ), host=CPULimitedHost, link=TCLink)
    return net

def connectToRootNS( network, switch, ip, prefixLen, routes ):
    "Connect hosts to root namespace via switch. Starts network."
    "network: Mininet() network object"
    "switch: switch to connect to root namespace"
    "ip: IP address for root namespace node"
    "prefixLen: IP address prefix length (e.g. 8, 16, 24)"
    "routes: host networks to route to"
    # Create a node in root namespace and link to switch 0
    root = Node( 'root', inNamespace=False )
    intf = TCLink( root, switch ).intf1
    root.setIP( ip, prefixLen, intf )
    # Start network that now includes link to root namespace
    network.start()
    # Add routes from root ns to hosts
    for route in routes:
        root.cmd( 'route add -net ' + route + ' dev ' + str( intf ) )

def sshd( network, cmd='/usr/sbin/sshd', opts='-D' ):
    "Start a network, connect it to root ns, and run sshd on all hosts."
    switch = network.switches[ 0 ]  # switch to use
    ip = '10.123.123.1'  # our IP address on host network
    routes = [ '10.0.0.0/8' ]  # host networks to route to
    connectToRootNS( network, switch, ip, 8, routes )
    for host in network.hosts:
        host.cmd( cmd + ' ' + opts + '&' )

    dumpNodeConnections(network.hosts)

    CLI( network )
    for host in network.hosts:
        host.cmd( 'kill %' + cmd )
    network.stop()

def sorted_dict(d):
    res = OrderedDict()
    for k, v in sorted(d.items(), key=lambda x: x[0]):
        res[k] = v
    return res

def get_switch_ip(x):
    return '20.0.' + str(x / 1000) + '.' + str(x % 1000)

def create_topo_for_veriflow(net):
    if net is None:
        return

    host_ips = {}
    for host in net.hosts:
        host_ips[host.name] = host.IP()

    connections = defaultdict(list)
    for link in net.links:
        src, src_port = str(link.intf1).split('-eth')
        dst, dst_port = str(link.intf2).split('-eth')
        connections[src].append((src_port, dst))
        connections[dst].append((dst_port, src))

    switch_connection, host_connection = OrderedDict(), OrderedDict()
    for k, v in connections.items():
        if k.startswith('s'):
            switch_connection[int(k.replace('s', ''))] = v
        else:
            host_connection[k] = v

    switch_connection = sorted_dict(switch_connection)
    host_connection = sorted_dict(host_connection)

    with open('Arpanet19723.txt', 'w') as topo_file:
        # switch
        topo_file.write('# switches\n')
        for k, v in switch_connection.items():
            line = str(k) + ' '
            line += get_switch_ip(k) + ' ' + '0'
            for port, node in v:
                if node.startswith('s'):
                    line += ' ' + port + ' ' + get_switch_ip(int(node.replace('s', '')))
                else:
                    line += ' ' + port + ' ' + host_ips[node]
            topo_file.write(line + '\n')

        topo_file.write('\n# hosts\n')
        for k, v in host_connection.items():
            id = 100 + int(host_ips[k].split('.')[-1])
            line = str(id) + ' '
            line += host_ips[k] + ' ' + '1'
            for port, node in v:
                line += ' ' + port + ' ' + get_switch_ip(int(node.replace('s', '')))
            topo_file.write(line + '\n')

# by zys
def start_network(network):
    network.start()

    create_topo_for_veriflow(network)
    dumpNodeConnections(network.hosts)

    CLI( network )
    network.stop()

if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    # sshd( setupNetwork(controller_ip) )
    start_network(setupNetwork(controller_ip))
