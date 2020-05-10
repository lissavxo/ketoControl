import json
import os

def updateJson(file_name,data):
    with open(file_name, 'w') as f:
            json.dump(data, f, ensure_ascii=False)

def getUpdatedData(file_name, new_data):
    data = None 
    with open(file_name) as json_file:
                data = json.load(json_file)
                data.update(new_data)
    if not data:
        print("Error | file_handler | getUpdatedData")
    return data

def getJson(file_name):
    data = None
    if os.path.exists(file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)
            #print(data)
    else:
        print(file_name)
    if not data : 
        print("Error | file_handler | getJson")
    return data 

def getJsonKeys(file_name):
    data = getJson(file_name)
    return data.keys()

def getJsonObjectByKey(file_name, key):
    response = None
    with open(file_name) as json_file:
        data = json.load(json_file)
        response = data[key]
    
    if not response : 
        print("Error | file_handler | getJsonObjectByKey")
    return response 