import os
import re
import paramiko
import smtplib

def sendmail(message):
	smtpObj = smtplib.SMTP('smtp-mail.outlook.com',587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login('admin@live.cn','222222')
	smtpObj.sendmail('admin@live.cn','admin@qq.com',message)
	smtpObj.quit()


print('input urls------------------:')

input_url = input()
#远程连接服务器，进行信息收集，并下载到本地
transport = paramiko.Transport(('45.1.1.1', 22))
transport.connect(username='root', password='22222222')
ssh = paramiko.SSHClient()
ssh._transport = transport
stdin,stdout,stderr = ssh.exec_command('python3 /root/server.py '+input_url)
cat_ = stdout.read().decode()
print(cat_)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get('/root/url_list.txt', 'url_list.txt')
#---------------------------------------------------

ls=open('url_list.txt','r')
for i in ls: 
	get_ip = i.strip('\n')
	get_scan = os.popen('wvs_console.exe /scan '+get_ip).read()
	print(get_scan)
	if get_scan in '0 high':
		print('don\'t need look '+i+'\n\n')
	else:
		message = 'Subject: Vulnerability \n'+i
		sendmail(message) 
