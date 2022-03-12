# Given a position, delete the element at the position in the list using list concatenation

class Deletelist():

    # Initialize the class and use it to assign value to object properties
    def __init__(self, inputlist):
        self.inputlist = inputlist

    # Create a function that returns the output of the new/updated list
    def deleteelement(self, inputindex):
        # Used list slicing to delete the element at the given position and return the list
        outputlist = self.inputlist[:inputindex] + self.inputlist[inputindex+1:]
        return outputlist


if __name__ == "__main__":
    # Providing the input to the problem
    givenlist = [1,2,3,4,5,6]
    index = 3

    # Handling the use case where index is not an integer or less than 0 or greater than equal to length of given list
    if index < 0 or index >= len(givenlist) or type(index) is not int:
        result = givenlist
        print("This position %d is an invalid input" % index)
    else:
        # Creating the class object
        inputlist = Deletelist(givenlist)
        # Calling the deleteelement function of Deletelist class
        result = inputlist.deleteelement(index)

    # Testing the code and making sure the result is what we expect
    assert result == [1,2,3,5,6]
    # Printing the result and output
    print("Final Output is", result)
