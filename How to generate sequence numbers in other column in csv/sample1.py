import statistics
import pandas as pd
import itertools

csv_data = pd.read_csv("/home/gangadhar/test.csv")

a = []
for i in range(1, len(csv_data["A"])):
    a.append(i)

remaining = len(csv_data["A"]) - len(a)
for i in range(0, remaining):
    a.append("")
csv_data["A_id"] = a



print(csv_data)
