from pprint import pprint
import csv

def build_car_list():
    INPUT_PATH = "files/input.txt"
    CARS_PATH = "files/car-ids.txt"
    cars={}
    with open(INPUT_PATH) as input_file:
        rows = csv.DictReader(input_file, delimiter=",")
        for row in rows:
            #print(str(row))
            miles =row.get(' Miles')[1:] 
            if(miles.isnumeric()):
                cars.update({row.get('CarId'): {"CarId": row.get('CarId'), "Miles":int(row.get(' Miles')[1:])}})
    with open(CARS_PATH) as cars_file:
        rows = csv.DictReader(cars_file, fieldnames=("CarId", "Make"), delimiter=",")
        for row in rows:
            if(cars.keys().__contains__(row["CarId"])):
                cars[row["CarId"]]["Make"] = row["Make"]
    return list(cars.values())


def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
