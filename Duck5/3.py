from functools import cmp_to_key

def build_fishbone_quality(line: str):
    """
    Given a line like '58:5,3,7,8,9,10,4,5,7,8,8',
    build the fishbone and return (quality, spine, left, right).
    """
    line = line.strip()
    if not line:
        return None

    sword_id, seq_part = line.split(":", 1)
    nums = [int(x) for x in seq_part.split(",") if x != ""]

    spine = []
    left = []
    right = []

    first = nums[0]
    spine.append(first)
    left.append(None)
    right.append(None)

    for num in nums[1:]:
        placed = False
        for i, spine_val in enumerate(spine):
            if num < spine_val and left[i] is None:
                left[i] = num
                placed = True
                break
            if num > spine_val and right[i] is None:
                right[i] = num
                placed = True
                break
        if not placed:
            spine.append(num)
            left.append(None)
            right.append(None)

    quality_str = "".join(str(v) for v in spine)
    quality = int(quality_str)

    return quality, spine, left, right


def level_scores(spine, left, right):
    """
    Compute per-level numbers (concatenation of digits at each level).
    """
    levels = []
    for i in range(len(spine)):
        s = ""
        if left[i] is not None:
            s += str(left[i])
        s += str(spine[i])
        if right[i] is not None:
            s += str(right[i])
        levels.append(int(s))
    return levels


def compare_swords(a, b):
    """
    Compare two swords (id, quality, levels) according to the rules.
    """
    id_a, qa, la = a
    id_b, qb, lb = b

    # 1) Higher quality is better
    if qa != qb:
        return -1 if qa > qb else 1

    # 2) Compare per-level numbers from the top
    max_len = max(len(la), len(lb))
    for i in range(max_len):
        va = la[i] if i < len(la) else 0
        vb = lb[i] if i < len(lb) else 0
        if va != vb:
            return -1 if va > vb else 1

    # 3) If fishbones identical, higher id is better
    if id_a != id_b:
        return -1 if id_a > id_b else 1

    return 0


def main():
    with open("text3.txt", "r") as f:
        lines = f.readlines()

    swords = []  # list of (id, quality, levels)

    for line in lines:
        line = line.strip()
        if not line:
            continue

        sword_id_str, _ = line.split(":", 1)
        sword_id = int(sword_id_str)

        quality, spine, left, right = build_fishbone_quality(line)
        levels = level_scores(spine, left, right)

        swords.append((sword_id, quality, levels))

    # Sort from best to weakest
    swords_sorted = sorted(swords, key=cmp_to_key(compare_swords))

    # Compute checksum: id * position (1-based)
    checksum = 0
    for idx, (sword_id, quality, levels) in enumerate(swords_sorted, start=1):
        checksum += sword_id * idx

    print("Checksum:", checksum)


if __name__ == "__main__":
    main()
