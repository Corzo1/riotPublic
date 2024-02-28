import json
import requests


def get_puuid():
    inp = str(input("acc name: "))
    inp = inp.lower()
    url = (
        "https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
        + inp
        + "?api_key="
    )
    z = requests.get(url)
    zJson = z.json()
    puuid = str(zJson.get("puuid"))
    return puuid
