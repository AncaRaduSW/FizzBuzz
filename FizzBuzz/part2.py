import numpy as np


def FizzBuzz(the_range, rules):
    for number in range(1, the_range + 1):
        tokens = []
        if number % 11 == 0 and rules[11] == True:
            tokens.append("Bong")
        else:
            if number % 15 == 0 and rules[3] == True and rules[5] == True:
                tokens.append("Fizz")
                tokens.append("Buzz")
            elif number % 3 == 0 and rules[3] == True:
                tokens.append("Fizz")
            elif number % 5 == 0 and rules[5] == True:
                tokens.append("Buzz")

            if number % 7 == 0 and rules[7] == True:
                tokens.append("Bang")

        if number % 13 == 0 and rules[13] == True:
            where_is_b = -1
            for tok in tokens:
                where_is_b = tok.find("B")
                if where_is_b != -1:
                    index = tokens.index(tok)
                    tokens.insert(index, "Fezz")
                    break

            if where_is_b == -1:
                tokens.append("Fezz")

        if number % 17 == 0 and rules[17] == True:
            tokens.reverse()

        if len(tokens) == 0:
            print(number)
        else:
            final_string = ""
            for tok in tokens:
                final_string += tok
            print(final_string)



my_rules = np.full(20, False)

my_range = int(input("Enter a range: "))

# User enters the rules to be followed --> ends when 0 is received
input_no = int(input("Enter rule: "))

while input_no > 0:
    my_rules[input_no] = True
    input_no = int(input("Enter rule: "))


FizzBuzz(my_range, my_rules)
