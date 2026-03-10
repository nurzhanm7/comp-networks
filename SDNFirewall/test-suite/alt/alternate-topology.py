#!/usr/bin/python
# CS 6250 Spring 2021 - SDN Firewall Project with POX
# build leucosia-v20

# This file defines the default topology used to grade your assignment.  You
# may create additional firewall topologies by using this file as a template.
# All commands in here are standard Mininet commands like you have used in the first
# project.  This file has been updated to Python 3.

from mininet.topo import Topo
from mininet.net  import Mininet
from mininet.node import CPULimitedHost, RemoteController
from mininet.util import custom
from mininet.link import TCLink
from mininet.cli  import CLI

class FirewallTopo(Topo):

    def __init__(self, cpu=.1, bw=10, delay=None, **params):
        super(FirewallTopo,self).__init__()
        
        # Host in link configuration
        hconfig = {'cpu': cpu}
        lconfig = {'bw': bw, 'delay': delay}
        
        # Create the firewall switch
        s1 = self.addSwitch('s1')

        h1 = self.addHost( 'h1', ip='10.0.1.1', mac='00:00:00:00:00:01', **hconfig)
        h2 = self.addHost( 'h2', ip='10.0.1.2', mac='00:00:00:00:00:02', **hconfig)
        h3 = self.addHost( 'h3', ip='10.0.1.3', mac='00:00:00:00:00:03', **hconfig)
        h4 = self.addHost( 'h4', ip='10.0.1.4', mac='00:00:00:00:00:04', **hconfig)
        h5 = self.addHost( 'h5', ip='10.0.1.5', mac='00:00:00:00:00:05', **hconfig)
        h6 = self.addHost( 'h6', ip='10.0.1.6', mac='00:00:00:00:00:06', **hconfig)
        h7 = self.addHost( 'h7', ip='10.0.1.7', mac='00:00:00:00:00:07', **hconfig)
        h8 = self.addHost( 'h8', ip='10.0.1.8', mac='00:00:00:00:00:08', **hconfig)
        h9 = self.addHost( 'h9', ip='10.0.1.8', mac='00:00:00:00:00:09', **hconfig)
        h10 = self.addHost( 'h10', ip='10.0.1.10', mac='00:00:00:00:00:10', **hconfig)
        h11 = self.addHost( 'h11', ip='10.0.1.11', mac='00:00:00:00:00:11', **hconfig)
        h12 = self.addHost( 'h12', ip='10.0.1.12', mac='00:00:00:00:00:12', **hconfig)
        h13 = self.addHost( 'h13', ip='10.0.1.13', mac='00:00:00:00:00:13', **hconfig)
        h14 = self.addHost( 'h14', ip='10.0.1.14', mac='00:00:00:00:00:14', **hconfig)
        h15 = self.addHost( 'h15', ip='10.0.1.15', mac='00:00:00:00:00:15', **hconfig)
        h16 = self.addHost( 'h16', ip='10.0.1.16', mac='00:00:00:00:00:16', **hconfig)
        h17 = self.addHost( 'h17', ip='10.0.1.17', mac='00:00:00:00:00:17', **hconfig)
        h18 = self.addHost( 'h18', ip='10.0.1.18', mac='00:00:00:00:00:18', **hconfig)
        h19 = self.addHost( 'h19', ip='10.0.1.19', mac='00:00:00:00:00:19', **hconfig)
        h20 = self.addHost( 'h20', ip='10.0.1.20', mac='00:00:00:00:00:20', **hconfig)
        h21 = self.addHost( 'h21', ip='10.0.1.21', mac='00:00:00:00:00:21', **hconfig)
        h22 = self.addHost( 'h22', ip='10.0.1.22', mac='00:00:00:00:00:22', **hconfig)
        h23 = self.addHost( 'h23', ip='10.0.1.23', mac='00:00:00:00:00:23', **hconfig)
        h24 = self.addHost( 'h24', ip='10.0.1.24', mac='00:00:00:00:00:24', **hconfig)
        h25 = self.addHost( 'h25', ip='10.0.1.25', mac='00:00:00:00:00:25', **hconfig)
        h26 = self.addHost( 'h26', ip='10.0.1.26', mac='00:00:00:00:00:26', **hconfig)
        h27 = self.addHost( 'h27', ip='10.0.1.27', mac='00:00:00:00:00:27', **hconfig)
        h28 = self.addHost( 'h28', ip='10.0.1.28', mac='00:00:00:00:00:28', **hconfig)
        h29 = self.addHost( 'h29', ip='10.0.1.29', mac='00:00:00:00:00:29', **hconfig)
        h30 = self.addHost( 'h30', ip='10.0.1.30', mac='00:00:00:00:00:30', **hconfig)
        h31 = self.addHost( 'h31', ip='10.0.1.31', mac='00:00:00:00:00:31', **hconfig)
        h32 = self.addHost( 'h32', ip='10.0.1.32', mac='00:00:00:00:00:32', **hconfig)
        h33 = self.addHost( 'h33', ip='10.0.1.33', mac='00:00:00:00:00:33', **hconfig)
        h34 = self.addHost( 'h34', ip='10.0.1.34', mac='00:00:00:00:00:34', **hconfig)
        h35 = self.addHost( 'h35', ip='10.0.1.35', mac='00:00:00:00:00:35', **hconfig)
        h36 = self.addHost( 'h36', ip='10.0.1.36', mac='00:00:00:00:00:36', **hconfig)
        h37 = self.addHost( 'h37', ip='10.0.1.37', mac='00:00:00:00:00:37', **hconfig)
        h38 = self.addHost( 'h38', ip='10.0.1.38', mac='00:00:00:00:00:38', **hconfig)
        h39 = self.addHost( 'h39', ip='10.0.1.39', mac='00:00:00:00:00:39', **hconfig)
        h40 = self.addHost( 'h40', ip='10.0.1.40', mac='00:00:00:00:00:40', **hconfig)
        h41 = self.addHost( 'h41', ip='10.0.1.41', mac='00:00:00:00:00:41', **hconfig)
        h42 = self.addHost( 'h42', ip='10.0.1.42', mac='00:00:00:00:00:42', **hconfig)
        h43 = self.addHost( 'h43', ip='10.0.1.43', mac='00:00:00:00:00:43', **hconfig)
        h44 = self.addHost( 'h44', ip='10.0.1.44', mac='00:00:00:00:00:44', **hconfig)
        h45 = self.addHost( 'h45', ip='10.0.1.45', mac='00:00:00:00:00:45', **hconfig)
        h46 = self.addHost( 'h46', ip='10.0.1.46', mac='00:00:00:00:00:46', **hconfig)
        h47 = self.addHost( 'h47', ip='10.0.1.47', mac='00:00:00:00:00:47', **hconfig)
        h48 = self.addHost( 'h48', ip='10.0.1.48', mac='00:00:00:00:00:48', **hconfig)
        h49 = self.addHost( 'h49', ip='10.0.1.49', mac='00:00:00:00:00:49', **hconfig)
        self.addLink(s1,h1)
        self.addLink(s1,h2)
        self.addLink(s1,h3)
        self.addLink(s1,h4)
        self.addLink(s1,h5)
        self.addLink(s1,h6)
        self.addLink(s1,h7)
        self.addLink(s1,h8)
        self.addLink(s1,h9)
        self.addLink(s1,h10)
        self.addLink(s1,h11)
        self.addLink(s1,h12)
        self.addLink(s1,h13)
        self.addLink(s1,h14)
        self.addLink(s1,h15)
        self.addLink(s1,h16)
        self.addLink(s1,h17)
        self.addLink(s1,h18)
        self.addLink(s1,h19)
        self.addLink(s1,h10)
        self.addLink(s1,h21)
        self.addLink(s1,h22)
        self.addLink(s1,h23)
        self.addLink(s1,h24)
        self.addLink(s1,h25)
        self.addLink(s1,h26)
        self.addLink(s1,h27)
        self.addLink(s1,h28)
        self.addLink(s1,h29)
        self.addLink(s1,h20)
        self.addLink(s1,h31)
        self.addLink(s1,h32)
        self.addLink(s1,h33)
        self.addLink(s1,h34)
        self.addLink(s1,h35)
        self.addLink(s1,h36)
        self.addLink(s1,h37)
        self.addLink(s1,h38)
        self.addLink(s1,h39)
        self.addLink(s1,h30)
        self.addLink(s1,h41)
        self.addLink(s1,h42)
        self.addLink(s1,h43)
        self.addLink(s1,h44)
        self.addLink(s1,h45)
        self.addLink(s1,h46)
        self.addLink(s1,h47)
        self.addLink(s1,h48)
        self.addLink(s1,h49)
        self.addLink(s1,h40)

def main():
    print("Starting Mininet Topology...")
    print("If you see a Unable to Contact Remote Controller, you have an error in your code...")
    print("Remember that you always use the Server IP Address when calling test scripts...")
    topo = FirewallTopo()
    net = Mininet(topo=topo, link=TCLink, controller=RemoteController("SDNFirewall",port=6633))

    net.start()
    CLI(net)

if __name__ == '__main__':
    main()
