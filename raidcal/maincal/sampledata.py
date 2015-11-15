# -*- coding: utf-8 -*-

from raidcal.maincal.models import Topic, Message
from django.contrib.auth.models import User


def generate_sampledata(options):
    threads = int(options.get('thread_count', 10))
    posts = int(options.get('post_count', 10))
    user = User.objects.get(pk=1)

    for m in xrange(0, threads):
        topic = Topic()
        topic.title = u'Lorem ipsum dolor sit amet'
        topic.user = user
        topic.save()
        for k in xrange(0, posts):
            message = Message()
            message.topic = topic
            message.user = user
            message.content = u'Lorem Ipsum dolor sit amet <a href="asdasd">aasdasdasd</a>'
            message.save()
