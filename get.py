import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint as pp 
USER = 'arista'
PASS = 'arista'
requests.packages.urllib3.disable_warnings()
#headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}
headers = {'Accept': 'application/yang-data+json'}
api_call = "https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/state"
#api_call = "https://10.73.1.105:6020/restconf/data/netconf-state/capabilities" 
#api_call = "https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/config/description"
#api_call = "https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/state/counters/in-octets"
#api_call = "https://10.73.1.105:6020/restconf/data/ietf-interfaces:interfaces"
#api_call = "https://10.73.1.105:6020/restconf/data/ietf-interfaces:interfaces/interface=Ethernet1"
#api_call = "https://10.73.1.105:6020/restconf/data/system/state/hostname"
#api_call = "https://10.73.1.105:6020/restconf/data/interfaces/interface=Ethernet1"
#api_call = "https://10.73.1.105:6020/restconf/data/interfaces/interface=Ethernet1/state/description"
result = requests.get(api_call, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)
#result.status_code
#result.ok
#result.url 
#result.content
#result.json()
pp(result.json())
