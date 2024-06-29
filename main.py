def main():

    numbers = []
    
    # get the list
    for i in range(5):
        numbers.append(int(input('Please enter an integer: ')))
        
    # find min
    for i in numbers:
        for j in numbers:
            if numbers[i] < numbers[j]:
                minval = numbers[i]
                print(minval)
    
    # find max          
    for i in numbers:
        for j in numbers:
            if numbers[i] > numbers[j]:
                maxval = numbers[i]
                print(maxval)
        

    print(*numbers)
    # print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
