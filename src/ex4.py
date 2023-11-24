import boto3
from botocore.exceptions import ClientError

def calculate():
    LOG = "files/calculator-log.txt"
    with open(LOG,"w") as log:   
        while True:
            num1 = input("Enter the first number: ")
            if(num1=="q"):
                break
            num2 = input("Enter the second number: ")
            if(num2=="q"):
                break
            total = int(num1)+int(num2)
            print(total)
            log.write(f"{num1} + {num2} = {total}\n")
    



def ex4():
    calculate()

ex4()
