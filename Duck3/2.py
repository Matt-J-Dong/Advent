with open('./text2.txt', 'r') as f:
    lines = f.readlines()

boxes = lines[0].split(",")
boxes = [ float(x) for x in boxes ]
boxes = sorted(boxes)
print(boxes)
current = 0
total = 0
only_20 = 0
for num in boxes:
    if num>current and only_20<20:
        current = num
        total = total + current
        only_20 = only_20 + 1

print(total)