import pandas as pd

one = pd.read_excel("oversize_2/unique.xlsx", names = ["title", "call", "itemID", "checkout", "last checkout"])

# print(one.loc[1])

# print(one)

two = pd.read_excel("oversize_2/Oversize.xlsx") 

# print(two.loc[1])

final = pd.merge(
    one, two, how="left", left_on= "call", right_on = "Call Number", indicator=True
)

# print(final)

left = final[final["_merge"] == "left_only"]

right = final[final["_merge"] == "right_only"]

both = final[final["_merge"] == "both"]

# final = final.drop(final.columns[5:], axis=1)

print(left)

print(right)

print(both)


# # print(final.loc[1])

# print(final)

# final.to_excel("oversize_2/new_uniquw.xlsx", index=False)