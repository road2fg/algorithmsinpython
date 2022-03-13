# Print the fibonacci series until input length and calculate the sum of numbers with recursion

class Fibonacciseries:

    # Initialize the class and use it to assign value to object properties
    def __init__(self, series=[]):
        self.series = series

    # Create a recursive function that returns the next elements in the series
    def sequence(self, length):
        # If input value is 1 or 0 return the input value directly
        if length <= 1:
            return length
        # Recursively Adding the last two elements of the series to get the next element
        return self.sequence(length - 1) + self.sequence(length - 2)


if __name__ == "__main__":
    # Providing the input to the problem
    inputlength = 5
    # Checking the input using assert function
    assert inputlength > 0, f"{inputlength} is not valid, please check again. Input should be greater than 0"
    # Declaring the result sum as 0
    resultsum = 0
    # Creating the class object
    fibseries = Fibonacciseries()
    # Running for loop on the range of given input
    for i in range(inputlength):
        # Getting the nextelement from the sequence function for Fibonacciseries class
        nextelement = fibseries.sequence(i)
        # Appending the value of nextelement to the fibonacci series
        fibseries.series.append(nextelement)
        # Adding the value of nextelement to the resultsum
        resultsum = resultsum + nextelement
    # Testing the code and making sure the result is what we expect
    assert fibseries.series == [0, 1, 1, 2, 3]
    assert resultsum == 7
    # Printing the series and result of sum of all elements
    print("The Fibonacci series for the given input is", fibseries.series)
    print("The sum of all elements of the above fibonacci series is", resultsum)
