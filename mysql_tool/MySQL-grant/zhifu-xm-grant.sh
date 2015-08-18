#!/bin/sh



CLONE="False"
DROPUSERIP="False"


function Zhifu_xm_grants()
{

egrep -v '^#|^$' ip.list | while read line
do
    hostname=`echo ${line}|awk '{printf $1}'`
    gran_group_file=${hostname}.sql
    egrep -v '^#|^$' ip2.list | while read line
    do
        old_ip=`echo ${line}|awk '{printf $1}'`
        new_ip=`echo ${line}|awk '{printf $2}'`
#        echo "-- old_ip:$old_ip,new_ip:$new_ip"
#DORP
        if [ $CLONE = "False" -a $DROPUSERIP = "True" ];then
            sh ./xm-grant -v -D -h ${hostname} -o ${old_ip} -n ${new_ip} |tee -a ${gran_group_file}
        fi
        if [ $DROPUSERIP = "False" -a $CLONE = "True" ];then
#clone
            sh ./xm-grant  -h ${hostname} -o ${old_ip} -n ${new_ip} |tee -a ${gran_group_file}
        fi
    done
done
}


function usage(){
    echo "Usage: $0 [OPTIONS]"
    echo -e "\tClone user:\t$0 -C"
    echo -e "\tDrop user@ip:\t$0 -D"
    echo -e "\n\tOther:\n\t\t-h see xm-grants help \n\t\t-C Clone ip \n\t\t-D drop user"
}


while getopts 'DC' OPT
do
    case $OPT in
        C)
            CLONE="True";;
        D)
            DROPUSERIP="True";;
        \?)
            usage
            exit -1;;
    esac
done

if [ $OPTIND -le 1 ];then
    usage
    exit 2
fi    

Zhifu_xm_grants


