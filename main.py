#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import schedule
import time
import cv2

camera = cv2.VideoCapture(0)

while (camera.isOpened()):
    def job():
        # take a photo
        return_value, image = camera.read()
        # save the photo, use current time as name
        image_name = time.strftime('images/%Y-%m-%dT%H:%M:%S',time.localtime(time.time())) + '.jpg'
        cv2.imwrite(image_name, image)
        print '{} written!'.format(image_name)

        # send a http request
        url = 'http://lunch.xiaodabao.xyz/image'
        files = {'file': open(image_name, 'rb')}
        r = requests.post(url, files = files)
        # handle http response
        print r.content

    schedule.every(5).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

camera.release()