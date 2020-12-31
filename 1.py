numbers = []

with open("data/1/input.txt") as input_file:
    for line in input_file.readlines():
        numbers.append(int(line.strip()))


for index1, number1 in enumerate(numbers):
    for index2, number2 in enumerate(numbers):
        for index3, number3 in enumerate(numbers):
            if index1 == index2 or index2 == index3 or index1 == index3:
                continue

            if number1 + number2 + number3 == 2020:
                print("%d" % (number1 * number2 * number3))
                exit(0)
