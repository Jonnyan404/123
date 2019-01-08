# zabbix-AWS_SQS-monitor

> AWS SQS status monitor with zabbix
> zabbix通过 AWS 云api 自动发现、监控阿里云RDS-Mysql数据库  
> 本版本数据的图表展示，是以**监控项进行分组**.

使用方法
注意事项
脚本会收集RDS别名，
不要默认别名
不要使用中文别名（zabbix不识别）
切记aliyun-python-sdk-core==2.3.5，新版本的sdk有bug
环境要求
python = 2.7

模块安装
/usr/local/python2.7/bin/pip2.7 install aliyun-python-sdk-core==2.3.5 aliyun-python-sdk-rds datetime
使用方法
从阿里云控制台获取 AccessKey ,并修改脚本中的 ID 与 Secret
修改区域 RegionId
将两个脚本放置于以下目录
/etc/zabbix/script
chmod +x /etc/zabbix/script/*
修改zabbix-agentd.conf，添加以下内容
#rds
UserParameter=rds.discovery,/usr/local/python2.7/bin/python2.7 /etc/zabbix/script/discovery_rds.py
UserParameter=check.rds[*],/usr/local/python2.7/bin/python2.7 /etc/zabbix/script/check_rds.py $1 $2 $3
重启zabbix-agent
zabbix控制台导入模板，并关联主机
