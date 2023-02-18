import csv
import sys
import json

counter = 0
counter2 = 0

with open("new_dowjones.csv", "r") as file:
    # Read the csv file into a list of dictionaries
    reader = csv.DictReader(file)
    rows = list(reader)
    for i, row in enumerate(rows):
        if row["date"].startswith("Thu"):
            try:
                # Thursday
                Thu_high = float(row["high"].replace(",", ""))
                # Thu_low = float(row["low"].replace(",", ""))
                # Friday
                Fri_high = float(rows[i - 1]["high"].replace(",", ""))
                Fri_low = float(rows[i - 1]["low"].replace(",", ""))
                # Next monday
                # Next_monday_high = float(rows[i - 2]["high"].replace(",", ""))
                Next_monday_low = float(rows[i - 2]["low"].replace(",", ""))

                
                if Thu_high > Fri_high:
                    counter += 1
                    if Next_monday_low < Fri_low:
                        counter2 += 1

            except IndexError:
                print("Could not find the last Firday's high becasue there was no more Fridays")
               
result = {"counter": counter, "counter2": counter2}
print(json.dumps(result))    
sys.stdout.flush()


