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
inday = input("Check in date?: ")
intime = input("Check in time?: ")
data['checkinday'].update({inday:intime})
#print(data)
with open('data_file.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(json.dumps(data, ensure_ascii=False, indent=4))
