import numpy as np

def FizzBuzz(my_range, rules):
    for number in range(1, my_range + 1):
        string = ""
    
        if number % 11 == 0 and rules[11]:
            string = "Bong"
        elif number % 15 == 0 and rules[3] and rules[5]:
            string = "FizzBuzz"
        elif number % 3 == 0 and rules[3]:
            string = "Fizz"
        elif number % 5 == 0 and rules[5]:
            string = "Buzz"
    
        if number % 7 == 0 and rules[7]:
            string = string + "Bang"
    
        if number % 13 == 0 and rules[13]:
            where_is_B = string.find("B")
            if where_is_B == -1:
                string = string + "Fezz"
            else:
                string = string[:where_is_B] + "Fezz" + string[where_is_B:]
    
        if number % 17 == 0 and rules[17]:
            index = 0
            while index <= len(string):
                substring = string[0:4]
                string = string[4:] + substring
                index += 4
    
        if string == "":
            print(number)
        else:
            print(string)


rules = np.full(20, False)

my_range = int(input("Enter a range: "))

# User enters the rules to be followed --> ends when 0 is received
input_no = int(input("Enter rule: "))

while (input_no > 0):
    rules[input_no] = True
    input_no = int(input("Enter rule: "))


FizzBuzz(my_range, rules)