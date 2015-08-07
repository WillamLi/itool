#!/bin/python
#coding=utf-8


#可以全部到数据库中去执行，也可以查出列之后再单独执行

#table_name = 'tb_pac_glide_history'
def GetCloumnSQL(table_name):
    table_name = table_name
    cloumn_sql = "select concat(group_concat(COLUMN_NAME)) from information_schema.COLUMNS where table_name = '%s'" %(table_name)
    return table_name

#GetCloumnSQL('tb_pac_glide_history')

#print cloumn_sql


cloumn = 'ID,ORGI_ID,SETTLE_API,GLIDE_TYPE,BANK_CODE,BIZ_CODE,BIZ_NO,AMOUNT,BIZ_DATE,TRANS_ID,COMPARE_BATCH_NO,COMPARE_DATE,VOUCHER_NO,STANDBY_VOUCHER_NO,GMT_CREATE_ORGI,GMT_CREATE,GMT_MODIFIED,OPERATOR,CONFIRM_OPERATOR,MEMO,CLEARING_FLAG,BRANCH,PAYMENT_SEQ_NO,FUNDS_CHANNEL,BIZ_TYPE,COMPARE_FLAG,ORGI_MEMO,PRODUCT_CODE,PAYMENT_CODE,IS_WRITEOFF,OUT_NO,FILE_NAME,OPERATOR_MEMO,AUDIT_MEMO'


def Result_sql():
    table_name = GetCloumnSQL('tb_pac_glide_history')
    cloumn_list = list(cloumn.split(','))
    vlues_concat_sql = ''
    #str="select %s from %s values(%s)" % (cloumn,table_name,vlues_concat_sql)
    for i in cloumn_list:
        pass
        #print i
        vlues_concat_sql += "'IFNULL(%s,'')'," % (i)
    str="select %s from %s values(%s)" % (cloumn,table_name,vlues_concat_sql)
    print "str:-----------",str
    print "v_c_s:------------",vlues_concat_sql
    #print str



Result_sql()
