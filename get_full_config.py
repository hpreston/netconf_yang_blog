#!/usr/bin/env python

# import the ncclient library and xml libraries 
from ncclient import manager
import xml.dom.minidom

# Connection details for the IOS XE Device
HOST = '10.10.20.48'
PORT = 830
USER = 'root'
PASS = 'D_Vay!_10&'

# Establish connection to the device
netconf_connection = manager.connect(host=HOST, 
                    port=PORT, 
                    username=USER,
                    password=PASS, 
                    hostkey_verify=False,
                    )

# Use the <get-config> NETCONF Operation to retrieve full configuration
config = netconf_connection.get_config("running")

# Print out the XML Data to the screen 
print(xml.dom.minidom.parseString(config.xml).toprettyxml())                    

# Close the NETCONF Connection to the device 
netconf_connection.close_session()