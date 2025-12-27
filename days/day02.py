# %%
from pathlib import Path

# %%
inp_text = Path("../inputs/day02.txt").read_text().strip()

ranges = []

for range_str in inp_text.split(","):
    start, end = map(int, range_str.split("-"))
    ranges.append((start, end))

len(ranges)


# %%
def is_invalid_id(num: int) -> bool:
    """check if number if made of a repeated sequence"""
    seq = str(num)

    # don't check if odd length
    if len(seq) % 2 != 0:
        return False

    # check if first half = second half
    mid = len(seq) // 2
    return seq[:mid] == seq[mid:]


# %%
invalid_ids = []

for start, end in ranges:
    for id_num in range(start, end + 1):
        if is_invalid_id(id_num):
            invalid_ids.append(id_num)

total = sum(invalid_ids)
print(total)
