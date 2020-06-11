import os
import time
import requests
print('if you need multiple requests separate them with commas')
ping = input('Enter ping.php location: ')
requests.get(ping)
while True:
	time.sleep(15)
	requests.get(ping)
	print('ping command send')
	
