from re import A
from TheGuardian_credentials import api_key
import requests
import pandas as pd
from pprint import pprint
import json

# 2000
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2000-01-01&to-date=2000-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

# perform the request and print the query
r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

# output the responses to a file
Guardian = json.loads(r.text)
with open('Guardian_data_2000.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2000.json')

# 2001
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2001-01-01&to-date=2001-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2001.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2001.json')

# 2002
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2002-01-01&to-date=2002-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2002.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2002.json')

# 2003
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2003-01-01&to-date=2003-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2003.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2003.json')

#2004
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2004-01-01&to-date=2004-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2004.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2004.json')

# 2005
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2005-01-01&to-date=2005-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2005.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2005.json')

# 2006
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2006-01-01&to-date=2006-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2006.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2006.json')

# 2007
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2007-01-01&to-date=2007-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2007.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2007.json')

# 2008
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2008-01-01&to-date=2008-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2008.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2008.json')

# 2009
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2009-01-01&to-date=2009-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2009.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2009.json')

# 2010-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2010-01-01&to-date=2010-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2010_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2010_1.json')

# 2010-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2010-6-30&to-date=2010-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2010_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2010_2.json')

# 2011-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2011-01-01&to-date=2011-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2011_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2011_1.json')

# 2011-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2011-6-30&to-date=2011-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2011_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2011_2.json')

# 2012-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2012-01-01&to-date=2012-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2012_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2012_1.json')

# 2012-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2012-6-30&to-date=2012-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2012_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2012_2.json')

# 2013-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2013-01-01&to-date=2013-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2013_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2013_1.json')

# 2013-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2013-6-30&to-date=2013-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2013_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2013_2.json')

# 2014-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2014-01-01&to-date=2014-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2014_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2014_1.json')

# 2014-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2014-6-30&to-date=2014-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2014_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2014_2.json')

# 2015-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2015-01-01&to-date=2015-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2015_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2015_1.json')

# 2015-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2015-6-30&to-date=2015-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2015_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2015_2.json')

# 2016-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2016-01-01&to-date=2016-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2016_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2016_1.json')

# 2016-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2016-6-30&to-date=2016-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2016_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2016_2.json')

# 2017-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2017-01-01&to-date=2017-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2017_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2017_1.json')

# 2017-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2017-6-30&to-date=2017-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2017_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2017_2.json')

# 2018-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2018-01-01&to-date=2018-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2018_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2018_1.json')

# 2018-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2018-6-30&to-date=2018-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2018_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2018_2.json')

# 2019-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2019-01-01&to-date=2019-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2019_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2019_1.json')

# 2019-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2019-6-30&to-date=2019-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2019_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2019_2.json')

# 2020-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2020-01-01&to-date=2020-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2020_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2020_1.json')

# 2020-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2020-6-30&to-date=2020-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2020_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2020_2.json')

# 2021-1
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2021-01-01&to-date=2021-6-30&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2021_1.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2021_1.json')

# 2021-2
finalized_url = "https://content.guardianapis.com/search?/&format=json&section=technology&from-date=2021-6-30&to-date=2021-12-31&order-by=oldest&page-size=199&q=%27privacy%27&api-key=test"

r = requests.get(url = finalized_url, verify=False)

print(finalized_url, '\t')

Guardian = json.loads(r.text)
with open('Guardian_data_2021_2.json', 'w') as outfile:  json.dump(Guardian, outfile, indent=4)

df = pd.read_json('Guardian_data_2021_2.json')