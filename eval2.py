import os
import pathlib
import sys

#  calculate precision & recall per category from naivebayes.output.sortedTweets file

# P(c) = sys correct(c) / identified(c)
# R(c) = sys correct(c) / actual(c)

file = "naivebayes.output.sortedTweets"
filePath = pathlib.Path(file)
if not os.path.exists(filePath):
        print("file path doesnt exist")
outFile = "eval2.output"

aCorrect = 0
iCorrect = 0
aIdentified = 0
iIdentified = 0
aActual = 0  # 61
iAcutal = 0 # 49

# first word = file,  second word = prediction

with open(filePath, 'r') as  f:
    # read each line, separate each line into 2 words by space
    data = f.readlines()

    for line in data:
        temp = line.split()
        print(temp)

        if "android" in temp[0]:
            aActual += 1
            if "android" in temp[1]:
                # match
                aCorrect += 1
                aIdentified += 1
            else:
                iIdentified  += 1
        elif "iphone" in temp[0]:
            iAcutal += 1
            if "iphone" in temp[1]:
                iCorrect += 1
                iIdentified += 1
            else:
                aIdentified += 1
        else:
            print("invalid line")


# P(c) = sys correct(c) / identified(c)
# R(c) = sys correct(c) / actual(c)

print(aCorrect, ", ", iCorrect, ", ", aIdentified, ", ", iIdentified, ", ", aActual, ", ", iAcutal)

androidRecall = aCorrect / aIdentified
androidPrec = aCorrect / aActual

iphoneRecall = iCorrect / iIdentified
iphonePrec = iCorrect / iAcutal

print("android recall: ", androidRecall)
print("android precision: ", androidPrec)
print("iphone recall: ", iphoneRecall)
print("iphone precision: ", iphonePrec)