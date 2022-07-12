from TheGuardian_credentials import api_key
import requests
import json

# set up base url
base_url = "https://content.guardianapis.com/"

# set up parameters
search_keyword = 'privacy'
data_format = 'json'
section = 'technology'
from_date = '2000-01-01'	
to_date = '2022-01-01'
page_size = 199
order_by = 'oldest'
lang = 'en'


# combine url
finalized_url = "{}search?/q={}&format={}&section={}&from-date={}&to-date={}&page-size={}&order-by={}&lang={}&api-key={}".format(base_url, search_keyword, data_format, section, from_date, to_date, page_size, order_by, lang, api_key)

# perform the request and print the query
r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

# output the responses to a file
Guardian = json.loads(r.text)
with open('Guardian_data_query1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

