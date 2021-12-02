
# Up is decreasing Depth, Y - Value
# Down is increasing Depth, Y + Value

# Forward is increasing X, X + Value
# Aim has varying results
# down increases aim
# up decreases aim
# forward does 2 things, increases x, and multiplies y
x = 0
y = 0
aim = 0
options = ['forward', 'up', 'down']
input_file = open('Input.txt', 'r')
for line in input_file:
    values = line.split()
    if(values[0] == 'forward'):
        x += int(values[1])
        y += int(values[1]) * aim
    elif(values[0] == 'down'):
        aim += int(values[1])
    else:
        aim -= int(values[1])


print(x * y)
