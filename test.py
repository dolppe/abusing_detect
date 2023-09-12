import requests

headers = {
    'accept': 'application/json',
    'x-api-key': 'GfWsaQabFx841lpntCkbG16ym46BFY019ck8GrEv',
}

#response = requests.options('https://open-api.bser.io/v1/rank/top/9/1', headers=headers)  #랭킹
response = requests.options('https://open-api.bser.io/v1/rank/top/9/1', headers=headers)
#response = requests.options('https://open-api.bser.io/v1/user/games/697828', headers=headers)  #랭킹
#response = requests.get('https://open-api.bser.io/v1/rank/top/1/1', headers=headers) #TOP 1000
#response = requests.get('https://open-api.bser.io/v1/data', headers=headers)


#response = requests.options('https://open-api.bser.io/v1/games/16566937', headers=headers)      #특정 게임의 매치 정보

#response = requests.get('https://d1wkxvul68bth9.cloudfront.net/l10n/l10n-Korean-20220404074450.txt', headers=headers)  

print(response.content)
print(response.text)
#https://open-api.bser.io/v1/user/games/392179 특정 유저 최근 전적
#sessionid => 9가 한국
#match type 1이 솔로




