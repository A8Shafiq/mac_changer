import subprocess
import re

print("[+] MAC changer for Staying anonymous ")
print("[+] $h4fik ")
print("")

print("Enter your new MAC Address :\n for Example 11:22:33:44:55 ")
New_MAC = input(">> ")
#print(New_MAC)
print("Enter your interface :\n for Example eth0 ")
interface = input(">> ")
#print(interface)


output = subprocess.run(["ifconfig"],shell=False, capture_output=True)
CMD_output = output.stdout.decode('utf-8')

pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
regex = re.compile(pattern)
data = regex.search(CMD_output)

Old_MAC = data.group().split(" ")[1]

output = subprocess.run(["ifconfig",interface,"down"],shell=False,capture_output=True)
print("1"+output.stderr.decode("utf-8"))
        
output = subprocess.run(["ifconfig",interface,"hw","ether",New_MAC],shell=False,capture_output=True)
print("2"+output.stderr.decode("utf-8"))
        
output = subprocess.run(["ifconfig",interface,"up"],shell=False,capture_output=True)
print("3"+output.stderr.decode("utf-8"))
        
print("Updated ...")
print("your new MAC is : "+ New_MAC )
print("your old MAC is : "+Old_MAC)










