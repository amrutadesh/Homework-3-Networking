#amruta

"""
Example topology of Quagga routers
"""

import inspect
import os
from mininext.topo import Topo
from mininext.services.quagga import QuaggaService

from collections import namedtuple

QuaggaHost = namedtuple("QuaggaHost", "name ip loIP")
net = None


class QuaggaTopo(Topo):

    "Creates a topology of Quagga routers"

    def __init__(self):
        """Initialize a Quagga topology with 5 routers, configure their IP
           addresses, loop back interfaces, and paths to their private
           configuration directories."""
        Topo.__init__(self)

        # Directory where this file / script is located"
        selfPath = os.path.dirname(os.path.abspath(
            inspect.getfile(inspect.currentframe())))  # script directory

        # Initialize a service helper for Quagga with default options
        quaggaSvc = QuaggaService(autoStop=False)

        # Path configurations for mounts
        quaggaBaseConfigPath = selfPath + '/configs/'

        # List of Quagga host configs

	router=QuaggaHost(name='r1', ip='172.0.1.1/16',loIP=None)




	quaggaContainer1 = self.addHost(name=router.name,
        	                                   ip=router.ip,
        	                                   hostname=router.name,
        	                                   privateLogDir=True,
                	                           privateRunDir=True,
                        	                   inMountNamespace=True,
                                	           inPIDNamespace=True,
                                        	   inUTSNamespace=True)

            # Add a loopback interface with an IP in router's announced range
	self.addNodeLoopbackIntf(node=router.name, ip=router.loIP)

            # Configure and setup the Quagga service for this node
	quaggaSvcConfig= \
		{'quaggaConfigPath': quaggaBaseConfigPath + router.name}
	self.addNodeService(node=router.name, service=quaggaSvc,
        	                        nodeConfig=quaggaSvcConfig)

            # Attach the quaggaContainer to the IXP Fabric Switch
           # self.addLink(quaggaContainer, ixpfabric)
##########################################################################
	router2=QuaggaHost(name='r2', ip='10.1.1.2/24',loIP=None)




        quaggaContainer2 = self.addHost(name=router2.name,
                                                   ip=router2.ip,
                                                   hostname=router2.name,
                                                   privateLogDir=True,
                                                   privateRunDir=True,
                                                   inMountNamespace=True,
                                                   inPIDNamespace=True,
                                                   inUTSNamespace=True)

	self.addNodeLoopbackIntf(node=router2.name, ip=router2.loIP)

            # Configure and setup the Quagga service for this node
        quaggaSvcConfig= \
                {'quaggaConfigPath': quaggaBaseConfigPath + router2.name}
        self.addNodeService(node=router2.name, service=quaggaSvc,
                                        nodeConfig=quaggaSvcConfig)
###############################################################################
	router3=QuaggaHost(name='r3', ip='10.10.120.2/24',loIP=None)




        quaggaContainer3 = self.addHost(name=router3.name,
                                                   ip=router3.ip,
                                                   hostname=router3.name,
                                                   privateLogDir=True,
                                                   privateRunDir=True,
                                                   inMountNamespace=True,
                                                   inPIDNamespace=True,
                                                   inUTSNamespace=True)

        self.addNodeLoopbackIntf(node=router3.name, ip=router3.loIP)

            # Configure and setup the Quagga service for this node
        quaggaSvcConfig= \
                {'quaggaConfigPath': quaggaBaseConfigPath + router3.name}
        self.addNodeService(node=router3.name, service=quaggaSvc,
                                        nodeConfig=quaggaSvcConfig)
##########################################################################
	router4=QuaggaHost(name='r4', ip='192.0.1.2/24',loIP=None)




        quaggaContainer4 = self.addHost(name=router4.name,
                                                   ip=router4.ip,
                                                   hostname=router4.name,
                                                   privateLogDir=True,
                                                   privateRunDir=True,
                                                   inMountNamespace=True,
                                                   inPIDNamespace=True,
                                                   inUTSNamespace=True)

        self.addNodeLoopbackIntf(node=router4.name, ip=router4.loIP)

            # Configure and setup the Quagga service for this node
        quaggaSvcConfig= \
                {'quaggaConfigPath': quaggaBaseConfigPath + router4.name}
        self.addNodeService(node=router4.name, service=quaggaSvc,
                                        nodeConfig=quaggaSvcConfig)


	leftHost = self.addHost( 'h1',ip='172.0.1.16/8',
                           defaultRoute='via 172.0.1.1' )
	rightHost = self.addHost( 'h2',ip='192.0.1.16/24',defaultRoute='via 192.0.1.2' )
	self.addLink( leftHost, quaggaContainer1 )
	self.addLink( rightHost, quaggaContainer4 )
	self.addLink( quaggaContainer1, quaggaContainer2 )
	self.addLink( quaggaContainer1, quaggaContainer3 )
	self.addLink( quaggaContainer4, quaggaContainer3 )
	self.addLink( quaggaContainer4, quaggaContainer2 )

topos = { 'topotest': ( lambda: QuaggaTopo() ) }

