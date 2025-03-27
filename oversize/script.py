import pandas as pd

dupes = pd.read_csv("oversize/dupesQandQX.csv", names = ["call#"])
ov = pd.read_csv("oversize/OVatQX.csv", names = ["call#"])


# print(dupes)

final = pd.merge(
    ov, dupes, how="left", on=["call#", "call#"], indicator=True
)

check = final[final["_merge"] != "left_only"]

final = final[final["_merge"] == "left_only"]

# print(final)

print(check)

final.to_csv("oversize/UniqueOV.csv", index=False)
