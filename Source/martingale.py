# Charles Young
# 6/6/2020
# This file parses through input2.txt and shows the number of different loss streaks
import probabilities
counts = []
counter = 0

for i in range(16):
    counts.append(0)

data = probabilities.Data()
data.generate_data("input2.txt")

for data_pt in data.lines:
    if data_pt < 2:
        counter += 1
    if data_pt > 2:
        if counter > 15:
            counter = 15
        counts[counter] += 1
        counter = 0

streak = 0
for element in counts:
    print(str(streak) + ":" + str(element))
    streak += 1


