def build_filesystem_string(file_path):
    """
    Reads the input from 'text2.txt' and builds the initial filesystem string.
    Alternates between file IDs and free space blocks based on the 'odd' flag.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    filesystem = []
    odd = True  # Indicates whether to append a file or free space
    number = 0  # File ID starts at '0'

    for line in lines:
        line = line.strip()
        for char in line:
            if odd:
                # Append the current file ID 'number' repeated 'int(char)' times
                filesystem.extend([str(number)] * int(char))
                odd = False
            else:
                # Append free space '.' repeated 'int(char)' times
                filesystem.extend(['.'] * int(char))
                number += 1  # Increment file ID for the next file
                odd = True

    filesystem.append('!')  # Sentinel to mark the end
    return filesystem

def identify_blocks(filesystem):
    """
    Identifies all file blocks and free space blocks in the filesystem.
    Returns two lists: dot_blocks and file_blocks.
    Each block is represented as [start_index, length, identifier].
    """
    dot_blocks = []
    file_blocks = []
    index = 0
    length = len(filesystem)

    while index < length:
        current_char = filesystem[index]
        if current_char == '.':
            start = index
            while index < length and filesystem[index] == '.':
                index += 1
            block_length = index - start
            dot_blocks.append([start, block_length, '.'])
        elif current_char != '!':
            start = index
            identifier = current_char
            while index < length and filesystem[index] == identifier:
                index += 1
            block_length = index - start
            file_blocks.append([start, block_length, identifier])
        else:
            index += 1  # Skip the sentinel

    return dot_blocks, file_blocks

def sort_blocks(dot_blocks, file_blocks):
    """
    Sorts the file blocks in decreasing order of file ID (numeric).
    Sorts the dot blocks in increasing order of starting index.
    Excludes file ID '0' from being moved.
    """
    # Filter out '0's from file_blocks
    filtered_file_blocks = [block for block in file_blocks if block[2] != '0']

    # Sort file_blocks in descending order of file ID
    sorted_file_blocks = sorted(
        filtered_file_blocks,
        key=lambda x: int(x[2]),
        reverse=True
    )

    # Sort dot_blocks in ascending order of starting index
    sorted_dot_blocks = sorted(
        dot_blocks,
        key=lambda x: x[0]
    )

    return sorted_dot_blocks, sorted_file_blocks

def move_files(filesystem, dot_blocks, sorted_file_blocks):
    """
    Moves each file to the leftmost available free space block that can accommodate it.
    Updates the filesystem and free space blocks accordingly.
    """
    for file_block in sorted_file_blocks:
        file_start, file_length, file_id = file_block
        # Search for the first dot block that can fit the file
        for dot in dot_blocks:
            dot_start, dot_length, _ = dot
            if dot_length >= file_length:
                # Move the file to the dot block's starting index
                for i in range(file_length):
                    filesystem[dot_start + i] = file_id
                # Overwrite the original file location with dots
                for i in range(file_length):
                    filesystem[file_start + i] = '.'
                print(f"Moved file ID {file_id} from index {file_start} to index {dot_start}")

                # Update the dot_blocks
                if dot_length == file_length:
                    # Exact fit; remove the dot block
                    dot_blocks.remove(dot)
                else:
                    # Partial fit; adjust the dot block's start and length
                    dot[0] += file_length
                    dot[1] -= file_length

                # Add the old file location as a new dot block
                new_dot = [file_start, file_length, '.']
                # Insert the new_dot in the correct position to maintain sorted order
                inserted = False
                for idx, existing_dot in enumerate(dot_blocks):
                    if new_dot[0] < existing_dot[0]:
                        dot_blocks.insert(idx, new_dot)
                        inserted = True
                        break
                if not inserted:
                    dot_blocks.append(new_dot)

                # Re-sort the dot_blocks to maintain order
                dot_blocks = sorted(dot_blocks, key=lambda x: x[0])
                break  # Move to the next file after a successful move

    return filesystem

def calculate_checksum(filesystem):
    """
    Calculates the filesystem checksum.
    For each file ID (non-dot), multiply its index by its integer value and sum all.
    """
    checksum = 0
    for index, char in enumerate(filesystem):
        if char.isdigit():
            checksum += index * int(char)
    return checksum

def main():
    # Step 1: Build the initial filesystem string
    filesystem = build_filesystem_string('./text2.txt')
    print("Initial filesystem:", ''.join(filesystem))

    # Step 2: Identify all dot blocks and file blocks
    dot_blocks, file_blocks = identify_blocks(filesystem)
    print("Initial Dot Blocks:", dot_blocks)
    print("Initial File Blocks:", file_blocks)

    # Step 3: Sort the blocks appropriately (excluding '0's)
    sorted_dot_blocks, sorted_file_blocks = sort_blocks(dot_blocks, file_blocks)
    print("Sorted Dot Blocks:", sorted_dot_blocks)
    print("Sorted File Blocks (Descending ID):", sorted_file_blocks)

    # Step 4: Move files to compact the filesystem
    filesystem = move_files(filesystem, sorted_dot_blocks, sorted_file_blocks)
    print("Compacted filesystem:", ''.join(filesystem[:-1]))  # Exclude the sentinel '!'

    # Step 5: Calculate the checksum
    checksum = calculate_checksum(filesystem)
    print("Filesystem Checksum:", checksum)

if __name__ == "__main__":
    main()
