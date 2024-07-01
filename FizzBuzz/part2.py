def FizzBuzz(my_range):
    for number in range(1,my_range):
        string = ""
    
        if number % 11 == 0:
            string = "Bong"
        elif number % 15 == 0:
            string = "FizzBuzz"
        elif number % 3 == 0:
            string = "Fizz"
        elif number % 5 == 0:
            string = "Buzz"
    
        if number % 7 == 0:
            string = string + "Bang"
    
        if number % 13 == 0:
            where_is_B = string.find("B")
            if where_is_B == -1:
                string = string + "Fezz"
            else:
                string = string[:where_is_B] + "Fezz" + string[where_is_B:]
    
        if number % 17 == 0:
            index = 0
            while index <= len(string):
                substring = string[0:4]
                string = string[4:] + substring
                index += 4
    
        if string == "":
            print(number)
        else:
            print(string)

FizzBuzz(300)