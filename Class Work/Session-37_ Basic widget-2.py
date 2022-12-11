"""
Chirag came to know that there are different units to measure the temperature.
To get a better idea about Fahrenheit measurement, he wants to make a program to change the temperature
from Celsius to Fahrenheit. Create a GUI program to help Chirag and to get a better understanding of
both the units of temperature.
Hint: Use the radio button to ask conversion type: 1. Celsius to Fahrenheit or Fahrenheit to Celsius
Use Scale to give the input and check the output as well.
Use the button to execute the function. ( Use command )
"""
from tkinter import *
root = Tk()
root.title("Learning scale and radio")
root.geometry("500x500")
marks_label = Label(text="temperature Converter")
marks_label.pack()

# radio button will store value here
convertionVariable = StringVar()

# if no radio button is slected then default value set is none
convertionVariable.set("none")

#celsiusformula = c = ( f - 32 ) * ( 5/9) | c to f
#farnheitformula = f = (c * 9/5) + 32 | f to c

# two radio buttons

# radio button for cf
tempreature_radio = Radiobutton(text="Celsius to farhenheit", value="cf" , variable=convertionVariable)
tempreature_radio.pack()

# radio button for fc
tempreature_radio = Radiobutton(text="Farhenheit to celsius", value="fc" , variable=convertionVariable)
tempreature_radio.pack()

# select tempreature label
Label(text="Select tempreature").pack()

# variable to store given tempreature
givenTempreature = IntVar()

# scale
scale = Scale(from_=0 , to=500 , orient=HORIZONTAL, length=200 , variable=givenTempreature)
scale.pack()

# variable for conveted trempreature scale
convetedTempreatureOnScale = IntVar()
convetedTempreatureOnScale.set(0)

# scale for converted tempreature
scale = Scale(from_=0 , to=500 , orient=HORIZONTAL, length=200 , variable=convetedTempreatureOnScale)
scale.pack()

# function to convert temprature

def convertTempreature():

    typeOfConvertion = convertionVariable.get() # cf or fc or none | getting the value from radion button

    # cf : cel to fer
    # fc : fer to cel
    # else : none

    # when you want to find f from c

    if typeOfConvertion == "cf" :

        cTempreature = givenTempreature.get()

        # formula to find the value of fer

        fTempreature = cTempreature * (9/5) + 32 # fromula to find f from c

        Label(text=fTempreature).pack() # displaying tempreature

        convetedTempreatureOnScale.set(fTempreature)


    # when you want to find c from f

    elif typeOfConvertion == "fc" :

        fTempreature = givenTempreature.get()

        cTempreature = ( fTempreature - 32 ) * ( 5/9)   # formula to find c from f

        Label(text=cTempreature).pack()     # displaying c tempreature

        convetedTempreatureOnScale.set(cTempreature)

    # when radio button not selected

    else:

        print("No option selected") # Radio button not used it means convertionVariable is none



# button to call the convertTempreature() function
calculate_button = Button(text="Convert" , command=convertTempreature)
calculate_button.pack()


root.mainloop()


"""
Ayman had created a college admission form. He used the entry widget to take the gender and course as input. 
After learning radio buttons and checkboxes he wants to use the radio button for the selection of gender and 
checkboxes to select the subjects/course. Use the radio button and checkboxes in the previous college admission 
form and help Ayman. Also, use spinbox for age.
"""

