import csv

# with open("test.csv", "r") as file:
#     for line in file:
#         print(line)

# catcher = []
# head = []
# tail = []

# with open('quinnX/test.csv', 'r', encoding="utf8") as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     catcher = []
#     head = []
#     tail = []
#     for row in csv_reader:
#         if row[0] != "":
#             head = [row[0]]
#             # print(head)
           
#         else:
#             # print(row[1])
#             tail = row
#             catcher.append(head + tail[1:])
           
#     # print(catcher[0])
   
import pandas as pd

# df = pd.DataFrame(catcher, columns=["marcEntry","callNumber","library","numberOfCharges","numberOfBills","numberOfCopyHolds","totalCharges","inhouseCharges","totalCheckouts","totalRenewals","intervalCheckouts","intervalRenewals","intervalStartDate","recirculate","dateLastUsed","isReserveItem","copyNumber","itemID","library2","libraryDescription","currentLibrary","location","inTransitTo","inTransitFrom","datePutInTransit","transitReason"])
# print(df.loc[0])
# print(df)

# df.to_csv("quinnX/output.csv", index=False)

# unique = pd.read_excel("quinnX/unique_quinnX.xlsx")

# unique_selected = unique.loc[unique['Date last charged'] > 0]
# print(unique_selected)

# unique_selected['Date last charged'] = pd.to_datetime(unique_selected['Date last charged'], format='%Y%m%d')


# print(unique_selected)

# print(unique_selected['Date last charged'].dtype)

# unique_selected_co = unique_selected.loc[(unique['Total Charges'] > 0) & (unique_selected['Date last charged'] > pd.to_datetime("2015-01-01"))]


# print(unique_selected_co)


# qdOnly = pd.merge(
#     df, unique, how="left", left_on ="callNumber", right_on =  "Call #", indicator=True
# )

# qxleft = qdOnly[qdOnly["_merge"] == "left_only"]

# print(qxleft)

# qxright = qdOnly[qdOnly["_merge"] == "right_only"]

# print(qxright)

# qxboth = qdOnly[qdOnly["_merge"] == "both"]

# print(qxboth)



# qdOnly = qdOnly.drop(qdOnly.columns[26:], axis=1)
# print(qdOnly)

# qdOnly.to_csv("quinnX/qxdupes.csv", index=False)
# print(qdOnly)


import math 

# all = pd.read_csv('quinnX\output.csv')

# # print(all['dateLastUsed'])

# all_used = all.loc[all['dateLastUsed'].notnull()]



# all_used['dateLastUsed'] = pd.to_datetime(all_used['dateLastUsed'], format='%Y-%m-%d')

# # print(all_used['dateLastUsed'].dtype)

# all_used_co = all_used.loc[(all_used['totalCheckouts'] > 0) & (all_used['dateLastUsed'] > pd.to_datetime("2015-01-01"))]


# print(all_used_co[['totalCheckouts', 'dateLastUsed']])

all = pd.read_csv('quinnX\output.csv')

all = all[all['marcEntry'].str.contains('for dummies')]

print(all.iloc[0])

print(all)

# all.to_csv("quinnX\dummies.csv", index = 'false')