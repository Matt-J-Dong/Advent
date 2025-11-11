# with open('./text4.txt', 'r') as f:
#     lines = f.readlines()

# boxes = lines[0].split(",")
# boxes = [ float(x) for x in boxes ]
# boxes = sorted(boxes,reverse=True)
# print(boxes)
# current = 99999999999
# total = 0
# num_sets = 0
# while len(boxes)>1:
#     for num in boxes:
#         if num<current:
#             current = num
#             total = total + current
#             boxes.remove(num)
#     current = 99999999999999999
#     print("One loop")
#     print(boxes)
#     num_sets = num_sets + 1

# print(boxes)
# print(f"Number of sets:{num_sets}")

with open('./text3.txt', 'r') as f:
    lines = f.readlines()

boxes = lines[0].split(",")
boxes = [ float(x) for x in boxes ]
boxes = sorted(boxes)
print(boxes)
current = 0
num_sets = 1
while len(boxes)>1:
    for num in boxes[:]: #element based looping still has the same issues when deleting in a list you iterate over
        #print(f"Current number:{num}")
        if num>current:
            current = num
            #print(current)
            dropped = boxes.remove(current)
            #print(f"Dropped this number {dropped}")
    current = 0
    #print("One loop")
    #print(boxes)
    num_sets = num_sets + 1

print(f"Number of sets:{num_sets}")