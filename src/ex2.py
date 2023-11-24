import csv
import functools 

def find_total_visits():
    visits=0
    files=["files/week-1.csv", "files/week-2.csv", "files/week-3.csv"]
    for f in files:
        with open(f) as csv_file:
            rows = csv.reader(csv_file)
            next(rows, None)
            for row in rows: 
                visits+=int(functools.reduce(lambda a,b: int(a)+int(b), row[1:]))
    return visits
def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()