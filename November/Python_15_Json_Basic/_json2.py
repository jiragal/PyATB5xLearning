# Extracting COVID information from free api to csv file
import requests
import json
import csv


url = "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true"
# Extracting COVID information from free api to csv file
response = requests.get(url=url)
print(response.text)
data = json.loads(response.text)
region_data = data['regionData']