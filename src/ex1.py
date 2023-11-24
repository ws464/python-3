from ValidationException import ValidationException
import csv
import re

def validate_file(file_name):
    with open(file_name) as csv_file:
        csvFile = csv.DictReader(csv_file, delimiter=",")
        for row in csvFile:
            #print(str(row))
            miles =row.get(' Miles')[1:] 
            if(not miles.isnumeric()):
                raise ValidationException(f"Invalid miles: {miles}")


def ex1():
    try:
        validate_file("files/input.txt")
    except ValidationException as ve:
        print(ve)

ex1()