# NETCONF/YANG Quick Example

This repository is a simple example of a couple Python scripts that can be used to retrieve and set configuration information from an IOS XE device.  This code is provided to accompany a blog on the same topic (link coming soon).  

You can execute these scripts yourself by reserving a [DevNet Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/32b0ae9b-3960-469f-8852-2a03389063d9?diagramType=Topology) (completely free) and following these steps.  

1. Clone the code 

```bash
git clone https://github.com/hpreston/netconf_yang_blog
cd netconf_yang_blog 
```

1. Install the Python requirements. 

```bash
pip install -r requirements.txt 
```

1. Get the configuration. 

```bash 
python get_full_config.py
```

1. Send the configuration. 

```bash
push_standard_config.py
```

