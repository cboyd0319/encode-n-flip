import sys
import base64

theNumber = sys.argv[1]

base64Conversions = []
backwardsConversions = []
#array from 0 - the number provided by sys.argv
#example "encodeFlip.py 100"
#base64 encode all the numbers in that range that was created


for i in range(0, int(theNumber)):
    base64Conversions.append(base64.b64encode(str(i)))

for element in base64Conversions:
    backwardsConversions.append(element[::-1])

theFile = open("conversions.txt","w+")
for element in backwardsConversions:
    theFile.write(str(element)+ "\n")
theFile.close()
