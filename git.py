import requests,json,argparse
from bs4 import BeautifulSoup
import time

parser = argparse.ArgumentParser()
parser.add_argument('--target', action='store', dest='target', help='Specify the target github user.')
parser.add_argument('--token', action='store', dest='apikey', help='Specify your github api key')
parser.add_argument('--cookie', action='store', dest='cookie', help='Specify github cookie')
results = parser.parse_args()
target = results.target
apikey = results.apikey
cookie = results.cookie
page = 1
loop = True
while loop == True:
    queryurl = "https://api.github.com/users/{0}/repos?page={1}&per_page=100?access_token={2}".format(target,page,apikey)
    r = requests.get(queryurl, headers={'Authorization': 'token {0}'.format(apikey)})
    response = r.json()
    if response != "[]":
        page += 1
        for repos in response:
            url = "https://github.com/{0}/{1}/wiki/_new".format(target,repos["name"])
            n = requests.get(url,headers={'Cookie': cookie})
            time.sleep(3)
            if "Create new page" in n.text:
                print("https://github.com/{0}/{1}/wiki/_new".format(target,repos["name"]))
    else:
        loop = False
