import json
import os
from datetime import date
import file_handler as fh
import food_itens as fi



class DayMeals:
    def __init__(self):
        self.day_meals_file= './day_meals.json'
        self.foods = fi.FoodItem()
    

    def addDayMeal(self,meal,params):
        dayDate = str(date.today())
        data = None
        with open(self.day_meals_file) as json_file:
                data = json.load(json_file)
                daysDate = []

                for key in list(data.keys()):
                    daysDate.append(data[key].get("date"))

                if dayDate not in daysDate:
                    self.addDay()
                    
                for key in list(data.keys()):

                    if data[key].get("date") == dayDate:

                        if(meal in data[key].get("meals")):
                            print("Ihhhhh parece que ja temos um registro dessa refecao aqui, deseja alterar ? ")
                            #todo
                        else:
                            data[key]["meals"][meal] = params
                            data.update(data)
                            print(data)
                            break



        if data:
            fh.updateJson(self.day_meals_file, data)

    def addDay(self,dayDate=None):
        if dayDate != True: dayDate = str(date.today())

        data = fh.getJson(self.day_meals_file)

        newId = int(max(list(data.keys())))+1

        day = {
            newId:{
                "date":dayDate,
                "meals": {

                }
            }
        }

        data = fh.getUpdatedData(self.day_meals_file,day)
        fh.updateJson(self.day_meals_file,data)

        
    # def getAllDaysResume(self):
    #     daysList = fh.getJson(self.day_meals_file)
        
    #     result = {}
        
    #     for day in daysList:
    #         dayInfo = fh.getJsonObjectByKey(self.day_meals_file)
    #         result[day]['resume'] = self.
        
    #     return result
                
        
        
    def getMealsByDay(self,day=None):
        if not day: day = str(date.today())
        data = fh.getJson(self.day_meals_file)
        dayKey =None
        for key in list(data.keys()):
            if data[key].get("date") == day:
                dayKey = key
        meals = data[dayKey].get("meals")
        return meals
    
    def getAmountPropertiesByDay(self, day=None):
        
        meals = self.getMealsByDay(day)
        breakfastAmount = self.getAmountPropertiesByMeal(meals['breakfast'])
        lunchAmount =  self.getAmountPropertiesByMeal(meals['lunch'])
        dinnerAmount =  self.getAmountPropertiesByMeal(meals['dinner'])
        afternoon_snackAmount = self.getAmountPropertiesByMeal(meals['afternoon-snack'])
        
        response = {
            'beakfast':breakfastAmount,
            'lunch':lunchAmount,
            'afternoon-snack':afternoon_snackAmount,
            'dinner':dinnerAmount
        }
        
        total = self.foods.formatedProperties()
        for value in response.values():
            for valueByProperty in list(value.keys()):
                amountProperty = value[valueByProperty]
                total[valueByProperty] = round(total[valueByProperty] + amountProperty)
        response['total'] = total

        return response
        
                
                
    def getAmountPropertiesByMeal(self ,meal):

        amountDay = self.foods.formatedProperties()
        
        for item in meal:
            
            for _property in list(amountDay.keys()):
                amountProperty = 0 
                amountProperty = self.foods.getPropertyByItem(item,_property)
                amountProperty = (meal[item]*amountProperty)/100
                
                    
                amountDay[_property] = round(amountDay[_property] + amountProperty)
                
        return amountDay
    
    
        
        
        #print(meals)
        

        
        
        
        

        
        
    
    
    





