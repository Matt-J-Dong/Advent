with open('./text.txt', 'r') as f:
    lines = f.readlines()

A=[165,57]

num = [0,0]

for i in range(3):
    #current_num = num
    first = num[0]
    second = num[1]
    num[0] = first*first-second*second
    num[1] = first*second+second*first
    print(f"After first step: {num}")
    num[0] = int(num[0]/10)
    num[1] = int(num[1]/10)
    print(f"After second step: {num}")
    num[0] = num[0]+A[0]
    num[1] = num[1]+A[1]
    print(f"After third step: {num}")

print(f"Final number: {num}")