import requests
import json
import csv
import time

currentAPIKey = 0
delay = 20 # This is a fail over as a default setting

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
    if currentAPIKey == len(_API_KEYS)-1:
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

# Reading the CSV
with open("import.csv") as resource_csv:
    csv_read = csv.reader(resource_csv, delimiter=",")
    line_count = 0
    # Creating a loop for each row in the CSV
    for row in csv_read:
        # Running the following segment if the currently selected line is the first line in the CSV
        if line_count == 0:
            # Printing the current working column
            print(f'Initializing scans using the following column: {", ".join(row)}\n')
            # Writing header to the export CSV
            with open("export.csv", mode='w') as export_csv:
                export_write = csv.writer(export_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                export_write.writerow(['Resource', 'MD5', 'SHA256'])
            # Updating the line counter
            line_count += 1
        else:
            # Determining delay based on the number of API Keys available
            delay = DetermineDelay()
            time.sleep(delay)
            # Rotating the API Key after use
            currentAPIKey = CurrentAPIKeyRoation()
            # Setting new API Key
            _API_KEY = _API_KEYS[currentAPIKey]
            print(f"Key in use: {currentAPIKey}") #DEBUG
            # Crafting and sending a new request
            r = CraftRequest(_API_KEY, row[0])
            data = r.json()
            if data["response_code"]==1:
                # Writing results to "export.csv"
                with open("export.csv", "a") as export_csv:
                    export_write = csv.writer(export_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    export_csv.write(row[0]+","+data["md5"]+","+data["sha256"]+"\n")
                print("Resource: "+row[0])
                print("MD5: "+data["md5"])
                print("SHA256: "+data["sha256"])
            else:
                print(f"{row[0]} is currently not on record.")
                with open("export.csv", "a") as export_csv:
                    export_write = csv.writer(export_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    export_csv.write(row[0]+","+"No Record"+","+"No Record"+"\n")
            print("\n")
            # Updating line counter
            line_count += 1
    # Printing total number of resources queried
    print(f'Processed {line_count} resources.')
