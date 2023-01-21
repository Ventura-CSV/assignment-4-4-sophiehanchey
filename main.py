def main():
    ##################################################
    # Comlete your code here
    ##################################################
    numbers = []
    for i in range(5):
        numbers.append(int(input('Enter a number: ')))
        if i == 0 or minval > numbers[i]:
            minval = numbers[i]
        if i == 0 or maxval < numbers[i]:
            maxval = numbers[i]

    for i in range(5):
        print(numbers[i], end=' ')
    print()
    print(f"The max value is {maxval} and min value is {minval}")

    # print (max(numbers),  min(numbers))
    # print (sorted(numbers))

    pass


if __name__ == '__main__':
    main()
