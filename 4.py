EXPECTED_ATTRS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

passports = []
ans = 0


def is_number(text):
    return text.isnumeric()


def is_hex(s):
    return all(c in '0123456789abcdef' for c in s)


with open("data/4/input.txt") as input_file:
    passport = []
    for line in input_file.readlines():
        if line == "\n":
            passports.append(passport)
            passport = []
            continue

        # Parse attributes
        parts = line.split(" ")
        for part in parts:
            item_parts = part.split(":")
            passport.append((item_parts[0].strip(), item_parts[1].strip()))

    if passport:
        passports.append(passport)

for passport in passports:
    is_valid = True
    attributes = set()

    for item in passport:
        attributes.add(item[0])

    for expected_attr in EXPECTED_ATTRS:
        if expected_attr not in attributes and expected_attr != 'cid':
            is_valid = False

    # Deep check attributes
    for item in passport:
        if item[0] == 'byr':
            if not is_number(item[1]) or int(item[1]) < 1920 or int(item[1]) > 2002:
                is_valid = False
        elif item[0] == 'iyr':
            if not is_number(item[1]) or int(item[1]) < 2010 or int(item[1]) > 2020:
                is_valid = False
        elif item[0] == 'eyr':
            if not is_number(item[1]) or int(item[1]) < 2020 or int(item[1]) > 2030:
                is_valid = False
        elif item[0] == 'hgt':
            if not item[1].endswith('cm') and not item[1].endswith('in'):
                is_valid = False
            else:
                height = item[1][:-2]
                if not is_number(height):
                    is_valid = False
                else:
                    if item[1].endswith('cm'):
                        if int(height) < 150 or int(height) > 193:
                            is_valid = False
                    elif item[1].endswith('in'):
                        if int(height) < 59 or int(height) > 76:
                            is_valid = False
        elif item[0] == 'hcl':
            if item[1][0] != '#':
                is_valid = False
            else:
                hexcode = item[1][1:]
                if len(hexcode) != 6:
                    is_valid = False
                else:
                    if not is_hex(hexcode):
                        is_valid = False
        elif item[0] == 'ecl':
            if item[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                is_valid = False
        elif item[0] == 'pid':
            if len(item[1]) != 9:
                is_valid = False
            elif not is_number(item[1]):
                is_valid = False

    if is_valid:
        ans += 1

print(ans)
