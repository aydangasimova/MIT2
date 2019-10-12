def MaxOdd(numbers):
    """Write a program that examines three variables— x , y , and z —
and prints the largest odd number among them. If none of them are odd, it
should print a message to that effect."""
    for x in numbers:
        if x == max(numbers) and x%2!=0:
            return x
        else:
            numbers = numbers.remove(x)
            return max(numbers)

    # if not sorted_odd_nums:
    #    # all numbers were even and filtered out.
    # elif sorted_odd_nums[0][0] == 0:
    #    # x is the biggest odd number
    # elif sorted_odd_nums[0][0] == 1:
    #    # y is the biggest odd number
    # elif sorted_odd_nums[0][0] == 2:
    #    # z is the biggest odd number
    #
    #    x, y, z = int(), int(), int()
    #    x, y, z = 8, 3, 5
    #    numbers = [x, y, z]
    #    for i in enumerate(numbers):
    #        print(i[1])
    pass
    # sorted_odd_numbers = sorted((x for x in numbers if x[1]%2), key = lambda x: x[1], reverse=True)

def AskInput():
    """Write a program that asks the user to input 10 integers, and
then prints the largest odd number that was entered. If no odd number was
    entered, it should print a message to that effect."""
    numbers = []
    for i in range(10):
        try:
            numbers.append(int(input("please enter an integer:")))
        except ValueError:
            numbers.append(int(input("Oops what you entered, doesn't seem to be an integer. Please enter an integer: ")))
    return numbers


AskInput()

MaxOdd(AskInput())
