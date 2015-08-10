#!/bin/python
#coding=utf-8

import MySQLdb
import sys
from optparse import OptionParser



user_value="reboot"
pass_value='reboot123'
port_value=3306




def CHECK_ARGV():
    usage = "usage: %prog [options] arg1 arg2" 
    parser = OptionParser(usage)
    parser.add_option("-H","--host",dest="hostname",help="hostname,you DB Hostname or IP")
    
    parser.add_option("-d","--database",dest="db",help="read database ")
    parser.add_option("-t","--table",dest="tb",help="read table")
    
    parser.add_option("-E","--SQL",dest="execsql",default="",help="Input U Exec SQL")
    
    
    (options,args)=parser.parse_args()
    
    len_argv=len(sys.argv[1:])
    print "len_argv:",len_argv
    if len_argv == 0 :
        print parser.print_help()
        parser.exit(1)
    if not options.db or not options.tb or not options.hostname:
        print 'Need database and table'
    else:
        return options 

#def Mysql_con():
#db=MySQLdb.connect(user=user_value,host=options.hostname,passwd=pass_value,port=port_value,charset='utf8')
#cursor = db.cursor()    
    
#statement = options.execsql
#cursor.execute(statement)
#s = cursor.fetchall()

#可以全部到数据库中去执行，也可以查出列之后再单独执行

#table_name = 'tb_pac_glide_history'
def GetCloumn(db_name,table_name):
    cloumn_sql = """select concat(group_concat(COLUMN_NAME)) from information_schema.COLUMNS where table_schema = '%s' and table_name = '%s'""" %(db_name,table_name)
    cursor.execute(cloumn_sql)
    result = cursor.fetchall()
    for i in result:
        cloumn = i[0]
    print cloumn,11111111111
    return cloumn

#GetCloumnSQL('tb_pac_glide_history')

#print cloumn_sql


#cloumn = "ID,ORGI_ID,SETTLE_API,GLIDE_TYPE,BANK_CODE,BIZ_CODE,BIZ_NO,AMOUNT,BIZ_DATE,TRANS_ID,COMPARE_BATCH_NO,COMPARE_DATE,VOUCHER_NO,STANDBY_VOUCHER_NO,GMT_CREATE_ORGI,GMT_CREATE,GMT_MODIFIED,OPERATOR,CONFIRM_OPERATOR,MEMO,CLEARING_FLAG,BRANCH,PAYMENT_SEQ_NO,FUNDS_CHANNEL,BIZ_TYPE,COMPARE_FLAG,ORGI_MEMO,PRODUCT_CODE,PAYMENT_CODE,IS_WRITEOFF,OUT_NO,FILE_NAME,OPERATOR_MEMO,AUDIT_MEMO"

#cloumn = "id,name"

def Result_sql(db_name,table_name):
    cloumn = GetCloumn(db_name,table_name)
    print cloumn,222222222222
    #table_name = GetCloumnSQL('tb_pac_glide_history')
    cloumn_list = list(cloumn.split(','))
    vlues_concat_sql = ''
    #str="select %s from %s values(%s)" % (cloumn,table_name,vlues_concat_sql)
    for i in cloumn_list:
        pass
        #print i
        #vlues_concat_sql += "'IFNULL(%s,'')'," % (i)
        vlues_concat_sql +=  "\"'\",IFNULL(%s,''),\"',\"," % (i)
    #vlues_concat_sql =  vlues_concat_sql[:-1]
    vlues_concat_sql =  vlues_concat_sql[:-3] + vlues_concat_sql[-2:-1]
    print vlues_concat_sql
    #str="select %s from %s values(%s)" % (cloumn,table_name,vlues_concat_sql)
    db_tb=db+"."+tb
    #str_2 = "select concat('insert into %s(%s) values(',%s,')') from %s" % (tabl_name,cloumn,vlues_concat_sql,table_name)
    str_2 = """select concat('insert into %s(%s) values(',%s,')') from %s""" % (db_tb,cloumn,vlues_concat_sql,db_tb)
    print "str:-----------",str_2
    #print str

def main():
    options = CHECK_ARGV()
    hostname = options.hostname
    DB = options.db
    table = options.tb
    db=MySQLdb.connect(user=user_value,host=hostname,passwd=pass_value,port=port_value,charset='utf8')
    cursor = db.cursor() 
    Result_sql(DB,table)
    
    

if __name__ == '__main__':
    main()
    #Result_sql()
