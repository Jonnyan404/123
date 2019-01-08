# coding=utf-8
# Auther:Jonnyan

import boto3
import json

# 账号相关信息
region = "cn-northwest-1" # 这是中国宁夏区域,其它区域请自查.
access_key = "xxxxxx"
secret_key = "xxxxxxx"


# 获取主队列列表并封装
def getSQSMainQueueByComponent():
    DBInstanceIdList = []
    SQSDataDict = {}
    # 登录 sqs
    sqs = boto3.client('sqs', region_name=region, aws_access_key_id=access_key,
                       aws_secret_access_key=secret_key)
    # 获取带有 prod 的队列信息
    queues = sqs.list_queues(
        QueueNamePrefix='prod'
    )
    # 处理队列信息,取出队列名称列表
    sp1 = ''.join(queues["QueueUrls"]).split('/')
    res1 = sp1[::4]
    sp2 = "".join(res1).split('https:')
    res2 = sp2[1:]
    # 循环添加字典到列表
    for x in res2:
        DBInstanceIdDict = {}
        DBInstanceIdDict["{#QUEUESNAME}"] = x
        DBInstanceIdList.append(DBInstanceIdDict)
    # 格式化为 json 格式
    SQSDataDict['data'] = DBInstanceIdList
    print json.dumps(SQSDataDict)


# 获取死信队列列表(未完成)
def getSQSDeadLetterQueueByComponent():
    '''
    可参考:https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_dead_letter_source_queues
    :return:
    '''
    DBInstanceIdList = []
    SQSDataDict = {}
    # 登录 sqs
    sqs = boto3.client('sqs', region_name=region, aws_access_key_id=access_key,
                       aws_secret_access_key=secret_key)

    response = sqs.list_dead_letter_source_queues(
        QueueUrl='string'
    )

if __name__ == '__main__':
    getSQSMainQueueByComponent()
