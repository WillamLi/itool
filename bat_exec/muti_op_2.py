#!/usr/bin/env python
#coding=utf-8
import pexpect
import threading
import os
import sys
import time
from optparse import OptionParser

#optparse - python 2.7+ argparse

#fileName,oper,ip,user,command

def CHECK_ARGV():
    m_argv = {}
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage,version="%prog 1.0")
    parser.add_option("-f","--file",dest="ip_file",
           help="ip filename",metavar="ip_filename")
    parser.add_option("-t","--type",dest="con_type",
            help="connect type ssh or mysql",metavar="con_type")
    parser.add_option("-i","--ip",dest="ip",default="",
            help="ip and ip_filename Parameters can not Coexist",metavar="ip")
    parser.add_option("-u","--user",dest="username",default="",
            help="connect ip username",metavar="username")
    parser.add_option("-c","--command",dest="command",default="",
            help="You need execut command",metavar="command")
    (options,args) = parser.parse_args()
    len_argv=len(sys.argv[1:])
    if len_argv == 0 :
        print parser.print_help()
        parser.exit(1)
    m_argv=str(parser.values)
    exec("m_argv="+m_argv)
    return m_argv

def ANALYZE_OPTIONS():
    sp='-'
    m_argv=CHECK_ARGV()
    try:
        url=m_argv['url']
        result = urllib2.urlopen(url)
    except urllib2.URLError,e:
        print "error"
    if sp in m_argv['page']:
        page_all=m_argv['page'].split(sp)
        page=xrange(int(page_all[0]),int(page_all[1])+1)
        m_argv['page']=page
        return m_argv
    else:
        page=m_argv['page']
        m_argv['page']=page
        return m_argv



ip=''

if len(sys.argv) < 5:
    print "fileName,oper,ip,user,command"



def choIce(self):
    if self.ssh_mysql == 'ssh':
        print "Type is: ",self.ssh_mysql
        osCmd()
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


if __name__ == '__main__':
    CHECK_ARGV()
