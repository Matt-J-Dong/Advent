with open('./text3.txt', 'r') as f:
    lines = f.readlines()

pattern = lines[0].strip()
repeats = 1000
D = 1000  # max distance

# Build the full layout once: length = len(pattern) * repeats
peoples = pattern * repeats
N = len(peoples)

pairs = [("A", "a"), ("B", "b"), ("C", "c")]
total = 0

for mentor_char, squire_char in pairs:
    # Collect indices for mentors and squires
    mentors = []
    squires = []

    for i, ch in enumerate(peoples):
        if ch == mentor_char:
            mentors.append(i)
        elif ch == squire_char:
            squires.append(i)

    # Sliding window over mentors for each squire
    m_left = 0  # first mentor that might still be in range
    m_right = 0 # first mentor that is *just outside* the upper bound
    count_for_pair = 0

    for s in squires:
        # Move left pointer until mentors[m_left] >= s - D
        while m_left < len(mentors) and mentors[m_left] < s - D:
            m_left += 1

        # Move right pointer until mentors[m_right] > s + D
        while m_right < len(mentors) and mentors[m_right] <= s + D:
            m_right += 1

        # All mentors in [m_left, m_right) are within distance D
        count_for_pair += (m_right - m_left)

    total += count_for_pair

print(total)
