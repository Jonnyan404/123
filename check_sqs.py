# coding=utf-8
# Auther:Jonnyan404

import sys
import boto3
import datetime

# 账号相关信息
region = "cn-northwest-1" # 中国宁夏区域,其它区域请自查.
access_key = "xxxxxx"
secret_key = "xxxxxx"

# 接收外部参数
Type = sys.argv[1]
Queuesname = sys.argv[2]
Key = sys.argv[3]

# 相关指标
metrics = {
    "SentMessageSize": {"type": "float", "value": None},
    "ApproximateNumberOfMessagesDelayed": {"type": "float", "value": None},
    "NumberOfMessagesSent": {"type": "float", "value": None},
    "NumberOfEmptyReceives": {"type": "float", "value": None},
    "ApproximateNumberOfMessagesVisible": {"type": "float", "value": None},
    "ApproximateNumberOfMessagesNotVisible": {"type": "float", "value": None},
    "NumberOfMessagesReceived": {"type": "float", "value": None},
    "ApproximateAgeOfOldestMessage": {"type": "float", "value": None},
    "NumberOfMessagesDeleted": {"type": "float", "value": None}
}

# 时间戳 UTC
end = datetime.datetime.utcnow()
start = end - datetime.timedelta(minutes=5)

# 登录 cloudwatch
cloudwatch = boto3.client(
    'cloudwatch',
    region_name=region,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

for k, v in metrics.items():
    if (k == Key):
        try:
            res = cloudwatch.get_metric_statistics(
                Namespace='AWS/SQS',
                MetricName=k,
                Dimensions=[
                    {
                        'Name': 'QueueName',
                        'Value': Queuesname
                    },
                ],
                StartTime=start,
                EndTime=end,
                Period=300,
                Statistics=[
                    'Average',
                ],
            )
        except Exception, e:
            print "[ERROR] %s" % e
            sys.exit(1)
        # 结果为空或者不支持,一律返回0.404
        if not res:
            average = res['Datapoints'][-1]["Average"]
        else:
            average = 0.404
        print "%s" % (average)
        break
