# %%
# 1. Parse input

# %%
with open("../inputs/day01.txt", "r") as f:
    rotations = [line.strip() for line in f.readlines()]

# %%
position = 50
zero_count = 0

for rotation in rotations:
    direction = rotation[0]  # L or R
    distance = int(rotation[1:])

    if direction == "L":
        position = (position - distance) % 100
    elif direction == "R":
        position = (position + distance) % 100

    if position == 0:
        zero_count += 1

print(f"password: {zero_count}")
