#coding=utf8
import MySQLdb
#import threading
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], 'package'))
from init_argpars import parse_args
from muilt_mysql import conn_db,muilt_dbthread



#a=parse_args()
#print a




if __name__ == "__main__":
    mysql_dict,host_dict = parse_args()
    #print mysql_dict
    #print host_dict
#    a=conn_db(**args_dict)
    a=muilt_dbthread(mysql_dict,host_dict)
