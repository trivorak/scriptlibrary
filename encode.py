from random import randint

# Initial Variables
inputList = []
convertedList = []

randomSeed = randint(1,15)

#Input Variables (For Testing)
inputstr = input("What's Your Input String? {Please keep on a single line} ")

#Debug
print(len(inputstr))

# Split each "digit" as an index
for i in range(0,len(inputstr)):
	inputList.append(inputstr[i:i+1])
	
# Encoding Process	
for element in inputList:
	convertedList.append(hex((int(element,16) + randomSeed)% 16)[2:])

# Attach Random Seed Int used in Offset
convertedList.append(str(0)+hex(randomSeed)[2:])

squashedList = "".join(convertedList)
print("")
print(squashedList)