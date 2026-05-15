from linked_list import LinkedList

def main():
    numbers = LinkedList[int]()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)

    numbers.prepend(0)
    numbers.insert(2, 100)

    print(numbers)
    # LinkedList([0, 1, 100, 2, 3])

    print(numbers[2])
    # 100

    print(len(numbers))
    # 5

    numbers.remove(100)

    print(list(numbers))
    # [0, 1, 2, 3]

    numbers.reverse()

    print(numbers)
    # LinkedList([3, 2, 1, 0])


if __name__ == "__main__":
    main()
