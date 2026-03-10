#!/usr/bin/python
# CS 6250 Fall 2025- SDN Firewall Project with POX
# build gibson-29

from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt
from pox.lib.revent import *
from pox.lib.addresses import EthAddr, IPAddr

# You may use this space before the firewall_policy_processing function to add any extra function that you 
# may need to complete your firewall implementation.  No additional functions "should" be required to complete
# this assignment.


def firewall_policy_processing(policies):
    '''
    This is where you are to implement your code that will build POX/Openflow Match and Action operations to
    create a dynamic firewall meeting the requirements specified in your configure.pol file.  Do NOT hardcode
    the IP/MAC Addresses/Protocols/Ports that are specified in the project description - this code should use
    the values provided in the configure.pol to implement the firewall.

    The policies passed to this function is a list of dictionary objects that contain the data imported from the
    configure.pol file.  The policy variable in the "for policy in policies" represents a single line from the
    configure.pol file.  Each of the configuration values are then accessed using the policy['field'] command. 
    The fields are:  'rulenum','action','mac-src','mac-dst','ip-src','ip-dst','ipprotocol','port-src','port-dst',
    'comment'.

    Your return from this function is a list of flow_mods that represent the different rules in your configure.pol file.

    Implementation Hints:
    The documentation for the POX controller is available at https://noxrepo.github.io/pox-doc/html .  This project
    is using the gar-experimental branch of POX in order to properly support Python 3.  To complete this project, you
    need to use the OpenFlow match and flow_modification routines (https://noxrepo.github.io/pox-doc/html/#openflow-messages
    for flow_mod and https://noxrepo.github.io/pox-doc/html/#match-structure for match.)  Also, do NOT wrap IP Addresses with
    IPAddr() unless you reformat the CIDR notation.  Look at the https://github.com/att/pox/blob/master/pox/lib/addresses.py
    for what POX is expecting as an IP Address.
    '''

    rules = []

    for policy in policies:
        # Enter your code here to implement matching and block/allow rules.  See the links
        # in Implementation Hints on how to do this. 
        # HINT:  Think about how to use the priority in your flow modification.

        rule = None # Please note that you need to redefine this variable below to create a valid POX Flow Modification Object
        rule = of.ofp_flow_mod()
        match = of.ofp_match()
        rule.match = match
        count = 0
        if policy['mac-src'] != '-':
            match.dl_src = EthAddr(policy['mac-src'])
            count += 1

        if policy['mac-dst'] != '-':
            match.dl_dst = EthAddr(policy['mac-dst'])
            count += 1

        if policy['ip-src'] != '-' or policy['ip-dst'] != '-' or policy['ipprotocol'] != '-' or policy['port-src'] != '-' or policy['port-dst'] != '-':
            match.dl_type = 0x0800

        if policy.get('ip-src', '-') != '-':
            match.nw_src = IPAddr(policy['ip-src-address'])
            match.nw_src_mask = int(policy['ip-src-subnet'])
            count += 2

        if policy.get('ip-dst', '-') != '-':
            match.nw_dst = IPAddr(policy['ip-dst-address'])
            match.nw_dst_mask = int(policy['ip-dst-subnet'])
            count += 2

        proto = None
        if policy.get('ipprotocol', '-') != '-':
            proto = int(policy['ipprotocol'])
            match.nw_proto = proto
            count += 1

        if policy.get('port-src', '-') != '-':
            match.tp_src = int(policy['port-src'])
            count += 1

        if policy.get('port-dst', '-') != '-':
            match.tp_dst = int(policy['port-dst'])
            count += 1

        priority = 2000 if policy['action'] == 'Allow' else 1000
        rule.priority = priority + count

        if policy['action'] == 'Allow':
            rule.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))


        # End Code Here
        print('Added Rule ',policy['rulenum'],': ',policy['comment'])
        #print(rule)   #Uncomment this to debug your "rule"
        rules.append(rule)
    
    return rules
