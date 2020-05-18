import food_itens as fi
import day_meals as dm
foodClass = fi.FoodItem()
dayMealsClass = dm.DayMeals()
def main():
    b = True
    while(b):
        print("MENU")
        option = int(input("1 - Adicionar Componente? \n2 - Cadastrar Refeição? \n3 - Visualiazar resumo do dia? \n4 - Visualizar resumo de todos os dias?\n5 - Visualizar resumo por refeição  \n6 - Sair>"))

        if (option == 1):
            first = True
            while True:
                if first:
                    addItem()
                    first = False
                else: 
                    if input("Mais 1?: S/N: ").upper() == "S":
                        addItem()
                    else:
                        break
        elif (option == 2):
            resp = addMeal()
            if resp:
                b = False
            
        elif (option == 3):
            resp =  choose_day()
            showDayResume(resp)
        elif (option == 4):
            showAllDayResume()
        elif (option == 5):
            showMealResume()
        elif (option == 6):
            print("Thanks")
            break


def addMeal():
    day = choose_day()
    meal = choose_meal()
    response = False
    if meal:
        print("Beleza, agora vamos preencher os intens.\n")
        ingredients = {}
        f = True
        while f:
            ingredientName = input("Nome: ")
            if foodClass.getItem(ingredientName) == False:
                resp = input("Nao achamos esse item aqui na base!\n Deseja adiconar? (s/n) ")
                if resp.lower() == 's':
                    addItem()
                    print("Ok, pode tentar novamente")
                    continue
                elif resp.lower() == 'n':
                    return False
            ingredientQtd = input("Quantidade (g): " )
            if float(ingredientQtd) % 2 == 0:
                ingredientQtd = int(ingredientQtd)
            else:
                ingredientQtd = float(ingredientQtd)
            # validar ingrediente
            ingredients[ingredientName] = ingredientQtd
            resp =  input("\noutro? (S/N) -> ")
            if resp.lower() == 'n':
                f = False
                response = False
        if not response:       
            dayMealsClass.addDayMeal(meal,ingredients,day)
    
    return response
            
def addItem():
    print("New Item")
    name = input("Name: ")
    properties = {}

    properties["carbohydrate"] = float(input("carbs g/(100g): "))
    properties["protein"] = float(input("protein g/(100g): "))
    properties["energy"] = int(input("energy kcal/(100g): "))
    properties["sodium"] = float(input("sodium mg/(100g): "))*1000
    properties["fibre"] = int(input("fibre g/(100g): "))
    properties["lipid"] = int(input("lipid g/(100g): "))


    foodClass.create(name.lower(), properties)


         
def showDayResume(date=None):
    #if not day: day = str(date.today())
    print("\n")
    
    response = dayMealsClass.getAmountPropertiesByDay(date)
    
    print("---------------------------------------------------------------\n")
    print ("---- {} ----".format(date))
    print('Cafe da manha:')
    show_properties(response['beakfast'])
    print('Almoco:')
    show_properties(response['lunch'])
    print('Lanche:')
    show_properties(response['afternoon-snack'])
    print('Jantar:')
    show_properties(response['dinner'])
    print('Total:')
    show_properties(response['total'])
    print("---------------------------------------------------------------")
    
def showMealResume():
    day= choose_day("da refeicao ")
    mealName = choose_meal()
    meals = dayMealsClass.getMealsByDay(day)
    meal_info = dayMealsClass.getAmountPropertiesByMeal(meals[mealName])
    show_properties(meal_info)
    
def choose_day(plus=""):
    resp = input("Me diz, voce deseja visualizar o resumo {} de hoje? (s/n) \n>".format(plus))
    if resp.lower() == 's':
        resp = None
    elif resp.lower() == 'n':
        resp = input("\nok, entao me diz o dia certinho .... (AAAA-MM-DD)\n>")
    
    return resp
    
def choose_meal():
    op = False
    while not op:
        op = input("\n 1- Cafe da Manha\n 2- Almoço\n 3- Lanchinho\n 4- Janta\n>")
        op = int(op)
        meal = None
        if op == 1: 
            meal = "breakfast"
        elif op == 2: 
            meal = "lunch"
        elif op == 3:
            meal = "afternoon-snack"
        elif op == 4:
            meal = "dinner"
        else:
            print("\nopção invalida, tente de novo")
            op = False
    return meal
def show_properties(meal):
    # todo -> move properties to day_meals  and put the properties in food_item like a array
    print('   carbs: {}g\n   prot: {}g\n   energia: {}kcal\n   sodio: {}mg\n   lipidios: {}g\n   fibras: {}g\n'.format(meal['carbohydrate'],meal['protein'],meal['energy'],meal['sodium'],meal['lipid'],meal['fibre']))
    
def showAllDayResume():
    resume = dayMealsClass.getAllDaysResume()

    for key in list(resume.keys()):
        print('DIA: ',key)
        show_properties(resume[key])
        
            


if __name__ == '__main__':
    main()

