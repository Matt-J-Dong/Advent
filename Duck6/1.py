with open('./text.txt', 'r') as f:
    lines = f.readlines()

print(lines)
peoples = lines[0]

pairs = [("A","a")]
mentors = []
squires = []
squires_teachers = []

for pair in pairs:
    for idx, people in enumerate(peoples):
        if people == pair[0]:
            mentors.append(idx)
        if people == pair[1]:
            squires.append(idx)

for squire in squires:
    teachers = 0
    for mentor in mentors:
        if squire>mentor:
            teachers = teachers+1
    squires_teachers.append(teachers)

total = 0
for num in squires_teachers:
    total = total + num

print(mentors)
print(squires)
print(squires_teachers)
print(total)
