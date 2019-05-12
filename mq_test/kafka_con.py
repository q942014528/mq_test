# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 09:41
# @Author  : huanghaohao
# @Email   : haohao.huang@easytransfer.cn
# @File    : kafka_con.py
# @Software: PyCharm


from pykafka import KafkaClient


class Kafka(object):

    def __init__(self, host='127.0.0.1:9092'):
        self.mq = KafkaClient(hosts=host)





kafka = Kafka()