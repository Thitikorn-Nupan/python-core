import os
class Input:

    def mathBasic(self, con):
        x = input("enter x : ")
        y = input("enter y : ")
        # type(x) # <class 'str'>
        if con == 1:  # plus numbers
            print(f"{x} + {y} = {int(x) + int(y)}")
        if con == 2:  # minus numbers
            print(f"{x} - {y} = {int(x) - int(y)}")
        if con == 3:  #
            print(f"{x} x {y} = {int(x) * int(y)}")
        if con == 4:  #
            print(f"{x} / {y} = {int(x) / int(y)}")

    def carInterest(self):
        # ,priceCar:float,downPayment:float,interestPerYear:float,totalYear:int
        priceCar = input("enter priceCar : ")
        downPayment = input("enter downPayment : ")
        interestPerYear = input("enter interestPerYear : ")
        # youcan input then convert in one line
        totalYear = int(input("enter totalYear : "))

        priceCar = float(priceCar)
        downPayment = float(downPayment)
        interestPerYear = float(interestPerYear)

        finance = priceCar - downPayment
        costInterestPerYear = finance * (interestPerYear / 100)
        costInterestAllYears = costInterestPerYear * totalYear
        costCar = finance + costInterestAllYears
        costPerMonth = costCar / (totalYear * 12)

        print(f"finance = {finance:,}\n" # :, add comma to number as 600,000.0
              f"costInterestPerYear = {costInterestPerYear}\n"
              f"costInterestAllYears = {costInterestAllYears}\n"
              f"costCar = {costCar}\n"
              f"costPerMonth = {costPerMonth:.2f}\n" # specify decimal 2 position
              # <do true> if true else <do false>
              f"interest = {'Not good 'if interestPerYear > 5 else 'Ok' }\n" # You can perform if...else statements inside the placeholders:
              )


    """
    "x" - Create - will create a file, returns an error if the file exists
    "a" - Append - will create a file if the specified file does not exists
    "w" - Write - will create a file if the specified file does not exists
    """
    def readTxtFile(self):
        file = open("../txt/message.txt","r")
        # print(file.read()) # get all text
        print(file.readline()) # get one line
        file.close() # It is a good practice to always close the file when you are done with it

    ## "w" - Write - will overwrite any existing content
    def writeTxtFile(self):
        file = open("../txt/message_2.txt","w")
        message = input("enter message : ")
        file.write(message)
        file.close()

    def createAndWrireTxtFile(self):
        file = open("../txt/message_3.txt","x") # create
        message = input("enter message : ")
        file.write(message) # then write
        file.close()
    def deleteTxtFile(self):
        # To delete a file, you must import the OS module, and run its os.remove() function:
        if os.path.exists("../txt/message_3.txt"):  # Check if File exist:
            os.remove("../txt/message_3.txt")
        else:
            print("The file does not exist")
    """
    Using @staticmethod
    This is a more subtle way of creating a Static method
    *** Python 3.6 uses the input() method.
    Python 2.7 uses the raw_input() method.
    """
    @staticmethod  # (self, ** don't need once it's static method
    def manageMethods(program):
        inputObj = Input()
        if program == 1:
            inputObj.mathBasic(2)
        if program == 2:
            inputObj.carInterest()
        if program == 3:
            inputObj.readTxtFile()
        if program == 4:
            inputObj.writeTxtFile()
        if program == 5:
            inputObj.createAndWrireTxtFile()
        if program == 6:
            inputObj.deleteTxtFile()

Input.manageMethods(6)
