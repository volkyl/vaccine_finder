#!/usr/bin/env python3

import json
import time
from datetime import datetime

import requests
import yagmail
from geopy import distance

# Personalize the below constants to suit your needs
MY_HOME = (0, 0)
MAX_DISTANCE_MILES = 25
SLEEP_PERIOD_SECONDS = 30
FROM_EMAIL_ADDRESS = ""
FROM_EMAIL_PASSWORD = ""
TO_EMAIL_ADDRESS = ""


def find_vaccine():
    recent_stores = []

    while True:
        response = json.loads(requests.get("https://www.vaccinespotter.org/api/v0/states/CA.json").text)

        for feature in response['features']:
            place = feature['properties']
            store_id = place['id']
            if place['appointments_available']:
                if store_id not in recent_stores:
                    if _is_near_me(feature['geometry']['coordinates']):
                        message_text = "{}: {} at {} {} has appointments! {}".format(datetime.now().time(),
                                                                                     place['name'],
                                                                                     place['city'],
                                                                                     place['address'],
                                                                                     place['url'])
                        print(message_text)
                        _send_email(place, message_text)
                        recent_stores.append(store_id)
            else:
                if store_id in recent_stores:
                    recent_stores.remove(store_id)
        time.sleep(SLEEP_PERIOD_SECONDS)


def _is_near_me(coordinates):
    point = (coordinates[1], coordinates[0])
    return distance.distance(MY_HOME, point).miles < MAX_DISTANCE_MILES


def _send_email(place, message_text):
    yag = yagmail.SMTP(FROM_EMAIL_ADDRESS)
    yag.send(
        to=TO_EMAIL_ADDRESS,
        subject="{} {} available".format(place['name'], place['address']),
        contents=message_text
    )


yagmail.register(FROM_EMAIL_ADDRESS, FROM_EMAIL_PASSWORD)
find_vaccine()
