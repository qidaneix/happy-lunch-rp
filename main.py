#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import schedule
import time

def job():
    r = requests.get('http://lunch.xiaodabao.xyz/')
    print r.content

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)