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
    try:
        with open(file_name) as json_file:
                    data = json.load(json_file)
                    data.update(new_data)
    except:
         print("Warning | file_handler | failed open file: %s" %file_name)
         return 0
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
    try:
        with open(file_name, newline='') as csvfile:
            datasheet = csv.reader(csvfile, quotechar='|')
            for row in datasheet:
                row = "".join(row)
                response.append(row)
    except:
        print('Warning | file_handler | getCsv | Acess document failed')
    if not len(response) > 0:     
        response =  False
        print('Error | file_handler | getCsv')
    
    return response
    


def getJson(file_name):
    data = None
    if os.path.exists(file_name):
        try:
            with open(file_name) as json_file:
                data = json.load(json_file)
                #print(data)
        except:
            print("Error | file_handler | getJson | It breaks tryng to open: %s" %file_name)
            data = 1
            return data 
    else:
        #print(file_name)
        print("Error | file_handler | getJson | We dont find a file in the path especified %s" %file_name)

    if not data : 
        print("Error | file_handler | getJson | We don't find the data you need")
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

