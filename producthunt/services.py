import os
import json
import requests

def get_totalcases(year, author):
    url = 'https://api.thevirustracker.com/free-api?global=stats' 
    params = {'total_cases': total_cases}
    print(params)
    r = requests.get(url, params=params)
    corona = r.json()
    books_list = {'totalcases':corona['results']}
    return books_list