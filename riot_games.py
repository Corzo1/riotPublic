import json
import requests

token = ""
dooma_summoner_id = "t0cMXOZy1X2BiUlRBGsDvZVUXd36Y2v5k64kBtWWZiiJwQ"
dooma_account_id = "HiZWEn_1JSpIKr2G4gobM2zL_ZWzv0XoSouCUcDL2dB7iRY"
dooma_puuid = (
    "somGU5FI3fUVbfQDUShK_XLPq1Mo9ofn6c3QsPTBsfpDJgC8y_ERDbPptwLmto3VRgK4Xfj9uzPGAg"
)

base = "https://oc1.api.riotgames.com/"

x = requests.get(
    base
    + "lol/champion-mastery/v4/champion-masteries/by-summoner/"
    + dooma_summoner_id
    + "?"
    + token
)
with open("riotspam.json", "w") as f:
    parsed = json.loads(x.text)
    parsed.sort(key=lambda x: x["championId"])
    f.write(json.dumps(parsed, indent=4, sort_keys=True))

with open("riotranks.json", "w") as f:
    page = 1
    deezed = []
    deez = requests.get(
        "https://oc1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/DIAMOND/IV?page="
        + str(page)
        + "&"
        + token
    )
    deezed.append(json.loads(deez.text))
    while deez.text != "[]":
        page += 1
        deez = requests.get(
            "https://oc1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/DIAMOND/IV?page="
            + str(page)
            + "&"
            + token
        )
        deezed.append(json.loads(deez.text))

    deezed.pop()
    deezed.sort(key=lambda x: x[0]["summonerName"])
    f.write(json.dumps(deezed, indent=2, sort_keys=False))
    print("lolz ")
