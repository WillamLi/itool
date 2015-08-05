#!/bin/sh

function Zhifu_xm_grants()
{
hostname=$1
egrep -v '^#|^$' ip.list | while read line
do
    hostname=`echo ${line}|awk '{printf $1}'`
    gran_group_file=${hostname}.sql
    egrep -v '^#|^$' ip2.list | while read line
    do
        old_ip=`echo ${line}|awk '{printf $1}'`
        new_ip=`echo ${line}|awk '{printf $2}'`
        #echo "-- old_ip:$old_ip,new_ip:$new_ip"
        sh ./xm-grant -h ${hostname} -o ${old_ip} -n ${new_ip} |tee -a ${gran_group_file}
    done
done
}

Zhifu_xm_grants
