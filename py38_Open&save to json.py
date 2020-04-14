import json

try:
    with open('data_file.json') as f:
        data = json.load(f)
        checkinday = data['checkinday']
        checkintime = checkinday['20200411']
        checkoutday = data['checkoutday']
        checkouttime = checkoutday['20200410']

  
    print(checkintime)
    #print(data)
except:
    print("File empty")

data['checkinday'].update({'19950514':'10:19'})
#print(data)
with open('data_filea.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
