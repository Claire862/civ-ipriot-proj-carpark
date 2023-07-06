

data2display = {'TIME': '21:39', 'SPACES': 129, 'TEMPC': 26}

# input list
inputList = ['TIME', 'SPACES', 'TEMPC']
inputList2 = ['TIME2', 'SPACES2', 'TEMPC2']

# combining input dictionary and list together
zippedObject = zip(inputList, inputList2)

print(zippedObject)

for item in zippedObject:
    print(item)