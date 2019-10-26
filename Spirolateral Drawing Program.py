from tkinter import *
import turtle
import pickle

class Spirolateral():
    def __init__(self, name, segment, angle):
        """A class has been made for spirolaterals so they can be easily be
        assigned multiple variables for the program to use later.
        """
        self.name = name
        self.segment = segment
        self.angle = angle


class GUI:
    def __init__(self, master):
        """Defines all GUI frames, widgets, turtle, and constants.
        """

        COLOUR_BG = "pale green"
        PAD_LX = 20
        PAD_LY = 10
        PAD_BX = 3
        PAD_BY = 3
        WIDTH = 10

        self.master = master
        self.frame_menu = Frame(master, bg = COLOUR_BG)
        self.frame_menu.grid(row = 0, column = 0, columnspan = 2,
                             sticky = 'nesw')

        self.label_menu = Label(self.frame_menu, text = "Menu", bg = COLOUR_BG)

        self.button_add = Button(self.frame_menu, text = "Add a spirolateral",
                                 command = self.spiro_add)
        self.button_remove = Button(self.frame_menu, text = "Remove a spiro"
                                    + "lateral", command = self.spiro_remove)
        self.button_draw = Button(self.frame_menu, text = "Draw a spirolateral"
                                  , command = self.spiro_draw)
        self.button_save = Button(self.frame_menu, text = "Save spirolateral "
                                  + "list", command = self.save)
        self.button_load = Button(self.frame_menu, text = "Load spirolateral "
                                  + "list", command = self.load)
        self.button_info = Button(self.frame_menu, text = "Information",
                                  command = self.display_information)

        self.label_menu.grid(row = 0, column = 0, rowspan = 2, padx = PAD_LX)

        self.button_add.grid(row = 0, column = 1, padx = PAD_BX, pady = PAD_BY,
                             sticky = EW)
        self.button_remove.grid(row = 1, column = 1, padx = PAD_BX,
                                pady = PAD_BY, sticky = EW)
        self.button_draw.grid(row = 1, column = 2, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)
        self.button_save.grid(row = 0, column = 2, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)
        self.button_load.grid(row = 0, column = 3, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)
        self.button_info.grid(row = 1, column = 3, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)

        self.frame_secondary = Frame(master)
        self.frame_secondary.grid(row = 1, column = 1, sticky = NW)

        self.label_prompt1 = Label(self.frame_secondary, pady = PAD_LY)
        self.label_prompt2 = Label(self.frame_secondary, pady = PAD_LY)
        self.label_prompt3 = Label(self.frame_secondary, pady = PAD_LY)

        self.label_response1 = Label(self.frame_secondary, padx = PAD_LX)
        self.label_response2 = Label(self.frame_secondary, padx = PAD_LX)
        self.label_response3 = Label(self.frame_secondary, padx = PAD_LX)

        self.button_enter = Button(self.frame_secondary, text = "Enter",
                                   width = WIDTH)
        self.button_yes = Button(self.frame_secondary, text = "Yes",
                                 width = WIDTH, command = root.destroy)
        self.button_draw2 = Button(self.frame_secondary, text = "Draw",
                                   width = WIDTH, command = self.start_draw)
        self.button_stop = Button(self.frame_secondary, text = "Stop",
                                  width = WIDTH, command = self.stop_draw)

        self.entry1 = Entry(self.frame_secondary)
        self.entry2 = Entry(self.frame_secondary)
        self.entry3 = Entry(self.frame_secondary)

        self.frame_spiro = Frame(master)
        self.frame_spiro.grid(row = 1, column = 0, rowspan = 2, sticky = NW)

        self.label_spiro = Label(self.frame_spiro, text = "Spirolaterals:")
        self.label_spiro.grid(row = 0, column = 0, padx = PAD_LX,
                              pady = PAD_LY, sticky = NW)

        self.label_spiros = Label(self.frame_spiro, justify = LEFT)
        self.label_spiros.grid(row = 1, column = 0, padx = PAD_LX,
                               sticky = NW)

        self.frame_draw = Frame(master)

        self.canvas = Canvas(self.frame_draw, width = 500, height = 500)
        self.canvas.grid(row = 0, column = 0)

        self.turtle = turtle.RawTurtle(self.canvas)

    def spiro_add(self):
        # Stops function from running when there's the max amount of spiros
        # by putting the rest of the function indented in the if statement
        if self.option_stop(MAX_SPIRO, "You can only have {} spirolaterals."
                            .format(MAX_SPIRO)) != -1:

            # Changes labels and buttons, and adds labels, entries, and buttons
            # to the grid
            self.label_prompt1.configure(text = "Name:")
            self.label_prompt2.configure(text = "Segments:")
            self.label_prompt3.configure(text = "Angle:")

            self.label_prompt1.grid(row = 0, column = 0, sticky = W)
            self.label_prompt2.grid(row = 1, column = 0, sticky = W)
            self.label_prompt3.grid(row = 2, column = 0, sticky = W)

            self.label_response1.grid(row = 0, column = 2, sticky = W)
            self.label_response2.grid(row = 1, column = 2, sticky = W)
            self.label_response3.grid(row = 2, column = 2, sticky = W)

            self.entry1.grid(row = 0, column = 1)
            self.entry2.grid(row = 1, column = 1)
            self.entry3.grid(row = 2, column = 1)

            self.button_enter.configure(command = self.check_add)

            self.button_enter.grid(row = 3, column = 0)

    def check_add(self):
        """Checks that entries are valid then adds a spirolateral if they are
        """
        name = self.entry1.get()
        if name == "":
            self.label_response1.configure(text = "Enter a name.")

        # Checks for duplicate name
        for index in range(len(spiros)):
            if name == spiros[index].name:
                self.label_response1.configure(text = "There's already a "
                                               + "spirolateral called {}."
                                               .format(name))
                name = ""

        segment = check_num(self.entry2, self.label_response2,
                            "Can't have 0 or less segments.",
                            MIN_CHOICE, float('inf'), int)
        angle = check_num(self.entry3, self.label_response3,
                          "Angle can't be less than 0° or greater than 360°.",
                          MIN_CHOICE, 360, int)

        # Adds a spirolateral if all the entry requirements have been met
        if name != "" and segment != -1 and angle != -1:
            spiros.append(Spirolateral(name, segment, angle))

            self.spiro_print()
            self.clear()

            self.label_prompt1.configure(text = "Spirolateral added.")
            self.label_prompt1.grid(row = 0, column = 0)

        # Rest of function checks if entries with responses now have their
        # requirements met and clears the response if they have
        elif name != "" and self.label_response1.cget("text") != "":
            self.label_response1.configure(text = "")

        elif segment != -1 and self.label_response2.cget("text") != "":
            self.label_response2.configure(text = "")

        elif angle != -1 and self.label_response3.cget("text") != "":
            self.label_response3.configure(text = "")

    def spiro_remove(self):
        if self.option_stop(0, "There are no spirolaterals to remove.") != -1:

            self.label_prompt1.configure(text = "Integer:")
            self.label_prompt1.grid(row = 0, column = 0, sticky = W)

            self.label_response1.grid(row = 0, column = 2, sticky = W)

            self.entry1.grid(row = 0, column = 1)

            self.button_enter.configure(command = self.check_remove)
            self.button_enter.grid(row = 1, column = 0)

    def check_remove(self):
        """Checks that the entry is valid then removes the spirolateral
        if they are
        """
        choice = check_num(self.entry1, self.label_response1, "That integer "
                           + "doesn't correspond to anything.", MIN_CHOICE,
                           len(spiros), int)

        if choice != -1:
            del spiros[choice - 1]

            self.spiro_print()
            self.clear()

            self.label_prompt1.configure(text = "Spirolateral removed.")
            self.label_prompt1.grid(row = 0, column = 0)

    def spiro_draw(self):
        print(3)

    def start_draw(self):
        print(4)

    def stop_draw(self):
        print(5)

    def save(self):
        print(6)

    def load(self):
        print(7)

    def display_information(self):
        print(8)

    def spiro_print(self):
        """Creates a label with all of the spirolaterals each time a
        spirolateral is added or removed.
        """
        text = ""
        # Adds to the text variable in a for loop so every spirolateral is
        # added no matter how many there are, and any spirolateral that's been
        # removed isn't added
        for index in range(len(spiros)):
            text += "{}) {} - {} segments and {}°\n".format(index + 1,
                    spiros[index].name, spiros[index].segment,
                    spiros[index].angle)
        self.label_spiros.configure(text = text)

    def clear(self):
        """Clears the secondary frame, all entries, response labels
        """
        for widget in self.frame_secondary.winfo_children():
            widget.grid_forget()

        self.frame_draw.grid_forget()

        self.label_response1.configure(text = "")
        self.label_response2.configure(text = "")
        self.label_response3.configure(text = "")

    def option_stop(self, num, text):
        """Runs at the start functions to stop them from running their code
        if their requirements aren't met
        """
        self.clear()
        if len(spiros) == num:
            self.label_prompt1.configure(text = text)
            self.label_prompt1.grid(row = 0, column = 0)
            return -1


def check_num(entry, label, response, lower_limit, upper_limit, integer):
    """Can be applied to any integer the user inputs to check that it's a valid
    integer that's in range. Uses parameters so each time this function is
    called there can be customised prompts, ranges, etc.
    """
    # Try and except statements test for an invalid input
    try:
        choice = integer(entry.get())
        # Checks that the choice is in range
        if choice < lower_limit or choice > upper_limit:
            label.configure(text = response)
            return -1
        else:
            return choice
    except ValueError:
        if integer == int:
            label.configure(text = "Not a valid integer.")
        elif integer == float:
            label.configure(text = "Not a valid number.")
        return -1

# Creates list of spiros for the program to add to
spiros = []
# Creates constant for the program to use. Defining here makes it easy to
# edit. Minimum choice used as constant because no input in the program should
# Require an input less than 1.
MAX_SPIRO = 30
MIN_CHOICE = 1

def main():
    """Runs the GUI and assigns it a name
    """
    global root
    root = Tk()
    root.title("Spirolateral Drawing Program")
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    """Runs main() if this program hasn't been imported
    """
    main()
