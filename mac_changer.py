import subprocess

interface = "w1p2s0"
new_mac = "00:11:22:33:44:77"

print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)

#subprocess.call('ifconfig wlp2s0 down', shell=True)
#subprocess.call('ifconfig wlp2s0 hw ether 00:11:22:33:44:55', shell=True)
#subprocess.call('ifconfig wlp2s0 up', shell=True)