from flatten_json import flatten
import urllib.parse
import pandas as pd
import requests
import json

def generate_proxies():

    SCRAPER_API_KEY="PUT_YOUR_API_HERE"

    proxies = {
        "http": "http://scraperapi:"+SCRAPER_API_KEY+"@proxy-server.scraperapi.com:8001"
    }

    return proxies


def extrat_params_from_url(url):
    
    parsed_url = urllib.parse.urlparse(url)
    query_string = parsed_url.query

    parsed_json = json.loads(urllib.parse.unquote(query_string).split("searchQueryState=")[1])

    params={"searchQueryState":parsed_json}

    cat1=[
        "listResults",
        "mapResults",
    ]

    cat2=["total"]

    wants={

        "cat1":cat1,
        "cat2":cat2,
    }

    params["wants"]=wants

    params["searchQueryState"]["pagination"]["currentPage"]=1

    return params


def extract_zillow_data(params,ouput_file):

    headers = {
        'authority': 'www.zillow.com',
        'accept': '*/*',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.zillow.com',
        'referer': 'https://www.zillow.com/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    flattened_results=[]

    

    while True:

        if PROXY:
            proxies=generate_proxies()
            response = requests.put("https://www.zillow.com/async-create-search-page-state", headers=headers, json=params,proxies=proxies)
        else:
            response = requests.put("https://www.zillow.com/async-create-search-page-state", headers=headers, json=params)


        json_response=response.json()

        results=json_response["cat1"]["searchResults"]["listResults"]

        print(" "+str(len(results))+" New results found!")

        for result in results:

            flattened_result=flatten(result)

            flattened_results.append(flattened_result)

        if params["searchQueryState"]["pagination"]["currentPage"] < json_response["cat1"]["searchList"]["totalPages"]:

            params["searchQueryState"]["pagination"]["currentPage"]+=1

        else:

            break



    df = pd.DataFrame(flattened_results)

    df.to_excel(ouput_file, index=False)




PROXY=False

url=input("\n Please provide a zillow search URL: ")

ouput_file=input("\n Save as (eg: data.xlsx)?: ")

params = extrat_params_from_url(url)

extract_zillow_data(params,ouput_file)

