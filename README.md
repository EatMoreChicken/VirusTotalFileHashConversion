# VirusTotal Automated File Hash Conversion
The program is designed to leverage VirusTotal to convert file hashes for files known to VT.

## Important Information
Requirements:
  - Python 3
  - Install the following Python modules:
    - requests
      - To install: `pip install requests`
    - json
      - Preinstalled module with Python 3, no need to install with pip
    - csv
      - Preinstalled module with Python 3, no need to install with pip
    - time
      - Preinstalled module with Python 3, no need to install with pip

## TODO
- Menu
- Properties file
- Add batch file reputation lookup

## Setup
### Create "imports.csv"
Create an empty CSV called `import.csv`. This CSV will contain all of the file hashes that need to be converted. In the first row and column, enter a name/header for the column, such as `File Hashes`. Below the header, populate the MD5, SHA256 or both hashes that need to be converted.

### Create exports.csv
Create an empty CSV called `exports.csv`. No need to populate this file with anything, that will be done by the program. This CSV will contain the resource, MD5, and SHA256 conversions after the program have run successfully. This file is cleaned automatically before every run.

### Create apikeys.csv
Create an empty CSV called `apikeys.csv`. Do not enter a column name/header in this file, it is not needed. Populate the CSV with API keys from VirusTotal. This program needs at least 2 API keys to function properly Each API key is limited to 4 queries per minute. Adding an API key adds 4 available queries per minute. The program will automatically calculate the query speed.

## Running the program
  1. Populate the `imports.csv` with the MD5 and SHA256 files you would like to convert. Make sure that the column has a header, such as "Hashes".
  2. Ensure that your API keys are populated in the 'apikeys.csv' file with no column header.
  3. Ensure that the empty file `exports.csv` has been created.
  4. Run `main.py`
