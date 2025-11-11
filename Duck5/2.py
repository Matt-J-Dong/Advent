def build_fishbone_quality(line: str) -> int:
    """
    Given a line like '58:5,3,7,8,9,10,4,5,7,8,8',
    build the fishbone and return the quality as an integer.
    """
    line = line.strip()
    if not line:
        return None  # skip empty lines
    # Split off the sword ID (ignored for fishbone, but handy to return)
    sword_id, seq_part = line.split(":", 1)

    # Parse the number sequence after the colon
    nums = [int(x) for x in seq_part.split(",") if x != ""]

    # Initialize the fishbone with the first number as the first spine segment
    spine = []
    left = []
    right = []

    first = nums[0]
    spine.append(first)
    left.append(None)
    right.append(None)

    # Insert the rest of the numbers according to the rules
    for num in nums[1:]:
        placed = False

        # Check all spine segments from top to bottom
        for i, spine_val in enumerate(spine):
            if num < spine_val and left[i] is None:
                left[i] = num
                placed = True
                break
            if num > spine_val and right[i] is None:
                right[i] = num
                placed = True
                break

        # If no place found, create a new spine segment at the bottom
        if not placed:
            spine.append(num)
            left.append(None)
            right.append(None)

    # Quality is spine digits concatenated
    quality_str = "".join(str(v) for v in spine)
    return int(quality_str)


def main():
    with open("text2.txt", "r") as f:
        lines = f.readlines()

    all_qualities = []
    for line in lines:
        line = line.strip()
        #print(line)
        if not line:
            continue
        sword_id, _ = line.split(":", 1)
        quality = build_fishbone_quality(line)
        print(f"Sword {sword_id} has quality {quality}")
        all_qualities.append(quality)
    all_qualities = sorted(all_qualities)
    difference = all_qualities[len(all_qualities)-1]-all_qualities[0]
    print(difference)


if __name__ == "__main__":
    main()
