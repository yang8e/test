import os
import re
import smtplib
import sys

def nmap_scan():
    os.system('nmap -T4 -p23,22,80,443,445,873,3128,3306,1433,4848,4440,6082,6379,7001,7021,7080,7474,7755,7766,7888,8060,8880,8000,8881,8008,8080,8081,8087,8443,8090,8099,8088,8882,8883,8884,8885,8886,8887,8888,9043,9080,9090,9200,10000,15672,18080,11211,27017,50000 --open -oG nmap_out.txt -iL url1.txt')
    list_nmap = []
    st = open('url1.txt','w')
    fo=open('nmap_out.txt','r')
    for i in fo.readlines():
        list_nmap.append(i)
    get_list = list(set(list_nmap))
    for line in get_list:
        if 'http' in line:
            ip = re.compile(r'(\d)*\.(\d)*\.(\d)*\.(\d)*')
            find_ip = ip.search(line)
            ip_cat = find_ip.group()
            line1 = line.split('Ports: ')
            line2 = line1[1].split(', ')
            for i in line2:
                if 'http' in i:
                    port = i.split('/')
                    url = 'http://'+ip_cat+':'+port[0]
                    st.write(url+'\n')

def theHarvester_scan(target):
    os.system('python /root/theHarvester/theHarvester.py -d '+target+' -b all -l 500 -s 300 > /root/url.txt')
    f=open('url.txt','r')
    file_read = f.read()
    r = re.findall("(.*?) : ",file_read)
    dd = "\n".join(r)
    d=open('url1.txt','w')
    d.write(dd)
    nmap_scan()

input_url = sys.argv[1]
theHarvester_scan(input_url)
