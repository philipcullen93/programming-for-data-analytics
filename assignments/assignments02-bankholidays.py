# Author: Philip Cullen
# Task 1: Write a program called assignment02-bankholdiays.py
# The program should print out the dates of the bank holidays that happen in northern Ireland.

# Task 2: 
# Modify the program to print the bank holidays that are unique to northern Ireland (i.e. do not happen elsewhere in the UK) 
# you can choose if you want to use the name or the date of the holiday to decide if it is unique

# Possible Approach: 
# CSV: I could take the data for Northern Ireland Bank Holidays from https://www.gov.uk/bank-holidays#northern-ireland aand create a CSV file
# However, I would also need to create a CSV file for all the other bank holidays accross the UK, so I could create a program to only print out unique bank holidays to NI

# JSON:  I could take the data for Northern Ireland Bank Holidays from https://www.gov.uk/bank-holidays.json, this gives me all the information I need on all bank holidays across the UK including NI.
# As the JSON file has more information than a CSV file, it should be easier and more straightforward to write a program.
# I have included a much clearer view of the .json file, I use in the bank_holidays.json also in the assignments folder.

# Assignment 02 Bank Holidays
# Part 1: Print the dates of all bank holidays in Northern Ireland

import json
import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# The above pulls all the data on all the UK & NI Bank Holidays
# This next step will be to write code so print() only displays the dates of NI Bank Holidays

ni_holidays = data["northern-ireland"]["events"]
# The above pulls the data on Northern Ireland Bank Holidays
# Now I need to get the dates of the holidays. To ensure accuracy I will also print what Bank Holiday it is.

for bank_holiday in ni_holidays:
    print(f"{bank_holiday["date"]} - {bank_holiday["title"]}")
 
# This print the information in the following format "date of bank holiday - Name of bank holiday"

# Part 2: Print only the holidays unique to NI

holidays_by_regions = {}

for region in data:
    titles = set()
    for holiday in data[region]["events"]:
        titles.add(holiday["title"])
    holidays_by_regions[region] = titles

unique_ni_holidays = []

for holiday in ni_holidays:
    name = holiday["title"]
    is_unique = True

    for region in data:
        if region != "northern-ireland":
            if name in holidays_by_regions[region]:
                is_unique = False
                break

    if is_unique:
        unique_ni_holidays.append(holiday)


print("\nUnique to Northern Ireland:")
for holiday in unique_ni_holidays:
    print(f"{holiday["date"]} - {holiday["title"]}")

            
