#!/usr/bin/env python
#
# Example output:
#
# Before changing the interface configuration
#
# !Command: show running-config interface Ethernet5/29
# !Time: Sat Oct 17 00:33:46 2015
#
# version 6.1(2)I3(1)
#
# interface Ethernet5/29
#
#
# After changing the interface configuration
#
# !Command: show running-config interface Ethernet5/29
# !Time: Sat Oct 17 00:33:47 2015
#
# version 6.1(2)I3(1)
#
# interface Ethernet5/29
#   description Layer 2 Trunk Interface Example
#   switchport mode trunk
#   switchport trunk native vlan 6
#   switchport trunk allowed vlan 15-20,100
#   no shutdown
#

import sys
from cisco.interface import Interface

# The interface name, it can be abrieviated as well - "Eth1/11"
INTERFACE_NAME = "Ethernet5/29"
# A description to configure on the interface, setting this to a NoneType
# object or an empty string will result in the description being unset on the
# interface.
INTERFACE_DESCRIPTION = "Layer 2 Trunk Interface Example"
# The switchport mode, can be access or trunk
INTERFACE_MODE = "trunk"
# The dot1q native vlan
TRUNK_NATIVE_VLAN = "6"
# The allowed vlans on the trunk
TRUNK_ALLOWED_VLANS = "15-20,100"
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

    # Configure "switchport" so the interface is L2
    INTERFACE.set_switchport()

    # Set the description on the interface
    INTERFACE.set_description(INTERFACE_DESCRIPTION)

    # Set the interface mode to be an a trunk port
    INTERFACE.set_mode(INTERFACE_MODE)

    # Set the dot1q native vlan for the port, there is no native setter
    # method to do this so we have to do it manually
    INTERFACE._if_cfg('switchport trunk native vlan ' +
                      '{0}'.format(TRUNK_NATIVE_VLAN))
    INTERFACE.apply_config()

    # Set the vlans allowed on the trunk
    INTERFACE._if_cfg('switchport trunk allowed vlan ' +
                      '{0}'.format(TRUNK_ALLOWED_VLANS))
    INTERFACE.apply_config()

    # Set the interface state
    INTERFACE.set_state(INTERFACE_STATE)

    print("After changing the interface configuration")
    print(INTERFACE.config())
