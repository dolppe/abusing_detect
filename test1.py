import requests

headers = {
    'accept': 'application/vnd.api+json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwYzYzOTdmMC04YjE2LTAxM2EtMzVmZS0yMTljOWI0OWJjOGMiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjQ3ODQ3NTQ2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InRlYW1pbmctZGV0ZWN0In0.Inlh7349ju3JCoIPWWm2qmmunrNU-YxGJqyB-RL2UJY',
}

response = requests.get('https://api.pubg.com/shards/steam/matches/b9d5d772-26e4-4145-aae3-335d8b605c83', headers=headers)

print(response)