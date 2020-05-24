import json
import os
import csv

def updateJson(file_name,data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f, ensure_ascii=False)    
    except:
         print("Error | file_handler | updateJson")

def getUpdatedData(file_name, new_data):
    data = None 
    with open(file_name) as json_file:
                data = json.load(json_file)
                data.update(new_data)
    if not data:
        print("Error | file_handler | getUpdatedData")
    return data

def addCsvLine(file_name,name):
    try:
        with open('file_name', 'a', newline='') as csvfile:
            data = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            data.writerow([name])
    except:
        print ("Error | file_handler | addCsvLine")


def getCsv(file_name):
    response = []
    with open(file_name, newline='') as csvfile:
        datasheet = csv.reader(csvfile, quotechar='|')
        for row in datasheet:
            row = "".join(row)
            response.append(row)
    if not len(response) > 0:     
        response =  False
        print('Error | file_handler | getCsv')
    
    return response
    


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
    return list(data.keys())

def getJsonObjectByKey(file_name, key):
    response = None
    with open(file_name) as json_file:
        data = json.load(json_file)
        response = data[key]
    
    if not response : 
        print("Error | file_handler | getJsonObjectByKey")
    return response 

