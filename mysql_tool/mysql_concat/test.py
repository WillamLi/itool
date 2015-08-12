#!/bin/python
#coding=utf-8

import MySQLdb
import sys
from optparse import OptionParser



user_value="reboot"
pass_value='reboot123'
port_value=3306




def CHECK_ARGV():
    argv_dict = {}
    usage = "usage: %prog [options] arg1 arg2" 
    parser = OptionParser(usage)
    parser.add_option("-H","--host",dest="hostname",help="hostname,you DB Hostname or IP")
    
    parser.add_option("-d","--database",dest="db",help="read database ")
    parser.add_option("-t","--table",dest="tb",help="read table")
    parser.add_option("-u","--user",dest="user",help="conn user")
    parser.add_option("-p","--passwd",dest="passwd",help="conn passwd")
    parser.add_option("-P","--port",dest="port",default=3306,help="MySQL Port")
    parser.add_option("-C","--character",dest="character",default='utf8',help="MySQL Charset")
    parser.add_option("-E","--SQL",dest="execsql",default="",help="Input U Exec SQL")
    
    
    (options,args)=parser.parse_args()
    
    len_argv=len(sys.argv[1:])
#    print "len_argv:",len_argv
    if len_argv == 0 :
        print parser.print_help()
        parser.exit(1)
    if not options.db or not options.tb or not options.hostname:
        print 'Need database and table'
    else:
        #print type(parser.values)
        #m=str(parser.values)
        exec("argv_dict ="+str(options))
 #       print argv_dict
#        print type(argv_dict)
        return argv_dict
        #print type(options)
        #return n
        #return options 
#        print "---------"


def Mysql_con(config):
#    print config
    host_value = config['hostname']
    user_value = config['user']
    passwd_value = config['passwd']
    db_value = config['db']
    tb_value = config['tb']
    port_value = config['port']
    charset_value = config['character']
    print host_value,user_value,passwd_value,db_value,tb_value,port_value,charset_value    

    try:
        db = MySQLdb.connect(user=user_value,host=host_value,passwd=passwd_value,port=port_value,charset=charset_value)
        cursor = db.cursor()
#    sql="select * from lr.tt"
#    cursor.execute(sql) 
#    result = cursor.fetchall()
#    print result   
        return cursor
    except Exception,e:
        print "---",e


if __name__ == '__main__':
    a=CHECK_ARGV()
#    print a
#    print type(a)
    cursor = Mysql_con(a)
    print cursor
    sql="select * from lr.tt"
    cursor.execute(sql) 
    result=cursor.fetchall()
    print result   
