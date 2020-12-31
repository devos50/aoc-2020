valid = 0

with open("data/2/input.txt") as input_file:
    for line in input_file.readlines():
        parts = line.strip().split(":")
        password = parts[1].strip()

        parts = parts[0].split(" ")
        character = parts[1]

        parts = parts[0].split("-")
        first_index = int(parts[0]) - 1
        second_index = int(parts[1]) - 1

        first_valid = (password[first_index] == character)
        second_valid = (password[second_index] == character)
        if (first_valid and not second_valid) or (not first_valid and second_valid):
            valid += 1

print(valid)