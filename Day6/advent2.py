with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

blocks = []
guard_pos = None

for output in range(n):
    lines[output] = lines[output].strip()
    line = lines[output]
    # print(line) 
    for col, char in enumerate(line):
        if char == '#':
            blocks.append((output, col))  # Use tuple for immutability
        elif char == '^':
            guard_pos = (output, col)

# Validate if guard was found
if guard_pos is None:
    print("Guard's starting position '^' not found.")
    exit(1)

# Step 2: Identify all possible obstruction positions ('.' excluding the guard's position)
possible_obstructions = []
for output in range(n):
    for col, char in enumerate(lines[output]):
        if char == '.' and (output, col) != guard_pos:
            possible_obstructions.append((output, col))

# Initialize the count of valid obstruction positions
valid_obstruction_count = 0

# Define directions: Up, Right, Down, Left
guard_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Convert blocks to a set for faster lookup
blocks_set = set(blocks)

# Step 3: Iterate over each possible obstruction position
for obstruction in possible_obstructions:
    # Temporarily add the obstruction
    blocks_with_obstruction = set(blocks_set)
    blocks_with_obstruction.add(obstruction)
    
    # Initialize guard's state
    guard_location = list(guard_pos)  # Mutable list to update position
    direction_idx = 0  # Start facing Up
    visited_states = set()
    loop_detected = False
    
    while True:
        # Current state: (output, col, direction)
        state = (guard_location[0], guard_location[1], direction_idx)
        
        # Check if this state has been visited before
        if state in visited_states:
            loop_detected = True
            break
        visited_states.add(state)
        
        # Calculate next position based on current direction
        dr, dc = guard_directions[direction_idx]
        new_row = guard_location[0] + dr
        new_col = guard_location[1] + dc
        
        # Boundary check
        if new_row < 0 or new_row >= n or new_col < 0 or new_col >= len(lines[new_row]):
            # Guard exits the map; no loop
            break
        
        # Check if the next position is blocked
        if (new_row, new_col) in blocks_with_obstruction:
            # Turn right (clockwise)
            direction_idx = (direction_idx + 1) % 4
            continue  # Do not move forward; just change direction
        else:
            # Move to the new position
            guard_location = [new_row, new_col]
    
    # If a loop was detected, increment the valid obstruction count
    if loop_detected:
        valid_obstruction_count += 1

# Step 4: Output the total count of valid obstruction positions
print(valid_obstruction_count)
