with open('./text3.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
odd = True
string = []
number = 0

def find_last_non_dot(s):
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ".":
            return i
    return -1

for output in range(n):
    lines[output] = lines[output].strip()
    line = lines[output]
    #print(line)
    for char in line:
        if(odd):
            for i in range(int(char)):
                #string = string + str(number)
                string.append(str(number))
                odd = False
        else:
            for i in range(int(char)):
                #string = string + "."
                string.append(".")
            number = number+1
            odd = True
#print(string)
new_string = []
for char in string:
    new_string.append(char)
#print(new_string)
index_non = find_last_non_dot(new_string)
index_dot = new_string.index(".")
while index_dot<index_non:
    new_string[index_dot:index_dot+1] = new_string[index_non:index_non+1]
    new_string[index_non:index_non+1] = "."
    index_non = find_last_non_dot(new_string)
    index_dot = new_string.index(".")

# final_string = "".join(new_string)
# print(final_string)

#85635411453
#6359213660505
print(new_string)
for index, num in enumerate(new_string):
    if(num=="."):
        break
    asdf = int(num)
    total = total + (index*asdf)

print(total)
