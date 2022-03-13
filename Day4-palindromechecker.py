# Given an input, check whether the input is a palindrome or not using recursion

class Palindrome:

    # Initialize the class and use it to assign value to object properties
    def __init__(self, giveninput):
        self.giveninput = giveninput

    # Create a recursive function that returns the result of comparison of characters
    def checker(self, start, end):
        # If first and last index are the same then return true
        if start >= end:
            return True
        # Recursively checking the result of comparison of first and last characters
        return (self.giveninput[start] == self.giveninput[end]) and (self.checker(start + 1, end - 1))


if __name__ == "__main__":
    # Providing the input to the problem
    givenstring = 1001001
    # Checking the base cases
    if len(str(givenstring)) <= 1:
        print("The given input %s is a palindrome" % givenstring)
    # Declaring the start and end pointers of the string
    startpointer = 0
    endpointer = len(str(givenstring)) - 1
    # Creating the class object
    palindrome = Palindrome(str(givenstring).lower())
    # Calling the checker function of Palindrome class
    result = palindrome.checker(startpointer, endpointer)
    # Testing the code and making sure the result is what we expect
    assert result == True
    # Printing the result
    print("The given input is a Palindrome: %s" % result)
