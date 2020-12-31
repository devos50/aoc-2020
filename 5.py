def get_seat_id(seat_string):
    # Determine row
    llim = 0
    rlim = 127
    window = 64
    for index in range(7):
        if seat_string[index] == 'F':
            rlim -= window
        elif seat_string[index] == 'B':
            llim += window
        window /= 2

    assert llim == rlim  # Sanity check
    row = int(llim)

    # Determine column
    llim = 0
    rlim = 7
    window = 4
    for index in range(3):
        if seat_string[index + 7] == 'L':
            rlim -= window
        elif seat_string[index + 7] == 'R':
            llim += window
        window /= 2

    assert llim == rlim  # Sanity check
    column = int(llim)

    return row * 8 + column


seats = set()
with open("data/5/input.txt") as input_file:
    for line in input_file.readlines():
        seats.add(get_seat_id(line.strip()))

print(seats)

for my_seat_guess in range(0, 848):
    if (my_seat_guess - 1) in seats and (my_seat_guess + 1) in seats and my_seat_guess not in seats:
        print(my_seat_guess)