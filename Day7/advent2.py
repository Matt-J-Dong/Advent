with open('./text2.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0

def maths(num1,num2):
    return [num1+num2,num1*num2,int(str(num1)+str(num2))]

for output in range(n):
    lines[output] = lines[output].strip()
    line = lines[output]
    print(line)
    numbers = line.split(" ")
    numbers[0] = numbers[0][0:len(numbers[0])-1]
    numbers = map(int, numbers)
    numbers = list(numbers)
    #print(numbers)
    goal = numbers.pop(0)
    current = 0
    group = []
    #print(goal)
    flag = True
    #932137733500 is not right
    for index, number in enumerate(numbers):
        if(index==0):
            group.append(number)
            #print(group)
        elif(index<len(numbers)):
            group2 = []
            for testing in group:
                test = maths(testing,numbers[index])
                #print(f"Test: {test}")
                # if goal in test:
                #     total = total + goal
                #     group = []
                #     flag = False
                #     break
                # else:
                group2.append(test[0])
                group2.append(test[1])
                group2.append(test[2])
                #print(f"Group2: {group2}")
            group = []
            for testing2 in group2:
                group.append(testing2)
            #print(f"Group: {group}") 
    if goal in group:
        total = total + goal
print(f"Total: {total}")