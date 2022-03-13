# Given an input, return the sum of digits using recursion

class Digits:

    # Initialize the class and use it to assign value to object properties
    def __init__(self, giveninput):
        self.giveninput = giveninput

    # Create a recursive function that returns the result of comparison of characters
    def sumofdigits(self):
        # If input is 0 return 0
        if self.giveninput == 0:
            return 0
        # Getting the last digit
        lastdigit = self.giveninput % 10
        # Removing the last digit
        self.giveninput = int(self.giveninput / 10)
        # Recursively adding the last digit to return output
        return lastdigit + self.sumofdigits()


if __name__ == "__main__":
    # Providing the input to the problem
    givennumber = 10
    # Checking the base cases
    if givennumber in range(0,10):
        print("The sum of digits is %d" % givennumber)
        exit(0)
    # Creating the class object
    number = Digits(givennumber)
    # Calling the sumofdigits function of Digits class
    result = number.sumofdigits()
    # Testing the code and making sure the result is what we expect
    assert result == 1
    # Printing the result
    print("The sum of digits of the number %d is %d" % (givennumber, result))
