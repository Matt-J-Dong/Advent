with open('./text.txt', 'r') as f:
    lines = f.readlines()

# A=[35300,-64910]
# B=[36300,-63910]
# position = [35300,-64910]
A=[-21723,-68997]
B=[-20723,-67997]
position = [-21723,-68997]
total = 0
for vertical in range(101):
    # position[1]+=10 #The issue was I moved before even calculating. This happened to work for the sample.
    # position[0]=A[0] #The issue was I moved before even calculating. This happened to work for the sample.
    for horizontal in range(101):
        # position[0]+=10 #The issue was I previously moved before even calculating. This happened to work for the sample.
        num = [0,0]
        fail = False

        for i in range(100):
            #current_num = num
            first = num[0]
            second = num[1]
            num[0] = first*first-second*second
            num[1] = first*second+second*first
            #print(f"After first step: {num}")
            num[0] = int(num[0]/100000)
            num[1] = int(num[1]/100000)
            #print(f"After second step: {num}")
            num[0] = num[0]+position[0]
            num[1] = num[1]+position[1]
            #print(f"After third step: {num}")
            if(num[0]>1000000 or num[0]<-1000000):
                fail = True
                break
            if(num[1]>1000000 or num[1]<-1000000):
                fail = True
                break
        if fail == False:
            total+=1
        position[0]+=10 #The issue was I previously moved before even calculating. This happened to work for the sample.
    position[1]+=10 #The issue was I moved before even calculating. This happened to work for the sample.
    position[0]=A[0] #The issue was I moved before even calculating. This happened to work for the sample.


print(total)
print(f"Final number: {num}")