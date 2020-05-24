import json
import os
from datetime import date
import file_handler as fh
import food_itens as fi



class DayMeals:
    def __init__(self):
        self.day_meals_file= './day_meals.json'
        self.foods = fi.FoodItem()
    

    def addDayMeal(self,meal,params,_date=None):
        if not _date: _date = str(date.today())
        
        # verifying if day exists in data base
        days = fh.getJson(self.day_meals_file)
        date_list = []

        for _id in days:
            date_list.append(days[_id].get("date"))
        
        if _date not in date_list:
            self.addDay(_date)
            days = fh.getJson(self.day_meals_file)

        if days:
            for _id in list(days.keys()):
                # veryfing if day is in the base
                if days[_id].get("date") == _date:
                    # veryfing if the meal already exists 
                    if(meal in days[_id].get("meals")):
                        print("Ihhhhh parece que ja temos um registro dessa refecao aqui, deseja alterar ? ")
                        #todo
                    # sending meal to the base
                    else:
                        days[_id]["meals"][meal] = params
                        days = fh.getUpdatedData(self.day_meals_file,days)
    
            fh.updateJson(self.day_meals_file, days)

    def addDay(self,dayDate=None):
        if not dayDate: dayDate = str(date.today())

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
        
        
    def getMealsByDay(self,day=None):
        if not day: day = str(date.today())
        data = fh.getJson(self.day_meals_file)
        dayKey =None
        for key in list(data.keys()):
            if data[key].get("date") == day:
                dayKey = key
        meals = data[dayKey].get("meals")

        if data[dayKey].get("dayOff"):
            meals = {
                "breakfast": {
                    'jejum':1
                },
                "lunch": {
                    'jejum':1
                },
                "afternoon-snack": {
                    'jejum':1
                },
                "dinner": {
                    "jejum": 1
                }
            }
        if meals:
            return meals
        else:
            print("Error | day_meals | getMealsByDay", meals,day)
    
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
    
    def getAllDaysResume(self):
        daysList = fh.getJsonKeys(self.day_meals_file)
        
        result = {}
        
        for day in daysList:
            day_info = fh.getJsonObjectByKey(self.day_meals_file, day)
            resume = self.getAmountPropertiesByDay(day_info["date"])
            result[day] = {}
            result[day]["total"] = resume['total']
            result[day]["date"] = day_info["date"]
            

        if result:
            return result
        else:
            print("Error | day_meals | getAllDaysResume")
                
    
    
        
        


    
    





