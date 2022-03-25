# Given a rope of length n, find maximum cuts so that length of every piece should be in set {a, b, c}

class Rope:

    # Initialize the class and use it to assign value to object properties
    def __init__(self, length, cutslengthset):
        self.length = length
        self.cutslengthset = cutslengthset

    def maxpieces(self, newlength):
        # If the length is 0 return 0
        if newlength == 0:
            return 0
        # If the length is negative return -1
        if newlength < 0:
            return -1
        # Take the max of the returned values and from the three cuts set values
        result = max(self.maxpieces(newlength- self.cutslengthset[0]),
                     self.maxpieces(newlength - self.cutslengthset[1]),
                     self.maxpieces(newlength - self.cutslengthset[2]))
        # If the result is -1, then the pieces are not possible
        if result == -1:
            return -1
        # Add 1 to the result and return the output
        return result + 1


if __name__ == "__main__":
    # Providing the input to the problem
    cutsset = [4, 2, 6]
    ropelength = 5
    # Creating the class object
    ropeobject = Rope(ropelength, cutsset)
    # Calling the maxpieces function of Rope class
    output = ropeobject.maxpieces(ropeobject.length)
    # Testing the code and making sure the result is what we expect
    assert output == -1
    # Printing the output
    if output == -1:
         print("Pieces are not possible")
    else:
         print("Maximum Number of Pieces is", output)


