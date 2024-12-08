with open('./text3.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0

nodes = []
for output in range(n):
    lines[output] = lines[output].strip()
    line = lines[output]
    #print(line)
    for char in line:
        if(char != "." and char not in nodes):
            nodes.append(char)
#print(nodes)
locations = []
for i in range(len(nodes)):
    locations.append([])
for output in range(n):
    lines[output] = lines[output].strip()
    line = lines[output]
    #print(line)
    for index, char in enumerate(line):
        if(char in nodes):
            found = nodes.index(char)
            locations[found].append([output,index])
#print(locations)
print(f"Locations: {locations}")
node_loc = []
for i in range(len(nodes)):
    for j in range(len(locations[i])):
        for k in range(len(locations[i])):
            try:
                distance_x = abs(locations[i][j][1]-locations[i][k][1])
                distance_y = abs(locations[i][j][0]-locations[i][k][0])
                #print(distance_x)
                #print(distance_y)
            except:
                pass
            y_axis_greater_left = False
            x_axis_greater_left = False
            try:
                if(locations[i][j][0]>locations[i][k][0]):
                    y_axis_greater_left = True
                if(locations[i][j][1]>locations[i][k][1]):
                    x_axis_greater_left = True
                
                node_1 = [0,0]
                node_2 = [0,0]

                if(y_axis_greater_left):
                    node_1[0] = locations[i][j][0]+distance_y
                    node_2[0] = locations[i][k][0]-distance_y
                else:
                    node_1[0] = locations[i][j][0]-distance_y
                    node_2[0] = locations[i][k][0]+distance_y
                if(x_axis_greater_left):
                    node_1[1] = locations[i][j][1]+distance_x
                    node_2[1] = locations[i][k][1]-distance_x
                else:
                    node_1[1] = locations[i][j][1]-distance_x
                    node_2[1] = locations[i][k][1]+distance_x

                flag1 = False
                flag2 = False

                for node_type in locations:
                    if(node_1 in node_type):
                        flag1 = True
                    if(node_2 in node_type):
                        flag2 = True
                if(flag1==False and node_1[0]>=0 and node_1[1]>=0 and node_1[0]<n-1 and node_1[1]<len(line)-1 and node_1 not in node_loc):
                    node_loc.append(node_1)
                if(flag2==False and node_2[0]>=0 and node_2[1]>=0 and node_2[0]<n-1 and node_2[1]<len(line)-1 and node_2 not in node_loc):
                    node_loc.append(node_2)
            except:
                pass
print(node_loc)
print(len(node_loc))