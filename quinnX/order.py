import csv

# with open("test.csv", "r") as file:
#     for line in file:
#         print(line)

catcher = []
head = []
tail = []

with open('quinnX/test.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    catcher = []
    head = []
    tail = []
    for row in csv_reader:
        if row[0] != "":
            head = [row[0]]
            # print(head)
           
        else:
            # print(row[1])
            tail = row
            catcher.append(head + tail[1:])
           
    # print(catcher[0])
   
import pandas as pd

df = pd.DataFrame(catcher, columns=["marcEntry","callNumber","library","numberOfCharges","numberOfBills","numberOfCopyHolds","totalCharges","inhouseCharges","totalCheckouts","totalRenewals","intervalCheckouts","intervalRenewals","intervalStartDate","recirculate","dateLastUsed","isReserveItem","copyNumber","itemID","library2","libraryDescription","currentLibrary","location","inTransitTo","inTransitFrom","datePutInTransit","transitReason"])
print(df.loc[0])
print(df)