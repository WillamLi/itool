#!/bin/python
#coding=utf8


import MySQLdb
import threading
import sys
import time
#def conn_db(**mydict,host_list):
def conn_db(mydict,host_list):
#    print mydict
    for hostname in host_list:
        print hostname,"------,111111111"
#        print mydict['username']
        try:
            conn = MySQLdb.connect(host = hostname,user = mydict["username"],passwd = mydict["password"],db = mydict["database"],port = mydict["port"],charset = mydict["charset"],connect_timeout=3)
        except Exception,e:
            print "MySQLdb.err",":",e
        
        cursor = conn.cursor()
        sql = mydict['SQL']
        sql1 = "select connection_id()"
        cursor.execute(sql)
        result=cursor.fetchall()
        #for i in result:
        #    print i
        for a,b in result:
            print "Thread: ",threading.current_thread().getName(),"hostname:"+hostname,a,b,"end"
        #    print a,b
        cursor.execute(sql1)
        conn.commit()
        conn.close()


def muilt_dbthread(mydict,host_dict):
    threads=[]
    host_list=host_dict['hostname']
    thread_num=mydict['thread']
    if thread_num == 1:
        conn_db(**mydict) 
    elif thread_num > len(host_dict['hostname']):
        print "thread_num is not more then host"
        exit()      
    else:
        host_len=len(host_dict['hostname'])
        #host_muilt_size=host_len % thread_num
        host_part_size=host_len/thread_num
        host_last_begin_size=(thread_num-1)*host_part_size
        host_last_index_begin = host_last_begin_size
        host_last_index_end = host_len
        host_rangelist=[(x,x+host_part_size) for x in xrange(0,host_len,host_part_size) if x < host_last_begin_size]
        print host_rangelist
        for host in host_rangelist:
            #host_index = "%d:%d" % host
            host_index_begin =  host[0]
            host_index_end =  host[1]
            host_thread_list = host_list[host_index_begin:host_index_end]
            #host_dict['hostname'] = host_thread_list
            print "host_thread_list:",host_thread_list
#            threads.append(threading.Thread(target = conn_db,name = "Threadasdf-"+str(threads_num),kwargs = mydict)) 
            threads.append(threading.Thread(target = conn_db,args=(mydict,host_thread_list),kwargs = {})) 
            print "add OK"
        else:
            host_last_thread_list = host_list[host_last_index_begin:host_last_index_end]
            #mydict['hostname'] = host_last_thread_list
            host_thread_list = host_last_thread_list
            print "host_last_thread_list:",host_thread_list
            threads.append(threading.Thread(target=conn_db,args=(mydict,host_thread_list),kwargs={}))

        for mutil_thread in threads:
            mutil_thread.start()
        for mutil_thread in threads:
            mutil_thread.join()
          
