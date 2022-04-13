#from asyncio import threads
from concurrent.futures import thread
import subprocess
import requests
from requests import get
import time
import _thread
from pythonping import ping
import urllib.request
from socket import timeout
# response_list = ping('8.8.8.8', size=1, count=10)
# print(response_list.rtt_avg_ms)  
import re
import os
hostname = "8.8.8.8" 

url = ["http://www.blogsearch.google.com/ping","http://googleping.com/","http://www.pingomatic.com"," http://www.pingler.com"]
timeout = 3
acount=len(url)-1
print(acount)
c=0
a=acount
b=0
threadstate=False
change_state=1
listis=[]
def print_time(urllink,arr):
        global acount
        global a 
        global threadstate
        if(a<0 or arr<0):
                
                return
        # response = os.system("ping -c 1 " + hostname)
        # if response == 0:
        #         print(hostname, 'is up!')
        #         a=a+1
        # else:
        #         print(hostname, 'is down!')
        url_stat=0
       
       

        try:
                print("sending ping request")
                response_list = ping('8.8.8.8', size=1, count=2)
                print(response_list.rtt_avg_ms)
                time.sleep(3)
                # try:                
                #         request = requests.get(urllink[a], timeout=timeout)   

                # except (requests.ConnectionError, requests.Timeout) as exception:

                #         print("No url connection.")  

                if(response_list.rtt_avg_ms<1800):
                        a=acount  
                        threadstate=False     
                        return True
                else:
                        threadstate=True
                        print("pibg was long") 
                        if(a<0 or arr<0):
                                return
                        
                        _thread.start_new_thread( print_time, (urllink,arr-1,) )
                        
                        
        except:
                print("no ping found")
                
                

        try:
                print("arr:"+str(arr))
                
                url_stat=int(urllib.request.urlopen(urllink[arr],timeout=3).getcode())
                print(urllink[arr])
                print(url_stat)
                if(url_stat==200):
                        a=acount
                        if arr==0:
                                threadstate=False
                        return True
                else:
                        a=a-1
                        return
        # except(urllib.requests.ConnectionError, urllib.requests.Timeout) as exception:
        
        # except (HTTPError, URLError) as error:
        #         print("HTTPERROR")
        # except timeout:
        #         print("TIMEOUTERROR")
        except:
                a=a-1
                if arr==0:
                        threadstate=False
                # arr=len(url)-1  
                print("url not reachable")
                
                return 
                
                
                # print(url_stat)
                # print(urllink[a])
        
                

def connect_net():
        
        global a
        global threadstate
        subprocess.run(["sudo","wpa_cli","-i","wlxd03745f41b5a","reconfigure"])
        time.sleep(.1)
        subprocess.run(["sudo","/usr/bin/ip","link","set","wlxd03745f41b5a","down"])
        time.sleep(.1)
        subprocess.run(["sudo","/usr/bin/ip","link","set","wlxd03745f41b5a","up"])
        time.sleep(2)
        subprocess.run(["sudo","/usr/sbin/dhclient","-r","wlxd03745f41b5a"])
        time.sleep(5)
        subprocess.run(["sudo","/usr/sbin/dhclient","-v","wlxd03745f41b5a"])
        time.sleep(5)
        subprocess.run(["sudo","/usr/sbin/dhclient","-v","wlxd03745f41b5a"])
        time.sleep(5)
        a=acount
        threadstate=False
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
               
            
                
        if(a<0):
                while True:
                        time.sleep(1)
                        try:
                                print("Scanning available connections")
                                ps = subprocess.Popen(("sudo", "/usr/sbin/iwlist" , "wlxd03745f41b5a","scan"), stdout=subprocess.PIPE)
                                output = subprocess.check_output(("/usr/bin/grep", "ESSID:"), stdin=ps.stdout)
                                ps.wait()
                                print(output)
                                listis=re.findall(r'"(.*?)"', str(output))
                                listis.sort()
                                b=listis[c]
                                c=c+1
                        except:       
                                c=0
                                b=''
                               
                        # change_state=1
                        
                        
                        if(b == "DEVU"):
                                print("Connecting to DEVU")
                                subprocess.run(["sudo","/usr/bin/cp","/home/pi/wificonfig07.conf","/etc/wpa_supplicant/wpa_supplicant.conf"])
                                connect_net()
                                break        
                        elif(b == "Papa"):
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
                arr=len(url)-1
                if(threadstate==False):
                        _thread.start_new_thread( print_time, (url,arr,) )
                        time.sleep(5)
                       
                        
        except:
                a=a-1
                print("No ping") 
        pausecount=0   
        print("runnning") 
        while(threadstate==True):
                print("paused") 
                pausecount=pausecount+1
                if pausecount>10:
                        # a=-1
                        print("loop exited")
                        threadstate=False
                        
                time.sleep(1)  
        # try:
                
        #         ip = get('https://api.ipify.org', timeout=timeout).text
        #         if(ip!='70.66.198.115'):
        #                 print("wrong ip")
        #                 a=0
                          
        # except (requests.ConnectionError, requests.Timeout) as exception:
        #          print("exception occured")                        

        #time.sleep(3)

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



	




