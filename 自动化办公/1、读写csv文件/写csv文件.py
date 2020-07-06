import csv

def writeCsv(path, data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        for rowData in data:
            writer.writerow(rowData)


path="data.csv"
data = [[1,2,3],[4,5,6],[7,8,9]]
writeCsv(path, data)