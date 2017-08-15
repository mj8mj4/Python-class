
import snmp_helper
#from snmp_helper import snmp_get_oid, snmp_extract

COMMUNITY_STRING  = 'galileo'
SNMP_PORT = 161
IP = '50.242.94.227'
OID = '1.3.6.1.2.1.1.1.0'
a_device = (IP, COMMUNITY_STRING, SNMP_PORT)

snmp_data =snmp_helper.snmp_get_oid(a_device, oid=OID)

output =snmp_helper.snmp_extract(snmp_data)

print output
