#!/usr/bin/env python
# encoding: utf-8

#sudo easy_install fabric
#fab -f mult.py dotask

from fabric.api import *

#操作一致的服务器可以放在一组，同一组的执行同一套操作
env.roledefs = {
            'testserver': ['user1@host1:port1',],  
            'realserver': ['user2@host2:port2', ]
            }

#env.password = '这里不要用这种配置了，不可能要求密码都一致的，明文编写也不合适。打通所有ssh就行了',否则如果不声明env.password，执行到对应机器时会跳出要求输入密码的交互

@roles('testserver')
def task1():
    run('ls -l | wc -l')

@roles('realserver')
def task2():
    run('ls ~/temp/ | wc -l')

def dotask():
    execute(task1)
    execute(task2)
