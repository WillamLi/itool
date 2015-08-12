#!/bin/python
#codint=utf-8

import MySQLdb
import sys
from optparse import OptionParser




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
    parser.add_option("-w","--where",dest="where",default="",help="Input U Where")
    
    
    (options,args)=parser.parse_args()
    
    len_argv=len(sys.argv[1:])
    if len_argv == 0 :
        print parser.print_help()
        parser.exit(1)
    if not options.db or not options.tb or not options.hostname:
        print 'Need database and table'
    else:
        exec("argv_dict ="+str(options))
        return argv_dict

    
def Mysql_con(config):
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
        return cursor
    except Exception,e:
        print "con mysql err:",e






def GetCloumn(db_name,table_name,config):
    cursor = Mysql_con(config)
    cloumn_sql = """select concat(group_concat(COLUMN_NAME)) from information_schema.COLUMNS where table_schema = '%s' and table_name = '%s'""" %(db_name,table_name)
    cursor.execute(cloumn_sql)
    result = cursor.fetchall()
    for i in result:
        cloumn = i[0]
    return cloumn






def Result_sql(db_name,table_name,config):
    cloumn = GetCloumn(db_name,table_name,config)
    cloumn_list = list(cloumn.split(','))
    vlues_concat_sql = ''
    for i in cloumn_list:
        pass
        vlues_concat_sql +=  "\"'\",IFNULL(%s,''),\"',\"," % (i)
    vlues_concat_sql =  vlues_concat_sql[:-3] + vlues_concat_sql[-2:-1]
    db_tb = db_name+"."+table_name
    sql = """select concat('insert into %s(%s) values(',%s,')') from %s""" % (db_tb,cloumn,vlues_concat_sql,db_tb)
    if not config['where']:
        str_2 = sql
        print "str:",str_2
    else:
        where1 = config['where']
        str_2 = sql + " where " + where1 
        print "str:",str_2

def main():
    config = CHECK_ARGV()
    result=Result_sql(config['db'],config['tb'],config)

    

if __name__ == '__main__':
    main()
