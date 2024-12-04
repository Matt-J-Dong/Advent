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

#1945 is right for somebody else but not for me... Because I did >3 instead of >2
for height in range(n):
    lines[height] = lines[height].strip()
    #print(lines[height])
    for index, letter in enumerate(lines[height]):
        length = len(lines[height])
        if(letter=='M'):
            try:
                if(lines[height+1][index+1]=='A'):
                    if(lines[height+2][index+2]=="S"):
                        if(lines[height+2][index]=="M"):
                            if(lines[height][index+2]=="S"):
                                total = total+1      
            except:
                pass
            try:
                if(lines[height-1][index+1]=='A'):
                    if(lines[height-2][index+2]=="S"):
                        if(lines[height][index+2]=="M"):
                            if(lines[height-2][index]=="S"):
                                if(height>1):
                                    total = total+1      
            except:
                pass
            try:
                if(lines[height-1][index-1]=='A'):
                    if(lines[height-2][index-2]=="S"):
                        if(lines[height-2][index]=="M"):
                            if(lines[height][index-2]=="S"):
                                if(height>1 and index>1):
                                    total = total+1     
            except:
                pass
            try:
                if(lines[height+1][index-1]=='A'):
                    if(lines[height+2][index-2]=="S"):
                        if(lines[height][index-2]=="M"):
                            if(lines[height+2][index]=="S"):
                                if(index>1):
                                    total = total+1      
            except:
                pass
print(total)
