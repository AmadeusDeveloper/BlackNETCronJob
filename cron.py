import os
import time
import requests
ping = input('Enter ping.php location: ')
remove = input('Enter remove.php location: ')
requests.get(ping)
requests.get(remove)
while True:
	time.sleep(15)
	requests.get(ping)
	print('ping command send')
	requests.get(remove)
	print('remove command send')
	