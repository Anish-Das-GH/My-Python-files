class Student :
    def getstudentdetails(self):
        self.roll = input("Enter The Roll no of the student ")
        self.name = input("What's the name of the student ? ")
        self.phy = int(input("Enter the marks of Physics "))
        self.chem = int(input("Enter the marks of Chemistry "))
        self.math = int(input("Enter the marks of Math "))

    def Printresults(self):
        self.average = int((self.phy+self.chem+self.math)/3)
        print(self.average)

S1=Student()
S1.getstudentdetails()

print("Average Result : ")
S1.Printresults()

