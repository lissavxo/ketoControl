import json
import os

class FoodItem:
    def __init__(self):
        self.base_food_info = './base_food_info.json'

    def create(self,item_name, params):
        # self.validade(params)
        item = {
            item_name: params
        }
        data = None
        if os.path.exists(self.base_food_info):
            with open(self.base_food_info) as json_file:
                data = json.load(json_file)
                data.update(item)
                #jsom.dump(data, json_file, ensure_ascii=False)
        else:
            print ('we dont find a path', self.base_food_info)

        with open(self.base_food_info, 'w') as f:
            json.dump(data, f, ensure_ascii=False)
            
    # def validateParams(self, params):
    #     if(params[""])

    def getItem(self, item_name, id=None):
        response = None

        with open(self.base_food_info) as file_data:
            itens = json.load(file_data)
            names = list(itens.keys())
            if item_name in itens:
                response = itens[item_name]
            else:
                response = False
        return response

    def getPropertyByItem(self,item_name,property_):
        #print(item_name, property_)
        if(item_name =="jejum"):
            return 0
        item = self.getItem(item_name)
        response = item[property_]
        
        return response 

    def getCarbsByItem(self,item_name):
        if item_name == "jejum":
            return False
        else:
            return self.getPropertyByItem(item_name,"corbohydrate")

    def getEnergyByItem(self,item_name):
        if item_name == "jejum":
            return False
        else:
            return self.getPropertyByItem(item_name,"energy")

    def getSodiumByItem(self,item_name):
        if item_name == "jejum":
            return False
        else:
            return self.getPropertyByItem(item_name,"sodium")

    def formatedProperties(self):
        return {"carbohydrate":0,"protein":0,"energy":0,"sodium":0}
        



