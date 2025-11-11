with open('./text3.txt', 'r') as f:
    lines = f.readlines()

#print(lines)
peoples = lines[0]
peoples = peoples * 1000

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

    for squire in squires:
        teachers = 0
        for mentor in mentors:
            #if abs(squire-mentor<=1): #I LITERALLY CAN'T DO BASIC MATH
            if abs(squire-mentor)<=1000: #distances both ways capped at max of 10
                #print(f"Squire is {squire}")
                #print(f"Mentor is {mentor}")
                teachers = teachers+1
        #print(teachers)
        squires_teachers.append(teachers)

    #print(squires_teachers)
    for num in squires_teachers:
        total = total + num

#print(mentors)
#print(squires)
#print(squires_teachers)
print(total)
