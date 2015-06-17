#!/usr/bin/python
#coding=utf-8


import pexpect
import threading


class oSorMs:
    def __init__(self):
        self.type = type
        self.cmd = cmd
        print self.type

    def choIce(type, ip,username,cmd,*password):
        print type
        self.type = type
        print "self.type",self.type
        if self.type == linux:
            print "type",os
            print "other",ip,username,cmd
            osCmd(ip,username,cmd,*password)
        elif self.type == mysql:
            mysqlCmd()
        else :
            print "noCmd type"

    def osCmd(ip,username,cmd,*password):
        ret = -1
        ssh = pexpect.spawn('ssh %s@%s "%s"' % (username,ip,cmd))
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
            print "EOF"
            ssh.close()
            ret = -1
        except pexpect.TIMEOUT:
            ssh.close()
            ret = -2
        
        return ret

#    def mysqlCmd()
            
a=oSorMs()
#print a.choIce()
b=a.choIce('linux','10.108.14.19','work','ls')      
print b      
