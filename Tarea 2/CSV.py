import csv
def lectorCSV(archivo):
    print("==========CSV==========")
    with open(archivo) as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)
