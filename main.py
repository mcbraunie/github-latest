# Micah Braun
# Lesson 06 - Assignment 1
# GitHub API Latest Activity Script
# Final Modifications: 05/30/2019
import sys
import json

import requests

# Access functionality via terminal:
# python main.py 

if __name__ == "__main__":
	try:
		# obtain user input
		username = input('Enter a valid GitHub username: ')
		# list range
		user_history = list(range(0, 10))
		# URL for requests lib to hook into
		response = requests.get("https://api.github.com/users/{}/events".format(username))
		# event count (for formatting only)
		count = 1

		# iteration over list within range of user's event history
		for item in user_history:    
			event = response.json()[item]['type']
			tstamp = response.json()[item]['created_at']
			# newline
			print()
			# message
			print('Event {}.) GitHub user {}, performed the following activity: {} on {}'.format
		    	(count, username, event, tstamp))
			# newline
			print()
			# increment count, after event 10, loop will end
			count+=1

	# was introduced as potential error-catching block, doesn't appear
	# to be necessary
	except NameError as e:
		print('{} is not a recognized username. Program ending...'.format(username))
		# print(e)

	# on incorrect username entry, KeyError is thrown and e = 0
	except KeyError as e:
		print('"{}" is not a recognized username. Please try running again with\
		 a correct name.'.format(username))
		# print(e)


    
