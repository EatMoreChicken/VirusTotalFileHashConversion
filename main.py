import requests
import json
import csv
import time

# This script should be split to individual tasks once they are developed
''' 
	Naming:
	"_" and all caps means a constant: _API_KEY
	Starts with cap and no _ means function: PrintAPI
 '''

'''
TODO
Add a menu system
Add batch file reputation lookup
Add properties file (JSON?)
'''

# Defining all GLOBAL variables
currentAPIKey = 0
delay = 20 # This is a fail over for a default setting


# Defining all functions here for now
# Function for printing the API KEY
def PrintAPI():
	print("============================= API KEY =============================")
	print(_API_KEY)
	print("===================================================================")
# Function to craft request with "x":_API_KEY and "y":"resource"
def CraftRequest(x, y):
	url = "https://www.virustotal.com/vtapi/v2/file/report"
	params = {"apikey": x, "resource": y}
	r = requests.get(url, params=params)
	return r
# Function to import API Keys
def ImportAPIKeys():
	with open("apikeys.csv", newline="") as api_keys:
		_API_KEYS = list(csv.reader(api_keys))
		return _API_KEYS
# Function to rotate API Key used
def CurrentAPIKeyRoation():
	global currentAPIKey
	if currentAPIKey == len(_API_KEYS)-1:# We are substracting 1 because ARRAYS START AT 0
		return 0
	else:
		currentAPIKey += 1
		return currentAPIKey
# Function to determine the proper delay
def DetermineDelay():
	totalKeys = len(_API_KEYS)
	totalRequests = totalKeys*3.5
	delay = 60//totalRequests
	return delay

#START
# Importing API Keys
_API_KEYS = ImportAPIKeys()
_API_KEY = "" # Enter API here for testing

# Reading the CSV
with open("import.csv") as resource_csv:
	csv_read = csv.reader(resource_csv, delimiter=",")
	line_count = 0
	for row in csv_read:
		if line_count == 0:
			print(f'Initializing scans using the following column: {", ".join(row)}\n')
			line_count += 1
		else:
			delay = DetermineDelay()
			time.sleep(delay)
			currentAPIKey = CurrentAPIKeyRoation()
			_API_KEY = _API_KEYS[currentAPIKey]
			print(f"Key in use: {currentAPIKey}") #DEBUG
			r = CraftRequest(_API_KEY, row[0])
			data = r.json()
			if data["response_code"]==1:
				# print(f"Converting {row[0]} to MD5: "+data["md5"])
				# print(f"Converting {row[0]} to SHA256: "+data["sha256"])
				print("Resource: "+row[0])
				print("MD5: "+data["md5"])
				print("SHA256: "+data["sha256"])
			else:
				print(f"{row[0]} is currently not on record.")
			print("\n")
			line_count += 1
	print(f'Processed {line_count} resources.')