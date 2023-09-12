import json
import os
from pandas import json_normalize
import pandas
import requests
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import time

def getUserJson():
    file_path = "Ranking_Sol.json"
    print(os.listdir(os.getcwd()))
    userNumArr = []
    with open(file_path,'r',encoding='UTF8') as file:
        json_file = json.load(file)
    for js in json_file["topRanks"]:
        #userNumArr.append((js["userNum"],js["nickname"]))
        userNumArr.append(js["userNum"])
    return userNumArr
arr = getUserJson()


headers = {
    'accept': 'application/json',
    'x-api-key': 'GfWsaQabFx841lpntCkbG16ym46BFY019ck8GrEv',
    'encoding': 'UTF-8',
}

#response = requests.options('https://open-api.bser.io/v1/user/games/308142', headers=headers)

#response = requests.get('https://open-api.bser.io/v1/user/games/'+ str(arr[0])+'?next=15244526', headers=headers)
response = requests.get('https://open-api.bser.io/v1/user/games/'+ str(arr[0]), headers=headers)

firstArr = []
secondArr = []

while(True):
    time.sleep(1)
    text = response.text
    info = json.loads(text)
    if 'next' in info:
        next = info['next']
        for js in info['userGames']:
            firstArr.append(js['bestWeaponLevel'])
            secondArr.append(js['gameRank'])
        print(next)
    else:
        for js in info['userGames']:
            firstArr.append(js['bestWeaponLevel'])
            secondArr.append(js['gameRank'])
        break

    response = requests.get('https://open-api.bser.io/v1/user/games/'+ str(arr[0])+'?next='+str(next), headers=headers)

print('asdf')


frame = pandas.DataFrame(arr)



for js in info['userGames']:
    firstArr.append(js['bestWeaponLevel'])
    secondArr.append(js['gameRank'])

points = pandas.DataFrame(firstArr).reset_index(drop=True)
points.columns = ['x']
points.head()

