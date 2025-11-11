with open('./text3.txt', 'r') as f:
    lines = f.readlines()

#print(lines)
peoples = lines[0]

pairs = [("A","a"),("B","b"),("C","c")]
#pairs = [("A","a")]
mentors = []
squires = []
squires_teachers = []
total = 0

for pair in pairs: #This one is probably necessary, you want to check all 3 separately
    mentors = []
    squires = []
    squires_teachers = []
    for idx, people in enumerate(peoples): #By extension then this should be necessary?
        if people == pair[0]:
            mentors.append(idx)
        if people == pair[1]:
            squires.append(idx)

    mentors = sorted(mentors)

    for squire in squires:
        teachers = 0
        bottom = (squire-1000)%10000
        top = (squire+1000)%10000
        for mentor in mentors:
            #check if between bottom and top
            pass #temp to resolve errors

    #print(squires_teachers)
    for num in squires_teachers:
        total = total + num

#print(mentors)
#print(squires)
#print(squires_teachers)
print(total)
print(total*500)
