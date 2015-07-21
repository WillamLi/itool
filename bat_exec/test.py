#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect

def ssh_cmd(username, ip, passwd, cmd):
    ret = -1
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (username,ip, cmd))
    try:
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)
        if i == 0 :
            ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('password: ')
            ssh.sendline(passwd)
        ssh.sendline(cmd)
        r = ssh.read()
        print r
        ret = 0
    except pexpect.EOF:
    	ssh = pexpect.spawn('ssh %s@%s "%s"' % (username,ip, cmd))
        r = ssh.read()
	print r
        print "EOF"
        ssh.close()
        ret = -1
    except pexpect.TIMEOUT:
        print "TIMEOUT"
        ssh.close()
        ret = -2

    return ret 

ssh_cmd('work', '10.105.11.47','work','ls')
