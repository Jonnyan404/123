# zabbix-AWS_SQS-monitor

> AWS SQS status monitor with zabbix
> zabbix通过 AWS 云api 自动发现、监控阿里云RDS-Mysql数据库  
> 本版本数据的图表展示，是以**监控项进行分组**.

## 使用方法
### 注意事项
- 脚本会收集所有带 prod 关键字队列名称，
- 每4分钟取一次数据,可自行在模板上更改.
- 触发器默认只有一条死信队列超过12小时.
- 值 0.404 代表不支持的项目/无数据

### 环境要求
- python = 2.7
- 需要模块 boto3

### 模块安装
/usr/local/python2.7/bin/pip2.7 install boto3

### 使用方法
1. 从 AWS 云控制台获取 AccessKey ,并修改脚本中的 Access 与 Secret
2. 修改区域 RegionId
3. 将两个脚本放置于以下目录
`/etc/zabbix/script`
`chmod +x /etc/zabbix/script/*`
4. 把 zabbix3.4 目录下的 AWSSQS.conf 文件放到被监控主机 /etc/zabbix/zabbix_agentd.d/ 目录下
5. 重启zabbix-agent
6. zabbix控制台导入模板，并关联主机
