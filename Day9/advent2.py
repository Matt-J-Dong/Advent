with open('./text2.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
odd = True
string = []
number = 0

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
new_string.append("!")
print(new_string)

dot_blocks = []
non_blocks = []

#index_non = find_last_non_dot(new_string)
index_non = new_string.index(str(number))
index_dot = new_string.index(".")
print(index_dot)
while index_dot>-1 and index_non>-1:
    flag = True
    index_dot_continue = index_dot
    index_non_continue = index_non
    check_dot = 0 #length
    check_non = 0 #length
    
    while(flag==True):
        try:
            if(new_string[index_dot_continue]==new_string[index_dot]):
                check_dot = check_dot+1
                index_dot_continue+=1
                #print("qwertykjrsdr")
            else:
                #print("qwer")
                add_in = [index_dot,check_dot,"."]
                dot_blocks.append(add_in)
                print(f"DOT APPENDED: {add_in}")
                break
        except:
            print("DOT OUT OF RANGE")
            break
    while(flag==True):
        #print(index_non)
        try:
            #print(new_string[index_non])
            #print(new_string[index_non_continue])
            if(new_string[index_non_continue]==new_string[index_non]):
                check_non = check_non+1
                index_non_continue+=1
                #print("hewtrjthwetrjy")
            else:
                #print("hewtrjth")
                add_in = [index_non,check_non,new_string[index_non]]
                non_blocks.append(add_in) #this was dot_blocks
                print(f"NON APPENDED: {add_in}")
                break
        except:
            print("NON OUT OF RANGE")
            break
    #print(new_string)
    #print(index_dot+check_dot)
    try:
        index_dot = new_string.index(".",index_dot+check_dot)
        number = number-1
        index_non = new_string.index(str(number))
        #print("YOYELAKCE")
    except:
        break

print(dot_blocks)
print(non_blocks)
testing = "".join(new_string)
print(f"Comparing to this string: {testing}")

# dot_blocks_copy = dot_blocks.copy()
# non_block_copy = non_block.copy()
for index, group in enumerate(non_blocks):
    for dot_index, dot_group in enumerate(dot_blocks):
        dot_group_length = dot_group[1]
        if(group[1]<dot_group_length):
            for i in range(group[1]):
                new_string[dot_group[0]+i] = int(group[2])
                print(new_string)
            for i in range(group[1]):
                new_string[group[0]+i] = "."
            dot_group_length = dot_group_length - group[1]
            print(index)
            print(non_blocks[index])
            non_blocks.pop(index)
            break

new_string = new_string[0:len(new_string)-1]
print(new_string)
for index, num in enumerate(new_string):
    if(num=="."):
        pass
    else:
        asdf = int(num)
        total = total + (index*asdf)

print(total)
