result = []

def main():
    list1 = []
    list2 = []

    with open("input.txt", "r") as open_file:
        for line in open_file:
            left, right = map(int, line.strip().split())
            list1.append(left)
            list2.append(right)

    for element in list1:
        count = list2.count(element)
        result.append(count * element)
    
    print(sum(result))

if __name__ == "__main__":
    main()