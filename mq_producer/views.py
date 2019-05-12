from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from mq_test.kafka_con import kafka


class Producer(View):

    def get(self):
        kafka.mq


