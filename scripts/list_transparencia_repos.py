# Python program to read
# json file
  
import json
import os
  
# Get transparencia-mg repos
os.system('gh repo list transparencia-mg --json url > transparencia_repo.json')

# Opening JSON file
f = open('transparencia_repo.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

print(f'Organização transparencia-mg tem {len(data)} repositórios!')  

# Iterating through the json
# list
for i in data:
    print('- [ ]', i['url'])

# Closing file
f.close()

# Remove transparencia_repo.json files
os.system('rm transparencia_repo.json')