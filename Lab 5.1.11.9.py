def split(number):
    return[char for char in number]

number = 19991229

number = str(number)
number = split(number)

for i in range(len(number)):
    number[i] = int(number[i])

while len(number)>1:

    temp = []
    temp.append(number[0])
    for i in range(1, len(number)):
        temp[0] += number[i]

    temp[0] = str(temp[0])
    number = split(temp[0])
    

    for i in range(len(number)):
        number[i] = int(number[i])

print(number[0])

