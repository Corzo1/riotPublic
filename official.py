import json
import requests
import getdeets
from pprint import pprint

puuid = getdeets.get_puuid()

riotchall = requests.get(
    "https://oc1.api.riotgames.com/lol/challenges/v1/player-data/" + puuid + "?api_key="
)
riotdesc = requests.get(
    "https://oc1.api.riotgames.com/lol/challenges/v1/challenges/config?api_key="
)


def get_rank(challengeRank):
    if challengeRank == " level: NONE":
        challengeRank = 0
    elif challengeRank == " level: IRON":
        challengeRank = 1
    elif challengeRank == " level: BRONZE":
        challengeRank = 2
    elif challengeRank == " level: SILVER":
        challengeRank = 3
    elif challengeRank == " level: GOLD":
        challengeRank = 4
    elif challengeRank == " level: PLATINUM":
        challengeRank = 5
    elif challengeRank == " level: DIAMOND":
        challengeRank = 6
    elif challengeRank == " level: MASTER":
        challengeRank = 7
    elif challengeRank == " level: GRANDMASTER":
        challengeRank = 8
    elif challengeRank == " level: CHALLENGER":
        challengeRank = 9
    return challengeRank


def clean_string(d):
    d = str(d)
    d = d.strip()
    d = d.replace("{", "")
    d = d.replace("}", "")
    d = d.replace("'", "")
    return d


def replace_chars(list):
    newList = []
    for i in list:
        convert = i.split()[0]
        convert = challenge_name(convert)
        rank = int(i.split()[1])
        rank = rank_name(rank)
        convert += " RANK: "
        convert += rank
        newList.append(convert)
    return newList


def challenge_name(id):
    for data in ids:
        if id == data.split()[1]:
            finished = data.split(" ", 2)[2]
            return finished
        else:
            continue


def rank_name(challengeRank):

    if challengeRank == 0:
        challengeRank = "UNRANKED"
    elif challengeRank == 1:
        challengeRank = "IRON"
    elif challengeRank == 2:
        challengeRank = "BRONZE"
    elif challengeRank == 3:
        challengeRank = "SILVER"
    elif challengeRank == 4:
        challengeRank = "GOLD"
    elif challengeRank == 5:
        challengeRank = "PLATINUM"
    elif challengeRank == 6:
        challengeRank = "DIAMOND"
    elif challengeRank == 7:
        challengeRank = "MASTER"
    elif challengeRank == 8:
        challengeRank = "GRANDMASTER"
    elif challengeRank == 9:
        challengeRank = "CHALLENGER"
    return challengeRank


with open("riotchall.json", "w") as f:
    challenges = []
    chall = []
    xJson = riotchall.json()
    for d in xJson["challenges"]:

        d = clean_string(d)
        challenges.append(d)
    for challengeData in challenges:
        challengeRank = challengeData.split(",")[-3]
        challengeRank = get_rank(challengeRank)
        challengeId = challengeData.split(",")[0]
        challengeId = str(challengeId)
        challengeId = challengeId.replace("challengeId: ", "")
        challenge = challengeId + " " + str(challengeRank)
        chall.append(challenge)
    sortedc = sorted(chall, key=lambda s: s[-1])
    f.write(json.dumps(xJson, indent=4, sort_keys=False))


with open("riotdesc.json", "w") as z:
    yJson = riotdesc.json()
    ids = []

    for i in yJson:

        descID = i.get("id")
        descName = i.get("localizedNames")["en_AU"]["name"]
        descDetails = i.get("localizedNames")["en_AU"]["shortDescription"]
        desc = (
            "id: "
            + str(descID)
            + " name: "
            + str(descName)
            + " description: "
            + str(descDetails)
        )
        clean_string(desc)
        ids.append(desc)
    sortedIds = sorted(ids, key=lambda s: int(s.split()[1]), reverse=False)
    z.write(json.dumps(yJson, indent=4, sort_keys=False))

with open("base.txt", "w") as p:
    p.write("\n".join(sortedIds))

with open("mystats.txt", "w") as mystats:
    newL = replace_chars(sortedc)
    mystats.write("\n".join(newL))
    print("done")
