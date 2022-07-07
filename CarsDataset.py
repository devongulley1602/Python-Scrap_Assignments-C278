#Devon Gulley
#Assignment looking at car data set using filter, map, reduce 
import pandas as pd
df = pd.DataFrame.from_records(pd.read_csv('data/car_data.csv'))
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
#df = pd.DataFrame.from_records(pd.read_csv('data/car_data.csv'),columns = ['make','city_mpg','highway_mpg','horsepower'])
df
#Each element should be in the form {'make':make, 'city_mpg':city_mpg, 'highway_mpg':highway_mpg, 'horsepower':horsepower}
headers = list(df)
cars = df.values.tolist()

for i in range(len(cars)):
    cars[i] = {headers[j]: cars[i][j] for j in range(len(headers))}

cars
make = input("Select a make: ")
carsOfThisMake = list(filter(lambda car: car['make'] == make,cars))
carsOfThisMake
fuelEfficientCars = list(filter(lambda car: car['city_mpg'] >35, cars))
fuelEfficientCars

def isPowerful(car):
    try:
        return float(car['horsepower'])>100
    except:
        return False

powerfulCars = list(filter(isPowerful,cars))
powerfulCars
cost = float(input("Enter the current dollars per gallon cost of fuel: "))
drivingCost_100Miles = list(map(lambda car: (1/car['city_mpg'])*cost*100,cars))
drivingCost_100Miles
import functools as ft
mpgList_city = list(map(lambda car: car['city_mpg'],cars))
avgMPG_city = ft.reduce(lambda a,b: a+b,mpgList_city)/len(mpgList_city)
avgMPG_city

#Same idea applies to the other parts of this assignment
countAdjust = 0
def addSafely(a,b):
    try:
        return float(a) + float(b)
    except:
        global countAdjust
        countAdjust += 1
        return 0
carPrices = list(map(lambda car: car['price'],cars))
carPrices
avgPrice = ft.reduce(addSafely,carPrices) / (len(cars) - countAdjust)
avgPrice
