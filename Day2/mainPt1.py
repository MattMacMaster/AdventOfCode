
# Up is decreasing Depth, Y - Value
# Down is increasing Depth, Y + Value

# Forward is increasing X, X + Value
# No backword option
x = 0
y = 0
options = ['forward', 'up', 'down']
input_file = open('Input.txt', 'r')
for line in input_file:
    values = line.split()
    if(values[0] == 'forward'):
        x += int(values[1])
    elif(values[0] == 'down'):
        y += int(values[1])
    else:
        y -= int(values[1])


print(x * y)
