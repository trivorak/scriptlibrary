# Decode Key is always the last 2 digits of the hex string

inputString = input("What's your encoded String? {Keep on a Single Line} \n")
encodedString = []
decodedString = [] 

def getKey(input):
    return input[len(input)-2:len(input)]

key = getKey(inputString)

# Split Each Digit
for i in range(0,len(inputString)):
    encodedString.append(inputString[i:i+1])

# Strip key for array
encodedString.pop(-1)
encodedString.pop(-1)

# Decode Loop
for element in encodedString:
    decodedString.append(hex((int(element,16) - int(key,16))% 16)[2:])

# Squash it all together
squashedList = "".join(decodedString)

# Make all digits uppercase
squashedList = squashedList.upper()

print("")

# print sting in 32 character length
for x in range(0,len(squashedList),32):
    print(squashedList[x:x+32])
