# zabbix-AWS_SQS-monitor

> AWS SQS status monitor with zabbix
> zabbix通过 AWS 云api 自动发现、监控阿里云RDS-Mysql数据库  
> 本版本数据的图表展示，是以**监控项进行分组**.

## 使用方法
### 注意事项
脚本会收集所有带 prod 关键字队列名称，
不要使用中文名称（zabbix不识别）

### 环境要求
python = 2.7
需要模块 boto3

### 模块安装
/usr/local/python2.7/bin/pip2.7 install boto3

### 使用方法
1. 从 AWS 云控制台获取 AccessKey ,并修改脚本中的 Access 与 Secret
2. 修改区域 RegionId
3. 将两个脚本放置于以下目录
`/etc/zabbix/script`
`chmod +x /etc/zabbix/script/*`
4. 修改zabbix-agentd.conf，添加以下内容
```shell
#sqs
UserParameter=rds.discovery,/usr/local/python2.7/bin/python2.7 /etc/zabbix/script/discovery_rds.py
UserParameter=check.rds[*],/usr/local/python2.7/bin/python2.7 /etc/zabbix/script/check_rds.py $1 $2 $3
```
5. 重启zabbix-agent
6. zabbix控制台导入模板，并关联主机
