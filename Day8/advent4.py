from math import gcd

with open('./text4.txt', 'r') as f:
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
        for k in range(j+1,len(locations[i])):
            try:
                distance_x = locations[i][j][1]-locations[i][k][1]
                distance_y = locations[i][j][0]-locations[i][k][0]
                #print(distance_x)
                #print(distance_y)
            except:
                pass
            try:
                node_1 = [0,0]
                node_2 = [0,0]

                aerghpqworighpowijgpoiqwrg = gcd(distance_x,distance_y)
                qwoeiugfhqwoirughqerwg = distance_y/aerghpqworighpowijgpoiqwrg
                qwirughqewirughioeqrghwerg = distance_x/aerghpqworighpowijgpoiqwrg
                for p in range(50):
                    node_1[0] = locations[i][j][0]+(qwoeiugfhqwoirughqerwg*p)
                    node_2[0] = locations[i][k][0]-(qwoeiugfhqwoirughqerwg*p)
                    node_1[1] = locations[i][j][1]+(qwirughqewirughioeqrghwerg*p)
                    node_2[1] = locations[i][k][1]-(qwirughqewirughioeqrghwerg*p)

                    if(node_1[0]>=0 and node_1[1]>=0 and node_1[0]<n and node_1[1]<len(line)):
                        node_loc.append(node_1.copy())
                    if(node_2[0]>=0 and node_2[1]>=0 and node_2[0]<n and node_2[1]<len(line)):
                        node_loc.append(node_2.copy())
            except:
                pass

hwriguweoriughg = set()

for askjdhflkajsdhflkjasdf in node_loc:
    hwriguweoriughg.add(tuple(askjdhflkajsdhflkjasdf))

print(len(hwriguweoriughg))
print(len(node_loc))

# print(node_loc)
#print(hwriguweoriughg)
#\qwrkejgiohreoiguhewroiughq3proefbhpowqrihgboq34hw4t[gobiqewhsrgdovkcgjl3brqpeosfhvnbpqweorhfdbn obeiwrqjtkgbp woherosdtgpobhjqewrdfigjbveprwiudfabghvpoadfxi]
#23thijgeowiurjtorhne[qsfpdgba[qFKLDNS;OGJNQWSTRJOWFQENLBASFHD[0-GSTGBKHEONSMGPWF;GLN F-0WT  MKLRH,[FQBKSWRQGSLPFKTSJWPORQ3GBFWLJBNFAODK]]]]