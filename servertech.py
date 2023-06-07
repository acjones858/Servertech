#This version of the script is meant to be on a laptop directly connected to a CDU. 
#This allows the SOC Technician to skip returning to the SOC and they can run this script on the laptop to configure all settings.
#The CDU must be pingable first and set to its default ip: 192.168.1.254 and subnet: 255.255.255.0
#The Laptop's IPv4 setting should also be set to reach the CDU ala ip: 192.168.1.200 and subnet: 255.255.255.0

import paramiko, time
from collections import OrderedDict
from sentry_sdk.integrations.logging import ignore_logger
ignore_logger("paramiko.transport")

print("Enter the following information:")
print("Row:")
row = input()
print("Cab:")
cab = input()
print("Is this CDU 1,2,3?")
print("CDU:")
cduNo = input()

strHost = "10-31-{}-{}".format(row,cab)
strLoc = "S1 F1 Row {} Cab {} CDU {}".format(row,cab,cduNo)
ip = "10.31.{}.{}{}".format(row,cab,cduNo) 

print("Connecting to CDU...")
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host_name = "192.168.1.254"
user = "admn"
pw = "admn"
port = 22
ssh.connect(host_name,port,user,pw)
channel = ssh.invoke_shell()
time.sleep(1.5)

print("Setting network settings...")
print("Setting IPv4...")
channel.sendall("set ipv4 address\n")
time.sleep(1)
channel.sendall("{}\n".format(ip))
time.sleep(1)
print("Setting subnet...")
channel.sendall("set ipv4 subnet\n")
time.sleep(1)
channel.sendall("255.255.0.0\n")
time.sleep(1)
print("Setting gateway IP...")
channel.sendall("set ipv4 gateway\n")
time.sleep(1)
channel.sendall("10.31.0.1\n")
time.sleep(1)
print("Setting DNS1...")
channel.sendall("set dns1\n")
time.sleep(1)
channel.sendall("10.0.3.3\n")
time.sleep(1)
print("Setting DNS2...")
channel.sendall("set dns2\n")
time.sleep(1)
channel.sendall("10.0.3.4\n")
time.sleep(1)
print("Setting to IPv4 Only...")
channel.sendall("set net ipv4only\n")
time.sleep(1)
print("Disabling DHCP...")
channel.sendall("set dhcp disabled\n")
time.sleep(1)
print("Disabling Boot Delay...")
channel.sendall("set dhcp bootdelay disabled\n")
time.sleep(1)
print("Enabling Static Fallback...")
channel.sendall("set dhcp staticfallback enabled\n")
time.sleep(1)
print("Enabling FQDN...")
channel.sendall("set dhcp fqdn enabled\n")
time.sleep(1)
print("Setting FQDN name...")
channel.sendall("set dhcp fqdn name\n")
time.sleep(1)
channel.sendall("{}\n".format(ip))
time.sleep(1)

print("Setting location...")
channel.sendall("set location\n")
time.sleep(1)
channel.sendall("{}\n".format(strLoc))
time.sleep(1)
print("Setting strong passwords...")
channel.sendall("set option strongpasswords enabled\n")
time.sleep(1)
print("Setting temperature to fahrenheit...")
channel.sendall("set option tempscale fahrenheit\n")
time.sleep(1)
print("Disabling Telnet...")
channel.sendall("set telnet disabled\n")
time.sleep(1)
print("Enabling SSH...")
channel.sendall("set ssh enabled\n")
time.sleep(1)
print("Setting SSH port 22...")
channel.sendall("set ssh port 22\n")
time.sleep(1)
print("Enabling http...")
channel.sendall("set http enabled\n")
time.sleep(1)
print("Setting HTTP port 80...")
channel.sendall("set http port 80\n")
time.sleep(1)
print("Enabling SSL...")
channel.sendall("set ssl enabled\n")
time.sleep(1)
print("Setting SSL Access Requirement...")
channel.sendall("set ssl access required\n")
time.sleep(1)
print("Setting SSL port 443...")
channel.sendall("set ssl port 443\n")
time.sleep(1)
print("Setting SNTP Primary Host...")
channel.sendall("set sntp primary 10.0.3.3\n")
time.sleep(1)
print("Setting SNTP Secondary Host...")
channel.sendall("set sntp secondary 10.0.3.4\n")
time.sleep(1)
print("Setting GMT Offset...")
channel.sendall("set sntp gmtoffset -8\n")
time.sleep(1)
print("Setting DST...")
channel.sendall("set sntp dst enabled\n")
time.sleep(1)
print("Setting Syslog primary...")
channel.sendall("set syslog host1 10.0.4.22\n")
time.sleep(1)
print("Setting Syslog port 514...")
channel.sendall("set syslog port 514\n")
time.sleep(1)
print("Setting LDAP...")
channel.sendall("set LDAP enabled\n")
time.sleep(1)
print("Setting LDAP primary host...")
channel.sendall("set ldap primary 10.0.3.3\n")
time.sleep(1)
print("Setting LDAP secondary host...")
channel.sendall("set ldap secondary 10.0.3.4\n")
time.sleep(1)
print("Setting LDAP port 636...")
channel.sendall("set ldap port 636\n")
time.sleep(1)
print("Setting LDAP Bindtype...")
channel.sendall("set ldap usetls\n")
time.sleep(1)
print("Setting Bind DN...")
channel.sendall("set ldap binddn\n")
time.sleep(1)
channel.sendall("cn=Ldap Query,cn=Users,dc=sdsm,dc=local\n")
time.sleep(1)
print("Setting User Search Base DN...")
channel.sendall("set ldap userbasedn\n")
time.sleep(1)
channel.sendall("ou=all-users,dc=sdsm,dc=local\n")
time.sleep(1)
print("Setting User Search Filter...")
channel.sendall("set ldap userfilter\n")
time.sleep(1)
channel.sendall("(&(samaccountname=%s),(memberOf={},OU=Power,OU=Systems,DC=sdsm,DC=local)\n".format(strHost))
time.sleep(1)
print("Setting Group Membership Attribute...")
channel.sendall("memberof\n")
time.sleep(1)
print("Setting Group Membership Type...")
channel.sendall("set ldap grouptype DN\n")
time.sleep(1)
print("Setting Authentication order...")
channel.sendall("set authorder remotelocal\n")
time.sleep(1)
print("Setting LDAP groups...")
channel.sendall("create ldapgroup st-admin\n")
time.sleep(1)
channel.sendall("create ldapgroup st-power-user\n")
time.sleep(1)
channel.sendall("create ldapgroup st-user\n")
time.sleep(1)
channel.sendall("create ldapgroup st-reboot-only\n")
time.sleep(1)
channel.sendall("create ldapgroup st-on-only\n")
time.sleep(1)
channel.sendall("create ldapgroup st-view-only\n")
time.sleep(1)
print("Setting LDAP permissions...")
channel.sendall("set ldapgroup access st-admin Admin\n")
time.sleep(1)
channel.sendall("set ldapgroup access st-power-user Power-User\n")
time.sleep(1)
channel.sendall("set ldapgroup access st-user User\n")
time.sleep(1)
channel.sendall("set ldapgroup access st-reboot-only Reboot-Only\n")
time.sleep(1)
channel.sendall("set ldapgroup access st-on-only On-Only\n")
time.sleep(1)
channel.sendall("set ldapgroup access st-view-only View-Only\n")
time.sleep(1)
print("Configuring complete... Rebooting now")
channel.sendall("restart\n")
channel.sendall("y\n")
channel.close()


