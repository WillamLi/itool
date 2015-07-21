#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import MySQLdb
import os
import sys
import time
from optparse import OptionParser

user_value="autopilot";pass_value="YTkzNDJjZDRhNWMyNzJkOTZiMTllMTI4";port_value=3306;

def main():
    parser = OptionParser()
    parser.add_option("-H","--host",dest="hostname",help="hostname,please use replica!!!It will taste lots I/O !!!if not,ensure: SET GLOBAL innodb_stats_on_metadata = OFF;")
    
    parser.add_option("-d","--database",dest="db",default="%",help="the database need to stats: suport %")
    parser.add_option("-t","--table",dest="tb",default="%",help="tables need to stats: suport %")
    
    parser.add_option("-l","--lines",dest="lines",default="",help="if rows more than lines, then print")
    
    parser.add_option("-o","--order",dest="orderby",default="",help="order by :db,table_name,table_rows,ibd,idx,total(seperated by ',')")
    
    parser.add_option("-T","--topN",dest="topN",default="",help="numbers like :10 or 10,100 ,if result topN: default all")
    
    (options,args)=parser.parse_args()
    

    
    #stat1 = "SELECT table_schema as 'DB',table_name as 'TABLE',CONCAT(ROUND((data_length + index_length)/(1024 * 1024 * 1024), 2), 'G') 'TOTAL' FROM information_schema.TABLES"
    #stat2 = "ORDER BY data_length + index_length DESC"
    stat1 = "SELECT table_schema as 'DB',table_name,TABLE_ROWS,CONCAT(ROUND(data_length/(1024 * 1024 * 1024), 2),'G') as IBD,CONCAT(ROUND(index_length/(1024 * 1024 * 1024), 2),'G') as IDX,CONCAT(ROUND((data_length + index_length)/(1024 * 1024 * 1024), 2), 'G') 'TOTAL' FROM information_schema.TABLES "
    where1 = " "
    where2 = " "
    where3 = " "
    order1 = " "
    limit1 = " "

    db=MySQLdb.connect(user=user_value,host=options.hostname,passwd=pass_value,port=port_value,charset='utf8')
    cursor = db.cursor()    
    
    statement = """show global variables like 'innodb_stats_on_metadata'"""
    cursor.execute(statement)
    s = cursor.fetchone()
    if s[1] == "on":
        statement = """SET GLOBAL innodb_stats_on_metadata = OFF"""
        cursor.execute(statement)
    
    statement = ""
       
    if options.db:
        if options.tb or options.lines:
            where1 = "TABLE_SCHEMA like '%s' and " %options.db
        else:
            where1 = "TABLE_SCHEMA like '%s' " %options.db
        
    if options.tb:
        if options.lines:
            where2 = "TABLE_NAME like '%s' and " %options.tb
        else:
            where2 = "TABLE_NAME like '%s' " %options.tb
        
    if options.lines:
        iline = int(options.lines)
        where3 = "TABLE_ROWS > %d " %(iline)
    
    if options.orderby:
        order1 = "order by %s desc " %options.orderby
    
    if options.topN:
        itop = int(options.topN)
        limit1 = "limit %d" %(itop)

    if options.db or options.tb or options.lines:
        statement = stat1 + "where " + where1 + where2 + where3 + order1 + limit1
    else:
        statement = stat1 + order1 + limit1
       
    cursor.execute(statement)
    results = cursor.fetchall()
    print "DB\t\t    Table\t\t\t\t\t  TABLE_ROWS  Data    Index   TOTAL\t"
    for row in results:
        DB = row[0]
        TABLE = row[1]
        TABLE_ROWS = row[2]
        IBD = row[3]
        IDX = row[4]
        TOTAL = row[5]
        print "%-20s%-45s%10s%8s%8s%8s" %(DB,TABLE,TABLE_ROWS,IBD,IDX,TOTAL)
    statement = """SET GLOBAL innodb_stats_on_metadata = on"""
    cursor.execute(statement)
        
main()
