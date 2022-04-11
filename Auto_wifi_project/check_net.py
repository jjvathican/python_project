import subprocess
import requests
from requests import get
import time
import _thread
from pythonping import ping
# response_list = ping('8.8.8.8', size=1, count=10)
# print(response_list.rtt_avg_ms)  
import re
import os
hostname = "8.8.8.8" 

url = ["https://www.google.com","https://www.google.com","https://www.google.com","https://www.google.com","https://www.google.com"]
timeout = 5
c=0
a=5
b=0
change_state=1
listis=[]
def print_time(urllink):
        global a 
        # response = os.system("ping -c 1 " + hostname)
        # if response == 0:
        #         print(hostname, 'is up!')
        #         a=a+1
        # else:
        #         print(hostname, 'is down!')
        try:
                print("sending ping request")
                response_list = ping('8.8.8.8', size=1, count=2)
                print(response_list.rtt_avg_ms)     
                if(response_list.rtt_avg_ms<1800):
                                
                        return
                else:
                        a=a-1
                        if(a<0):
                                return
                        time.sleep(5)
                        print_time(urllink)
        except:
                print("no ping found")
                a=a-1
                if(a<0):
                        return
                time.sleep(5)
                print_time(urllink)

        # try:                
        #         request = requests.get(urllink, timeout=timeout)          
        #         #print("Connected to the Internet")
        #         a=a+1       

        # except (requests.ConnectionError, requests.Timeout) as exception:
        #         print("No internet connection.")
                

def connect_net():
        
       
        subprocess.run(["sudo","wpa_cli","-i","wlxd03745f41b5a","reconfigure"])
        time.sleep(.1)
        subprocess.run(["sudo","/usr/bin/ip","link","set","wlxd03745f41b5a","down"])
        time.sleep(.1)
        subprocess.run(["sudo","/usr/bin/ip","link","set","wlxd03745f41b5a","up"])
        time.sleep(.1)
        subprocess.run(["sudo","/usr/sbin/dhclient","-r","wlxd03745f41b5a"])
        time.sleep(.1)
        subprocess.run(["sudo","/usr/sbin/dhclient","-v","wlxd03745f41b5a"])
        time.sleep(5)
        
        # command = "sudo /usr/local/vpnclient/vpnclient stop"
        # subprocess.run(command, shell=True)
        # time.sleep(1)

        # command = "sudo ip route del default via 192.168.49.1"
        # subprocess.run(command, shell=True)
        # time.sleep(.1)

        # command = "sudo /usr/local/vpnclient/vpnclient start"
        # subprocess.run(command, shell=True)
        # time.sleep(5)

        # command = "sudo dhclient -v vpn_vpn"
        # subprocess.run(command, shell=True)
        # time.sleep(5)

        # command = "sudo ip route del default via 192.168.49.1"
        # subprocess.run(command, shell=True)
        # time.sleep(.1)
        
        # command = "sudo ip route add 192.168.49.20/32 via $(netstat -n -r | grep 'UG .*wlxd03745f41b5a' | awk '{print $2}' | head -n 1) "
        # subprocess.run(command, shell=True)
        # time.sleep(.1)
        
        # command =  "sudo ip route del default  via $( netstat -n -r | grep 'UG .*wlxd03745f41b5a' | awk '{print $2}' | head -n 1) "
        # subprocess.run(command, shell=True) 
        # time.sleep(60)
        

        
        
        
        

while True:
        
       
        

        # for i in url: 
        #         time.sleep(2)
        #         print(i)
        #         _thread.start_new_thread( print_time, (i,) )

        # time.sleep(10)
        # if(change_state==0):
        #         time.sleep(10)
        #         for i in url:
        #                 time.sleep(2)
        #                 print("S2:")
        #                 print(i)
        #                 _thread.start_new_thread( print_time, (i,) )
               
        restart=False    
                
        if(a<1 or restart == True):
                while True:
                        try:
                                c=c+1
                                b=listis[c]

                        except:
                                print("Scanning available connections")
                                ps = subprocess.Popen(("sudo", "/usr/sbin/iwlist" , "wlxd03745f41b5a","scan"), stdout=subprocess.PIPE)
                                output = subprocess.check_output(("/usr/bin/grep", "ESSID:"), stdin=ps.stdout)
                                ps.wait()
                                print(output)
                                listis=re.findall(r'"(.*?)"', str(output))
                                c=0
                                b=listis[c]
                        # change_state=1
                        
                        
                                
                        if(b == "Papa"):
                                print("Connecting to Papa")
                                subprocess.run(["sudo","/usr/bin/cp","/home/pi/wificonfig03.conf","/etc/wpa_supplicant/wpa_supplicant.conf"])
                                connect_net()
                                break
                                
                        elif(b == "jj"):
                                print("Connecting to jj")
                                subprocess.run(["sudo","/usr/bin/cp","/home/pi/wificonfig04.conf","/etc/wpa_supplicant/wpa_supplicant.conf"])
                                connect_net()
                                break
                                
                        elif(b == "Rani"):
                                print("Connecting to Rani")
                                subprocess.run(["sudo","/usr/bin/cp","/home/pi/wificonfig05.conf","/etc/wpa_supplicant/wpa_supplicant.conf"])
                                connect_net()
                                break 

                        elif(b == "MM"):
                                print("Connecting to Merin")
                                subprocess.run(["sudo","/usr/bin/cp","/home/pi/wificonfig01.conf","/etc/wpa_supplicant/wpa_supplicant.conf"])
                                connect_net()
                                break
                            
                        elif(b == "jjm"):
                                print("Connecting to jjm")
                                subprocess.run(["sudo","/usr/bin/cp","/home/pi/wificonfig06.conf","/etc/wpa_supplicant/wpa_supplicant.conf"])
                                connect_net()
                                break

                        elif(b == "BAHU"):
                                print("Connecting to bahu")
                                subprocess.run(["sudo","/usr/bin/cp","/home/pi/wificonfig02.conf","/etc/wpa_supplicant/wpa_supplicant.conf"])
                                connect_net()
                                break      
                                              
                                
        
        try:
                a=5
                _thread.start_new_thread( print_time, (1,) )  
        except:
                print("No ping") 
                restart=True   

        # try:
                
        #         ip = get('https://api.ipify.org', timeout=timeout).text
        #         if(ip!='70.66.198.115'):
        #                 print("wrong ip")
        #                 a=0
                          
        # except (requests.ConnectionError, requests.Timeout) as exception:
        #          print("exception occured")                        

        time.sleep(3)

        # response = os.system("ping -c 1 " + hostname)

        # if response == 0:
        #         print(hostname, 'is up!')
        
        # else:
        #         print(hostname, 'is down!') 
        #         time.sleep(5)       
        # else:
        #         change_state=0        
#subprocess.run(["sudo","/usr/bin/cp","/home/pi/wificonfig01.conf","/etc/wpa_supplicant/wpa_supplicant.conf"])
#subprocess.run(["sudo","/usr/bin/ip","/usr/bin/link","set","wlxd03745f41b5a","down"])
#subprocess.run([sudo /usr/bin/ip /usr/bin/link set wlxd03745f41b5a up])
#subprocess.run([sudo /usr/sbin/dhclient -r wlxd03745f41b5a])
#subprocess.run([sudo /usr/sbin/dhclient -v wlxd03745f41b5a])



	




