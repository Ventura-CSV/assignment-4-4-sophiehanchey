def main():

    numbers = []
    
    # get the list
    for i in range(5):
        numbers.append(int(input('Please enter an integer: ')))
        
    # find min
    minval = numbers[0]
    for i in numbers[1:]:
        if i < minval:
            minval = i
    
    # find max          
    maxval = numbers[0]
    for i in numbers[1:]:
        if i > maxval:
            maxval = i

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
