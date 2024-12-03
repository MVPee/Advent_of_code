result = []

def find_next_smallest(list1, list2):
    number1 = min(list1)
    list1.remove(number1)
    number2 = min(list2)
    list2.remove(number2)
    return number1, number2

def main():
    list1 = []
    list2 = []

    with open("input.txt", "r") as open_file:
        for line in open_file:
            left, right = map(int, line.strip().split())
            list1.append(left)
            list2.append(right)

    while len(list1) > 0:
        number1, number2 = find_next_smallest(list1, list2)
        result.append(number1 - number2 if number1 > number2 else number2 - number1)
    print(sum(result))

if __name__ == "__main__":
    main()