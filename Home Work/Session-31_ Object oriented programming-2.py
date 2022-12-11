
"""
Homework questions
Nidhi is trying to understand how the phone gets updated with new features with all the
old features already available in the new phone. Write a program to explain this with
the help of inheritance and method overriding.
Hint: Create class Nokia1, then create class Nokia2 and inherit all the methods from Nokia1 to Nokia2.
Also, modify the required methods in Nokia2 and add a few additional methods as well.
In the same way, you can create Nokia3 and Nokia4 as well.
# creating Nokia1 class
"""
class Nokia1 :
    def __init__(self , model , price , ram , rom , camera):
        self.model = model
        self.price = price
        self.ram = ram
        self.rom = rom
        self.camera = camera

    def switchOn(self):
        print("Turning on phone ...")

    def switchOff(self):
        print("Turning off phone ...")

    def call(self):
        print("Calling ...")

# creating Nokia2 class - Higher version

class Nokia2(Nokia1) :

    # camera introduced in Nokia2 phones

    def takePicture(self):
        print("Clicking image ...")

    def recordVideo(self):
        print("Recording video ...")

    # fm radio introduced in Nokia2 phones

    def playFm(self):
        print("Playing fm")

# creating Nokia3 class - Higher version | more features than Nokia2

class Nokia3(Nokia2):

    # hd camera introduced in Nokia3 phones

    def takePicture(self):
        print("Clicking hd image ...")

    def recordVideo(self):
        print("Recording hd video ...")

    # front camera introduced in Nokia3 phones

    def videoCall(self):
        print("Video calling ...")


# Main_Program

# creating nokia1 phone
phone1 = Nokia1(515 , 1000 , 0.2 , 1 , "Nill")

# creating nokia2 phone
phone2 = Nokia2("Lumia 928" , 2500 , 0.512 , 2 , "VGA")

# crating nokia3 phone
phone3 = Nokia3("Asha 210" , 4800 , 1 , 8 , "12 hd")


# The end


