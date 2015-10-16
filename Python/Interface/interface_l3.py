#!/usr/bin/env python
#
# Example output:
#
# Before changing the interface configuration
# !Command: show running-config interface Ethernet1/9
# !Time: Fri Oct 16 06:07:29 2015
# version 7.0(3)I2(1)
# interface Ethernet1/9
#
# After changing the interface configuration
# !Command: show running-config interface Ethernet1/9
# !Time: Fri Oct 16 06:07:32 2015
# version 7.0(3)I2(1)
# interface Ethernet1/9
#   description Interface to HQ
#   no switchport
#   mac-address 0050.5689.d30f
#   ip address 192.168.17.10/24
#   no shutdown
#

import sys
from cisco.interface import Interface


# The interface name, it can be abrieviated as well - "Eth1/11"
INTERFACE_NAME = "Ethernet1/9"
# The IP Address to configure on the interface
INTERFACE_IP_ADDRESS = "192.168.17.10/24"
# A description to configure on the interface, setting this to a NoneType
# object or an empty string will result in the description being unset on the
# interface.
INTERFACE_DESCRIPTION = "Layer 3 Routed Interface Example"
# Interface state can be set to up using: "up", "no shut" or "noshut"
# Setting it to any other value will cause "shut" to be configured on
# the interface
INTERFACE_STATE = "no shut"

if __name__ == "__main__":
    if not INTERFACE_NAME:
        print("The interface name is required")
        sys.exit(-1)

    # Instantiate an interface object
    INTERFACE = Interface(INTERFACE_NAME)

    print("Before changing the interface configuration")
    print(INTERFACE.config())

    # Configure "no switchport" so the interface is L3
    INTERFACE.set_switchport(no=True)

    # Set an IP address on the interface
    if INTERFACE_IP_ADDRESS != "":
        INTERFACE.set_ipaddress(INTERFACE_IP_ADDRESS)

    # Set the description on the interface
    INTERFACE.set_description(INTERFACE_DESCRIPTION)

    # Set the interface state
    INTERFACE.set_state(INTERFACE_STATE)

    print("After changing the interface configuration")
    print(INTERFACE.config())
