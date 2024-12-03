all_numbers = []

def is_safe_stage(stage):
    n = len(stage)
    if n < 2:
        return True

    if stage[1] > stage[0]:
        increasing = True
    else:
        increasing = False

    for i in range(n - 1):
        diff = stage[i + 1] - stage[i]

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if increasing and diff < 0:
            return False
        if not increasing and diff > 0:
            return False

    return True


def main():
    count = 0

    with open("input.txt", "r") as open_file:
        for line in open_file:
            numbers = list(map(int, line.split()))
            all_numbers.append(numbers)

    for stage in all_numbers:
        if is_safe_stage(stage):
            count += 1

    print("Safed stages:", count)


if __name__ == "__main__":
    main()
