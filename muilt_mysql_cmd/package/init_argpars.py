#coding=utf8

import MySQLdb
import argparse
import threading
import re
def parse_args():
    #nargs：命令行参数的个数，一般使用通配符表示，其中，'?'表示只用一个，'*'表示0到多个，'+'表示至少一个
    #action='store_true' 表明该参数不接受参数传递， 即， 只接受 -t 或 --tcp 下面是错误例子 -t tcp  或 --tcp=yes 
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--username",help="input MySQL user")
    parser.add_argument("-p","--password",help="input MySQL user's password")
    parser.add_argument("-H","--hostname",nargs= "+",default="127.0.0.1",help="input MySQL user's password")
    parser.add_argument("-P","--port",default=3306,type=int,help="input MySQL port")
    parser.add_argument("-D","--database",default="",help="database name")
    parser.add_argument("-Q","--SQL",help="SQL")
    parser.add_argument("-t","--tcp",help="only tcp",action="store_true")
    parser.add_argument("-T","--thread",help="muilt thread",default=1,type=int)
    parser.add_argument("--charset",help="chaset ",default="utf8")

#    host_name = re.sub(r'\s+'," ",args.hostname)

    args = parser.parse_args()
    args_dict=vars(args)
    if isinstance(args.hostname,str):
        host_list_str = args_dict['hostname']
        host_list = list(host_list_str.split())
    else:
        host_list = args_dict['hostname']
    
    host_dict={}
    host_dict['hostname'] = host_list
    del args_dict['hostname']

    mysql_args_dict=args_dict


    return mysql_args_dict,host_dict
    


if __name__ == '__main__':
    args_dict = parse_args()
    print args_dict
