import json
import urllib.request


# loading json data from URL
def load_json_data():
    url = "https://gist.githubusercontent.com/kumarpani/1e759f27ae302be92ad51ec09955e765/raw/184cef7125e6ef5a774e60de31479bb9b2884cb5/TeamRCB.json"
    response = urllib.request.urlopen(url)
    data_json = json.loads(response.read().decode())
    return data_json
