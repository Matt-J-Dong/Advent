with open('./text.txt', 'r') as f:
    lines = f.readlines()

boxes = lines[0].split(",")
boxes = [ float(x) for x in boxes ]
boxes = sorted(boxes,reverse=True)
print(boxes)
current = 9999999
total = 0
for num in boxes:
    if num<current:
        current = num
        total = total + current

print(total)