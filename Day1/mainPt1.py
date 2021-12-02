

tempSumN1 = 0
tempSumN2 = 0
ValArray = []
input_file = open('Input.txt', 'r')
total = 0
skip = 0
for line in input_file:
    ValArray += int(line)

    if skip == 0:
        skip += 1
    else:
        if(tempvar < int(line)):
            print('high')
            total += 1
        else:
            print('low')
        tempvar = int(line)
print(ValArray)
