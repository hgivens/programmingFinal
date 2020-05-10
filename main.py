
# Car Dealer
# Create a cart based on user input

from tkinter import *
 
class Application(Frame):
    """ GUI application that creates a story based on user input. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get the custermers infromation """
        # create instruction label
        Label(self,
              text = "Please slect the car and parts you would like to get. "
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create a label and text entry for the name of a person
        Label(self,
              text = "Name of Order: "
              ).grid(row = 2, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 2, column = 1, sticky = W)

        # create a label and text entry for a Email
        Label(self,
              text = "Email:"
              ).grid(row = 1, column = 0, sticky = W)
        self.email_ent = Entry(self)
        self.email_ent.grid(row = 1, column = 1, sticky = W)

        # create a label for parts check buttons
        Label(self,
              text = "Car Parts:"
              ).grid(row = 5, column = 0, sticky = W)

        # create tinted windows check button
        self.is_windows = BooleanVar()
        Checkbutton(self,
                    text = "tinted windows $50",
                    variable = self.is_windows
                    ).grid(row = 5, column = 1, sticky = W)

        # create double muffler check button
        self.is_muffler = BooleanVar()
        Checkbutton(self,
                    text = "Double Mufflers $1k",
                    variable = self.is_muffler
                    ).grid(row = 5, column = 2, sticky = W)

        # create stereo upgrade check button
        self.is_stereo = BooleanVar()
        Checkbutton(self,
                    text = "Stereo Upgrade $2k",
                    variable = self.is_stereo
                    ).grid(row = 5, column = 3, sticky = W)

        # create a label for car types radio buttons
        Label(self,
              text = "Car Type:"
              ).grid(row = 4, column = 0, sticky = W)

        # create variable for single, car type
        self.car_type = StringVar()
        self.car_type.set(None)
  
        # create Car type radio buttons
        car_type = ["Toyota $10k", "Chevey $9k", "Ford $8k","Volvo $7k"]
        column = 1
        for car in car_type:
            Radiobutton(self,
                        text = car,
                        variable = self.car_type,
                        value = car
                        ).grid(row = 4, column = column, sticky = W)
            column += 1

        # create a submit button
        Button(self,
               text = "Check out",
               command = self.check_out
               ).grid(row = 6, column = 0, sticky = W)

        self.cart_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.cart_txt.grid(row = 7, column = 0, columnspan = 4)

    def check_out (self):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        person = self.person_ent.get()
        email = self.email_ent.get()
        parts = ""
        if self.is_windows.get():
            parts += "Tinted Windows $50, "
        if self.is_muffler.get():
            parts += "Double Mufflers $1k, "
        if self.is_stereo.get():
            parts += "Stereo Upgrade $2k, "
        car_type = self.car_type.get()

        # create the story
        story = "The order for "
        story += person
        story += " with the email of  "
        story +=  email
        story += " Today you ordered: "
        story += car_type  
        story += " with "
        story += parts 
        story += " added on to your car. "

        
       # display the cart                               
        self.cart_txt.delete(0.0, END)
        self.cart_txt.insert(0.0, story)

# main
root = Tk()
root.title("Buying a Car!")
app = Application(root)
root.mainloop()
