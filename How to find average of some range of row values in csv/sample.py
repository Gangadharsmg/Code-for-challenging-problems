import statistics
import pandas as pd
import itertools

csv_data = pd.read_csv("/home/gangadhar/test.csv")

def averageColumnAdded(csv_data, N, column_name):
    c = []
    split_data = (csv_data[column_name][i:i+N] for i in range(0,len(csv_data[column_name]),N))
    for i in split_data:
        c.append(statistics.mean(i))


    remaining = len(csv_data[column_name]) - len(c)
    for i in range(0, remaining):
        c.append(None)
    csv_data[column_name] = c
    return csv_data[column_name]

averageColumnAdded(csv_data, 5, "A")
averageColumnAdded(csv_data, 5, "B")

print(csv_data)


################################  OR other way ########################################


import statistics
import pandas as pd
import itertools

csv_data = pd.read_csv("/home/gangadhar/test.csv")

config = [
    {
        "input_column_name": "A",
    },
    {
        "input_column_name": "B",
    }
]

WINDOW_SIZE = 5
def FindAverage(geyser, WINDOW_SIZE, config):
    for prop in config:
        c = []
        split_data = (geyser[prop["input_column_name"]][i:i + WINDOW_SIZE] for i in
                      range(0, len(geyser[prop["input_column_name"]]), WINDOW_SIZE))
        for i in split_data:
            c.append(statistics.mean(i))

        remaining = len(geyser[prop["input_column_name"]]) - len(c)
        for i in range(0, remaining):
            c.append(None)
        geyser[prop["input_column_name"]] = c

    return geyser

print(FindAverage(csv_data, WINDOW_SIZE, config))

