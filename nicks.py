# Open the file in read mode

output = []

with open("duplicates.txt", "r", encoding="utf8") as file:
    # Read each line in the file
    for line in file:
        # Print each line
        # print(line.strip())

        start = line.find("|")
        start += 1
        end = line.find("|", start)
        callNum = line[start:end]

        parts = line.split("/")
        if len(parts) > 1:
            title = parts[0]
        else:
            start = 0
            end = line.find("|", start)
            title = line[start:end]

        output.append([title, callNum])


# print(output)
import pandas as pd

df = pd.DataFrame(output, columns=["title", "call number"])
df.to_excel("duplicates.xlsx", index=False)
