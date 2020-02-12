import csv

class foodItem:
    def __init__(self,name,wgt,cal,pro,car,fat):
        self.name = name
        self.wgt = wgt
        self.cal = cal
        self.pro = pro
        self.car = car
        self.fat = fat
        
    def description(self):
        print("There are {} calories, {} grams of protein, {} grams of carbohydrates and {} grams of fat in {} grams of {}".format(self.cal,self.pro,self.car,self.fat,self.wgt,self.name))

def menu():
    print("Please select from the following options.\n1. Log Meal\n2. Add Food\n3. Remove Food")
    menuChoice = input("Choice: ")
    
def addFood():
    newFood = foodItem(input("Enter Name: "),input("Enter Weight: "),input("Enter Calories: "),input("Enter Protein: "),input("Enter Carbs: "),input("Enter Fat: "))
    with open("foods.csv","a") as f:
        csvFile = csv.writer(f,delimiter=",")
        csvFile.writerow([newFood.name.lower(),newFood.wgt,newFood.cal,newFood.pro,newFood.car,newFood.fat])

def addMeal():
    foods=[]
    with open("foods.csv","r") as f:
        csvFile = csv.reader(f,delimiter=",")
        for row in csvFile:
            tempFoods=[]
            for item in row:
                try:
                    tempFoods.append(int(item))
                except ValueError:
                    tempFoods.append(item)
            foods.append(tempFoods)
            
    print(foods)
addFood()
addMeal()