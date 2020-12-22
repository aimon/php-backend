from django.conf import settings
import sys
import requests
import urllib

apiUrl = settings.SEMAPHORE.get("API_URL")
apikey = settings.SEMAPHORE.get("API_KEY")
sendername = settings.SEMAPHORE.get("SENDER_ID")


def send_message(number, message):
    print("Sending Message...")
    params = (
        ("apikey", apikey),
        ("sendername", sendername),
        ("message", message),
        ("number", number),
    )
    path = apiUrl + "?" + urllib.parse.urlencode(params)
    requests.post(path)
    print("Message Sent!", urllib.parse.urlencode(params))


send_sms = send_message
