import pandas as pd
import csv

# # Read the excel file into a dataframe
# df = pd.read_excel("Walsh.xlsx")

# # Print the dataframe
# print(df)


# df = df[df.duplicated(subset=["callNumber"], keep=False)]

# rslt_df = df.loc[df["libraryDescription"] == "Lincoln Center--Quinn Library"]

# print(rslt_df)


# df = pd.read_csv("Walsh.csv")

# print(df)

# with open("Walsh.csv", "r", encoding="utf8") as file:
#     # Read each line in the file
#     i = 0
#     for line in file:
#         # Print each line
#         print(line.strip())
#         i += 1

#         if i > 10:
#             break


# final = []

# with open("Quinn.csv", "r", encoding="utf-8") as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         # Process each row
#         if row[0] != "":
#             title = [row[0]]
#         else:
#             rest = row[2:]
#             combined_list = title + rest
#             # print(combined_list)
#             final.append(combined_list)


# headers = [
#     "marcEntry",
#     "callNumber",
#     "itemID",
#     "library",
#     "location",
# ]

# # print(final[0][0])

# with open("Quinn2.csv", "w", newline="", encoding="utf-8") as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)

#     csvwriter.writerow(headers)

#     # writing the fields
#     csvwriter.writerows(final)

quinn = pd.read_csv("Quinn2.csv")

# print(df.iloc[:2])

walsh = pd.read_excel("Walsh.xlsx")

# dfe = pd.merge(
#     quinn, walsh, how="left", on=["callNumber", "callNumber"], indicator=True
# )

# dfe = dfe[dfe["_merge"] == "left_only"]

# dfe = dfe.drop(dfe.columns[5:], axis=1)

# # print(dfe)

westchester = pd.read_excel("Westchester.xlsx")


# final = pd.merge(
#     dfe, westchester, how="left", on=["callNumber", "callNumber"], indicator=True
# )

# final = final[final["_merge"] == "left_only"]

# final = final.drop(final.columns[5:], axis=1)

# print(final)

# df_no_duplicates = final.drop_duplicates(subset=["callNumber"])

# print(df_no_duplicates)

# df_no_duplicates.to_csv("uniqueDVDs.csv", index=False)

# dupesWalsh = pd.merge(
#     quinn, walsh, how="inner", on=["callNumber", "callNumber"], indicator=True
# )

# print(dupesWalsh)

# dupesWest = pd.merge(
#     quinn, westchester, how="inner", on=["callNumber", "callNumber"], indicator=True
# )

# print(dupesWest)

# combo = pd.concat([dupesWalsh, dupesWest])

# print(combo)

# combo = combo.drop_duplicates(subset=["callNumber"])

# combo = combo.drop(combo.columns[5:], axis=1)


# print(combo)

# combo.to_csv("dupes.csv", index=False)


# combo = combo.drop_duplicates(subset=["callNumber"])

# quinn_dupes = quinn[quinn.duplicated(["callNumber"], keep=False)]

# quinn_dupes.to_csv("QuinnDupes.csv", index=False)


# dupes = pd.read_csv("dupes.csv")

# quinnDupes = pd.read_csv("QuinnDupes.csv")

# qdOnly = pd.merge(
#     quinnDupes, dupes, how="left", on=["callNumber", "callNumber"], indicator=True
# )

# qdOnly = qdOnly[qdOnly["_merge"] == "left_only"]

# qdOnly = qdOnly.drop(qdOnly.columns[5:], axis=1)
# # print(qdOnly)

# qdOnly.to_csv("qdOnly.csv", index=False)

import re


def callN(alist):
    for element in alist:
        if (element * 1).isdigit():
            return element


qdOnly = pd.read_csv("qdOnly.csv")
# probbaly best to just remove the dvd part, then split then take first thing in list

qdOnly["callNum2"] = qdOnly["callNumber"].apply(lambda x: x[6:])

qdOnly["callNum2"] = qdOnly["callNum2"].apply(lambda x: x.split(" "))

qdOnly["callNum2"] = qdOnly["callNum2"].apply(lambda x: x[0] if len(x) > 0 else x)


qdOnly["callNum2"] = qdOnly["callNum2"].apply(
    lambda x: "".join(c for c in x if c.isdigit())
)


print(qdOnly)

qdOnly.to_csv("qdOnly.csv", index=False)
