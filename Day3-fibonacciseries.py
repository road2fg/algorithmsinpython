# Print the fibonacci series until input length and calculate the sum of numbers without recursion

class Fibonacciseries:

    # Initialize the class and use it to assign value to object properties
    def __init__(self, length, series=[0,1]):
        self.length = length
        self.series = series

    # Create a function that appends the next element in fibonacci series and returns the updated series
    def displaysequence(self, index):
        # Appending the next element in the series list
        self.series.append(self.series[index] + self.series[index-1])
        # Returning the new list
        return self.series

    # Create a function that returns the sum of last 2 elements in the series
    def sumofnumbers(self, index):
        # Adding the last two elements of the series
        output = self.series[index] + self.series[index-1]
        return output


if __name__ == "__main__":
    # Providing the input to the problem
    inputlength = 10
    assert inputlength > 0, f"{inputlength} is not valid, please check again. Input should be greater than 2"
    if inputlength == 1:
        print("Input is 1,hence series is [0] and sum is 0")
        exit(0)
    else:
        # Declaring the start index as 1 and initial sum as 1
        start = 1
        resultsum = 1
        # Creating the class object
        fibseries = Fibonacciseries(inputlength)
        # Calling the function until the given input
        while start < inputlength-1:
            # Calling the function to create the series until the given length
            resultseries = fibseries.displaysequence(start)
            # Calling the function to add all the elements of the series
            resultsum = resultsum + fibseries.sumofnumbers(start)
            # Increasing the start pointer
            start = start + 1
        # Testing the code and making sure the result is what we expect
        assert resultsum == 88
        if inputlength == 2:
            assert fibseries.series == [0, 1]
            # Printing the resulted series
            print("The fibonacci series is", fibseries.series)
        else:
            assert resultseries == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
            # Printing the resulted series
            print("The fibonacci series is", resultseries)
        # Printing the resulted sum
        print("The sum of all elements of the above fibonacci series is", resultsum)
