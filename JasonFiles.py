import json

jason_data='{"id":101, "name":"Login test","status":"PASS"}'
data = json.loads(jason_data)
print(data)

with open("data.json","w") as f:
    json.dump(jason_data,f)

with open("data.json","r") as f:
    dataa = json.load(f)
    print(dataa)