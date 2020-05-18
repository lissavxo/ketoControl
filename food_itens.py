import json
import os
import file_handler as fh

class FoodItem:
    def __init__(self):
        self.nutrition_facts_file = './nutrition_facts.json'
        self.properties_file = './properties.csv'
        self.properties = fh.getCsv(self.properties_file)

    def create(self,item_name, params):
        # self.validade(params)
        item = {
            item_name: params
        }
        data = None
        if os.path.exists(self.nutrition_facts_file):
            with open(self.nutrition_facts_file) as json_file:
                data = json.load(json_file)
                data.update(item)
                #jsom.dump(data, json_file, ensure_ascii=False)
        else:
            print ('we dont find a path', self.nutrition_facts_file)

        with open(self.nutrition_facts_file, 'w') as f:
            json.dump(data, f, ensure_ascii=False)
    

    def addPropertyByItem(self,item_name,_property):
       
        response = None
        food_list = fh.getJsonKeys(self.nutrition_facts_file)

        if item_name in food_list:

            item = fh.getJsonObjectByKey(self.nutrition_facts_file,item_name)
            try:
                item[_property]
                response = (" %s : %s " %(item[_property], _property))
            except:
                #print("excecao", item_name)
                value = float(input('%s -(100g): '%_property))
                item[_property] = value
                new_item = {item_name:item}
                data = fh.getUpdatedData(self.nutrition_facts_file,new_item)
                fh.updateJson(self.nutrition_facts_file,data)
                response = 'added'

        else:
            print("Error | food_itens | addPropertyByItem | We cant find %s in our base!" % item_name)
        return response
    
    def addNewProperty(self,_property):
        food_list = fh.getJsonKeys(self.nutrition_facts_file)
        try:
            for food in food_list:
                print(food)
                if type(_property) == list:
                    for p in _property:
                        response = self.addPropertyByItem(food,p)
                else:
                    response = self.addPropertyByItem(food,_property)
                
                if response:
                    print(response)
            fh.addCsvLine(self.properties_file,_property)
        except:
            print("Error | food_itens | addNewProperty ")

        
    # def validateParams(self, params):
    #     if(params[""])

    def getItem(self, item_name, id=None):
        response = None
        itens = fh.getJson(self.nutrition_facts_file)
        if item_name in list(itens.keys()):
            response = itens[item_name]
        else:
            print("Error | food_itens | getItem", item_name)
            response = False

       
        return response

    def getPropertyByItem(self,item_name,property_):
        #print(item_name, property_)
        if(item_name =="jejum"):
            return 0
        item = self.getItem(item_name)
        response = item[property_]
        if type(response) != int and type(response) != float:
            print("Error | food_itens | getPropertyByItem", item_name,property_)
        return response

    def formatedProperties(self):
        response = {}
        for _property in self.properties:
            response[_property] = 0
        return response
        


# fi = FoodItem()

# fi.addNewProperty(["lipid","fibre"])