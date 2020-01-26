"""Example REST API call with urllib.request"""
import urllib.request
import json
from random import choice

baseurl = "https://restcountries-v1.p.rapidapi.com/alpha/"
country = choice(["hu", "de", "fr", "us", "jp", "kr", "cn"])
headers = {'x-rapidapi-host':
           "restcountries-v1.p.rapidapi.com",
           'x-rapidapi-key':
           "2e00962308msh48d80e5c383cfcfp11cafdjsn8335711ec5f1"}
request = urllib.request.Request(url=baseurl+country,
                                 headers=headers, 
                                 method="GET")
with urllib.request.urlopen(request) as response:
    result = json.load(response)
    print(f'Country:     {result["name"]}')
    print(f'Capital:     {result["capital"]}')
    print(f'Population:  {result["population"]:,}')
    print(f'Currencies:  {" ".join(result["currencies"])}')
    print(f'Native name: {result["nativeName"]}')
    print(f'Borders:     {" ".join(result["borders"])}')
    print(f'Languages:   {" ".join(result["languages"])}')
    # Uncomment last line to see full data
    # print(json.dumps(result, indent=4))