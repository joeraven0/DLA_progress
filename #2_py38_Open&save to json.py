import json
import sys

try:
    #Open file and read json
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
    sys.exit("Program stopped. Create a json-file before running!!!")

#User input to register check in date
inday = input("Check in date?: ")
intime = input("Check in time?: ")
#Add user input to json buffer
data['checkinday'].update({inday:intime})
#Save json buffer data to existing file
with open('data_file.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(json.dumps(data, ensure_ascii=False, indent=4))
