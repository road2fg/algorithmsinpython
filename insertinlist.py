# Given a position and input,insert the input at the position in the list

class Insertlist():

    # Initialize the class and use it to assign value to object properties
    def __init__(self, inputlist):
        self.inputlist = inputlist

    # Create a function that returns the output of the new/updated list
    def addnewelement(self, inputindex, inputvalue):
        # Used list slicing to add the new element at the given position and return the concatenated list
        outputlist = self.inputlist[:inputindex] + [inputvalue] + self.inputlist[inputindex:]
        return outputlist


if __name__ == "__main__":
    # Providing the input to the problem
    givenlist = [1,2,3,4,5,6]
    newindex  = 4
    newelement = 8

    # Handling the use case where new index is not an integer or less than 0 or greater than length + 1 of given list
    if newindex < 0 or newindex > len(givenlist) + 1 or type(newindex) is not int:
        result = givenlist
        print("This position %d is an invalid input" % newindex)
    # Handling the use case where we are inserting the element at beginning
    elif newindex == 0:
        result = [newelement] + givenlist
    # Handling the use case where we are inserting the element at end
    elif newindex == len(givenlist):
        result = givenlist + [newelement]
    else:
        # Creating the class object
        inputlist = Insertlist(givenlist)
        # Calling the addnewelement function of Insertlist class
        result = inputlist.addnewelement(newindex, newelement)

    # Testing the code and making sure the result is what we expect
    assert result == [1,2,3,4,8,5,6]
    # Printing the result and output
    print("Final Output is", result)
