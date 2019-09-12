# Virus Total Automation
Program designed to leverage Virus Total to conduct semi-automated OSINT and hash conversions of know files on VT.

## TODO
- Menu
- Properties file
- Add batch file reputation lookup

## Setup
### imports.csv
This CSV contains the file hashes to convert. The first row contains the header and all additional rows contain either the MD5 or SHA256 (or a mix) to use as a resource to lookup. Currently additional columns are not used.
### exports.csv
This CSV will contain the resource, MD5, and SHA256 conversions after the program has ran successfully. This file is cleaned before every run.
### apikeys.csv
This CSV contains is where your free or premium API key should be inserted. One API key per row and no column header. This program can use multiple API keys and automatically rotate them when performing conversations. The program will also automatically select the idle time between requests based on the number of API keys within the file.
### main.py
This is currently the home of all functions of the system. The program will be broken up eventually.

## Running the program
  1. Populate the `imports.csv` with the MD5 and SHA256 files you would like to convert. Make sure that the column has a header, such as "Hashes".
  2. Ensure that your API key(s) is populated in the 'apikeys.csv' file with no column header.
  3. Run `main.py`
