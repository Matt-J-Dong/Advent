with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
A=0
B=0
C=0
D=0
E=0
F=0
G=0
H=0
for height in range(n):
    lines[height] = lines[height].strip()
    #print(lines[height])
    for index, letter in enumerate(lines[height]):
        length = len(lines[height])
        if(letter=='X'):
            try:
                if(lines[height][index+1]=='M'):
                    if(lines[height][index+2]=="A"):
                        if(lines[height][index+3]=="S"):
                            A = A +1
                            total = total+1
            except:
                pass
            try:
                if(lines[height][index-1]=='M'):
                    if(lines[height][index-2]=="A"):
                        if(lines[height][index-3]=="S"):
                            B = B +1
                            if(index>2):
                                total = total+1
            except:
                pass
            try:
                if(lines[height+1][index]=='M'):
                    if(lines[height+2][index]=="A"):
                        if(lines[height+3][index]=="S"):
                            C = C+1
                            total = total+1
            except:
                pass
            try:
                if(lines[height-1][index]=='M'):
                    if(lines[height-2][index]=="A"):
                        if(lines[height-3][index]=="S"):
                            D = D+1
                            if(height>2):
                                total = total+1
            except:
                pass
            try:
                if(lines[height+1][index+1]=='M'):
                    if(lines[height+2][index+2]=="A"):
                        if(lines[height+3][index+3]=="S"):
                            E= E+1
                            total = total+1
            except:
                pass
            try:
                if(lines[height-1][index-1]=='M'):
                    if(lines[height-2][index-2]=="A"):
                        if(lines[height-3][index-3]=="S"):
                            print(f"Location: {height} {index}")
                            F= F+1
                            if(height>2 and index>2):
                                total = total+1
            except:
                pass
            try:
                if(lines[height-1][index+1]=='M'):
                    if(lines[height-2][index+2]=="A"):
                        if(lines[height-3][index+3]=="S"):
                            G= G+1
                            if(height>2):
                                total = total+1
            except:
                pass
            try:
                if(lines[height+1][index-1]=='M'):
                    if(lines[height+2][index-2]=="A"):
                        if(lines[height+3][index-3]=="S"):
                            H= H+1
                            if(index>2):
                                total = total+1
            except:
                pass
print(total)
#print(A)
#print(B)
#print(C)
#print(D)
#print(E)
#print(F)
#print(G)
#print(H)