#!/usr/bin/python
#coding=utf-8


import pexpect
import threading
import os
import sys
import time


ip=''

if len(sys.argv) < 5:
    print "fileName,oper,ip,user,command"


class batExec(threading.Thread):
#class batExec():
    def __init__(self, ssh_mysql, ip ,username, cmd):
        self.ssh_mysql = ssh_mysql
        self.cmd = cmd
	self.ip = ip
	self.username = username
    

    def choIce(self):
        if self.ssh_mysql == 'ssh':
#            print "Type is: ",self.ssh_mysql
            self.osCmd()
        elif self.ssh_mysql == 'mysql':
            #self.mysqlCmd()
	    pass
        else :
           print "noCmd ssh_mysql"

    def osCmd(self):
        ret = -1
        ssh = pexpect.spawn('ssh %s@%s "%s"' % (self.username, self.ip, self.cmd))
        try:
            i = ssh.expect(['password','continue connecting (yes/no)?'],timeout=5)
            if i == 0 :
                ssh.sendline(passwd)
            elif i ==1:
                ssh.sendline('yes\n')
                ssh.expect('password:')
                ssh.sendline(passwd)
        
            ssh.sendline(cmd)
            r = ssh.read()
            print t
            ret =0
        except pexpect.EOF:
            ssh = pexpect.spawn('ssh %s@%s "%s"' % (self.username, self.ip, self.cmd))
	    r = ssh.read()
	    print r
            #print "EOF"
            ssh.close()
            ret = -1
        except pexpect.TIMEOUT:
            ssh.close()
            ret = -2
        
        return ret

#    def mysqlCmd(self)
            
#a=batExec('ssh','10.105.11.47','work','ls')
#a.choIce()


#sourcefile=sys.path[0]+"/"+sys.argv[1]
#print source

threads = []
threadlock = threading.Lock()

def readIp(sourcefile,ssh_mysql,user,command):
    f = open(sourcefile,'r')
    for ip in f.readlines():
	time_start=time.time()
	print "time_start",time_start
        ip = ip.strip('\n')
        print "ip",ip
    	#batExec(ssh_mysql,ip,user,command).choIce()   
    	a=batExec(ssh_mysql,ip,user,command)   
	a.choIce()
	time_stop=time.time()
	print "time_stop",time_stop
	user_time=time_stop-time_start
	print "user_time",user_time
	
	print "--------------"


def start():
    for i in xrange(4):
	threads.append(threading.Thread(target=batExec,args=(ssh_mysql,ip,user,command)))
    for t in threads:
	t.start()
    for t in threads:
	t.join()



if __name__ == "__main__":
    sourcefile=sys.path[0]+"/"+sys.argv[1]
    ssh_mysql=sys.argv[2]
    user=sys.argv[3]
    command=sys.argv[4]	
#    readIp(sourcefile,ssh_mysql,user,command)
    start()


#b=a.choIce()      
#print b      
