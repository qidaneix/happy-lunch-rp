#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import requests
import schedule
import cv2

cap = cv2.VideoCapture(0)
# set the Horizontal resolution
cap.set(3, 1280)
# Set the Vertical resolution
cap.set(4, 720)

while (cap.isOpened()):
    def job():
        # take a photo
        return_value, image = cap.read()

        if return_value == True:
            # save the photo, use current time as name
            image_name = time.strftime('images/%Y-%m-%dT%H:%M:%S',time.localtime(time.time())) + '.jpg'

            # get image height, width
            (h, w) = image.shape[:2
                                ]
            # calculate the center of the image
            center = (w / 2, h / 2)
            # Perform the counter clockwise rotation holding at the center
            # rotate 180 degrees
            M = cv2.getRotationMatrix2D(center, 180, 1.0)
            image_rotated180 = cv2.warpAffine(image, M, (w, h))

            # save the photo
            cv2.imwrite(image_name, image_rotated180)
            print(image_name + ' image written!')

            try:
                # send a http request
                url = 'http://lunch.xiaodabao.xyz/image'
                files = {'file': open(image_name, 'rb')}
                r = requests.post(url, files = files)
                # handle http response
                print(r.content)
            except:
                pass

            # delete image
            os.remove(image_name)
            print(image_name + ' image deleted!')

    schedule.every(10).seconds.do(job)

    while (True):
        schedule.run_pending()
        time.sleep(1)

cap.release()