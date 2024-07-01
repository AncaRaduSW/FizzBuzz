
for number in range(1,300):
    my_print = ""

    if number % 11 == 0:
        my_print = "Bong"
    elif number % 3 == 0 and number % 5 == 0:
        my_print = "FizzBuzz"
    elif number % 3 == 0:
        my_print = "Fizz"
    elif number % 5 == 0:
        my_print = "Buzz"

    if number % 7 == 0:
        my_print = my_print + "Bang"

    if number % 13 == 0:
        where_is_B = my_print.find("B")
        if where_is_B == -1:
            my_print = my_print + "Fezz"
        else:
            my_print = my_print[:where_is_B] + "Fezz" + my_print[where_is_B:]

    if number % 17 == 0:
        index = 0
        while index <= len(my_print):
            substring = my_print[0:4]
            my_print = my_print[4:] + substring
            index += 4

    if my_print == "":
        print(number)
    else:
        print(my_print)
