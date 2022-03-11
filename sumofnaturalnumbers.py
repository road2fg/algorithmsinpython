# Given an input n, we need to find out the sum of first n natural numbers

class Naturalnumber:
    # Initialize the class and use it to assign value to object properties
    def __init__(self, number):
        self.number = number
    # Create a function that returns the output of the first n natural numbers

    def sumofnumbers(self):
        # Basic formula to calculate the sum is n * n+1/2
        # I would return the value from the above formula
        output = self.number * (self.number + 1)/2
        return output


if __name__ == "__main__":
    # Providing the input to the problem
    num = 15
    # Creating the class object
    n_natural_nums = Naturalnumber(num)
    # Calling the sumofnumbers function of Naturalnumber class
    result = n_natural_nums.sumofnumbers()
    # Testing the code and making sure the result is what we expect
    assert result == 120
    # Printing the result and output
    print("The result of first %d natural numbers is %d" % (num, result))

