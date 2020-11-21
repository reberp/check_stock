#!/usr/bin/env python

import os
from twilio.rest import Client
from time import sleep

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
from_phone = os.environ.get("from_phone")
to_phone = os.environ.get("to_phone")
client = Client(account_sid, auth_token)


def send_message(url):
	message = client.messages \
                .create(
                     body=url,
                     from_=from_phone,
                     to=to_phone
                 )
	
urls = []

import requests
found=False
while(not found):
	print("Trying again")
	for url in urls:
		try:		
			resp = requests.get(url)
		except Exception as e:
			print("Error: "+url)
			continue
		if (resp.status_code != 200):
			print("ERROR: "+url)
		if ("SOLD OUT" in resp.text) or ("OUT OF STOCK" in resp.text) or ("Notify When Available" in resp.text):
			pass
		else:
			print(url)
			found=True
			send_message(url)
			break
	print("sleeping")
	sleep(20)

